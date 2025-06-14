import pytest
from src.train import train_model
import pandas as pd

def test_train_model_runs(monkeypatch, tmp_path):
    # Patch config loading to use a minimal config
    dummy_config = {
        "target": "target",
        "rf_hp": {
            "n_estimators": 1,
            "max_depth": 2,
            "random_state": 42
        },
        "MODEL_NAME": "dummy_model"
    }
    monkeypatch.setattr("src.train.config", dummy_config)

    # Patch setup_mlflow and mlflow functions to avoid side effects
    monkeypatch.setattr("src.train.setup_mlflow", lambda: None)
    monkeypatch.setattr("src.train.mlflow", type("DummyMLflow", (), {
        "start_run": lambda *a, **k: None,
        "log_params": lambda *a, **k: None,
        "log_param": lambda *a, **k: None,
        "log_metrics": lambda *a, **k: None,
        "sklearn": type("DummySklearn", (), {
            "log_model": lambda *a, **k: None
        })()
    })())

    # Patch logger to avoid output
    monkeypatch.setattr("src.train.logger", type("DummyLogger", (), {
        "info": lambda *a, **k: None
    })())

    # Patch infer_signature
    monkeypatch.setattr("src.train.infer_signature", lambda x, y: None)

    # Create dummy train and test data
    train_df = pd.DataFrame({"a": [1, 2], "target": [0, 1]})
    test_df = pd.DataFrame({"a": [3, 4], "target": [1, 0]})
    train_df.to_csv("data/train.csv", index=False)
    test_df.to_csv("data/test.csv", index=False)

    # Run the function (should not raise)
    train_model()