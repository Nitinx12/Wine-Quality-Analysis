# Methodology — Placeholder

## 1. Exploratory Data Analysis
- Quality counts by type (bar)
- Alcohol vs quality (jitter/strip)
- Chemical attributes by quality (faceted boxplots)
- Correlation heatmap (numeric vars)

## 2. PCA
- Standardized predictors (center + scale)
- Scree + biplot (factoextra / sklearn)

## 3. Regression
- `lm(num_quality ~ alcohol + sulphates + pH + type)` (R) / `statsmodels OLS` (Python)
- Diagnostics: residuals vs fitted, fitted vs actual

## 4. Clustering & Classification (scripts/Wine_Clustering_and_Classification.R)
- K-means (elbow + silhouette, k=3)
- Train/test 70/30, logistic + RF (caret), CV=5, ROC/AUC

> TODO: Expand with equations, hyperparams, cross-val scheme.

## Reproducibility
- `set.seed(123)` (R), `StandardScaler` + fixed splits.
- `Makefile` + `run_analysis.sh` + `Dockerfile` + GitHub Actions CI.

## Limitations — Placeholder
- Class imbalance (high quality >=7 is minority)
- Linear model R² ~0.22 suggests non-linearity
- Data is observational, not causal
