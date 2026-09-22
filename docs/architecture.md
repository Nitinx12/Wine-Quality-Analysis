# Architecture — Placeholder

> TODO: Describe high-level pipeline.

## Pipeline
```
data/raw (UCI) -> scripts/* (R + Python) -> output/ + figures/ -> reports/report.Rmd -> output/report.html
```

## Components
- **Ingestion**: `scripts/Wine_Quality_Analysis.R:reads` + `scripts/wine-data-analysis.py:reads` fetch CSVs via URL.
- **EDA**: count plots, boxplots, correlation heatmap.
- **Dimensionality Reduction**: PCA (scaled, prcomp / sklearn.decomposition.PCA).
- **Modeling**: OLS regression, clustering (k-means), classification (logistic + RF).
- **Reporting**: RMarkdown + LaTeX, Docker reproducibility.

## Decisions
- Keep R + Python in sync; Python resolves project root via `Path(__file__).parent.parent`.
- Outputs gitignored; CI uploads artifacts.

## Future
- [ ] Migrate report to Quarto
- [ ] Add DVC for data versioning
- [ ] Centralize params in `config/config.yaml`
