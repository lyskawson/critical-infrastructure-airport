# Team responsibilities and presentation

This is the original team-planning note. The current technical model and execution status are recorded in `docs/design-decisions.md`; the original four-node presentation example below refers to the earlier concept.

## Suggested packages

| Package | Owner | Main sections/ sources |
|---|---|---|
| Site, risks, site plan, and routes | Person A | 01, 02, 08-10; JSON geometry |
| CCTV, ACS, IDS, and register | Person B | 03, 04; equipment schedule |
| FAS, power, and procedures | Person C | 05, 12, 13, 15 |
| Network, AI, editing, and sources | Person D | 06, 07, 11, 16-18 |

A smaller team may combine packages. Agree dates within the team; course week numbering is not a requirement here.

## Editing rules

1. Assign one person to merge changes.
2. Any device-count change requires checking prose, drawings, power, and materials.
3. After geometry changes, regenerate applicable drawings and include final figure PDFs in the commit. The legacy generator remains disabled for the current model until rebuilt.
4. Check the PDF before merging, not only the build status.
5. Agree the final title page and document version together.

## Suggested presentation, about 8-10 minutes

- **1 min:** site fragment and protection objectives.
- **2 min:** site plan, four nodes, and routing in the original concept; adapt to the accepted model.
- **2 min:** a door alarm - ACS, camera, SOC, and security response.
- **1 min:** fire - local panel, evacuation, and independence from AI.
- **1 min:** what remains available after network and power failure.
- **1 min:** recording, power, and backup runtime.
- **1-2 min:** AI evaluation and remaining limitations.

There is no need to read every page. Show plans, architecture, and power; use tables to support selections.

## Topics for instructor consultation

- Acceptance of a fictional site and terminal/technical-area scope.
- Need for specific device models or a cost estimate.
- Expected detail of floor plans and FAS control matrices.
- Whether voice alarm, fire transmission, or the whole airport perimeter belongs in an extension.
