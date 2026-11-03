# Executor A - technical design and calculations

Updated 21 October 2026 with the user's first-class notes and clarification that the passage comment means several CCTV views of a walking person. The 19 October audit describes the starting state; account for the additions below when defining scope. Language updated to English at the user's request on 3 November 2026.

You are executor A for the Critical Infrastructure academic project. Implement a consistent CCTV, ACS, IDS, and FAS design for the fictional North Airport. This is the first of three sequential packages: A - model, technology, calculations; then B - vector drawings from the accepted model; finally C - editing and LaTeX layout. Do not launch agents or new chats. Do not stop at advice or another plan: edit files and verify the result.

## Files and starting state

Local repository:
`/Users/aleklyskawa/Desktop/critical_project /airport-project`

There is a space after `critical_project`; quote the complete path in commands. Work on current files, inspecting `git status` and the diff first. Do not reset user changes. Audit base: HEAD `8112694`; untracked `docs/orchestrator-prompt.md` and `docs/project-outline.md` were present. Absence from a commit does not authorise deletion. Do not independently commit, push, or publish.

Read applicable `AGENTS.md` and referenced instructions. The audit found none in the project or checked ancestors; verify the current state. Read first:

- `/Users/aleklyskawa/Desktop/critical_project /airport-project/docs/design-decisions.md`
- `/Users/aleklyskawa/Desktop/critical_project /airport-project/docs/initial-audit.md`
- `/Users/aleklyskawa/Desktop/critical_project /airport-project/README.md`
- `/Users/aleklyskawa/Desktop/critical_project /airport-project/data/design.json`
- `/Users/aleklyskawa/Desktop/critical_project /airport-project/docs/device-register.md`
- `/Users/aleklyskawa/Desktop/critical_project /airport-project/main.tex`, `preamble.tex`, `metadata.tex`, and all `.tex` files in `/Users/aleklyskawa/Desktop/critical_project /airport-project/sections/`
- `/Users/aleklyskawa/Desktop/critical_project /airport-project/tools/validate_design.py`, `tools/generate_figures.py`, `tools/bundle_overleaf.py`, and `/Users/aleklyskawa/Desktop/critical_project /airport-project/Makefile`
- `/Users/aleklyskawa/Desktop/critical_project /airport-project/output/pdf/north-airport.pdf`, particularly FAS, locations, power, and materials; inspect pages 7, 10-12, and 14-17 if the PDF still matches the baseline.

Edit `data/design.json`, technical content in `sections/01-assumptions.tex` through `sections/18-references.tex`, `docs/device-register.md`, `tools/validate_design.py`, and `docs/design-decisions.md`. If needed, add a small data-to-LaTeX/register export and adapt Makefile and README. Keep new files inside the repository. Change `main.tex` only to include data or preserve compilation. Modify the figure generator only for the data interface or to disable an old register export that would overwrite the new one; leave graphical rebuilding to B. Do not edit this prompt, the original orchestrator prompt, or the initial audit.

The style reference `/Users/aleklyskawa/Desktop/master-thesis` is read-only. If using it, read its `AGENTS.md` and referenced `CLAUDE.md`. Do not copy personal data, topic, instructor, or master's-thesis labels. Leave project formal details for the user.

## Current decisions

The core scope is selected entrances, rooms, and areas of the terminal/technical zone, not the entire airport, runway, navigation, counter-drone systems, or fuel facilities. You may reduce dimensions, building count, and topology with functional justification and complete dependency updates. Neither 24 ha nor four buildings must be retained. Hypothesis to evaluate: a smaller terminal with SOC/back-of-house rooms, a staff entrance, adjacent car park, and controlled vehicle gate permits a more complete design. This is a recommendation, not accepted geometry or an additional instructor requirement. Keep a hangar only with defined conditions and justified detection. Assess runway-direction access as described below.

The user supplied these **informal first-class notes**. Distinguish requirements, scope recommendations, and hypotheses; do not add every alternative simultaneously:

- **Select specific components.** Selection must follow functions and parameters of the adopted site. Explain why a device type is used rather than expanding a technology catalogue.
- **Person and behaviour detection.** Define person detection and one main observable scenario, such as line crossing or entry to a designated area. Assign cameras, region, and rule. Do not equate person detection with biometric identification or recognising intent. Person detection and line crossing are examples in the [AXIS Object Analytics manufacturer documentation](https://help.axis.com/en-us/axis-object-analytics), read 21 October 2026; it is verification material, not a mandated supplier.
- **“A sufficiently bent path to scan from every side.”** The user clarified that this means several CCTV views during passage. Set the observation-direction objective first, then choose passage shape and camera count/positions. Compare straight and bent routes by required views; justify with fields of view, occlusion, and observation directions. Record the person's route, camera IDs, viewing directions, and movement segments for each view. A bend alone does not prove all-side observation. Consider accessibility, throughput, and free egress; do not extend or obstruct evacuation for analytics. B must be able to draw the passage and justified views from the data.
- **Employee verification by code, biometrics, or card.** Briefly compare alternatives and select for specific access points; using all three is not required. Start with a cryptographically authenticated card and extra PIN for selected rooms. Consider biometrics as an alternative requiring technical and legal necessity, without assuming the word “airport” suffices. Check, among other provisions, Labour Code Article 22¹b and relevant data protection: [ELI consolidated Labour Code](https://eli.gov.pl/api/acts/DU/2025/277/text/U/D20250277Lj.pdf), read 21 October 2026. Egress must not depend on biometrics, PIN, card, or server.
- **An exact fictional or real airport plan.** Retain the fictional site. Design a concrete site plan and protected floor plans with dimensions, functions, and actual equipment positions for B to reproduce. Do not substitute a rendering or satellite photograph. Do not seek a real airport merely for its name; a real site needs accessible geometry and is unnecessary for this package.
- **Possible car park/vehicle gate and runway protection.** Prefer evaluating a small car park and controlled gate linked to the terminal. Define vehicle and pedestrian functions separately. Briefly assess one specific airside access point towards the runway; if adopted, include geometry, CCTV tasks, ACS, connections, and budgets. Otherwise justify exclusion. Do not describe one access point as full runway protection. A whole-runway or perimeter design is a separate extension, not automatic scope. Neither parking nor runway access replaces building FAS design.

Existing counts - 24 cameras, 14 ACS points, 80 FAS detectors, 1520 m routes, 1335 W, four fire panels, eight AI streams, and declared backup targets - are provisional. Do not keep them for a green validator. Useful IDs `N0`-`N3`, `C01`-`C24`, `D01`-`D12`, `G01`-`G02`, `CSP-0`-`CSP-3`, `SSWiN-0`-`SSWiN-3`, and `R1`-`R4` may remain; map changes/removals in shared decisions. Add unambiguous room, device, and circuit IDs.

The audit found room/door functions partly hidden in drawing code; terminal D01-D06 are all internal, with no external doors. Forty-eight FAS points are an arbitrary 6 x 8 grid and I/O modules are only a reserve. Individual locations and circuits are missing. Storage and ring geometry calculate correctly, but local cable lengths and power do not follow a connection list. The old validator fixes totals and checks PDF existence only. ZIP lacks reproducible drawing sources; final packaging is completed after B.

FAS and evacuation egress must work without LAN, VMS, AI, or the ACS server. SOC receives FAS information; AI assists the operator. Never invent measurements, field tests, certificates, or full standards compliance.

The target is academic English, Latin Modern 12 pt, margins around 25 mm, black text and links, a page-number footer, and a plain title without renderings, boxes, or slogans. C will rebuild layout; prepare factual technical content now, without repeated future-design announcements. Team/AI information belongs in README/docs apart from required academic disclosure. Do not prescribe page count or schedule.

## Implement these changes

1. **Resolve the site model.** Define building/room functions, protection boundaries, dimensions, heights, environmental conditions, occupancy, doors, and exits. Distinguish protected areas from context. Do not wait for a real airport map. Make justified fictional-site decisions and label them as assumptions rather than measurements.

2. **Extend one data source.** `data/design.json` must contain B's geometry, installed-device/point register, positions, types, room/area, node, port/circuit, and power-source assignments, connections, and routes with lengths. Define coordinates, units, and local-to-site transformation. Derive totals, BOM, and material LaTeX quantities from data or verify them automatically. Register and export must not become independent models. Avoid elaborate project-management infrastructure.

3. **Select CCTV, ACS, and IDS by function.** Each camera needs an ID, observation task, mounting position/height, direction, target area, image width, and resolution/px-per-metre justification in the target plane. Include walls and occlusion; PTZ does not continuously protect every preset. Each ACS point needs sides/zones, equipment, controller channel, door-state sensor, egress, and behaviour under voltage loss, LAN failure, and fire; show a physical release path where required. Assign intrusion detectors to positions, inputs, and armed partitions with tamper supervision. Do not count one contact twice without defining the real interface.

4. **Design FAS rather than reserving dots.** Detector types/counts must follow rooms, heights, obstacles, and conditions. State the selection basis and available-source limits. Use a specific compatible device family for critical interfaces; do not assume arbitrary vendor mixing or an undocumented optical ring. Define panels, loops, addresses, isolators, call points, notification, fault supervision, and modules. The cause-and-effect matrix must state event, condition/time, effect, actual output, supervision, and reset. Count outputs for stated controls rather than calling them I/O reserve. Resolve voice alarm and fire notification/transmission for this model using current sources. Do not add control of undesigned installations without their interfaces.

5. **Derive routes, materials, and calculations from that model.** Each connection needs endpoints, cable type, route, plan length, vertical length, slack, and purchase quantity; connection order must allow B to reconstruct circuits. Separate ACS, RS-485, IDS, FAS, and power cables by function and parameters. Check copper lengths, normal/failure ports and links, PoE, fibre usage/optical budget if retained, bitrate/retention/RAID, and local buffering. Separate equipment/licences, cables, accessories, and stock in BOM. Do not leave thousands of cable metres as an unexplained estimate.

6. **Resolve power.** Assign loads to actual UPS/DC supplies. Include maxima, losses, PD/PSE relationships, reserve, standby/alarm currents, and charging without double counting. Calculate capacities, supply currents, and voltage drop for critical/longest circuits at low battery voltage. Base UPS selection on published runtime or manufacturer curves for the exact battery configuration; kWh alone is insufficient. Select circuits/protection within scope; define PWP and reserve-source/automatic-transfer relationships if retained. Include supplies and chargers. Distinguish calculated sizing from future load testing and unavailable measurements.

7. **Complete AI, procedures, and sources.** Choose one AI case with camera IDs, region, inputs, analysis frequency, processing location, operator output, and TP/FP/FN, latency, and workload evaluation. Thresholds are acceptance targets, not results. Fire, intrusion, ACS, power/communications, and cyber procedures need trigger, responsibility, action, restoration, and safe behaviour after backup depletion. Verify device data in manufacturer datasheets/manuals and law in official sources including amendments. Provide document, version/page/section, URL, and access date. Separate project assumptions from law/standards and catalogue parameters. A standards catalogue does not establish knowledge of the provisions.

## Dependencies on B and C

B needs complete geometry and connections to draw site/floor plans, routes, schematic, and power without inventing technical solutions. Leave presentation, palette, sheet divisions, and editable vector sources to B. Do not run old `make figures` if it recreates an obsolete model or overwrites the register. If geometry/counts change, disable obsolete figure inclusions, retain their sources, and state replacements needed. Do not present an old drawing as the new model. The post-A PDF is intermediate technical review material.

C will organise title, contents, structure, typography, captions, references, and page breaks. Do not defer technical decisions to C. Suggested final structure: scope/model; protection systems; network/integration/AI; locations/routes; power/calculations; materials; procedures/verification; references. Calculations may remain beside their selections.

Keep one short `docs/design-decisions.md` with decisions, IDs, actual open issues, and B's drawing scope. Do not create more orchestrators, schedules, or extensive task registers.

## Acceptance criteria and verification

- Record treatment of class notes: specific person/event scenario, employee-authentication comparison, exact plan model, parking/gate decision, and runway-direction option. For multi-view passage, define the route, cameras, observation segments, and occlusion checks; route shape alone is insufficient.
- Every installed point/device has an unambiguous ID, position, and connection; every cable endpoint and control channel exists. Geometry/circuits suffice for B. Every protected area has justified detection/observation or an explicit exclusion.
- FAS has justified placement and a complete control matrix; ACS has individual states and independent egress. No placeholder grids or unassigned I/O reserve in place of required outputs.
- Description, register, cables, BOM, and calculations describe one model version. Selection-critical parameters have sources; no unperformed or unverified test/compliance claims.
- Validator checks relationships rather than old totals: IDs/references, connection geometry/endpoints/lengths, circuit/port capacities, PoE, fibres, storage, power/battery assignments, and material totals. Do not present these checks as proof of engineering correctness. Independently check critical results too.
- Run checks and PDF compilation; inspect changed rendered pages and the final-pass log. Fix errors, undefined references, and clipped content; do not claim to inspect unrendered pages. Start from `make pdf` and adapt export dependencies if necessary. Final `git diff --check` should be clean.
- The model must be ready for technical acceptance before B. Formal details and checks requiring actual measurements/implementation may remain open with a defined acceptance plan. Do not leave detector counts, channels, or cable lengths for B/C.

Return briefly: (1) changed files, (2) scope/main decisions and count changes, (3) commands/results and PDF path, (4) actual unresolved issues and B's input. “Done” and a green build are insufficient.

If file access is unavailable, say so immediately. Minimum text inputs: decisions and audit, `data/design.json`, `docs/device-register.md`, all `sections/*.tex`, `main.tex`, `preamble.tex`, `metadata.tex`, `Makefile`, `tools/validate_design.py`, and `tools/generate_figures.py`; the current PDF helps assess drawings. No personal reference-template data is needed. Without repository access, provide complete replacement contents or a patch and verification instructions, explicitly stating what you did not run; do not claim local implementation.
