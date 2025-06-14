import pytest
from src.data_prep import prepare_data
import pandas as pd

def test_prepare_data_runs_without_exception(tmp_path, monkeypatch):
    # Minimal config mock
    config = {
        "data": {
            "data_dir": str(tmp_path),
            "test_size": 0.2,
            "random_state": 42
        }
    }

    # Create a dummy CSV file
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5], "b": [5, 4, 3, 2, 1]})
    df.to_csv(tmp_path / "winequality-red.csv", index=False)

    # # Patch MLflow and logger to avoid side effects
    # monkeypatch.setattr("src.data_prep.setup_mlflow", lambda: None)
    # monkeypatch.setattr("src.data_prep.get_or_create_run", lambda x: type("DummyRun", (), {"__enter__": lambda s: s, "__exit__": lambda s, exc_type, exc_val, exc_tb: None, "info": type("Info", (), {"run_id": "dummy"})()})())
    # monkeypatch.setattr("src.data_prep.mlflow", type("DummyMLflow", (), {"log_params": lambda params: None})())
    # monkeypatch.setattr("src.data_prep.logger", type("DummyLogger", (), {"info": lambda *a, **k: None, "debug": lambda *a, **k: None, "error": lambda *a, **k: None})())

    # Run function (should not raise)
    prepare_data(config)

    # Check that train.csv and test.csv are created
    assert (tmp_path / "train.csv").exists()
    assert (tmp_path / "test.csv").exists()