"""Placeholder tests for data schema — replace with real assertions."""
import pathlib

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]

def test_raw_samples_exist():
    """Sample CSVs should exist to illustrate schema."""
    assert (PROJECT_ROOT / "data" / "raw" / "winequality-red-sample.csv").exists()
    assert (PROJECT_ROOT / "data" / "raw" / "winequality-white-sample.csv").exists()

def test_sample_headers():
    """Sample files should have 12 columns semicolon-delimited."""
    sample = PROJECT_ROOT / "data" / "raw" / "winequality-red-sample.csv"
    header = sample.read_text().splitlines()[0]
    assert header.count(";") == 11
    assert "alcohol" in header and "quality" in header

# TODO: add test_full_data_download (mocked), test_no_null_quality, etc.
