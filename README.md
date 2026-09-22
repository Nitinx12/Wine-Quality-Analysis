# Wine Quality Analysis

Analysis of the UCI Wine Quality datasets (red & white) – EDA, PCA, regression, clustering & classification.

## Overview
This repository fetches the UCI Wine Quality datasets, merges red & white wines, explores chemical attributes vs. quality, runs PCA, and fits regression/classification models. R and Python pipelines are kept in sync.

## Prerequisites
- **R >= 4.0** with `tidyverse`, `corrplot`, `factoextra`, `rmarkdown` (and `caret`/`randomForest`/`pROC` for clustering)
- **Python >= 3.10** – managed via [`uv`](https://docs.astral.sh/uv/) (recommended)
- `pandoc` for `report.Rmd` rendering

## Getting Started
```bash
# Clone the repo
git clone https://github.com/Nitinx12/Wine-Analysis.git
cd Wine-Analysis

# Python deps (uv) – creates .venv and installs pandas, sklearn, statsmodels, etc.
uv sync

# Or with pip
pip install -e .
```

## Usage
```bash
# Full pipeline (R analysis + Python analysis + HTML report)
make all
# Outputs: output/wine-1.png … output/wine-8.png  +  figures/*.png  +  output/report.html

# Individual steps
make analysis   # R only (scripts/Wine_Quality_Analysis.R -> output/)
make python     # Python only (uv run python scripts/wine-data-analysis.py -> figures/)
make clustering # R clustering & classification (scripts/Wine_Clustering_and_Classification.R -> output/)
make report     # Knit reports/report.Rmd -> output/report.html

# Shell helper (same as make all)
bash run_analysis.sh
# One-shot Python run
uv run python scripts/wine-data-analysis.py          # headless (Agg backend)
uv run python scripts/wine-data-analysis.py --show   # interactive display
```

## Project Structure
```
Wine-Analysis/
├── .github/
│   ├── workflows/ci.yml            # CI: Python + R pipelines
│   ├── ISSUE_TEMPLATE/             # bug_report / feature_request placeholders
│   ├── pull_request_template.md    # PR template placeholder
│   └── CODEOWNERS                  # placeholder
├── assets/
│   └── images/                     # logo/banner placeholders
├── config/
│   ├── config.yaml                 # central params placeholder
│   └── params.json                 # JSON params placeholder
├── data/
│   ├── raw/                        # sample CSVs (full data fetched at runtime)
│   │   ├── winequality-red-sample.csv
│   │   └── winequality-white-sample.csv
│   ├── interim/                    # interim artifacts (gitignored, placeholder)
│   ├── processed/                  # processed CSVs (gitignored, placeholder)
│   └── external/                   # third-party data placeholder
├── docs/
│   ├── architecture.md             # pipeline design placeholder
│   ├── data_dictionary.md          # column docs placeholder
│   ├── methodology.md              # methods placeholder
│   ├── faq.md                      # FAQ placeholder
│   └── roadmap.md                  # roadmap placeholder
├── examples/
│   ├── example_usage.py            # programmatic usage placeholder
│   └── quickstart.md               # 5-min quickstart placeholder
├── figures/                        # Python outputs (gitignored) — 8 pngs
├── notebooks/
│   ├── Wine_Quality_Analysis.ipynb # R notebook (IR kernel)
│   ├── 02_eda_placeholder.ipynb    # placeholder — extended EDA
│   ├── 03_modeling_placeholder.ipynb # placeholder — model comparison
│   ├── 04_clustering_placeholder.ipynb # placeholder — clustering deep dive
│   └── README.md
├── output/                         # R outputs (gitignored) — wine-*.png, cluster-*.png, report.html
├── reports/
│   ├── report.Rmd                  # RMarkdown → output/report.html
│   ├── report.tex                  # LaTeX (uses ../output/wine-*.png)
│   ├── report.qmd                  # Quarto placeholder
│   └── figures/                    # report figures placeholder
├── scripts/
│   ├── Wine_Quality_Analysis.R
│   ├── Wine_Clustering_and_Classification.R
│   ├── wine-data-analysis.py
│   ├── utils/
│   │   ├── helpers.R               # shared R helpers placeholder
│   │   └── helpers.py              # shared Python helpers placeholder
│   └── README.md
├── tests/
│   ├── test_data.py                # data schema placeholder tests
│   ├── test_analysis.py            # pipeline smoke placeholder tests
│   └── README.md
├── .gitignore / LICENSE / CHANGELOG.md / CONTRIBUTING.md / CODE_OF_CONDUCT.md
├── Dockerfile
├── Makefile                        # all / analysis / python / clustering / report / clean
├── pyproject.toml / uv.lock
└── run_analysis.sh
```

## Docker
```bash
docker build -t wine-analysis .
docker run --rm -v $(pwd)/output:/home/wine_analysis/output -v $(pwd)/figures:/home/wine_analysis/figures wine-analysis
```

## References
- Cortez, Paulo, et al. "Modeling wine preferences by data mining from physicochemical properties." *Decision Support Systems*, 47.4 (2009): 547–553.
- UCI Machine Learning Repository: Wine Quality Data Sets.
