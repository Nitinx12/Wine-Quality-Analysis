#!/usr/bin/env python3
"""
Wine Quality Analysis
---------------------

A comprehensive Python script to fetch, analyze, and visualize the UCI Wine Quality
datasets (red & white) from the UCI Machine Learning Repository.

Features:
  1. Downloads both red and white wine CSVs via URL
  2. Merges into a single DataFrame with a "type" column
  3. Exploratory plots:
       • Distribution of quality by wine type
       • Scatter of alcohol vs. quality
       • Boxplots of key chemical attributes by quality
       • Correlation heatmap of numeric variables
  4. PCA on standardized predictors
       • Scree plot + biplot
  5. Linear regression model predicting quality
       • Prints summary & residuals vs fitted
       • Scatter of fitted vs. actual

Usage:
  $ uv run python scripts/wine-data-analysis.py
  $ uv run python scripts/wine-data-analysis.py --no-show   # headless / CI
  $ make python   # via Makefile

Dependencies:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn
  - statsmodels

Notes:
  - Uses Agg backend for headless execution; --show displays interactively.
  - Dummy trap fixed: type encoded with drop_first=True before OLS.
"""

# 0. Imports & matplotlib backend (must be set before pyplot)
import os
from pathlib import Path
import argparse
import pandas as pd
import numpy as np
import matplotlib

# Use non-interactive backend by default for CI / headless runs
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm

# 1. Parse CLI args
parser = argparse.ArgumentParser(description="Wine Quality Analysis")
parser.add_argument("--no-show", dest="show", action="store_false",
                    help="Disable interactive plt.show() (default: save only)")
parser.add_argument("--show", dest="show", action="store_true",
                    help="Enable interactive display")
parser.set_defaults(show=False)
args = parser.parse_args()
SHOW = args.show


def maybe_show():
    """Display figure only when --show is passed; always close afterwards."""
    if SHOW:
        plt.show()
    plt.close("all")


def main():  # noqa: C901 - script is linear analysis
    # 2. Ensure output directory exists (resolve relative to project root)
    # Project root is one level above scripts/ regardless of cwd
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    OUTDIR = PROJECT_ROOT / "figures"
    os.makedirs(OUTDIR, exist_ok=True)

    # 3. URLs for the datasets
    URL_RED = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
    URL_WHITE = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"

    # 4. Read CSVs (semicolon-delimited) with error handling
    try:
        red = pd.read_csv(URL_RED, sep=";", decimal=".")
        red["type"] = "red"
        white = pd.read_csv(URL_WHITE, sep=";", decimal=".")
        white["type"] = "white"
    except Exception as exc:
        raise SystemExit(f"Failed to download wine data: {exc}") from exc

    # 5. Combine & basic cleaning
    wine = pd.concat([red, white], ignore_index=True)
    wine["quality"] = wine["quality"].astype(int)

    print(f"Total observations: {len(wine)}")
    print("Counts by type:\n", wine["type"].value_counts())

    # 6. Distribution of quality by type
    plt.figure(figsize=(8, 5))
    sns.countplot(data=wine, x="quality", hue="type")
    plt.title("Wine Quality Counts by Type")
    plt.xlabel("Quality Score")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(f"{OUTDIR}/wine_quality_counts.png", dpi=150)
    maybe_show()

    # 7. Alcohol vs. Quality scatter
    plt.figure(figsize=(8, 5))
    sns.stripplot(data=wine, x="quality", y="alcohol", hue="type",
                  jitter=True, alpha=0.5)
    plt.title("Alcohol Content vs. Quality")
    plt.xlabel("Quality Score")
    plt.ylabel("Alcohol (%)")
    plt.tight_layout()
    plt.savefig(f"{OUTDIR}/alcohol_vs_quality.png", dpi=150)
    maybe_show()

    # 8. Boxplots of key chemical attributes by quality
    attrs = ["pH", "residual sugar", "citric acid", "sulphates"]
    wine_melt = wine.melt(id_vars=["quality"], value_vars=attrs,
                          var_name="attribute", value_name="value")
    g = sns.catplot(data=wine_melt, x="quality", y="value",
                    col="attribute", kind="box", col_wrap=2, sharey=False,
                    height=4, aspect=1.2)
    g.fig.subplots_adjust(top=0.9)
    g.fig.suptitle("Chemical Attributes by Wine Quality")
    # Fix y-label mapping: iterate over axes in column order, not enumerate order
    for ax, attr in zip(g.axes.flat, attrs):
        ax.set_xlabel("Quality")
        ax.set_ylabel(attr.title())
    # Handle case of fewer axes than attrs (future-proof)
    plt.savefig(f"{OUTDIR}/attributes_by_quality.png", dpi=150)
    maybe_show()

    # 9. Correlation heatmap (numeric vars only, keep quality for insight)
    numeric = wine.select_dtypes(include=np.number)
    # Include quality in corr so its relationships are visible; drop only if needed
    corr = numeric.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", square=True)
    plt.title("Correlation Matrix of Wine Attributes (incl. quality)")
    plt.tight_layout()
    plt.savefig(f"{OUTDIR}/correlation_heatmap.png", dpi=150)
    maybe_show()

    # 10. PCA on scaled numeric predictors (exclude quality as target)
    numeric_for_pca = numeric.drop(columns=["quality"])
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(numeric_for_pca)
    pca = PCA()
    pca.fit(X_scaled)

    # Scree plot
    plt.figure(figsize=(6, 4))
    plt.plot(np.cumsum(pca.explained_variance_ratio_) * 100, marker="o")
    plt.xlabel("Number of Components")
    plt.ylabel("Cumulative Explained Variance (%)")
    plt.title("PCA Scree Plot")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{OUTDIR}/pca_scree.png", dpi=150)
    maybe_show()

    # Biplot (first two PCs)
    pcs = pca.transform(X_scaled)
    plt.figure(figsize=(8, 6))
    plt.scatter(pcs[:, 0], pcs[:, 1], c=wine["quality"], cmap="viridis", alpha=0.5)
    # Biplot arrows: scale factor chosen so longest arrow ~ 50% of axis range
    arrow_scale = 3.0
    for i, feature in enumerate(numeric_for_pca.columns):
        plt.arrow(0, 0,
                  pca.components_[0, i] * arrow_scale,
                  pca.components_[1, i] * arrow_scale,
                  color="r", alpha=0.7, head_width=0.1)
        plt.text(pca.components_[0, i] * (arrow_scale + 0.2),
                 pca.components_[1, i] * (arrow_scale + 0.2),
                 feature, color="r", fontsize=8)
    plt.xlabel(f"PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)")
    plt.ylabel(f"PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)")
    plt.title("PCA Biplot")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{OUTDIR}/pca_biplot.png", dpi=150)
    maybe_show()

    # 11. Linear regression: Predicting quality (as numeric)
    # Fix dummy trap: drop_first=True avoids singular matrix with const
    wine["quality_num"] = wine["quality"]
    type_dummies = pd.get_dummies(wine["type"], prefix="type", drop_first=True, dtype=float)
    X = pd.concat([wine[["alcohol", "sulphates", "pH"]], type_dummies], axis=1)
    X = sm.add_constant(X, has_constant="add")
    y = wine["quality_num"]

    model = sm.OLS(y, X).fit()
    print("\n=== Regression Summary ===\n")
    print(model.summary())

    # Residuals vs Fitted
    plt.figure(figsize=(6, 4))
    plt.scatter(model.fittedvalues, model.resid, alpha=0.5)
    plt.axhline(0, color="red", linestyle="--")
    plt.xlabel("Fitted Values")
    plt.ylabel("Residuals")
    plt.title("Residuals vs Fitted")
    plt.tight_layout()
    plt.savefig(f"{OUTDIR}/residuals_vs_fitted.png", dpi=150)
    maybe_show()

    # 12. Fitted vs Actual
    plt.figure(figsize=(6, 4))
    plt.scatter(model.fittedvalues, wine["quality_num"], alpha=0.5)
    plt.plot([wine["quality_num"].min(), wine["quality_num"].max()],
             [wine["quality_num"].min(), wine["quality_num"].max()],
             "k--", lw=2)
    plt.xlabel("Fitted Quality")
    plt.ylabel("Actual Quality")
    plt.title("Fitted vs Actual Quality")
    plt.tight_layout()
    plt.savefig(f"{OUTDIR}/fitted_vs_actual.png", dpi=150)
    maybe_show()

    print(f"\nAll figures saved to ./{OUTDIR}/")


# 13. Entry point
if __name__ == "__main__":
    main()
