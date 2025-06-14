import pytest
import pandas as pd
from src.inference import generate_predictions

class DummyModel:
    def predict(self, X):
        # Return a constant value for each row
        return [42] * len(X)

def test_generate_predictions_simple():
    model = DummyModel()
    test_data = pd.DataFrame({"a": [1, 2, 3]})
    preds = generate_predictions(model, test_data)
    assert all(preds == 42)
    assert len(preds) == 3