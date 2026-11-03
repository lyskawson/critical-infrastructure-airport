# North Airport - Critical Infrastructure Security

An academic security-system design for a fictional airport terminal and staff car park. The project combines CCTV, access control, intrusion and hold-up alarms, fire detection, network design, and backup power in a reproducible LaTeX report.

[Technical report](output/pdf/north-airport.pdf) · [Device and connection register](docs/device-register.md) · [Overleaf guide](docs/overleaf.md)

## Scope

The model covers an 80 × 60 m site with a 24 × 16 m terminal, seven rooms, and ten parking spaces. It includes eight fixed cameras, four controlled doors, a manually operated card-controlled vehicle gate, one intrusion panel, and one fire panel. A single video-analytics scenario detects a person crossing a line in the vehicle lane.

Geometry, device specifications, cable routes, material quantities, and calculation inputs are defined in `data/design.json`. The report includes storage and bandwidth budgets, PoE allocation, battery sizing, voltage drop, UPS runtime, and incident-response procedures. The design is an academic model; its dimensions and operating targets are stated assumptions rather than site measurements.

## Build

Requires Python 3 and TeX Live or MacTeX with `latexmk`, pdfLaTeX, `longtable`, and `xurl`. Data export and validation use only the Python standard library.

```sh
make pdf
```

The report is written to `output/pdf/north-airport.pdf`; the compilation log is `build/main.log`.

```sh
make data
make check
python3 tools/validate_design.py --self-test
```

`make data` regenerates tables and the device register. `make check` verifies model consistency and export freshness. The self-test checks that intentionally invalid variants are rejected without changing the source model.

## Overleaf

```sh
make overleaf
```

Upload `output/airport-overleaf.zip` as an Overleaf project, using `main.tex` and pdfLaTeX. The archive includes the report sources, model, generated tables, and supporting tools. See [the Overleaf guide](docs/overleaf.md) for import and synchronisation options.

## Repository structure

| Path | Contents |
|---|---|
| `data/design.json` | Site geometry, devices, ports, connections, power sources, materials, and source references |
| `sections/` | Technical descriptions, calculations, procedures, and references |
| `generated/` | LaTeX tables and bibliography generated from the model |
| `tools/design_geometry.py` | Camera projection and vehicle-envelope calculations |
| `tools/export_design.py` | Calculations and deterministic document exports |
| `tools/validate_design.py` | Geometry, connectivity, capacity, power, and materials checks |
| `docs/` | Register, design documentation, and development records |
| `figures/` | Archived vector drawings of the earlier site concept, excluded from the current report |
| `output/` | Compiled report and Overleaf archive |

## Licence

[MIT](LICENSE). Illustration provenance and AI-use information are documented in [AI assets](docs/ai-assets.md).
