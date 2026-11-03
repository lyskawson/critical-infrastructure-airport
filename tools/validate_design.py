#!/usr/bin/env python3
"""Check relational/quantitative consistency, never engineering or legal compliance."""
import argparse
import copy
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from export_design import ROOT, bom_quantities, calculate, lengths, load_design, outputs
from design_geometry import optical_results, parking_results, vehicle_poses, vehicle_box


def validate(d):
    errors=[]
    def check(ok,msg):
        if not ok:errors.append(msg)
    def unique(items,name):
        ids=[x['id'] for x in items];check(len(ids)==len(set(ids)),name+': duplicate ID')
    for name in ['devices','rooms','areas','openings','nodes','routes','connections','access_points','circuits','sources','bom_accessories']:
        unique(d[name],name)
    dev={x['id']:x for x in d['devices']};models=d['equipment_models'];rooms={x['id']:x for x in d['rooms']};areas={x['id']:x for x in d['areas']};sources={x['id'] for x in d['sources']};connections={x['id']:x for x in d['connections']}
    places=set(rooms)|set(areas);ports=defaultdict(list);links=defaultdict(list)
    check(d['schema_version']==2,'unsupported schema')
    frame=d['coordinates']['local_transform']['T0']
    ox,oy,oz=frame['translation_m']
    terminal=next(x for x in d['buildings'] if x['id']=='T0')
    tw,th=terminal['size_m']
    check(frame['rotation_deg']==0 and terminal['origin_site_m']==[ox,oy],'building coordinate frame')
    for m in models.values():check(m['source'] in sources,'model source: '+m['name'])
    for x in dev.values():
        if x['model'] not in models:check(False,'unknown model: '+x['id']);continue
        l=x['location'];check(l['room_or_area'] in places,'unknown location: '+x['id'])
        xyz=l['xyz_m'];site=l['xyz_site_m']
        expected=[xyz[0]+ox,xyz[1]+oy,xyz[2]+oz] if l['frame']=='T0' else xyz
        check(all(math.isclose(a,b,abs_tol=1e-5) for a,b in zip(expected,site)),'coordinate transform: '+x['id'])
        if l['room_or_area'] in rooms:
            rect=rooms[l['room_or_area']]['rect_local_m'];xx,yy,w,h=rect
            check(l['frame']=='T0' and xx-.01<=xyz[0]<=xx+w+.01 and yy-.01<=xyz[1]<=yy+h+.01,'device outside assigned room: '+x['id'])
            check(0<=xyz[2]<=rooms[l['room_or_area']]['height_m'],'mount height: '+x['id'])
            temp=models[x['model']].get('temperature_C')
            if temp:check(temp[0]<=d['site']['indoor_temperature_C'][0] and temp[1]>=d['site']['indoor_temperature_C'][1],'indoor temperature: '+x['id'])
        if x['power_source'] not in ['passive','none','BOUNDARY-230V']:
            source=x['power_source'].split(':')[0];check(source in dev,'power source: '+x['id'])
        if x.get('node') not in {n['id'] for n in d['nodes']}:check(False,'node: '+x['id'])
    rects=[r['rect_local_m'] for r in rooms.values()]
    for i,a in enumerate(rects):
        check(a[0]>=0 and a[1]>=0 and a[0]+a[2]<=tw and a[1]+a[3]<=th,'room outside T0')
        for b in rects[i+1:]:check(not(max(a[0],b[0])<min(a[0]+a[2],b[0]+b[2])-1e-6 and max(a[1],b[1])<min(a[1]+a[3],b[1]+b[3])-1e-6),'overlapping rooms')
    check(math.isclose(sum(r[2]*r[3] for r in rects),tw*th),'room model does not tile terminal')
    for c in d['connections']:
        check(c['cable_type'] in d['cable_types'],'unknown cable: '+c['id'])
        if not all(e['device'] in dev for e in c['ends']):check(False,'unknown cable endpoint: '+c['id']);continue
        for i,e in enumerate(c['ends']):
            check(e['port'] in models[dev[e['device']]['model']]['ports'],'unknown port: '+c['id']+' '+str(e))
            ports[(e['device'],e['port'])].append(c['id'])
            pt=c['points_site_m'][0 if i==0 else -1]
            check(math.dist(pt,dev[e['device']]['location']['xyz_site_m'])<1e-5,'cable endpoint geometry: '+c['id'])
        try:
            pl,ve,ins,buy=lengths(c)
            check(all(math.isclose(a,b,abs_tol=1e-4) for a,b in [(pl,c['plan_m']),(ve,c['vertical_m']),(ins,c['installed_m'])]) and buy==c['purchase_m'],'cable quantities: '+c['id'])
            check(c['service_m']>=0 and 0<=c['waste_fraction']<=.3,'cable allowances: '+c['id'])
        except (KeyError,ValueError):check(False,'invalid geometry: '+c['id'])
        check(all(-.71<=p[2]<=4.2 and 0<=p[0]<=80 and 0<=p[1]<=60 for p in c['points_site_m']),'route outside site: '+c['id'])
        check(all(a[2]==b[2] or a[:2]==b[:2] for a,b in zip(c['points_site_m'],c['points_site_m'][1:])),'missing plan/elevation elbow: '+c['id'])
        if 'link_group' in c:links[c['link_group']].append(c)
    for x in dev.values():check(any(key[0]==x['id'] for key in ports) or x.get('mechanical_parent') in {o['id'] for o in d['openings']},'unconnected device: '+x['id'])
    for key,cs in ports.items():
        if key[0]=='SW-0' and key[1].startswith('P') or key[1] in ['ETH','AC','DPS','REX','LOCK','IN','OUT'] and models[dev[key[0]]['model']]['category'] not in ['distribution','reader']:
            check(len(cs)==1,'port used twice: '+str(key))
    for lid,cs in links.items():
        ends=Counter(e['device'] for c in cs for e in c['ends'])
        terminals=[id for id,n in ends.items() if n==1]
        check(len(terminals)==2 and 'SW-0' in terminals,'Ethernet chain endpoints: '+lid)
        if len(terminals)==2:
            other=next(x for x in terminals if x!='SW-0');check(other==lid.removeprefix('NET-'),'Ethernet endpoint identity: '+lid)
    for x in d['devices']:
        if x['model']!='CAM':continue
        c=x;pt=c['location']['xyz_m'];target=c['target']['xyz_m'];dist=math.dist(pt,target);width=c['target']['width_m'];hfov=math.degrees(2*math.atan(width/(2*dist)))
        check(models['CAM']['hfov_range_deg'][0]<=hfov<=models['CAM']['hfov_range_deg'][1],'lens cannot obtain frame: '+c['id'])
        check(math.isclose(hfov,c['view']['hfov_deg'],abs_tol=.002),'HFOV stale: '+c['id'])
        check(math.isclose(c['video_horizontal_px']/width,c['view']['ppm'],abs_tol=.002) and c['view']['ppm']>=c['target']['minimum_ppm'],'pixel density: '+c['id'])
        vfov=math.degrees(2*math.atan(math.tan(math.radians(hfov/2))*c['video_vertical_px']/c['video_horizontal_px']))
        check(math.isclose(vfov,c['view']['vfov_deg'],abs_tol=.001),'VFOV stale: '+c['id'])
        check(models['CAM']['vfov_range_deg'][0]<=vfov<=models['CAM']['vfov_range_deg'][1],'vertical lens range: '+c['id'])
        check([c['video_horizontal_px'],c['video_vertical_px']]==d['optical_model']['resolution_px'] and c['view']['roll_deg']==d['optical_model']['roll_deg']==0,'optical format/roll: '+c['id'])
        az=math.degrees(math.atan2(target[1]-pt[1],target[0]-pt[0]))%360
        tilt=math.degrees(math.atan2(pt[2]-target[2],math.dist(pt[:2],target[:2])))
        check(abs((az-c['view']['azimuth_deg']+180)%360-180)<.002 and abs(tilt-c['view']['down_tilt_deg'])<.002,'camera optical axis stale: '+c['id'])
        # A same-room ray cannot cross an internal partition; outdoor rays must remain outside the building.
        loc=c['location']['room_or_area']
        if loc in rooms:
            xx,yy,w,h=rooms[loc]['rect_local_m'];check(xx<=target[0]<=xx+w and yy<=target[1]<=yy+h,'camera target crosses a wall: '+c['id'])
        else:
            for step in range(1,101):
                p=[pt[j]+(target[j]-pt[j])*step/100 for j in range(2)]
                check(not(20.05<p[0]<43.95 and 25.05<p[1]<40.95),'outdoor target ray crosses building: '+c['id'])
    path=d['path_observation'];check(path['clear_width_m']>=1.5 and path['turning_diameter_m']>=1.5,'path accessibility')
    check(path['design_service_capacity_per_hour']>=path['arrival_target_persons_per_hour'],'staff passage capacity')
    for v in path['views']:check(v['camera'] in dev,'path camera reference')
    optics=optical_results(d)
    for v in optics['path']:
        check(v['visible'],'PATH1 upper-body outside 3D frame: '+v['camera'])
        check(v['min_ppm']>=v['minimum_ppm'],'PATH1 pixel density: '+v['camera'])
    for v in optics['kd']:
        check(v['visible'],'ACS opening outside verification 3D frame: '+v['id']+'/'+v['camera'])
        check(v['min_ppm']>=v['minimum_ppm'],'ACS verification pixel density: '+v['id'])
    check(optics['ai_line']['visible'],'AI line feet/body outside 3D frame')
    check(optics['ai_roi']['visible'],'AI ROI feet/body outside 3D frame')
    check(optics['ai_roi']['min_person_height_px']>=d['ai']['minimum_image_height_fraction']*dev[d['ai']['camera_ids'][0]]['video_vertical_px'],'AI human image height')
    ai=d['ai'];poly=ai['zone_polygon_site_m'];xs=sorted({p[0] for p in poly});ys=sorted({p[1] for p in poly})
    check(len(xs)==len(ys)==2 and len({tuple(p) for p in poly})==4,'AI ROI must be explicit rectangle')
    check(all(xs[0]<=p[0]<=xs[-1] and ys[0]<=p[1]<=ys[-1] for p in ai['line_site_m']),'AI line outside ROI')
    check(ai['visible_preline_distance_m']<=min(p[1] for p in ai['line_site_m'])-ys[0] and ai['visible_preline_distance_m']/ai['maximum_design_walk_speed_m_s']>=ai['minimum_track_time_s'],'AI pre-line tracking time')
    lane=ai['context_lane_polygon_site_m'];lx=min(p[0] for p in lane);rx=max(p[0] for p in lane);ly=min(p[1] for p in lane);ry=max(p[1] for p in lane)
    half=ai['person_envelope']['half_size_xy_m'];cx,cy,_=dev[ai['camera_ids'][0]]['location']['xyz_site_m']
    check(lx<=cx<=rx and ly<=cy<=ry and xs[0]-half>=lx-1e-8 and xs[-1]+half<=rx+1e-8 and ys[0]-half>ly and ys[-1]+half<=ry,'AI rays cross closed side boundary / gate')
    check(ys[0]-half>max(r[1]+r[3] for r in d['site']['parking_layout']['open_gate_leaf_rects_site_m']),'AI body intersects open gate leaves')
    controls=set()
    for a in d['access_points']:
        check(a['controller'] in dev and dev[a['controller']]['model']=='CTRL','ACS controller: '+a['id'])
        check((a['controller'],a['channel']) not in controls,'ACS channel reused');controls.add((a['controller'],a['channel']))
        check(a['channel']==1 and 1<=len(a['readers'])<=2,'ACS capacity')
        check(all(r in dev and dev[r]['model']=='READER' for r in a['readers']),'ACS reader reference')
        check(sum(models[dev[r]['model']]['max_current_a'] for r in a['readers'])<=models['CTRL']['reader_current_capacity_a'],'ACS reader power')
        load=sum(models[dev[r]['model']]['max_current_a'] for r in a['readers'])
        if dev[a['lock']]['model']=='STRIKE':load+=models['STRIKE']['max_current_a']
        check(load<=models['CTRL']['peripheral_capacity_a'],'ACS peripheral current budget')
        check(a['door_contact'] in dev and a['dps_supervision']['series_ohm']==a['dps_supervision']['parallel_ohm'],'ACS supervised DPS')
        check(a['from_zone'] in places and a['to_zone'] in places,'ACS side/zone reference: '+a['id'])
        check(bool(a['no_lan'] and a['no_power'] and a['fire'] and a['physical_egress_path']),'ACS missing failure state')
        for cid in a['verification_cameras']:check(cid in dev and dev[cid]['model']=='CAM','ACS verification camera reference')
        check(bool(a['verification_cameras']),'ACS missing verification frame: '+a['id'])
        if a['id']!='G01':
            check(a['door_contact'] in dev and a['rex'] in dev,'ACS contact/exit reference')
            check(models[dev[a['lock']]['model']]['max_current_a']<=models['CTRL']['lock_current_capacity_a'],'ACS strike overload')
            check(a['ssprelease_channel'] is None,'unnecessary electrical unlock for mechanical egress')
    check(dev['DC-D01']['id']!=dev['IC-D01']['id'],'ACS/IDS same contact counted twice')
    intrusion_lines=[]
    for c in d['connections']:
        for e in c['ends']:
            if e['device']=='SSWiN-0' and e['port'].startswith('Z'):intrusion_lines.append(int(e['port'][1:]))
    check(len(intrusion_lines)==len(set(intrusion_lines)) and all(1<=n<=15 for n in intrusion_lines),'IDS input capacity/reuse')
    check(len(d['intrusion_zones'])<=2,'VERSA partitions')
    for z in d['intrusion_zones']:check(all(x in dev for x in z['devices']),'intrusion zone reference')
    loop=d['fire']['loops'][0];order=loop['devices'];loop_cs=loop['connections']
    check(len(order)==len(set(order)) and len(order)<=loop['capacity'],'loop point capacity/duplicate')
    check(all(x in dev for x in order),'loop reference')
    check(len(loop_cs)==len(order)+1,'loop connection count')
    if all(x in dev for x in order) and all(x in connections for x in loop_cs):
        check(len({dev[x]['address'] for x in order})==len(order),'duplicate loop address')
        check(all(1<=dev[x]['address']<=loop['capacity'] for x in order),'address range')
        expected=['CSP-0']+order+['CSP-0']
        for i,cid in enumerate(loop_cs):check([e['device'] for e in connections[cid]['ends']]==expected[i:i+2],'loop continuity: '+cid)
        check(all(models[dev[x]['model']].get('isolator') for x in order),'missing loop isolator')
    for ce in d['fire']['control_matrix']:
        for output in ce['outputs']:
            base,port=output.split(':')
            check((base=='L1' and port in order and dev[port]['model']=='SND') or (base in dev and port in models[dev[base]['model']]['ports']),'fire output reference: '+output)
        check(bool(ce['supervision'] and ce['reset']),'fire matrix missing supervision/reset')
    # Conservative ceiling coverage over every room, own radius, no normative compliance claim.
    for room in rooms.values():
        detectors=[x for x in dev.values() if x['model'] in ['DMP','DCP'] and x['location']['room_or_area']==room['id']]
        check(bool(detectors),'no fire detector for room: '+room['id'])
        if not detectors:continue
        xx,yy,w,h=room['rect_local_m']
        for i in range(math.ceil(w*2)+1):
            for j in range(math.ceil(h*2)+1):
                pt=[xx+min(w,i*.5),yy+min(h,j*.5)]
                check(any(math.dist(pt,x['location']['xyz_m'][:2])<=x['coverage_radius_assumed_m']+1e-7 for x in detectors),'fire geometric coverage: '+room['id'])
    # Shortest walk via actual room door centres, without crossing walls, for ROP reachability.
    nodes={o['id']:(o['centre_local_m'],o['sides']) for o in d['openings'] if o.get('building')=='T0'}
    for x in dev.values():
        if x['model']=='ROP':nodes[x['id']]=(x['location']['xyz_m'][:2],[x['location']['room_or_area']])
    graph={x:{} for x in nodes}
    for a,(pa,ra) in nodes.items():
        for b,(pb,rb) in nodes.items():
            if a!=b and set(ra)&set(rb)&set(rooms):graph[a][b]=math.dist(pa,pb)
    max_walk=0
    for room in rooms.values():
        xx,yy,w,h=room['rect_local_m']
        for pt in [[xx,yy],[xx+w,yy],[xx,yy+h],[xx+w,yy+h]]:
            distances={id:math.dist(pt,p) for id,(p,rs) in nodes.items() if room['id'] in rs};todo=set(nodes)
            while todo:
                a=min(todo,key=lambda a:distances.get(a,math.inf));todo.remove(a)
                if a.startswith('ROP-'):max_walk=max(max_walk,distances.get(a,math.inf));break
                for b,dist in graph[a].items():distances[b]=min(distances.get(b,math.inf),distances.get(a,math.inf)+dist)
    check(max_walk<=d['fire']['max_rop_walk_m'],'ROP walking reach')
    for pr in d['penetrations']:
        check(pr['wall'] in {w['id'] for w in d['walls']} and all(cid in connections for cid in pr['connections']),'penetration reference: '+pr['id'])
        for cid in pr['connections']:
            if cid not in connections:continue
            point=pr['xyz_site_m'];segments=connections[cid]['points_site_m']
            check(any(abs(math.dist(a,point)+math.dist(point,b)-math.dist(a,b))<1e-4 for a,b in zip(segments,segments[1:])),'penetration outside cable trace: '+pr['id'])
    for actual,expected in zip(d['bom_accessories'],bom_quantities(d)):
        check(actual['quantity']==expected['quantity'] and actual.get('purchase_quantity')==expected.get('purchase_quantity'),'BOM quantity: '+actual['id'])
    parking=d['site']['parking_layout'];sweep=parking_results(d)
    unique(parking['stalls'],'parking stalls');unique(parking['chambers'],'parking chambers')
    duct_segments=[(a[:2],b[:2]) for route in d['routes'] if route['id'] in ['R5','R6','R7','R8'] for a,b in zip(route['points_m'],route['points_m'][1:])]
    for chamber in parking['chambers']:
        pt=chamber['centre_site_m']
        check(any(abs(math.dist(a,pt)+math.dist(pt,b)-math.dist(a,b))<1e-5 for a,b in duct_segments),'chamber outside duct route: '+chamber['id'])
    check(not sweep['clashes'],'parking entry / occupied stall collision: '+', '.join(sweep['clashes']))
    check(d['site']['parking_spaces']==len(parking['stalls']),'parking count')
    vehicle=parking['design_vehicle'];sw=parking['sweep']
    check(math.isclose(vehicle['length_m'],vehicle['wheelbase_m']+vehicle['front_overhang_m']+vehicle['rear_overhang_m']),'vehicle geometry')
    check(sw['turn_radius_m']>=vehicle['minimum_rear_axle_turn_radius_m'] and sweep['steering_deg']<=vehicle['maximum_steering_deg'],'vehicle turning envelope')
    poses=vehicle_poses(parking)
    max_motion=max(math.dist(p,q) for a,b in zip(poses,poses[1:]) for p,q in zip(vehicle_box(parking,a),vehicle_box(parking,b)))
    check(max_motion<=sw['inter_sample_motion_bound_m']<=sw['clearance_m'],'vehicle sweep sampling allowance')
    for c in d['connections']:
        vc=c.get('voltage_check',{})
        if 'upstream_connection' in vc:
            upstream=connections.get(vc['upstream_connection'])
            check('source_min_v' not in vc,'DC cascade has independent source voltage: '+c['id'])
            check(upstream is not None and upstream['ends'][1]==c['ends'][0],'DC cascade continuity: '+c['id'])
    gate=d['network']['external_gate_bus'];common=connections[gate['power_connections'][0]];last=connections[gate['power_connections'][1]]
    gate_current=sum(models[dev[id]['model']]['max_current_a'] for id in gate['reader_ids'])
    check(math.isclose(common['voltage_check']['current_a'],gate_current),'G01 common reader current')
    check(last['voltage_check'].get('upstream_connection')==common['id'],'G01 downstream voltage source')
    check(math.isclose(last['voltage_check']['current_a'],models[dev[gate['reader_ids'][-1]]['model']]['max_current_a']),'G01 last reader current')
    # Pedestrians are routed outside the complete vehicle corridor, independent of AI ROI.
    pedestrian=d['site']['parking_layout']['pedestrian_route_site_m']
    lx,ly,lw,lh=parking['entry_corridor_rect_site_m'];rx=lx+lw;ry=ly+lh
    for a,b in zip(pedestrian,pedestrian[1:]):
        for step in range(101):
            px=a[0]+(b[0]-a[0])*step/100;py=a[1]+(b[1]-a[1])*step/100
            check(not(lx<px<rx and ly<py<ry),'pedestrian path crosses controlled vehicle lane')
    if errors:return errors,None
    r=calculate(d);r['rop_max_walk_m']=max_walk
    check(r['poe_with_margin_w']<=models['SW']['poe_budget_w'],'PoE budget')
    check(r['max_copper_channel_m']<=d['network']['copper_channel_max_m'],'copper channel length')
    check(all(x<=d['network']['copper_permanent_max_m'] for x in r['link_lengths'].values()),'copper permanent length')
    check(r['network_mbps']<=d['network']['uplink_mbps'],'uplink overload')
    check(r['storage_available_tb']>=r['storage_required_tb'],'recording storage capacity')
    check(d['video']['raid']=='RAID6' and d['video']['parity_disks']==2 and len(d['video']['disk_device_ids'])>=4,'RAID6 topology')
    check(all(id in dev and dev[id]['model']=='HDD' for id in d['video']['disk_device_ids']),'storage disk reference')
    check(r['sd_hours']>=d['video']['local_buffer_target_h'],'local storage buffer')
    check(d['video']['licences']['core_device_5y']==r['count']['camera']+r['count']['access_controller'],'VMS licence count')
    check(r['loop_alarm_a']<=loop['max_current_a'] and r['loop_resistance_ohm']<=models['CSP']['loop_max_resistance_ohm'],'loop current/resistance')
    check(r['loop_far_voltage_v']>=max(models[dev[x]['model']]['voltage_min'] for x in order),'FAS far voltage')
    for v in r['voltage_checks']:check(v['voltage_v']>=v['required_v'],'DC voltage: '+v['connection'])
    for bank,selected in zip(r['banks'],d['power']['dc_batteries']):
        check(bank['required_ah']<=bank['selected_ah'],'battery capacity: '+bank['id'])
        check(bank['recharge_h']<=selected['recharge_goal_h'],'recharge duration: '+bank['id'])
        check(len(selected['battery_ids'])==selected['series']*selected['parallel'],'battery series/parallel topology')
    check(r['fire_supply_with_charge_a']<=models['CSP']['psu_i_max_a'],'FAS PSU charging overload')
    check(r['intrusion_supply_with_charge_a']<=models['SSWIN']['psu_a'],'IDS PSU charging overload')
    alarm_aux=sum(models[x['model']].get('alarm_a',0) for x in dev.values() if x['model'] in ['PIR','ETHM'])
    check(alarm_aux<=.5 and models['KEYPAD']['alarm_a']<=.5 and models['SIREN']['alarm_a']<=1.1,'IDS AUX/KPD/output capacity')
    check(r['ups_design_w']<=models['UPS']['rating_w'],'UPS rating')
    check(r['ups_derated_minutes']>=d['power']['ups_target_minutes'],'UPS published runtime insufficient')
    # No independent AC load may disappear from the UPS calculation; PoE counted within switch AC envelope.
    actual={x['id'] for x in dev.values() if x['power_source']=='UPS-0' and x['model']!='EBM'}
    check(actual==set(d['power']['ups_load_device_ids']),'AC load assignment')
    for link in d['network']['media_links_fibre']:
        check(link['used_fibres']+link['spare_fibres']<=link['total_fibres'],'fibre count')
        check(link['loss_db']+link['reserve_db']<=link['budget_db'],'optical budget')
    return errors,r


def self_test(d):
    cases=[]
    def case(name,change,expected=None):
        changed=copy.deepcopy(d);change(changed);cases.append((name,changed,expected))
    case('duplicate ID',lambda x:x['devices'].append(copy.deepcopy(x['devices'][0])))
    case('unknown cable end',lambda x:x['connections'][0]['ends'][0].update(device='MISSING'))
    case('wrong cable quantity',lambda x:x['connections'][0].update(purchase_m=1))
    case('wrong port',lambda x:x['connections'][0]['ends'][0].update(port='MISSING'))
    case('room mismatch',lambda x:x['devices'][0]['location'].update(room_or_area='R103'))
    case('PoE overload',lambda x:x['equipment_models']['SW'].update(poe_budget_w=1))
    case('disk undersizing',lambda x:x['video'].update(disk_tb=.1))
    case('battery undersizing',lambda x:x['equipment_models']['BAT'].update(capacity_ah=1))
    case('UPS runtime',lambda x:x['power'].update(ups_target_minutes=999))
    case('loop address collision',lambda x:[v.update(address=1) for v in x['devices'] if 'address' in v])
    case('bad DC voltage',lambda x:next(c for c in x['connections'] if 'voltage_check' in c)['voltage_check'].update(source_min_v=1))
    case('stale BOM',lambda x:next(b for b in x['bom_accessories'] if b['id']=='B-LIC').update(quantity=1))
    case('unsafe pedestrian path',lambda x:x['site']['parking_layout'].update(pedestrian_route_site_m=[[65,11],[65,19]]))
    case('stale penetration geometry',lambda x:x['penetrations'][0].update(xyz_site_m=[0,0,0]))
    case('nonexistent control output',lambda x:x['fire']['control_matrix'][0]['outputs'].append('CSP-0:UNKNOWN'))
    case('occupied stall blocks entry',lambda x:x['site']['parking_layout']['stalls'].append(dict(id='P04',rect_site_m=[62,20,2.5,5],accessible=False)), 'parking entry / occupied stall collision')
    case('D01 outside far clip',lambda x:next(v for v in x['devices'] if v['id']=='C01')['view'].update(far_clip_m=8), 'ACS opening outside verification 3D frame: D01')
    case('AI line below image',lambda x:next(v for v in x['devices'] if v['id']=='C08')['view'].update(down_tilt_deg=0), 'AI line feet/body outside 3D frame')
    case('PATH1 upper body clipped',lambda x:next(v for v in x['devices'] if v['id']=='C02')['view'].update(down_tilt_deg=45), 'PATH1 upper-body outside 3D frame: C02')
    case('independent optimistic last-reader voltage',lambda x:next(c for c in x['connections'] if c['id']=='DC-RD-G01-OUT')['voltage_check'].update(source_min_v=12), 'DC cascade has independent source voltage')
    for name,changed,expected in cases:
        errors,_=validate(changed)
        if not errors:raise SystemExit('Self-test failed to reject '+name)
        if expected and not any(expected in e for e in errors):raise SystemExit('Self-test rejected for unrelated reason: '+name)
    print(f'Validator negative tests: {len(cases)}/{len(cases)} rejected.')


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--self-test',action='store_true');ap.add_argument('--report',type=Path);args=ap.parse_args()
    d=load_design();errors,r=validate(d)
    if errors:raise SystemExit('\n'.join(sorted(set(errors))))
    stale=[str(p.relative_to(ROOT)) for p,t in outputs(d).items() if not p.exists() or p.read_text()!=t]
    if stale:raise SystemExit('Stale export: '+', '.join(stale)+'; make data')
    if args.self_test:self_test(d)
    if args.report:args.report.parent.mkdir(parents=True,exist_ok=True);args.report.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    print(f"OK: {len(d['devices'])} devices/assemblies, {len(d['connections'])} connections; 1 data source.")
    print(f"PoE with reserve {r['poe_with_margin_w']:.1f}/384W; longest channel {r['max_copper_channel_m']:.1f}m; FAS {r['loop_length_m']:.1f}m, {r['loop_far_voltage_v']:.2f}V; manual call-point walk {r['rop_max_walk_m']:.2f}m.")
    print(f"Recording {r['storage_required_tb']:.3f}/{r['storage_available_tb']:.1f}TB; UPS {r['ups_load_w']:.1f}W, after derating {r['ups_derated_minutes']:.2f}min; cable purchase {r['cable_purchase_m']}m.")
    print('Consistency checks do not establish engineering correctness or standards compliance and are not site-test results.')


if __name__=='__main__':main()
