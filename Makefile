# Makefile for Wine Quality Analysis

.PHONY: all data analysis report python clean

# Default: reproduce full analysis (R + Python + report)
all: analysis python report

# Run the R analysis script (downloads data, generates output/wine-*.png)
analysis:
	Rscript scripts/Wine_Quality_Analysis.R

# Kept for backward compat – data and analysis are the same step (no double run)
data: analysis

# Run Python analysis via uv (generates figures/*.png)
python:
	uv run python scripts/wine-data-analysis.py

# Knit the RMarkdown report (output/report.html)
report: analysis
	Rscript -e "rmarkdown::render('reports/report.Rmd', output_dir='output')"

# Clustering / classification (optional, not in default all)
clustering:
	Rscript scripts/Wine_Clustering_and_Classification.R

# Clean up generated files (keep source)
clean:
	rm -rf output/*.png output/*.html output/*.pdf figures/*.png
	rm -f *.pdf *.html wine-*.png
