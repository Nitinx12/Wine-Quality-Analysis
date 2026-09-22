# Data Directory
This directory stores datasets for Wine Quality Analysis.

## Structure
- \aw/\ — original UCI CSVs (downloaded via scripts, gitignored - see placeholder samples)
- \interim/\ — intermediate cleaned files
- \processed/\ — final analysis-ready datasets
- \xternal/\ — third-party or reference data

## Source
UCI Machine Learning Repository:
- https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv
- https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv

> **Note:** Full datasets are fetched at runtime by \scripts/Wine_Quality_Analysis.R\ and \scripts/wine-data-analysis.py\. Placeholders in \aw/\ illustrate schema.

## Placeholder
See \aw/winequality-red-sample.csv\ and \aw/winequality-white-sample.csv\ for schema examples.
