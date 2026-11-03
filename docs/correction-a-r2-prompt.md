# A - resolve G01 reader placement after R1

Continue as the same executor A in `/Users/aleklyskawa/Desktop/critical_project /airport-project` (quote the complete path including the space after `critical_project`). R1 has been reviewed: A2(D01), A3(optics/PATH1/AI), and A4(G01 supply cascade) are closed in the adopted model. Do not revisit them or FAS/UPS without a direct dependency. Do not launch agents/new chats, commit, push, or publish.

Read current status in `/Users/aleklyskawa/Desktop/critical_project /airport-project/docs/design-decisions.md` and the final section of `/Users/aleklyskawa/Desktop/critical_project /airport-project/docs/review-a.md`. Check applicable AGENTS.md and preserve existing user changes.

**One A1 collision remains:** RD-G01-IN is at SITE `[64.5,9,1.1]`, RD-G01-OUT at `[64.5,11,1.1]`. The rear axle follows x=65,y=5..28. A 1.8 m-wide body occupies x=64.1..65.9, or x=63.9..66.1 with the 0.2 m margin. Both readers lie inside that envelope. At rear axle `[65,9]`, the body footprint also spans both reader y coordinates. `parking_results` omits readers/supports from obstacles.

Implement physically consistent reader positions/mounts or revise the car path. Define support/panel footprints and how the card is presented at a stop; manual patrol operation may remain. Retain clear passage, gate swing, pedestrian strip, and corrected parking spaces. If mounting on a moving element, explicitly model operating positions and cable routing. B must not decide mounting or move symbols away from actual points.

Edit `/Users/aleklyskawa/Desktop/critical_project /airport-project/data/design.json`, `tools/design_geometry.py`, `tools/validate_design.py`, and necessary export, section08, and ACS-description dependencies. After moving points/mounts, check cable endpoints/paths/slack, BOM, and G01 voltage cascade; after changing the path, check its full envelope in both directions. Also reconcile the minor obsolete `areas.A03.scope` C08 x=68 text with camera `[63,20,3]`.

Extend the manoeuvre check to physical readers and mounts. Add one targeted regression rejecting the old arrangement or an equivalent collision; retain the previous20 cases. Do not add a whole new system or rebuild C layout/B drawings.

Assign the next revision. Regenerate register/tables(`make data`), run validator/negative tests, compilation, packaging, and a fresh-ZIP build. Inspect relevant PDF pages and diff. Briefly update decisions; do not edit historical reviews or prompts. Return reader positions/mounts or new path, clearance result, cable/voltage/material impact, and PDF path. This narrowly closes A1, rather than repeating all of A. The orchestrator decides acceptance for B.
