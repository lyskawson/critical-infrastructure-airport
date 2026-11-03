#!/usr/bin/env python3
"""Deterministic calculations and text exports. design.json is the only input model."""
import argparse
from collections import Counter, defaultdict
import hashlib
import json
import math
from pathlib import Path
from design_geometry import camera_axes, optical_results, parking_results, project

ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / 'data/design.json'


def load_design(path=MODEL):
    return json.loads(Path(path).read_text())


def lengths(c):
    p = c['points_site_m']
    plan = sum(math.dist(a[:2], b[:2]) for a, b in zip(p, p[1:]))
    vertical = sum(abs(a[2]-b[2]) for a, b in zip(p, p[1:]))
    installed = plan + vertical + c['service_m']
    purchase = math.ceil(installed*(1+c['waste_fraction'])-1e-8)
    return plan, vertical, installed, purchase


def calculate(d):
    dev = {v['id']: v for v in d['devices']}
    models = d['equipment_models']
    count = Counter(models[v['model']]['category'] for v in dev.values())
    cables = defaultdict(lambda: dict(plan_m=0., vertical_m=0., installed_m=0., purchase_m=0, connections=0))
    link_lengths = defaultdict(float)
    voltage = []
    for c in d['connections']:
        pl, ve, ins, buy = lengths(c)
        if not c.get('included_in_assembly') and not c.get('covered_by_bom'):
            t = cables[c['cable_type']]
            for key, val in [('plan_m', pl), ('vertical_m', ve), ('installed_m', ins), ('purchase_m', buy), ('connections', 1)]:
                t[key] += val
        if 'link_group' in c:
            link_lengths[c['link_group']] += ins
    by_id = {c['id']: c for c in d['connections']}
    resolved = {}; resolving = set()
    def voltage_result(cid):
        if cid in resolved:return resolved[cid]
        if cid in resolving:raise ValueError('Cyclic DC supply: '+cid)
        resolving.add(cid)
        c = by_id[cid]; v = c['voltage_check']; ct = d['cable_types'][c['cable_type']]
        upstream = v.get('upstream_connection')
        source = voltage_result(upstream)['voltage_v'] if upstream else v['source_min_v']
        resistance = 2*ct['rho_ohm_mm2_per_m']*lengths(c)[2]/ct['section_mm2']
        drop = resistance*v['current_a'] + v.get('extra_loss_v', 0)
        result = dict(connection=cid, resistance_ohm=resistance, source_v=source, drop_v=drop,
                      voltage_v=source-drop, required_v=v['min_device_v'])
        resolving.remove(cid);resolved[cid]=result
        return result
    voltage = [voltage_result(c['id']) for c in d['connections'] if 'voltage_check' in c]
    poe_pd = sum(models[v['model']].get('poe_pd_max_w', 0) for v in dev.values())
    poe_pse = sum(models[v['model']].get('poe_pse_allocation_w', 0) for v in dev.values())
    p = d['power']; v = d['video']; ncam = count['camera']
    ups_w = sum(models[dev[id]['model']].get('ac_max_w', models[dev[id]['model']].get('ac_design_w', 0)) for id in p['ups_load_device_ids'])
    ups_design = ups_w*p['ups_reserve_factor']
    curve = p['ups_runtime_curve']
    point = next((x for x in curve['points_w_min'] if x[0] >= ups_design), None)
    runtime = point[1]*curve['manufacturer_tolerance_factor']*curve['age_design_factor'] if point else 0
    recording_tb = ncam*v['bitrate_mbps_max']*1e6/8*v['retention_days']*86400/1e12
    available_tb = (len(v['disk_device_ids'])-v['parity_disks'])*v['disk_tb']*v['usable_fraction']
    sd_h = v['sd_gb']*1e9*v['sd_usable_fraction']/(v['bitrate_mbps_max']*1e6/8)/3600
    loop_points = [x for x in dev.values() if x.get('fire_loop') == 'L1']
    loop_s = sum(models[x['model']]['standby_a'] for x in loop_points)
    loop_a = sum(models[x['model']]['alarm_a'] for x in loop_points)
    loop_length = sum(lengths(c)[2] for c in d['connections'] if c['id'] in d['fire']['loops'][0]['connections'])
    ct = d['cable_types']['FIRE']; loop_r = 2*ct['rho_ohm_mm2_per_m']*loop_length/ct['section_mm2']
    # At one feed after an open circuit, all loop loads are pessimistically at the far end.
    loop_v = d['fire']['loops'][0]['output_min_v'] - loop_r*loop_a
    f = d['fire']; fm = models[dev[f['panel']]['model']]
    i_fs = fm['battery_base_standby_a']+24*loop_s/(f['battery_min_v']*f['loop_converter_efficiency_min'])
    i_fa = fm['battery_base_alarm_a']+24*loop_a/(f['battery_min_v']*f['loop_converter_efficiency_min'])
    intrusion = [x for x in dev.values() if x['power_source'] == 'SSWiN-0' and x['model'] != 'BAT']
    im = models['SSWIN']
    i_is = im['standby_a']+sum(models[x['model']].get('standby_a', 0) for x in intrusion)+p['intrusion_input_supervision_a']
    i_ia = im['alarm_a']+sum(models[x['model']].get('alarm_a', 0) for x in intrusion)+p['intrusion_input_supervision_a']
    banks = []
    for bank in p['dc_batteries']:
        standby, alarm = (i_fs, i_fa) if bank['source'] == 'CSP-0' else (i_is, i_ia)
        q = bank['factor']*(standby*bank['standby_h']+alarm*bank['alarm_h'])
        cap = models[dev[bank['battery_ids'][0]]['model']]['capacity_ah']*bank['parallel']
        ch = p['fire_charge_effective_a'] if bank['source'] == 'CSP-0' else im['charge_a']
        banks.append(dict(id=bank['id'], standby_a=standby, alarm_a=alarm, required_ah=q, selected_ah=cap, charge_a=ch,
                          recharge_h=p['recharge_fraction']*cap*p['recharge_loss_factor']/ch))
    bw = d['network']['bandwidth']
    recording_mbps = ncam*v['bitrate_mbps_max']
    nas_mbps = recording_mbps*(2 if bw['nas_write_and_read'] else 1)
    pc_mbps = recording_mbps + nas_mbps + bw['other_mbps']
    network_mbps = pc_mbps*bw['headroom']
    return dict(optical=optical_results(d), parking=parking_results(d),
                count=dict(count), cables=dict(cables), cable_purchase_m=sum(x['purchase_m'] for x in cables.values()),
                cable_installed_m=sum(x['installed_m'] for x in cables.values()), link_lengths=dict(link_lengths),
                max_copper_channel_m=max(link_lengths.values())+d['network']['patch_allowance_m'], voltage_checks=voltage,
                poe_pd_w=poe_pd, poe_pse_w=poe_pse, poe_with_margin_w=poe_pse*d['network']['poe_reserve_factor'],
                ups_load_w=ups_w, ups_design_w=ups_design, ups_curve_point=point, ups_derated_minutes=runtime,
                storage_raw_tb=recording_tb, storage_required_tb=recording_tb*v['capacity_factor'], storage_available_tb=available_tb,
                sd_hours=sd_h, loop_standby_a=loop_s, loop_alarm_a=loop_a, loop_length_m=loop_length,
                loop_resistance_ohm=loop_r, loop_far_voltage_v=loop_v, banks=banks,
                fire_supply_with_charge_a=.3+24*loop_a/(18*.8)+p['fire_charge_supply_allocation_a'],
                intrusion_supply_with_charge_a=i_ia+im['charge_a'], network_mbps=network_mbps,
                fire_standby_battery_a=i_fs, fire_alarm_battery_a=i_fa,
                recording_mbps=recording_mbps, nas_mbps=nas_mbps,
                ac_boundary_va=p['ups_load_device_ids'] and (ups_design/p['ups_efficiency_floor']+p['ups_charge_input_allowance_w']+p['fire_ac_max_va']+p['intrusion_transformer_va']))


def bom_quantities(d):
    """Quantities that can be derived, with no independent material inventory."""
    categories = Counter(d['equipment_models'][x['model']]['category'] for x in d['devices'])
    route = {r['id']: r for r in d['routes']}
    links = {c['link_group'] for c in d['connections'] if 'link_group' in c}
    zones = {e['port'] for c in d['connections'] for e in c['ends'] if e['device']=='SSWiN-0' and e['port'].startswith('Z')}
    spine = lambda ids: sum(math.ceil(sum(math.dist(a,b) for a,b in zip(route[id]['points_m'],route[id]['points_m'][1:]))/5)*5 for id in ids)
    duct = sum(math.dist(a,b) for id in ['R5','R6','R7','R8'] for a,b in zip(route[id]['points_m'],route[id]['points_m'][1:]))
    values = {
        'R1_R2_5m_stock': spine(['R1','R2']),
        'R3_R4_5m_stock': spine(['R3','R4']),
        'R5_R8_plus10_5m_stock': math.ceil(duct*1.1/5)*5,
        'penetrations': len(d['penetrations']),
        'licensed_devices': categories['camera']+categories['access_controller'],
        'intrusion_eol': 2*len(zones),
        'access_dps_eol': 2*len(d['access_points']),
        'ethernet_patchcords': 2*len(links),
        'patchpanels': math.ceil(len(links)/24),
        'parking_chambers': len(d['site']['parking_layout']['chambers']),
        'egress_hardware': sum(o.get('egress_mechanical',False) and (o.get('access_controlled') or o['id'].startswith('E')) for o in d['openings']),
        'fire_clamps': math.ceil(sum(c['plan_m']+c['vertical_m'] for c in d['connections'] if c['cable_type']=='FIRE')/.3*1.1),
    }
    result=[]
    for entry in d['bom_accessories']:
        x=dict(entry)
        x['quantity']=values.get(x.get('quantity_rule'),x['quantity'])
        if x.get('quantity_rule')=='intrusion_eol':
            x['purchase_quantity']=x['quantity']-2*categories['intrusion_detector']
        result.append(x)
    return result


def tex(s):
    mapping = {'\\': r'\textbackslash{}', '&': r'\&', '%': r'\%', '$': r'\$', '#': r'\#', '_': r'\_', '{': r'\{', '}': r'\}', '~': r'\textasciitilde{}', '^': r'\textasciicircum{}'}
    return ''.join(mapping.get(c, c) for c in str(s)).replace('≤', r'$\leq$').replace('>=', r'$\geq$').replace('<=', r'$\leq$')


def num(x, decimals=2):
    return f'{x:.{decimals}f}'


def coordinate(point):
    return '('+'; '.join(num(v,2) for v in point)+')'


def table(headers, rows, widths):
    fmt = '@{}' + ''.join('P{'+w+'}' for w in widths) + '@{}'
    return '\\begingroup\\small\\setlength{\\tabcolsep}{3pt}\\setlength{\\LTleft}{0pt}\n\\begin{longtable}{'+fmt+'}\n\\toprule\n'+' & '.join(r'\textbf{'+tex(h)+'}' for h in headers)+r'\\\midrule\endhead'+'\n'+''.join(' & '.join(str(v) for v in row)+r'\\'+'\n' for row in rows)+r'\bottomrule\end{longtable}\endgroup'+'\n'


def outputs(d):
    r = calculate(d); dev = {v['id']: v for v in d['devices']}; models = d['equipment_models']; counts = r['count']
    digest = hashlib.sha256(MODEL.read_bytes()).hexdigest()
    macros = {'ModelRevision': d['revision'], 'ModelHash': digest[:12], 'ParkingCount':len(d['site']['parking_layout']['stalls']), 'CameraCount': counts['camera'], 'DoorCount': len(d['access_points'])-1,
              'AccessCount':len(d['access_points']), 'ReaderCount':counts['reader'], 'FireDetectorCount':counts['fire_detector'], 'RopCount':counts['fire_callpoint'],
              'FireSounderCount':counts['fire_sounder'], 'PirCount':counts['intrusion_detector'], 'ConnectionCount':len(d['connections']), 'DeviceCount':len(dev),
              'PoePD':num(r['poe_pd_w'],1), 'PoePSE':num(r['poe_pse_w'],1), 'PoeMargin':num(r['poe_with_margin_w'],1),
              'UPSLoad':num(r['ups_load_w'],1), 'UPSDesign':num(r['ups_design_w'],2), 'UPSCurveW':str(r['ups_curve_point'][0]),
              'UPSCurveMin':num(r['ups_curve_point'][1],1), 'UPSMinutes':num(r['ups_derated_minutes'],1),
              'StorageRaw':num(r['storage_raw_tb'],4), 'StorageNeed':num(r['storage_required_tb'],3), 'StorageHave':num(r['storage_available_tb'],1),
              'SDHours':num(r['sd_hours'],1), 'LoopLength':num(r['loop_length_m'],1), 'LoopResistance':num(r['loop_resistance_ohm'],2),
              'LoopVoltage':num(r['loop_far_voltage_v'],2), 'LoopStandbyMA':num(r['loop_standby_a']*1000,2),'LoopAlarmMA':num(r['loop_alarm_a']*1000,2),
              'CopperMax':num(r['max_copper_channel_m'],1), 'CableTotal':num(r['cable_purchase_m'],0), 'NetworkLoad':num(r['network_mbps'],1),
              'FireSupplyA':num(r['fire_supply_with_charge_a'],3), 'IntrusionSupplyA':num(r['intrusion_supply_with_charge_a'],3), 'BoundaryVA':num(r['ac_boundary_va'],0)}
    gate_in=next(v for v in r['voltage_checks'] if v['connection']=='DC-RD-G01-IN')
    gate_out=next(v for v in r['voltage_checks'] if v['connection']=='DC-RD-G01-OUT')
    gate_c=next(c for c in d['connections'] if c['id']=='DC-RD-G01-IN')
    macros.update(GateReaderVoltage=num(gate_out['voltage_v'],3),GateFirstVoltage=num(gate_in['voltage_v'],3),
                  GateCurrent=num(gate_c['voltage_check']['current_a'],2),GateSection=num(d['cable_types'][gate_c['cable_type']]['section_mm2'],0),
                  DuctLength=num(sum(math.dist(a,b) for route in d['routes'] if route['id'] in ['R5','R6','R7','R8'] for a,b in zip(route['points_m'],route['points_m'][1:])),1),
                  DuctPurchase=next(v['quantity'] for v in bom_quantities(d) if v['id']=='B-DUCT'),
                  AIHeightPx=num(r['optical']['ai_roi']['min_person_height_px'],0))
    for prefix, bank in zip(['Fire','Intrusion'],r['banks']):
        for key, val in [('Standby',bank['standby_a']),('Alarm',bank['alarm_a']),('Ah',bank['required_ah']),('Recharge',bank['recharge_h'])]:macros[prefix+key]=num(val,3 if key in ['Standby','Alarm'] else 2)
    t = '% Generated from data/design.json; do not edit. SHA256 '+digest+'\n'
    t += ''.join('\\newcommand{\\'+k+'}{'+tex(v)+'}\n' for k,v in macros.items())
    t += '\\newcommand{\\ModelRooms}{\n'+table(['ID / function','Local plan [m]','Protection'],[(tex(x['id']+' '+x['name']),tex(str(x['rect_local_m'])),tex(x['coverage'])) for x in d['rooms']],['32mm','32mm','86mm'])+'}\n'
    t += '\\newcommand{\\CameraTable}{\n'+table(['ID / location','Position / target [m]','View / direction'],[(tex(x['id']+' / '+x['location']['room_or_area']),tex(coordinate(x['location']['xyz_m'])+' / '+coordinate(x['target']['xyz_m'])+' ('+x['target']['frame']+')'),tex(num(x['target']['width_m'],2)+' m; '+num(x['view']['ppm'],0)+' px/m; az. '+num(x['view']['azimuth_deg'],1)+'; tilt '+num(x['view']['down_tilt_deg'],1)+'; HFOV '+num(x['view']['hfov_deg'],1))) for x in d['devices'] if x['model']=='CAM'],['25mm','63mm','62mm'])+'}\n'
    t += '\\newcommand{\\FirePointTable}{\n'+table(['ID / model','Room / local position [m]','L1 / address'],[(tex(x['id']+' / '+x['model']),tex(x['location']['room_or_area']+' '+str(x['location']['xyz_m'])),str(x['address'])) for x in sorted(d['devices'],key=lambda x:x.get('address',999)) if 'fire_loop' in x],['40mm','88mm','22mm'])+'}\n'
    t += '\\newcommand{\\DeviceBom}{\n'+table(['Model and devices','Count','Power supply'],[(tex(models[mid]['name']),str(sum(x['model']==mid for x in d['devices'])),tex(', '.join(sorted({x['power_source'] for x in d['devices'] if x['model']==mid})))) for mid in models if any(x['model']==mid for x in d['devices'])],['92mm','13mm','45mm'])+'}\n'
    t += '\\newcommand{\\CableBom}{\n'+table(['Cable type','Sections','Plan / vertical [m]','Purchase [m]'],[(tex(k),str(v['connections']),num(v['plan_m'],1)+' / '+num(v['vertical_m'],1),str(v['purchase_m'])) for k,v in sorted(r['cables'].items())],['46mm','18mm','54mm','32mm'])+'}\n'
    t += '\\newcommand{\\AccessoryBom}{\n'+table(['Accessory / licence / stock','Purchase qty','Unit'],[(tex(x['name']),str(x.get('purchase_quantity',x['quantity'])),tex(x['unit'])) for x in bom_quantities(d)],['110mm','23mm','17mm'])+'}\n'
    t += '\\newcommand{\\ConnectionTable}{\n'+table(['Cable','Devices and ports','Type','Plan/vertical/slack [m]','Purchase [m]'],[(tex(c['id']),tex(' -> '.join(e['device']+':'+e['port'] for e in c['ends'])),tex(c['cable_type']),num(c['plan_m'],1)+'/'+num(c['vertical_m'],1)+'/'+num(c['service_m'],1),str(c['purchase_m'])+('*' if c.get('included_in_assembly') or c.get('covered_by_bom') else '')) for c in d['connections']],['28mm','51mm','19mm','33mm','19mm'])+'}\n'
    t += '\\newcommand{\\VoltageTable}{\n'+table(['Circuit','Current [A]','Input / drop [V]','Voltage / min. [V]'],[(tex(x['connection']),num(next(c['voltage_check']['current_a'] for c in d['connections'] if c['id']==x['connection']),2),num(x['source_v'],3)+' / '+num(x['drop_v'],3),num(x['voltage_v'],3)+' / '+num(x['required_v'],2)) for x in r['voltage_checks']],['48mm','20mm','35mm','47mm'])+'}\n'
    t += '\\newcommand{\\OpticalVerificationTable}{\n'+table(['Point / camera','Height [m]','Min. px/m','Max. |x| / |y|'],[(tex(v['id']+' / '+v['camera']),'1.2--2.0',num(v['min_ppm'],1),num(v['max_abs_x'],3)+' / '+num(v['max_abs_y'],3)) for v in r['optical']['kd']],['40mm','30mm','25mm','55mm'])+'}\n'
    t += '\\newcommand{\\PathViewTable}{\n'+table(['Camera / view','y segment [m]','Min. px/m','Max. |x| / |y|'],[(tex(v['camera']+' / '+['front','rear','left profile','right profile'][i]),num(d['path_observation']['views'][i]['segment_local_m'][0][1],1)+'--'+num(d['path_observation']['views'][i]['segment_local_m'][1][1],1),num(v['min_ppm'],1),num(v['max_abs_x'],3)+' / '+num(v['max_abs_y'],3)) for i,v in enumerate(r['optical']['path'])],['44mm','27mm','25mm','54mm'])+'}\n'
    t += '\\newcommand{\\OpticsTable}{\n'+table(['Camera','Azimuth / tilt','HFOV / VFOV','Near / far [m]'],[(tex(c['id']),num(c['view']['azimuth_deg'],2)+' / '+num(c['view']['down_tilt_deg'],2),num(c['view']['hfov_deg'],2)+' / '+num(c['view']['vfov_deg'],2),num(c['view']['near_clip_m'],1)+' / '+num(c['view']['far_clip_m'],1)) for c in d['devices'] if c['model']=='CAM'],['23mm','43mm','43mm','41mm'])+'}\n'
    t += '\\newcommand{\\OpeningTable}{\n'+table(['Opening','Position / frame [m]','Clear width [m]','Sides'],[(tex(o['id']),tex(str(o.get('centre_local_m',o.get('centre_site_m')))+' / '+('T0' if 'centre_local_m' in o else 'SITE')),num(o['width_clear_m'],1),tex(' / '.join(o['sides']))) for o in d['openings']],['20mm','65mm','25mm','40mm'])+'}\n'
    t += '\\newcommand{\\RouteTable}{\n'+table(['Route / frame','Main points [m]'],[(tex(o['id']+' / '+o['frame']),tex(' -> '.join(map(str,o['points_m'])))) for o in d['routes']],['27mm','123mm'])+'}\n'
    t += '\\newcommand{\\PowerTable}{\n'+table(['UPS load','AC envelope [W]','Basis'],[(tex(i),num(models[dev[i]['model']].get('ac_max_w',models[dev[i]['model']].get('ac_design_w',0)),1),tex('full AC including PoE' if i=='SW-0' else 'design limit including adapter')) for i in d['power']['ups_load_device_ids']],['50mm','35mm','65mm'])+'}\n'
    # Authoritative bibliography from same source ledger.
    b = '\\begin{thebibliography}{99}\n'
    for s in d['sources']:
        b += '\\bibitem{'+s['id']+'} '+tex(s['title'])+'. '+tex(s['pinpoint'])+'. Accessed: '+s['access_date']+'.'
        b += '\n'+('\\texttt{data/design.json}' if s['id']=='OWN' else '\\url{'+s['url'].replace('%',r'\%')+'}')+'\n\n'
    b += '\\end{thebibliography}\n'
    # Markdown register is an export, including full 3D traces for independent handoff.
    md = ['# Device and connection register - package A','',f"Export from `data/design.json`, revision `{d['revision']}`, SHA256 `{digest}`.", 'Do not edit independently; regenerate with `make data`. Units: m, W, A; points are not surveyed.', '', '## Devices', '', '| ID | Model | Location; frame; (x,y,z) | Power supply | Port/circuit |', '|---|---|---|---|---|']
    con_by_dev = defaultdict(list)
    for c in d['connections']:
        for e in c['ends']:con_by_dev[e['device']].append(c['id']+':'+e['port'])
    for x in d['devices']:
        loc = x['location']; info = ', '.join(con_by_dev[x['id']]) or ('mechanical: '+x.get('mechanical_parent','no cable'))
        md.append(f"| {x['id']} | {models[x['model']]['name']} | {loc['room_or_area']}; {loc['frame']}; {loc['xyz_m']} | {x['power_source']} | {info} |")
    md += ['', 'DB-400 bases belong to assemblies F01-F11; each has its own base, included in its name and BOM. A bracket or fitting is not an additional electrical point.', '', '## ACS and independent egress', '']
    for a in d['access_points']:md += [f"### {a['id']} - {a['from_zone']} -> {a['to_zone']}", f"{a['controller']}, channel {a['channel']}; readers {', '.join(a['readers'])}; lock {a['lock']}; state {a['door_contact']}; handle {a['rex']}.",f"Normal: {a['normal']}. No LAN: {a['no_lan']}. No power: {a['no_power']}. Fire: {a['fire']}. Egress path: {a['physical_egress_path']}.", '']
    md += ['## CCTV / target geometry', '', '| ID | Purpose and target position | Width / px per m | Azimuth / tilt / HFOV |','|---|---|---|---|']
    for x in d['devices']:
        if x['model']=='CAM':md.append(f"| {x['id']} | {x['target']['purpose']}; {x['target']['frame']} {x['target']['xyz_m']} | {x['target']['width_m']} / {x['view']['ppm']} | {x['view']['azimuth_deg']} / {x['view']['down_tilt_deg']} / {x['view']['hfov_deg']} |")
    md += ['', '## 3D views and geometry for B', '',
           'Model: '+d['optical_model']['projection']+'. '+d['optical_model']['distortion']+'.',
           d['optical_model']['axes_definition']+'. Near/far: '+d['optical_model']['near_far_definition']+'.',
           'The corner rays below are unnormalised SITE vectors from the camera. The field is a rectangular pyramid between these rays, with positive optical depth and clipping by near/far radius and opaque walls. Target checks also require |x|,|y| <=0.96. Table image width refers to the plane perpendicular to the optical axis through the target, not a ground projection.', '']
    for c in d['devices']:
        if c['model']!='CAM':continue
        f,right,up=camera_axes(c);h=math.tan(math.radians(c['view']['hfov_deg']/2));v=math.tan(math.radians(c['view']['vfov_deg']/2))
        rays=[[round(f[j]+xx*h*right[j]+yy*v*up[j],8) for j in range(3)] for xx,yy in [(-1,-1),(1,-1),(1,1),(-1,1)]]
        md.append(f"- {c['id']}: HFOV/VFOV {c['view']['hfov_deg']:.6f}/{c['view']['vfov_deg']:.6f} deg; near/far {c['view']['near_clip_m']}/{c['view']['far_clip_m']} m; BL,BR,TR,TL rays: {rays}.")
    md += ['', 'PATH1: '+json.dumps(d['path_observation']['views'],ensure_ascii=False),
           '', 'AI: detection point at feet z=0; person envelope '+json.dumps(d['ai']['person_envelope'],ensure_ascii=False)+'.',
           'Feet ROI in SITE: '+str(d['ai']['zone_polygon_site_m'])+'; line: '+str(d['ai']['line_site_m'])+'.',
           'ROI in normalised image coordinates (x right, y up): '+str([[round(project(dev['C08'],p+[0])[key],6) for key in ['x','y']] for p in d['ai']['zone_polygon_site_m']])+'.',
           '', '## Car park and manoeuvre', '', json.dumps(d['site']['parking_layout'],ensure_ascii=False,indent=2),
           '', 'View and manoeuvre results are also included in the calculations at the end of the register.']
    md += ['', '## FAS: L1 in connection order', '', ' -> '.join(['CSP-0:L1A']+d['fire']['loops'][0]['devices']+['CSP-0:L1B']), '', '| ID | Address | Room | Local coordinates |','|---|---|---|---|']
    for id in d['fire']['loops'][0]['devices']:
        x=dev[id];md.append(f"| {id} | {x['address']} | {x['location']['room_or_area']} | {x['location']['xyz_m']} |")
    md += ['', '## Cause-and-effect matrix', '']
    for x in d['fire']['control_matrix']:md += [f"- **{x['id']}** {x['trigger']}; condition: {x['condition']}; outputs: {', '.join(x['outputs']) or 'no electrical control'}; effect: {x['action']}; supervision: {x['supervision']}; reset: {x['reset']}."]
    md += ['', '## Wall penetrations', '', '| ID | Wall | SITE position | Cables |', '|---|---|---|---|']
    for pr in d['penetrations']:md.append(f"| {pr['id']} | {pr['wall']} | {pr['xyz_site_m']} | {', '.join(pr['connections'])} |")
    md += ['', '## Cables - complete SITE paths', '', 'Purchase = ceil((plan + vertical + service slack) * (1 + waste)). Factory connections and patch cords listed as accessories do not increase installation-cable quantities. OSDP data (RS485) and reader power (DC-READER) use separate cables and connections, without counting one cable twice.', '', '| ID | Endpoints | Type; route | Plan / vertical / slack / purchase [m] | SITE points (x,y,z) |','|---|---|---|---|---|']
    for c in d['connections']:
        note = ' (factory / accessories)' if c.get('included_in_assembly') or c.get('covered_by_bom') else ''
        md.append('| '+c['id']+' | '+' -> '.join(e['device']+':'+e['port'] for e in c['ends'])+f" | {c['cable_type']}; {c['route']} | {c['plan_m']} / {c['vertical_m']} / {c['service_m']} / {c['purchase_m']}{note} | "+' -> '.join(map(str,c['points_site_m']))+' |')
    md += ['', '## Calculation results', '', '```json',json.dumps(r,ensure_ascii=False,indent=2),'```', '', '## Parameter sources', '']
    for s in d['sources']:md.append(f"- **{s['id']}** {s['title']}; {s['pinpoint']}; {s['url']}; accessed {s['access_date']}.")
    return {ROOT/'generated/design-data.tex':t, ROOT/'generated/references.tex':b, ROOT/'docs/device-register.md':'\n'.join(md)+'\n'}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');args=ap.parse_args()
    stale=[]
    for path,content in outputs(load_design()).items():
        if args.check:
            if not path.exists() or path.read_text()!=content:stale.append(str(path.relative_to(ROOT)))
        else:path.parent.mkdir(parents=True,exist_ok=True);path.write_text(content)
    if stale:raise SystemExit('Stale export: '+', '.join(stale)+'; run make data')
    print('Data export: '+('current' if args.check else 'written'))


if __name__=='__main__':main()
