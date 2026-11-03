"""Explicit pinhole geometry and low-speed vehicle envelope; no field-test claims."""
import math


def to_site(d, point, frame):
    xyz = list(point) + [0] * (3-len(point))
    if frame == 'SITE':
        return xyz
    transform = d['coordinates']['local_transform'][frame]
    if transform['rotation_deg'] != 0:
        raise ValueError('Unsupported rotated frame')
    return [v+offset for v, offset in zip(xyz, transform['translation_m'])]


def camera_axes(camera):
    a, t = map(math.radians, [camera['view']['azimuth_deg'], camera['view']['down_tilt_deg']])
    return ([math.cos(a)*math.cos(t), math.sin(a)*math.cos(t), -math.sin(t)],
            [math.sin(a), -math.cos(a), 0],
            [math.cos(a)*math.sin(t), math.sin(a)*math.sin(t), math.cos(t)])


def project(camera, point_site):
    delta = [p-c for p, c in zip(point_site, camera['location']['xyz_site_m'])]
    forward, right, up = camera_axes(camera)
    dot = lambda axis: sum(a*b for a, b in zip(delta, axis))
    depth = dot(forward)
    tangent = math.tan(math.radians(camera['view']['hfov_deg']/2))
    if depth <= 0:
        return dict(x=math.inf, y=math.inf, depth=depth, radius=math.hypot(*delta[:2]))
    aspect = camera['video_vertical_px']/camera['video_horizontal_px']
    return dict(x=dot(right)/(depth*tangent), y=dot(up)/(depth*tangent*aspect),
                depth=depth, radius=math.hypot(*delta[:2]))


def in_frame(d, camera, p):
    limit = d['optical_model']['normalised_image_limit']
    return (p['depth'] > 0 and abs(p['x']) <= limit and abs(p['y']) <= limit
            and camera['view']['near_clip_m'] <= p['radius'] <= camera['view']['far_clip_m'])


def image_ppm(camera, point, width_axis):
    # Project a physical 0.6 m transverse segment, including oblique perspective.
    a = project(camera, [point[i]-.3*width_axis[i] for i in range(3)])
    b = project(camera, [point[i]+.3*width_axis[i] for i in range(3)])
    return abs(b['x']-a['x'])*camera['video_horizontal_px']/1.2


def line_samples(a, b, step=.1):
    count = max(1, math.ceil(math.dist(a, b)/step))
    return [[x+(y-x)*i/count for x, y in zip(a, b)] for i in range(count+1)]


def frame_result(d, camera, points, axis):
    projected = [project(camera, p) for p in points]
    return dict(visible=all(in_frame(d, camera, p) for p in projected),
                max_abs_x=max(abs(p['x']) for p in projected),
                max_abs_y=max(abs(p['y']) for p in projected),
                min_ppm=min(image_ppm(camera, p, axis) for p in points),
                min_radius_m=min(p['radius'] for p in projected),
                max_radius_m=max(p['radius'] for p in projected), samples=len(points))


def optical_results(d):
    devices = {x['id']: x for x in d['devices']}
    openings = {x['id']: x for x in d['openings']}
    walls = {x['id']: x for x in d['walls']}
    kd, path = [], []
    for a in d['access_points']:
        opening = openings[a['id']]
        frame = 'T0' if 'centre_local_m' in opening else 'SITE'
        centre = opening.get('centre_local_m', opening.get('centre_site_m'))
        if opening.get('wall'):
            w = walls[opening['wall']]
            length = math.dist(w['a'], w['b'])
            axis = [(w['b'][i]-w['a'][i])/length for i in range(2)]+[0]
        else:
            axis = [1, 0, 0]
        v = a['verification']
        points = [to_site(d, [centre[0]+offset*axis[0], centre[1]+offset*axis[1], z], frame)
                  for offset in [-opening['width_clear_m']/2, 0, opening['width_clear_m']/2]
                  for z in v['height_range_m']]
        for cid in a['verification_cameras']:
            kd.append(dict(id=a['id'], camera=cid, minimum_ppm=v['minimum_ppm'],
                           **frame_result(d, devices[cid], points, axis)))
    spec = d['path_observation']
    for v in spec['views']:
        centres = line_samples(*v['segment_local_m'])
        half = spec['person_envelope']['half_size_xy_m']
        points = [to_site(d, [p[0]+lateral+dx, p[1]+dy, z], 'T0')
                  for p in centres for lateral in [-spec['centre_lateral_tolerance_m'], spec['centre_lateral_tolerance_m']]
                  for dx in [-half, half] for dy in [-half, half] for z in v['height_range_m']]
        path.append(dict(camera=v['camera'], minimum_ppm=v['minimum_ppm'],
                         **frame_result(d, devices[v['camera']], points, v['width_axis_site'])))
    ai = d['ai']; camera = devices[ai['camera_ids'][0]]
    polygon = ai['zone_polygon_site_m']
    # Current ROI is an axis-aligned rectangle; require exactly this contract.
    left, right = min(p[0] for p in polygon), max(p[0] for p in polygon)
    bottom, top = min(p[1] for p in polygon), max(p[1] for p in polygon)
    centres = [[x[0], y[0]] for x in line_samples([left], [right], .25)
               for y in line_samples([bottom], [top], .25)]
    line = line_samples(*ai['line_site_m'])
    half = ai['person_envelope']['half_size_xy_m']
    prism = lambda ps: [[p[0]+dx, p[1]+dy, z] for p in ps for dx in [-half, half]
                       for dy in [-half, half] for z in ai['person_envelope']['height_range_m']]
    axis = camera_axes(camera)[1]
    region = frame_result(d, camera, prism(centres), axis)
    event_line = frame_result(d, camera, prism(line), axis)
    heights = []
    for p in centres:
        foot = project(camera, p+[0])
        head = project(camera, p+[ai['minimum_person_height_m']])
        heights.append(abs(head['y']-foot['y'])*camera['video_vertical_px']/2)
    region['min_person_height_px'] = min(heights)
    return dict(kd=kd, path=path, ai_roi=region, ai_line=event_line)


def vehicle_poses(parking):
    step = parking['sweep']['sample_step_m']
    poses = []
    for leg in parking['sweep']['rear_axle_path']:
        if leg['type'] == 'line':
            a, b = leg['a'], leg['b']
            heading = math.atan2(b[1]-a[1], b[0]-a[0])
            poses += [(p[0], p[1], heading) for p in line_samples(a, b, step)]
        else:
            start, end = map(math.radians, leg['angles_deg'])
            n = math.ceil(abs(end-start)*leg['radius_m']/step)
            direction = 1 if end > start else -1
            for i in range(n+1):
                angle = start+(end-start)*i/n
                poses.append((leg['centre'][0]+leg['radius_m']*math.cos(angle),
                              leg['centre'][1]+leg['radius_m']*math.sin(angle), angle+direction*math.pi/2))
    return poses


def vehicle_box(parking, pose):
    x, y, a = pose; v = parking['design_vehicle']; m = parking['sweep']['clearance_m']
    front = v['wheelbase_m']+v['front_overhang_m']+m
    rear = -v['rear_overhang_m']-m
    half = v['width_m']/2+m
    return [[x+along*math.cos(a)-side*math.sin(a), y+along*math.sin(a)+side*math.cos(a)]
            for along, side in [(rear, -half), (front, -half), (front, half), (rear, half)]]


def rect_polygon(rect):
    x, y, w, h = rect
    return [[x, y], [x+w, y], [x+w, y+h], [x, y+h]]


def overlaps(a, b):
    # Separating-axis test, valid for convex vehicle/rectangular obstacles.
    for polygon in [a, b]:
        for p, q in zip(polygon, polygon[1:]+polygon[:1]):
            axis = [p[1]-q[1], q[0]-p[0]]
            aa = [sum(x*y for x, y in zip(point, axis)) for point in a]
            bb = [sum(x*y for x, y in zip(point, axis)) for point in b]
            if max(aa) <= min(bb)+1e-9 or max(bb) <= min(aa)+1e-9:
                return False
    return True


def parking_results(d):
    p = d['site']['parking_layout']; corridor = rect_polygon(p['entry_corridor_rect_site_m'])
    clashes = [s['id'] for s in p['stalls'] if overlaps(corridor, rect_polygon(s['rect_site_m']))]
    obstacles = [(s['id'], rect_polygon(s['rect_site_m'])) for s in p['stalls']]
    obstacles += [('pedestrian strip', rect_polygon(p['pedestrian_strip_rect_site_m']))]
    obstacles += [('camera support', rect_polygon(r)) for r in p.get('camera_support_rects_site_m', [])]
    obstacles += [('open gate leaf', rect_polygon(r)) for r in p.get('open_gate_leaf_rects_site_m', [])]
    obstacles += [(c['id'], rect_polygon([c['centre_site_m'][0]-.2, c['centre_site_m'][1]-.2, .4, .4])) for c in p['chambers']]
    for id, obstacle in obstacles:
        if id.startswith('JC') and overlaps(corridor, obstacle):clashes.append('chamber in vehicle corridor: '+id)
    poses = vehicle_poses(p)
    for pose in poses + [(x, y, a+math.pi) for x, y, a in reversed(poses)]:
        box = vehicle_box(p, pose)
        for id, obstacle in obstacles:
            if overlaps(box, obstacle):clashes.append('sweep: '+id)
        for x, y in box:
            inside = lambda r: r[0]-1e-6 <= x <= r[0]+r[2]+1e-6 and r[1]-1e-6 <= y <= r[1]+r[3]+1e-6
            if not any(inside(r) for r in p['sweep']['free_rectangles_site_m']):clashes.append('sweep outside free area')
    return dict(clashes=sorted(set(clashes)), poses_per_direction=len(poses),
                steering_deg=math.degrees(math.atan(p['design_vehicle']['wheelbase_m']/p['sweep']['turn_radius_m'])))
