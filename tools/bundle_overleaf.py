#!/usr/bin/env python3
"""Package the reproducible A sources; B will add current vector sources later."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parents[1]
dest = root / 'output/lotnisko-overleaf.zip'
dest.parent.mkdir(exist_ok=True)
files = [root / n for n in ('main.tex', 'preamble.tex', 'metadata.tex', 'Makefile', 'README.md', 'requirements-figures.txt')]
for directory, pattern in (('sections','*.tex'), ('generated','*.tex'), ('data','*.json'), ('tools','*.py')):
    files.extend((root / directory).glob(pattern))
files.extend(root / 'docs' / n for n in ('ustalenia-projektowe.md', 'rejestr-urzadzen.md'))
with ZipFile(dest, 'w', compression=ZIP_DEFLATED) as z:
    for f in sorted(set(files)):
        z.write(f, f.relative_to(root).as_posix())
    z.writestr('INSTRUKCJA.txt', 'Pakiet A: main.tex, pdfLaTeX. Bieżące tabele generated/ są włączone. Dawne rysunki wyłączone; nowe rysunki wektorowe wykonuje B. data/design.json jest jedynym modelem; lokalnie make data, make check, make pdf. Po B uzupełnić pakiet o aktualne rysunki i ich źródła.\n')
print(dest)
