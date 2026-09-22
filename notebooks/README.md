# Notebooks

Interactive analysis notebooks for Wine Quality.

| Notebook | Description | Kernel |
|----------|-------------|--------|
| `Wine_Quality_Analysis.ipynb` | Main R EDA + PCA + regression (IR kernel) — mirrors `scripts/Wine_Quality_Analysis.R` | R |
| `02_eda_placeholder.ipynb` | **Placeholder** — Extended EDA: distributions, outlier handling, feature engineering | Python |
| `03_modeling_placeholder.ipynb` | **Placeholder** — Model comparison: Ridge, Lasso, RF, XGBoost | Python |
| `04_clustering_placeholder.ipynb` | **Placeholder** — Deep dive on k-means + hierarchical clustering | R / Python |

## Usage
```bash
# R notebook (IR kernel)
jupyter notebook notebooks/Wine_Quality_Analysis.ipynb

# Python placeholders (create venv first)
uv sync
uv run jupyter notebook notebooks/02_eda_placeholder.ipynb
```

> Placeholders contain headers + TODO cells — replace with full analysis as needed.
