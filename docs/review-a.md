# Review of package A-2026-10-24

Review date: 24 October 2026. **Result: one A correction round before model acceptance for B.** Neither the technical model nor LaTeX files were changed by this review. The small-terminal scope and A's work are retained; the former four-building model is not restored. This report preserves historical findings; current R1 status is at the end.

## Checks and review scope

Read current JSON, all technical sections 01-18, register, export, validator, Makefile, ZIP packaging, README, and decisions. Inspected diff/file status; no applicable AGENTS.md found. No agents, new chats, or executor messaging were used.

- `python3 tools/validate_design.py --self-test --report tmp/odbior-a-2026-10-24/validation.json`: OK, 15/15 corrupted variants rejected.
- `python3 tools/export_design.py --check`: current exports. `git diff --check`: clean.
- Independent build in `tmp/pdfs/odbior-a-2026-10-24/build/`: 34 pages, final log without warnings, undefined references, or overfull/underfull messages.
- Existing ZIP: 37 entries, valid CRC; all included files matched local files at inspection time. Fresh extraction to `tmp/pdfs/odbior-a-2026-10-24/overleaf-unpacked/`, compiled into `build-review/`: 34 pages, clean final log. This was not an Overleaf-service import. Corrections and decision updates require a new ZIP.
- All34 pages freshly rendered. Reviewed six contact sheets and physical pages 16, 20, 24 at higher resolution. Text/table readability sufficed for A review, not final C layout acceptance.
- Independent polyline/cut calculation confirmed1658.843 m installed cable and 1873 m purchase, excluding factory connections/accessory patch cords. Recording3.6288 TB raw/4.536 TB with reserve. PoE273.2 W allocated/341.5 W with reserve. UPS envelope 861.1 W/1076.375 W with reserve.
- Read source `ebm2` series from the [Eaton curve](https://eg.eaton.com/ups-battery-runtime/en-gb/5PX1500IRT2UG2): all points matched JSON. The 1100 W/67 min point gives 45.56 min with 0.85 and 0.8 factors. This is calculated sizing, not an autonomy test.

Primary documents were checked selectively for review-critical claims: camera datasheet/Axis manuals, UPS curve, ACSP family, fire legislation, and the new Labour Code edition. This is not a full audit of every law/manual or construction compliance. Explicit assumed FAS radii and future installation tests are not treated as measurements/certificates.

## A1. Entry conflicts with parking spaces

Sources: `data/design.json`, `site.parking_layout.stalls`, G01 description, `sections/08-site.tex`.

G01 lane is x=63..67,y=10..20, while the manoeuvring aisle starts at y=25. Between them are:

- P04:x=62..64.5,y=20..25;
- P05:x=66..68.5,y=20..25.

The 4 m lane overlaps these spaces; only1.5 m remains at x=64.5..66. No clear connection to the aisle is defined with occupied spaces. A must correct geometry and check passage/manoeuvre for a specified vehicle, rather than leave it to the drawing executor. Twelve spaces need not be retained at the cost of access.

Also, B-CHAMBER specifies non-traffic chambers, but the third point(65, 11) lies in G01's lane and gate swing. Being between wheel tracks does not remove vehicle loading. Relocate it or explicitly select suitable equipment and update routes/quantities.

## A2. Neither assigned camera covers D01 within its recorded limits

Sources: `devices.C01/C02`, `access_points.D01`, `openings.D01`, `tools/validate_design.py:117`.

D01 is at local plan `[20,0]`. C01 `[20,9.5,2.4]` faces south but has `far_clip_m=8`; the door is9.5 m away horizontally. C02 `[20,0.5,2.4]` faces north, putting the door behind it. Both are assigned to D01 verification and C01's task names D01. The validator checks actual points only for D02-D04 and misses this discrepancy.

Select/document a D01 event view with task and image density. A sector-label change or promised field test is insufficient. Check every declared verification point in its correct frame, including near/far and target height.

## A3. C08 and PATH1 lack vertical framing checks

Sources: `devices.C08.view`, `ai.line_site_m`, `path_observation.views`, `tools/validate_design.py:89`, `sections/11-ai.tex:2`.

AI checks use azimuth, HFOV, and plan radius, without camera height, tilt, or VFOV, although the text claims the entire line is visible. [AXIS Object Analytics documentation](https://help.axis.com/en-us/axis-object-analytics) places the human detection point at the feet; upper-body visibility also matters. Estimating an occluded point does not establish full geometric coverage.

Independent ideal rectilinear1920x1080 projection for C08, HFOV51.699°/tilt16.602°, gives VFOV about 30.488°. Ground points projected into the normalised vertical range -1..1 give:

| SITE point, z=0 | Vertical image coordinate |
|---|---:|
| (65, 15, 0) | -0.968 |
| (66, 15, 0) | -1.140 |
| (67, 15, 0) | -1.343 |

The two eastern points lie below this checking model's image. This is a result under stated optical assumptions, **not a measured camera image or proof of the exact lens mapping**. The [P3265-LVE datasheet](https://www.axis.com/dam/public/ac/8e/70/datasheet-axis-p3265-lve-dome-camera-en-US-437931.pdf) gives HFOV/VFOV ranges, but the model lacks selected VFOV, projection, and distortion-correction settings.

A must resolve the optical model, justify parameters, and correct camera settings, line, or ROI if needed. Also check target heights and endpoint density over declared PATH1 segments. Full-body visibility in every view is not imposed, but required body parts and segments must be explicit. Distinguish AI requirements from front/profile views for operator verification. B needs sufficient sector data without independently changing optics.

## A4. Contradictory G01 reader supply description

`network.external_gate_bus` (`data/design.json:10688`) states240 mA and a common 2.5 mm2 pair. `DC-READER-O`, `DC-RD-G01-IN`, and `sections/09-routes.tex:17` use0.5 A/6 mm2. Voltage-drop calculations/table use the latter. Remove stale text or derive it from parameters so JSON contains one decision. Recalculate lengths and downstream voltage after geometry corrections.

## Condition for starting B

A corrects these issues/dependencies in the same model, export, prose, and package. The validator must reject at least passage collision, an assigned point outside the field, and incorrect vertical AI coverage. Checks must reflect actual dependencies rather than new constant totals. The orchestrator reviews corrected files/relevant PDF pages before accepting A. B and C were not started.

## Repeat R1 review - 26 October 2026

Checked `A-2026-10-24-R1`, differences from the retained A0 copy, new `tools/design_geometry.py`, export/validator changes, and relevant chapters. **A2, A3, and A4 are closed within the defined academic model. A1 needs a narrow reader-mounting or vehicle-path correction.** No A technical files were changed by the review; only the report, decisions, and prompt were updated.

Confirmed checks:

- Validator: 20/20 negative tests rejected; the five new cases also check the intended rejection reason. Exports current; diff whitespace check clean.
- Independent source build: 36 pages, final log without warnings/errors. ZIP: 38 entries, valid CRC, matching files at inspection; a fresh extraction also compiled cleanly. Decision/model changes require repackaging.
- All36 pages freshly rendered; six contact sheets reviewed; physical pages 6/22 inspected in detail. Retained former layout remains C's responsibility.
- D01: independent opening-corner projection in correctly transformed SITE gives maximum absolute image coordinates x=0.1742,y=0.4780, horizontal distances9.500-9.519 m; within C01's10.5 m limit.
- PATH1: independent envelope-corner checks at each adopted segment's endpoints confirm vertical/horizontal limits. C01/C02 and both profiles fit with reserve. Heights1.2-2.0 m explicitly limit required body parts.
- AI: full-body ROI corners give max |x|=0.7729,|y|=0.9060; line corners |x|=0.5554,|y|=0.6766. All are within 0.96. This confirms the ideal projection, without claiming lens measurement.
- G01: independent calculation gives 0.5 A, 6 mm2, IN11.66534 V, OUT11.57784 V; the second section uses the first result rather than an independent favourable constant.
- Current totals: 10 spaces, 100 devices/assemblies, 121 connections, 1882 m cable purchase, longest channel91.3 m. Basic FAS, UPS, recording, and PoE budgets were unchanged.

Check files: `tmp/odbior-a-r1-2026-10-26/validation.json`, `independent-checks.json`, and `tmp/pdfs/odbior-a-r1-2026-10-26/`.

### Remaining A1 issue: readers omitted from the vehicle envelope check

Sources: `data/design.json:2648`(RD-G01-IN), `data/design.json:2672`(RD-G01-OUT), `site.parking_layout.sweep`, `tools/design_geometry.py:162`.

Reader SITE positions are `[64.5,9,1.1]` and `[64.5,11,1.1]`. The straight rear-axle path follows x=65 from y=5 to 28. A 1.8 m-wide northbound car occupies x=64.1..65.9, or x=63.9..66.1 with 0.2 m margin. Both readers lie inside both intervals. At rear axle `[65,9]`, the body footprint spans x=64.1..65.9,y=8.1..12.6 and contains both points.

`parking_results` checks spaces, pedestrian strip, camera support, open gate leaves, and chambers. It omits reader panels/supports, so returns no collision despite unresolved physical placement. B cannot fix this by moving symbols later.

A must reconcile actual reader mounting/positions with the vehicle path or revise the path and recheck the manoeuvre. Define card use at a stop; manual patrol handling may remain. Update affected cable endpoints/paths, lengths, voltages, accessories, and text only where dependent. Checks must include physical devices/supports, not just the previously selected outlines. Also clean up the stale `areas.A03.scope` C08 x=68 description.

The only active prompt is `docs/correction-a-r2-prompt.md`. Neither B nor C has started.
