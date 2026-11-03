# Correction to package A-2026-10-24

Continue as the same executor A. Substantial work is implemented; compilation, exports, and 15 negative tests also passed independent review. Do not restart or restore the four-building model. Resolve the four issues below and direct dependencies before B acceptance. Do not launch agents/new chats or commit/push/publish.

Repository: `/Users/aleklyskawa/Desktop/critical_project /airport-project`; quote the complete path including the space after `critical_project`.

Inspect file status and applicable AGENTS.md first. Read:

- `/Users/aleklyskawa/Desktop/critical_project /airport-project/docs/review-a.md` for evidence/checks;
- `/Users/aleklyskawa/Desktop/critical_project /airport-project/docs/design-decisions.md` for current status;
- `/Users/aleklyskawa/Desktop/critical_project /airport-project/data/design.json`;
- `/Users/aleklyskawa/Desktop/critical_project /airport-project/tools/validate_design.py` and `tools/export_design.py`;
- sections 03, 04, 07-11, 13-14 in `/Users/aleklyskawa/Desktop/critical_project /airport-project/sections/` and dependent site descriptions.

Edit the model, validator, export, relevant sections, README if commands change, and brief decisions. Regenerate the register/`generated/` from data. Do not edit historical audits, prompts, or review reports; record implementation status in decisions and your response. Do not rebuild B drawings or C layout. Preserve user changes and formal details without guessing.

1. **Connect entry to the car park aisle.** Lane x=63..67,y=10..20 ends before P04(62..64.5 x20..25) and P05(66..68.5 x20..25). Only1.5 m remains between them; the aisle begins at y=25. Define a clear corridor and check a specified vehicle with spaces occupied. Space location/count may change; do not keep12 at the expense of passage. Retain accessible pedestrian separation. Check chamber(65, 11): it lies in the gate lane despite B-CHAMBER stating non-traffic ground. Relocate it or select appropriate loading capability. Propagate affected changes through cameras, AI, routes, penetrations, lengths, voltages, and BOM.

2. **Provide a real D01 verification view.** C01 local `[20,9.5,2.4]` is9.5 m horizontally from D01 `[20,0]`, beyond `far_clip_m=8`. C02 `[20,0.5,2.4]` faces north, with D01 behind it. Both are assigned to D01. Reconcile task, settings, field limits, and image density at the opening. Extend checks beyond the D02-D04 exception to every declared verification point, including near/far, angle, target height, and correct coordinate frame. Do not change only labels or reach without rechecking task and resolution.

3. **Check C08 vertical framing and declared PATH1 views.** Existing AI checks cover plan geometry only. For C08(68, 11, 3), tilt16.602° and HFOV51.699°, a checking rectilinear16: 9 projection gives VFOV about 30.488°; ground points(66, 15, 0)/(67, 15, 0) fall below the image. This is a calculation, not camera measurement. Define optical projection, VFOV/image format, and distortion assumptions. Check feet detection, required body parts, the entire line and analysis region; correct settings/geometry as needed. For PATH1 define required body parts, heights, and front/rear/profile segments, including endpoints and density. Do not promise full-body views without calculation or substitute future field testing for missing design. Sources: [Object Analytics manual](https://help.axis.com/en-us/axis-object-analytics), [P3265-LVE datasheet](https://www.axis.com/dam/public/ac/8e/70/datasheet-axis-p3265-lve-dome-camera-en-US-437931.pdf). B needs resolved parameters and a clear field definition.

4. **Remove contradictory G01 supply data.** `network.external_gate_bus` still states240 mA/2.5 mm2 while cables, budget, and text use0.5 A/6 mm2. Remove obsolete values or generate descriptions from parameters. Recalculate common load and last-reader voltage after route changes. Derive its input from the preceding section, or verify that any conservative bound does not exceed calculated available voltage.

Add targeted checks/negative cases for entry-space collision, ACS points outside frame, and vertical AI-line visibility. Do not increase test count for its own sake. Retain existing checks. Do not alter FAS or correctly verified UPS assumptions without a direct connection to this correction.

Assign a new revision and briefly describe changes. Run exports, validator/self-tests, compilation, packaging, and compilation of a fresh ZIP extraction. Inspect relevant rendered pages. A temporary data plot in `tmp/` may support geometry review but does not replace B drawings. Check diff and export freshness before finishing.

Acceptance: clear aisle access; consistent D01/PATH1 views; visible AI line in the defined3D model; one G01 parameter set; no new connection/calculation contradictions. Do not claim orchestrator acceptance yourself. Return changed files, A1-A4 solutions, current quantities, performed checks, and PDF path. B's prompt follows review of these corrections.
