#!/bin/sh
# Compila a dissertação (requer XeLaTeX, BibTeX, makeindex e ghostscript).
# Uso: sh compilar.sh
# set -e
# xelatex -interaction=nonstopmode thesis.tex
# bibtex thesis
# makeindex -s nomencl.ist -o thesis.nls thesis.nlo
# xelatex -interaction=nonstopmode thesis.tex
# xelatex -interaction=nonstopmode thesis.tex
# xelatex -interaction=nonstopmode thesis.tex

# Alteração da compilação para Lualatex
set -e
lualatex -interaction=nonstopmode thesis.tex
