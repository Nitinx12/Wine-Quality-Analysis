# Reports

Rendered reports and LaTeX source.

| File | Description |
|------|-------------|
| `report.Rmd` | R Markdown report — knits to `../output/report.html` |
| `report.tex` | LaTeX template — uses `../output/wine-*.png` |
| `figures/` | **Placeholder** — report-specific figures (copied from `../output/` / `../figures/` on build) |

## Build
```bash
make report
# or
Rscript -e "rmarkdown::render('reports/report.Rmd', output_dir='output')"
```

> TODO: Add Quarto placeholder (`report.qmd`) for future migration.
