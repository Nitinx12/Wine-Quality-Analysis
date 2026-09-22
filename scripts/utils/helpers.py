"""
helpers.py — Placeholder for shared Python utilities.

TODO: Fill with reusable functions as project grows.
Example stubs below — replace with real implementations.
"""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_RAW = PROJECT_ROOT / "data" / "raw"
FIGURES_DIR = PROJECT_ROOT / "figures"

def load_wine_sample() -> pd.DataFrame:
    """Placeholder: load sample CSV from data/raw/."""
    sample = DATA_RAW / "winequality-red-sample.csv"
    if sample.exists():
        return pd.read_csv(sample, sep=";")
    # fallback: return empty with expected columns
    cols = ["fixed acidity","volatile acidity","citric acid","residual sugar",
            "chlorides","free sulfur dioxide","total sulfur dioxide",
            "density","pH","sulphates","alcohol","quality"]
    return pd.DataFrame(columns=cols)

def save_figure(fig, name: str):
    """Placeholder: save matplotlib figure to figures/."""
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURES_DIR / name, dpi=150)

# TODO: add metrics, plotting helpers, etc.
