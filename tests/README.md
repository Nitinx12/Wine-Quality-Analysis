# Tests — Placeholder

Run placeholder tests:

```bash
uv sync --all-groups
uv run pytest tests/ -v
# or
uv run python -m pytest
```

## Coverage — TODO
- [ ] Data schema validation (columns, dtypes, no NAs in quality)
- [ ] Pipeline smoke: scripts generate expected files
- [ ] Regression coefficients sign checks
- [ ] PCA variance sanity (cumulative > 80% by 5 PCs)

See `test_data.py` and `test_analysis.py` for stubs.
