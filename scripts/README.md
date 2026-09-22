# Scripts

All executable analysis scripts. Run from **project root**.

| Script | Purpose | Outputs |
|--------|---------|---------|
| `Wine_Quality_Analysis.R` | Main R EDA + PCA + regression | `output/wine-*.png` |
| `Wine_Clustering_and_Classification.R` | K-means + logistic/RF classification | `output/cluster-*.png`, `output/roc-*.png` |
| `wine-data-analysis.py` | Python mirror of R analysis | `figures/*.png` |
| `utils/helpers.R` | **Placeholder** — shared R helpers (plotting, metrics) | — |
| `utils/helpers.py` | **Placeholder** — shared Python helpers | — |

## Running
```bash
make all        # full pipeline
make analysis   # R only
make python     # Python only
make clustering # clustering only
make report     # knit reports/report.Rmd
```

## Conventions
- Scripts are idempotent and create `output/` / `figures/` if missing.
- Resolve project root via `file.path(project_root, ...)` (R) or `Path(__file__).parent.parent` (Python) so they work from any cwd.
