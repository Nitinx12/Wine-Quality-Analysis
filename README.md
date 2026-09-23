<div align="center">

<img src="assets/wine-logo.png" width="355" alt="Wine Quality Analysis" />

# Wine Quality Analysis

**Which chemistry predicts a better-tasting wine?**

Exploratory analysis, regression, and clustering/classification on the UCI Wine Quality dataset — with parallel **R + Python** pipelines, a reproducible **RMarkdown report**, and a **Docker** image.

[![Python](https://img.shields.io/badge/python-%3E%3D3.10-blue?logo=python&logoColor=white)](pyproject.toml)
[![R](https://img.shields.io/badge/R-4.3-276DC3?logo=r&logoColor=white)](Dockerfile)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Ruff](https://img.shields.io/badge/lint-Ruff-000000?logo=ruff)](pyproject.toml)
[![Docker](https://img.shields.io/badge/container-Docker-2496ED?logo=docker&logoColor=white)](Dockerfile)

</div>

## Overview

This project asks a simple question: **can physicochemical measurements explain expert quality scores for wine?** Using the UCI Wine Quality dataset (red and white Vinho Verde from Portugal), it links 11 lab-measured properties — acidity, sugar, sulphates, alcohol, pH, and more — to sensory quality ratings (3–9).

Everything runs end-to-end and reproduces bit-for-bit:

- **Dual pipeline** — same analysis in R (`scripts/Wine_Quality_Analysis.R`) and Python (`scripts/wine-data-analysis.py`) for cross-validation
- **Interactive notebook** — `notebooks/Wine_Quality_Analysis.ipynb` for exploration
- **Knitted report** — `reports/report.Rmd` → `output/report.html`
- **One-command reproducibility** — `make all` or `docker run`

> Source: [UCI ML Repository — Wine Quality](https://archive.ics.uci.edu/dataset/186/wine+quality) (Cortez et al., 2009). 6,497 rows — 1,599 red, 4,898 white.

---

## Dataset at a Glance

| Property | Detail |
|---|---|
| **Samples** | 6,497 wines (4,898 white, 1,599 red) |
| **Features** | 11 numeric: fixed/volatile acidity, citric acid, residual sugar, chlorides, free/total SO₂, density, pH, sulphates, alcohol |
| **Target** | `quality` — sensory score 3–9 (median 6; 77% of samples are 5–6) |
| **Mean quality** | White 5.88 vs. Red 5.64 |
| **No missing values** | Semicolon-delimited CSVs fetched directly from UCI |

---

## What We Analyze

| # | Analysis | What it does | Output |
|---|---|---|---|
| 1 | **Distribution & class balance** | Quality histograms split by type; checks skew and imbalance | `wine_quality_counts.png` / `wine-1.png` |
| 2 | **Feature relationships** | Alcohol vs. quality (jitter/strip), boxplots of pH / sugar / citric acid / sulphates by quality | `alcohol_vs_quality.png`, `attributes_by_quality.png` |
| 3 | **Correlation structure** | Pearson heatmap across all 11 predictors + quality | `correlation_heatmap.png` |
| 4 | **Dimensionality reduction (PCA)** | Standardized PCA — scree + biplot with loadings | `pca_scree.png`, `pca_biplot.png` |
| 5 | **Regression** | OLS predicting quality from alcohol + sulphates + pH + type; residuals-vs-fitted & fitted-vs-actual diagnostics | `residuals_vs_fitted.png`, `fitted_vs_actual.png` |
| 6 | **Clustering** | K-means on scaled chemistry — elbow & silhouette to pick *k*, PCA scatter with clusters | `cluster-elbow.png`, `cluster-silhouette.png`, `cluster-pca.png` |
| 7 | **Classification** | Binary *high quality (≥7)* — 70/30 split, 5-fold CV: logistic regression vs. random forest, confusion matrices & ROC/AUC | `roc-logistic.png`, `roc-randomforest.png` |

> R main analysis: `scripts/Wine_Quality_Analysis.R:1` · Python mirror: `scripts/wine-data-analysis.py:1` · Clustering/classification: `scripts/Wine_Clustering_and_Classification.R:1`

---

## Key Findings

Based on the full 6,497-row dataset — not just plots, but the numbers behind them:

**1. Alcohol is the strongest single predictor.**
Pearson *r* = **0.44** with quality — far ahead of the next best (citric acid 0.09). Density (*r* = –0.31) and volatile acidity (*r* = –0.27) are the strongest negative correlates. Higher-alcohol wines consistently score higher, visible in both red and white.

**2. Chemistry explains some, but not all, of taste.**
OLS `quality ~ alcohol + sulphates + pH + type` gives **R² ≈ 0.22** (adj. R² 0.219, *n*=6,497). Significant: alcohol **+0.32 per vol%** (*p* < 0.001), sulphates **+0.70** (*p* < 0.001), white vs. red **+0.33** (*p* < 0.001). pH is not significant once the others are controlled — sensory quality is noisy and partly subjective.

**3. White and red wines live in different chemical neighborhoods.**
Whites average higher residual sugar and free SO₂; reds higher volatile acidity and sulphates. That shift drives PCA: **PC1 (27.5%)** loads on sulfur compounds and sugar vs. acidity, **PC2 (22.7%)** on density and acidity vs. alcohol. Together PC1+PC2 capture **~50%** of variance; five PCs reach ~80%.

**4. Structure without labels still finds groups.**
On standardized predictors, elbow and silhouette curves point to **k = 3** clusters. A PCA projection with K-means assignments shows reasonably separated ellipses — clustering recovers chemically coherent groups even before quality is introduced.

**5. Predicting "high quality" (≥7) is feasible but hard.**
Only **~16%** of wines score ≥7, so the task is imbalanced. Logistic regression and random forest (5-fold CV, tuned via `caret`) both produce meaningful ROC curves (see `output/roc-*.png`); random forest ranks **alcohol, sulphates, and volatile acidity** highest in variable importance, echoing the correlation/regression story.

> Bottom line: alcohol and sulphates matter most, whites score marginally higher, and chemistry alone gets you about a fifth of the way to predicting taste — useful signal, not a full substitute for a palate.

---

## Figures

Generated by the Python pipeline into `figures/` (R pipeline mirrors to `output/wine-*.png`):

<p align="center">
  <img src="figures/wine_quality_counts.png" width="48%" alt="Quality counts by type" />
  <img src="figures/alcohol_vs_quality.png" width="48%" alt="Alcohol vs quality" />
</p>
<p align="center">
  <img src="figures/correlation_heatmap.png" width="48%" alt="Correlation heatmap" />
  <img src="figures/pca_biplot.png" width="48%" alt="PCA biplot" />
</p>
<p align="center">
  <img src="figures/fitted_vs_actual.png" width="48%" alt="Fitted vs actual" />
  <img src="figures/residuals_vs_fitted.png" width="48%" alt="Residuals vs fitted" />
</p>

*See also `figures/pca_scree.png`, `figures/attributes_by_quality.png`, and clustering ROC plots in `output/`.*

---

## Project Structure

```
Wine-Analysis/
├── assets/                          # logo
├── figures/                         # Python-generated plots
├── notebooks/
│   └── Wine_Quality_Analysis.ipynb  # interactive R notebook
├── reports/
│   ├── report.Rmd                   # knitted HTML report
│   └── report.tex
├── scripts/
│   ├── Wine_Quality_Analysis.R              # main R pipeline
│   ├── Wine_Clustering_and_Classification.R # clustering + classification
│   └── wine-data-analysis.py                # Python pipeline
├── Dockerfile
├── Makefile
├── pyproject.toml
├── run_analysis.sh
└── uv.lock
```

---

## Tech Stack

`Python` `R` `Jupyter` `pandas` `numpy` `scikit-learn` `statsmodels` `matplotlib` `seaborn` `tidyverse` `corrplot` `factoextra` `caret` `randomForest` `pROC` `cluster` `RMarkdown` `Docker` `uv` `Ruff`

---

## Getting Started

### Prerequisites

- R 4.x + `tidyverse`, `corrplot`, `factoextra`, `rmarkdown`, `caret`, `randomForest`, `pROC`, `cluster`
- Python ≥3.10 + [uv](https://github.com/astral-sh/uv)
- pandoc (for the HTML report) — or just use Docker

### Install

```bash
# Python deps
uv sync

# R deps
R -e "install.packages(c('tidyverse','corrplot','factoextra','rmarkdown','caret','randomForest','pROC','cluster'), repos='https://cloud.r-project.org')"
```

---

## Usage

```bash
make all          # R + Python + report → output/*.png, figures/*.png, output/report.html
make analysis     # R only
make python       # Python only (uv run python scripts/wine-data-analysis.py)
make clustering   # K-means + classification
make report       # knit reports/report.Rmd
make clean        # remove generated files
```

Shell helper (same as `make all`):

```bash
bash run_analysis.sh
```

Python flags:

```bash
uv run python scripts/wine-data-analysis.py          # headless (Agg backend, CI-friendly)
uv run python scripts/wine-data-analysis.py --show    # interactive display
```

---

## Docker (no local setup)

```bash
docker build -t wine_analysis .
docker run --rm \
  -v "$(pwd)/output:/home/wine_analysis/output" \
  -v "$(pwd)/figures:/home/wine_analysis/figures" \
  wine_analysis   # runs `make all` by default
```

The image installs R, Python via `uv`, and pandoc.

---

## Reports

- **HTML report**: `make report` → `output/report.html` (from `reports/report.Rmd:1`)
- **LaTeX**: `reports/report.tex`
- **Notebook**: open `notebooks/Wine_Quality_Analysis.ipynb` with an R kernel

---

## References

- Cortez, P. et al. "Modeling wine preferences by data mining from physicochemical properties." *Decision Support Systems*, 47(4), 2009.
- UCI Machine Learning Repository: Wine Quality Datasets.

## License

MIT — see [LICENSE](LICENSE).

## Author

**Nitin Kumar Sharma** — [@Nitinx12](https://github.com/Nitinx12) · [nitinx12.github.io](https://nitinx12.github.io)
