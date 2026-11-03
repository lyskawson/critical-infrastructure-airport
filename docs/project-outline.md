# Initial project outline - Critical Infrastructure

**Topic:** Design of video surveillance, access control, and alarm systems, including fire detection and alarm, for a regional airport.

The proposed basis is a model regional airport. The initial scope includes the passenger terminal, selected technical buildings, entrances, and adjacent land. The report shows how systems cooperate to detect threats and respond to events. This outline records the original proposal; current scope is defined in `docs/design-decisions.md`.

## Planned report contents

1. **Title page and table of contents**
   Project topic, team, course/instructor details, and an ordered chapter list.

2. **Site description, purpose, and assumptions**
   Selected airport area, building functions, passenger/staff/technical zones, main threats, and protected locations.

3. **Technical description of systems and devices**
   CCTV, access control, intrusion/hold-up alarms, and FAS. For each system: tasks, basic equipment, operation, and adopted technology.

4. **Schematic and system cooperation**
   Camera, reader, detector, panel, network, and security-workstation connections; information flow and association of an alarm with a location and camera image.

5. **ML and AI application**
   A selected video-analytics use case, such as person entry into a designated region; operator information and evaluation method.

6. **Device positions and installation routes**
   Site and building plans with devices/cables, distribution points, inter-building links, and routing assumptions.

7. **Main materials schedule**
   Devices, cables, basic accessories, and quantities derived from schematics and positions.

8. **Electrical supply continuity**
   System supplies, UPS, batteries, and reserve sources; basic power and runtime calculations.

9. **Security procedures**
   Fire, intrusion, unauthorised access, and power/communication failures; security roles, safe egress, recording access, and operating permissions.

10. **Verification and conclusions**
    Proposed functional/integration tests and how the design addresses the initial threats.

11. **References and source documentation**
    Technical materials, device documentation, and relevant standards/regulations.

## Final format

One PDF with site/floor plans, device locations, connection schematics, materials, and basic calculations. The same drawings support the presentation.
