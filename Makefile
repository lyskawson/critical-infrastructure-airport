PYTHON ?= python3

.PHONY: pdf data check figures overleaf clean

data:
	$(PYTHON) tools/export_design.py

pdf: data check
	latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex
	mkdir -p output/pdf
	cp build/main.pdf output/pdf/lotnisko-polnoc.pdf

check:
	$(PYTHON) tools/validate_design.py

figures:
	cd figures/src && for f in fig-*.tex; do \
		latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=../../build/figures "$$f" && \
		cp "../../build/figures/$${f%.tex}.pdf" .. || exit 1; \
	done

overleaf: data check
	$(PYTHON) tools/bundle_overleaf.py

clean:
	latexmk -C -outdir=build main.tex
