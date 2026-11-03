# Design decisions

Package A, model **A-2026-10-24-R1**, base HEAD `8112694`. Technical data is prepared for review and B's drawings; this is not construction approval. The technical stages used no agents, new chats, commits, pushes, or publication. No applicable AGENTS.md was found in the repository or checked ancestors. Original audit findings and prompt requirements are preserved.

## English-language migration - 3 November 2026

At the user's request, report text, documentation, prompts, data descriptions, tool messages, and repository naming were converted to English. Technical IDs and the R1 design revision are retained. This language change does not close the remaining A1 issue or authorise B. English replaces the earlier Polish-language requirement. README is intended for external readers; detailed work status remains here. The GitHub repository is now `lyskawson/critical-infrastructure-airport`, the local directory is `airport-project`, and origin uses the new URL. English files remain local changes; no commit or push was made. Verification preserved all 4556 numeric/boolean/null model values and all calculated outputs; 20/20 negative tests pass. The English report has 36 pages, all rendered and reviewed; local and fresh-ZIP builds have clean final logs. Local Markdown links resolve.

## Current orchestrator review - 26 October 2026

**R1: A2, A3, and A4 are closed within the adopted calculation model. A1 has one remaining collision to resolve before B.** Removal of P04/P05 and relocation of JC03 are accepted. RD-G01-IN `[64.5,9,1.1]` and RD-G01-OUT `[64.5,11,1.1]` remain inside the envelope of a car following x=65; the manoeuvre check omits their supports. A must reconcile their physical mounting with the vehicle path and recalculate direct dependencies. The minor `areas.A03.scope` description also retains the former C08 x=68 position instead of current (63, 20).

Repeat-review checks: 20/20 negative tests, current exports, warning-free project and freshly extracted ZIP builds, independent D01/PATH1/AI projection and G01 voltage checks. The 36-page PDF received a fresh render, full contact-sheet review, and detailed review of physical pages 6 and 22. Results and collision evidence are in `docs/review-a.md`.

**The only current execution package is `docs/correction-a-r2-prompt.md`, for the same A.** The user transfers it manually. B and C remain unstarted. Do not revisit corrected views, FAS, UPS, or old scope without a new reason. The 24 October review and R1 implementation sections below are history, not current permission to start B.

## Orchestrator review - 24 October 2026, historical A-2026-10-24

**Historical status: A required one correction round before B acceptance.** Local/fresh-ZIP compilation, export freshness, and 15 negative tests passed; independent checks confirmed cable, storage, PoE, and UPS-curve totals. Details: `docs/review-a.md`. The active package at that time was `docs/correction-a-prompt.md`, manually transferred to the same A.

- A1: entry x=63..67 ends at P04/P05; define a clear connection to the aisle, check the manoeuvre and chamber (65, 11) in the lane.
- A2: D01 is 9.5 m from C01 with `far_clip_m=8`; C02 faces away. Reconcile the task, actual field of view, and image density at the door.
- A3: AI/PATH1 validation mainly checks azimuth/HFOV. Complete vertical framing and visibility; the C08 16: 9 checking projection indicates ground visibility problems at the east end of the line. This is a model result, not camera-image measurement.
- A4: `network.external_gate_bus` states 240 mA and 2.5 mm2 while connections/text use 0.5 A and 6 mm2. Remove the contradiction and update correction dependencies.

No A model or selection was changed by that review. B and C were not started; layout, larger table appendices, and final whole-document inspection remain C's work. This records the previous version's review. R1 implementation below does not override the orchestrator's acceptance decision.

## R1 implementation - submitted for repeat review

- **A1:** P04/P05 removed; 10 spaces and accessible P01 remain. Corridor x63..67 reaches the aisle; rear-axle path (65, 5)-(65, 28), R6 arc centred at (59, 28) to (59, 34), then (55, 34). Assumed car 4.5x1.8 m, wheelbase 2.7 m, overhangs 0.9 m; 368 poses in each direction with 0.2 m margin and all spaces occupied. JC03 moved to (62, 11) on unchanged R5, outside traffic and gate swing.
- **A2:** D01 is verified by C01: HFOV40°, tilt8°, far10.5 m, full 1.2 m opening at heights 1.2..2 m, minimum 275.5 px/m. C02 serves PATH1 only. Checks cover every declared D01-D04/G01 camera, full clear width, height, near/far, and SITE transform. C05 corrected to az49°/HFOV72°/far13 m for D03/D04 overview, without facial-identification claims.
- **A3:** shared rectilinear16: 9 projection, square pixels, roll0°, distortion correction ON, explicit zero-residual assumption with 2% of full image dimension reserved on each side. C08 moved to (63, 20, 3), az292°/tilt25°/HFOV72°/VFOV44.4577°. AI rays stay within side fencing and do not cross G01. Feet ROI x63.3..66.7/y12.5..16.5; line y15.5. The envelope also avoids open leaves ending at y12. Outer0.3 m strips are outside AI. Person0..2 m and 0.6x0.6 m fits; minimum image height for a1.4 m person is212.3 px against 86.4 px. PATH1 height 1.2..2 m, centre±0.6 m, envelope 0.6x0.6 m; segments y1..5.5(C01), 3.5..7(C02), 4.2..5.8(C03/C04). Minima297/309/430/430 px/m. Full-body visibility is not claimed in all four PATH1 views.
- **A4:** obsolete240 mA/2.5 mm² text removed. G01 parameters derive from reader/cable models: common 0.5 A, 6 mm², IN11.665 V. OUT derives its input directly from the preceding result, giving11.578 V against project minimum 11.4 V. G01 supply length unchanged.

New C08 route: R8 from(63, 11) to(63, 20); maximum channel91.263 m, permanent links up to 86.263 m; ducts85 m/purchase95 m, installed cable1666.843 m/purchase1882 m. BOM adds a3 m C08 pole with base outside the lane and 0.2 m bracket. Device/assembly count 100, connections 121, penetrations 30 unchanged. FAS, UPS, PoE, and recording retained. New `tools/design_geometry.py` supplies shared calculations/exports, not B's drawings.

Reported implementation checks: 20/20 negative tests(15 retained +5 targeted), current export, 36-page PDF rendered/reviewed, enlarged optics/manoeuvre/PATH1/AI/voltage/BOM pages without clipping, clean log. Fresh ZIP compiled locally without warnings; no Overleaf-service import. Cable, G01 voltage, D01, and AI-line endpoint projections were independently recalculated; working plots remain in tmp. Ideal-model and manoeuvre calculations are not installation tests. **Status: A implemented R1 and submitted it for repeat review; B acceptance is not claimed.** Review reports, prompts, formal details, and C layout were unchanged during R1 implementation.

## Resolved design decisions

- Fictional80x60 m(0.48 ha) site; one 24x16 m T0 terminal; seven rooms R101-R107; flat3 m ceiling without voids. Indoors15-30°C, outdoors-25..40°C. Terminal occupancy up to 60, hall40, entire airport150; two guards per shift. Ten parking spaces including an accessible3.6x5 m space. Dimensions are assumptions, not measurements.
- Eight fixed1920x1080 cameras, no PTZ. PATH1 is straight in R102; C01/C02 provide front/rear and C03/C04 opposite profiles over recorded segments. A bent route was rejected after comparing views and movement. No promise of all-side visibility during occlusion. Egress does not require stopping for a camera.
- ACS: D01-D04/G01, five A1210s, six HID Signo40K readers, Seos5006 SIO/AES128 cards, OSDP Secure Channel. D03/D04 also need PIN. Biometrics rejected for lack of demonstrated necessity; comparison and current Labour Code Article22¹b are in the text. Doors have mechanical egress, without magnets or electrically blocked evacuation. G01 is manual, with two readers, a contact, patrol handling, and no motor/powered lock.
- The car park has assumed existing architectural fencing, an open1.5 m pedestrian gap in the west, and a separated pedestrian strip. The D01 approach avoids G01's controlled lane. E02/E03 lead to open A06/A05. Protection does not cover the entire airport fence.
- IDS: one VERSA15, six PIRs, four separate perimeter contacts, 15 assigned inputs, two partitions, hold-up and tamper. ETHM provides local maintenance; undocumented VERSA/VMS integration is not promised. The operator uses the SOC keypad. D01 ACS and IDS contacts are physically separate.
- FAS: one ACSP402, ten DMP400 and one toilet DCP400, three call points, eight SPP400. L1 has22 addresses and 23 sections, an isolator in every device. OUT1/OUT8 information contacts to IDS, no MIO or optical bus. Immediate single-stage alarm. Project checking radii5/4 m, ceiling assumptions, and source limitations are explicit. FAS is voluntary for the below-threshold model; no voice alarm or automatic PSP transmission. Operator calls112. Legal changes2024/1716, 2026/1276, 2026/815 and Labour Code2026/1245 were considered.
- LAN: one 17-link star, PoE allocation 273.2 W/341.5 W with reserve against 384 W; longest channel91.3 m. No ring, fibre, or SFP. NAS4x8 TB RAID6; required4.536 TB, available14.4 TB; 128 GB SD gives 37.9 h at 6 Mb/s. One AI1 on C08: person crossing a line in the vehicle lane. Input25 fps is not a fictional25 Hz inference guarantee. TP/FP/FN and latency targets await measurement.
- UPS AC envelope 861.1 W, 1076.375 W with reserve. Eaton5PX1500IRT2UG2 +2EBM48: 67 min at 1100 W; after0.85x0.8, 45.56 min against 30 min. FAS and IDS each have one 12 V17 Ah battery; budgets, charging, and low-voltage conditions calculated. FAS upstream of PWP, UPS downstream with physical RPO and AC-input disconnection. No generator/automatic transfer. Egress remains mechanical after depletion.
- Counts changed24→8 cameras, 14→5 ACS points, 80→11 FAS detectors, 4→1 fire panel, 4→1 IDS panel, 24→6 PIRs. The former1520 m ring is replaced by 85 m duct tree; 1882 m is total cable purchase from individual cuts, not one route. Register: 100 devices/assemblies, 121 connections; factory items are not counted again in power/cable metres.

## IDs and input for B

`data/design.json` is the sole model; `make data` regenerates the register and `generated/` tables. SITE metres: x east, y north; add(20, 25, 0) to T0 local coordinates. Walls, openings, thicknesses, swings, obstacles, parking, person route, camera fields, and every3D cable polyline are in the data. `penetrations` lists30 actual wall crossings with cables. L1 order and port endpoints are binding. B does not select counts, addresses, channels, or lengths.

- N0 is the only cabinet; N1-N3 removed. CSP-0/SSWiN-0 retained; units1-3 removed.
- C01-C08 have new roles/positions; C09-C24 retired. D01-D04 are new ACS points; D05-D07 ordinary doors, D08-D12 retired. G01 is manual; G02 excluded. New E01-E03 are exits without ACS.
- R1-R4 now identify internal routes, not the old ring. R5-R8 are site ducts. Every cable also has its full polyline, plan/vertical/slack/purchase lengths; that polyline determines branch routing.
- Draw: site with open approaches; all-room/device plan; PATH1 and justified views; L1 and ACS/IDS/IP routes/circuits; functional schematic; Q0/Q1/Q2 and RPO power. B chooses presentation and vector sources.

Legacy drawings/sources are retained but excluded from PDF. Generator v1 refuses schema2 before writing, protecting the register. A's ZIP contains data/exports; add new drawings/sources after B. C completes Latin Modern12 pt, about 25 mm margins, black links, page numbering, and editing; A deliberately retains the main former layout.

## Actual outstanding issues

Formal details and university-required AI disclosure: user/C. Before real implementation: geometry/ground/PE/disconnection/RCD measurements; view, notification, accessibility, smoke/heat tests; low-battery voltage, autonomy and RPO tests; delivered device versions/documents. The 20.4 V regulated-loop threshold, minimum efficiencies, and placement radii are project checking assumptions, not fabricated catalogue data or research results. Missing complete standards and the restricted installer manual03/26 are disclosed. Full construction compliance is not claimed. A failed test requires model revision before implementation, not arbitrary redrawing by B.
