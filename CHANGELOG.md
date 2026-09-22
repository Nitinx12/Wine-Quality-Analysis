# Changelog — Placeholder

All notable changes to this project will be documented in this file.
Format based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]
### Added
- Professional layout: `notebooks/`, `scripts/`, `reports/`, `data/`, `docs/`, `tests/`, `config/`, `examples/`, `assets/`
- GitHub Actions CI (`ci.yml`) for Python + R
- Placeholder docs, configs, tests, GitHub templates

### Changed
- Moved `Wine_Quality_Analysis.R`, `Wine_Clustering_and_Classification.R`, `wine-data-analysis.py` → `scripts/`
- Moved `Wine_Quality_Analysis.ipynb` → `notebooks/`
- Moved `report.Rmd`, `report.tex` → `reports/`
- `Makefile`, `run_analysis.sh`, `report.tex` paths updated

### TODO
- [ ] Wire `config/config.yaml` into pipelines
- [ ] Fill notebook placeholders `02_`, `03_`, `04_`
- [ ] Add real tests beyond smoke
- [ ] Add Quarto report placeholder

## [0.1.0] - 2026-09-22
- Initial R + Python pipelines, figures, output
