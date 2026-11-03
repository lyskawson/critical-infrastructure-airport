# Initial audit and document structure

Date: 19 October 2026. Review of the local version at HEAD `8112694`, without changing the technical design. This is a historical assessment of the initial model.

## Basis and performed checks

Read all `sections/*.tex`, `main.tex`, `preamble.tex`, `metadata.tex`, `data/design.json`, the three `tools/` scripts, Makefile, workflow, and project documentation. No AGENTS.md was found in the project or checked ancestors. In the style reference, read AGENTS.md, its referenced CLAUDE.md, main.tex, latex-settings.tex, and README; inspected the title page. The reference was unchanged and no formal details were copied.

The then-current `output/pdf/north-airport.pdf` had 21 pages. All pages were freshly rendered, contact sheets reviewed, and pages 10 and 12 inspected in detail. This was not final acceptance of every page at its target scale. Working material: `tmp/pdfs/audyt-start-2026-10-19/`.

- `python3 tools/validate_design.py`: OK for the existing assumptions. Independent calculation confirmed 1520 m of routes and 7.2576 TB recording / 9.072 TB with 25% reserve; this did not validate camera selection or local-installation quantities.
- Baseline compilation using `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=tmp/pdfs/audyt-start-2026-10-19/build main.tex`: successful, 21 pages. Final main.log had no warnings, undefined references, or overfull/underfull messages. First-pass reference warnings disappeared after automatic reruns.
- Existing Overleaf ZIP: valid CRC, main.tex at root, 32 entries. Included figure PDFs but not data/design.json, the generator, or its dependencies; it therefore lacked reproducible drawing sources. No new Overleaf-service import was performed.

## Main gaps

1. **Unresolved site model.** JSON mainly held four aggregate nodes; functions of six terminal areas and D01-D06 positions were separately embedded in the generator (`tools/generate_figures.py:179`). Room heights/conditions and complete entrances/exits were missing. All six terminal-plan access points were internal; no exterior doors were shown. The register described assemblies rather than individual devices (`docs/device-register.md`). A must define geometry/IDs before B draws them.

2. **FAS remained a quantity allowance.** `sections/05-fire.tex:13` explicitly called 20 hangar detectors a reserve; eight I/O modules were not a control design. The generator created 48 points with `range(6)` and `range(8)` (`tools/generate_figures.py:198`) regardless of room functions. Missing: devices/addresses, real connections, detector-type/range justification, isolator allocation, alarm circuits, and cause-and-effect matrix. Voice alarm and fire transmission were unresolved. A must resolve this; B cannot fix it through drawing alone.

3. **CCTV, ACS, and IDS lacked specific tasks/circuits.** The 2688 px / 10 m example was arithmetically useful but not assigned to C01-C24. Mounting heights, directions, targets, and image widths were missing. The report correctly avoided claiming full 24 ha coverage; the issue was lack of designed selected views. Doors lacked individual locking types, release connections, and power-loss states. IDS detectors were not assigned to rooms, inputs, or partitions.

4. **Quantities and power did not follow a register.** R1-R4 had verifiable geometry, but 1800 m of Cat.6 A, 2200 m of ACS/IDS cable, local FAS lengths, and 1700 m of power cable were estimates (`sections/10-terminal.tex:5`, `sections/14-materials-b.tex:32`). There was no connection list, supply routing, or voltage-drop calculation. The 1335 W total and UPS split added correctly, but panels had equal assumed currents despite different assemblies; 400 W for DC/charging was generic reserve. The text correctly stated that 0.927 kWh did not prove 30 min; A must establish a checkable model and manufacturer curves, separately from later acceptance testing.

5. **Data/interface consistency was partial.** The validator hard-coded equipment totals, power, and 1520 m (`tools/validate_design.py:10`); drawing checks only tested file existence. IDs, rooms, connection lengths, port maps, FAS circuits, and materials were not checked. Drawings also contained numbers outside JSON. No compatible reference FAS family or optical-bus parameters were given. A must adopt a verifiable solution/data; B reproduces topology and relationships.

6. **AI and procedures needed completion.** Local processing and a sensible validation proposal were described without fictional results. Specific cameras, region, and one resolved scenario were missing (`sections/11-ai.tex`). Procedures had roles/actions, but restoration conditions were mainly a shared note rather than conditions for each scenario (`sections/15-procedures.tex`). These could be completed without writing an operations handbook.

7. **PDF presentation conflicted with the request.** It used 11 pt forced sans serif, 20-22 mm margins, coloured headings, boxes, and repeated working labels (`preamble.tex`). The title had a rendering/AI caption, contents a requirements panel, and the acceptance chapter team-allocation instructions. `main.tex` forced clearpage before each file, leaving large blank areas. Reference: Latin Modern 12 pt and about 25 mm, without copying the book class, university headings, or personal details. C is the layout-rebuild stage.

## Eight requirements against the starting state

All eight topics had source sections, but presence alone did not satisfy the assignment. Title needed layout/formal details(C/user); contents needed cleanup/automatic links(C); technical/AI content and materials needed resolved model/selections(A); locations/routes needed complete connections(A), then proper drawings(B). The schematic needed concrete interfaces(A/B), power needed load-derived sizing/manufacturer sources(A/B), and procedures needed clear response/restoration conditions(A). C finally assembles and checks the PDF.

## Proposed final structure

Conventional title page and contents, followed by:

1. **Subject, scope, and site model** - functions/geometry, assumed conditions, zones, and material threats; assumptions stated once.
2. **Protection-system design** - CCTV, ACS/IDS, FAS; selections, tasks, failure states, and cause-and-effect.
3. **Network, integration, and ML/AI** - topology, interfaces, ports/fibres, one AI case, access/data requirements.
4. **Locations and installation routes** - site/floor plans, IDs, circuits, lengths, and register references.
5. **Power and design calculations** - storage, transmission, PoE, power, voltage, batteries, reserve supply; calculations may accompany selections where clearer.
6. **Main materials** - equipment/licences, cables, accessories, explicit stock; model-derived quantities.
7. **Security procedures and verification** - trigger, responsibility, action, restoration, real test criteria; no team-work organisation.
8. **References** - primary sources tied to specific parameters/claims.

The full register and larger drawings may be appendices in the same PDF. No fixed page/drawing count or one-page-per-file rule. This numbering is an editorial proposal, not permission for C to alter technical quantities.

## Limited primary-source review

Reviewed available [Government Security Centre](https://www.gov.pl/web/rcb/infrastruktura-krytyczna), [ELI - Journal of Laws 2023, item 822](https://eli.gov.pl/eli/DU/2023/822/ogl), and [Polish Committee for Standardization notice](https://www.pkn.pl/komunikat-online). RCB distinguishes strategic significance from formal critical-infrastructure designation. PKN lists PN-EN IEC 62676-4:2026-01 as replacing PN-EN 62676-4:2015-06; this confirms the designation, not the provisions.

In the [2023 ELI text reviewed](https://eli.gov.pl/api/acts/DU/2023/822/text.html), Sections 28(1)(19) and 29(1)(8) concern stations and ports accommodating more than 500 people. The then-assumed terminal occupancy of 300 did not resolve whole-site assessment or other triggers. ELI listed two later amendments; they were not fully analysed in this audit. A must verify current law, applicability, device datasheets, and compatibility. This audit made no decision on mandatory voice alarm or PSP transmission.
