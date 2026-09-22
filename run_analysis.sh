#!/usr/bin/env bash
# run_analysis.sh — downloads data, runs R + Python analysis and builds report
# Usage: ./run_analysis.sh  (or) bash run_analysis.sh
# Requires: Rscript, uv (for Python), pandoc (for rmarkdown)

set -euo pipefail

echo "1. Running R analysis (scripts/Wine_Quality_Analysis.R)..."
Rscript scripts/Wine_Quality_Analysis.R

echo "2. Running Python analysis (scripts/wine-data-analysis.py)..."
if command -v uv >/dev/null 2>&1; then
  uv run python scripts/wine-data-analysis.py
else
  python scripts/wine-data-analysis.py
fi

echo "3. Rendering RMarkdown report (reports/report.Rmd -> output/)..."
Rscript -e "rmarkdown::render('reports/report.Rmd', output_dir='output')"

echo "Done. R outputs in ./output/, Python outputs in ./figures/."
