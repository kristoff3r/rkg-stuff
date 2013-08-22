#!/bin/bash
./genstregliste.py
for tex in *.tex; do pdflatex $tex; done
