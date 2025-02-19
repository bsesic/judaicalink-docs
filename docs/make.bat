# Makefile for JudaicaLink Documentation

# Default target
.DEFAULT_GOAL := help

# Variables
SPHINX_BUILD = sphinx-build
SPHINX_SOURCE = .
SPHINX_BUILD_DIR = _build

.PHONY: help
help:
	@echo "Available commands:"
	@echo "  make html      - Build the HTML documentation"
	@echo "  make clean     - Remove all build artifacts"
	@echo "  make latexpdf  - Build a PDF using LaTeX"
	@echo "  make gettext   - Extract translatable messages"
	@echo "  make serve     - Serve built documentation locally"

.PHONY: html
html:
	$(SPHINX_BUILD) -b html $(SPHINX_SOURCE) $(SPHINX_BUILD_DIR)/html

.PHONY: clean
clean:
	rm -rf $(SPHINX_BUILD_DIR)

.PHONY: latexpdf
latexpdf:
	$(SPHINX_BUILD) -b latex $(SPHINX_SOURCE) $(SPHINX_BUILD_DIR)/latex
	cd $(SPHINX_BUILD_DIR)/latex && latexmk -pdf -f *.tex

.PHONY: gettext
gettext:
	$(SPHINX_BUILD) -b gettext $(SPHINX_SOURCE) $(SPHINX_BUILD_DIR)/locale

.PHONY: serve
serve:
	python -m http.server --directory $(SPHINX_BUILD_DIR)/html

