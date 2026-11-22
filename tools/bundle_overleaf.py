#!/usr/bin/env python3
"""Package report sources, model, figures and their TikZ sources for Overleaf."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parents[1]
dest = root / 'output/lotnisko-overleaf.zip'
dest.parent.mkdir(exist_ok=True)
files = [root / n for n in ('main.tex', 'preamble.tex', 'metadata.tex', 'Makefile', 'README.md')]
for directory, pattern in (('sections','*.tex'), ('generated','*.tex'), ('data','*.json'), ('tools','*.py'), ('figures','*.pdf'), ('figures/src','*.tex')):
    files.extend((root / directory).glob(pattern))
files.extend(root / 'docs' / n for n in ('ustalenia-projektowe.md', 'rejestr-urzadzen.md'))
with ZipFile(dest, 'w', compression=ZIP_DEFLATED) as z:
    for f in sorted(set(files)):
        z.write(f, f.relative_to(root).as_posix())
    z.writestr('INSTRUKCJA.txt', 'main.tex, pdfLaTeX. Tabele generated/ i rysunki figures/*.pdf są włączone. Źródła rysunków TikZ: figures/src, lokalnie make figures. Lokalnie make data, make check, make pdf.\n')
print(dest)
