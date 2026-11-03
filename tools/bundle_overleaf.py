#!/usr/bin/env python3
"""Package the reproducible A sources; B will add current vector sources later."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parents[1]
dest = root / 'output/airport-overleaf.zip'
dest.parent.mkdir(exist_ok=True)
files = [root / n for n in ('main.tex', 'preamble.tex', 'metadata.tex', 'Makefile', 'README.md', 'requirements-figures.txt')]
for directory, pattern in (('sections','*.tex'), ('generated','*.tex'), ('data','*.json'), ('tools','*.py')):
    files.extend((root / directory).glob(pattern))
files.extend(root / 'docs' / n for n in ('design-decisions.md', 'device-register.md'))
with ZipFile(dest, 'w', compression=ZIP_DEFLATED) as z:
    for f in sorted(set(files)):
        z.write(f, f.relative_to(root).as_posix())
    z.writestr('INSTRUCTIONS.txt', 'Package A: main.tex, pdfLaTeX. Current generated/ tables are included. Legacy drawings are excluded; B produces new vector drawings. data/design.json is the sole model; locally run make data, make check, make pdf. After B, add current drawings and their sources to the package.\n')
print(dest)
