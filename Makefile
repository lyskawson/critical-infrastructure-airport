PYTHON ?= python3

.PHONY: pdf data check figures overleaf clean

data:
	$(PYTHON) tools/export_design.py

pdf: data check
	latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex
	mkdir -p output/pdf
	cp build/main.pdf output/pdf/north-airport.pdf

check:
	$(PYTHON) tools/validate_design.py

figures:
	$(PYTHON) tools/generate_figures.py

overleaf: data check
	$(PYTHON) tools/bundle_overleaf.py

clean:
	latexmk -C -outdir=build main.tex
