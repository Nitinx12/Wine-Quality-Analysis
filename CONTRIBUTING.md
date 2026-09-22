# Contributing — Placeholder

Thanks for considering contributing!

## Workflow
1. Fork + `git clone`
2. Create branch: `git checkout -b feat/your-feature`
3. Install deps: `uv sync --all-groups` (Python) / install R packages via `scripts/Wine_Quality_Analysis.R` header
4. Make changes, run `make all` locally
5. Run placeholders tests: `uv run pytest tests/ -v` (or `make python`)
6. Commit, push, open PR — CI must pass (`ci.yml`).

## Conventions
- Scripts live in `scripts/`, notebooks in `notebooks/`, reports in `reports/`.
- Do not commit `output/` or `figures/` (gitignored, CI uploads artifacts).
- Add placeholders as `TODO:` comments if feature is incomplete.

## Code Style — Placeholder
- Python: `ruff` / `black` (TODO: add config)
- R: `styler` (TODO)

## Questions
Open an issue using the templates in `.github/ISSUE_TEMPLATE/`.
