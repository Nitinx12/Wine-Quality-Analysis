"""
example_usage.py — Placeholder for programmatic usage examples.

Run:
  uv run python examples/example_usage.py
"""
from pathlib import Path
import sys
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

try:
    from utils.helpers import load_wine_sample
    df = load_wine_sample()
    print("Sample shape:", df.shape)
    print(df.head())
except Exception as e:
    print(f"Placeholder demo — helpers not fully wired: {e}")

# TODO: Add full pipeline example:
# - fetch data via pandas read_csv
# - StandardScaler + PCA
# - OLS regression + print summary
print("\nTODO: Expand with end-to-end example once helpers are filled.")
