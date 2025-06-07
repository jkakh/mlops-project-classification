import os
import joblib
import pandas as pd
from loguru import logger
import mlflow
from utils import setup_mlflow

def load_model(model_path):
    """
    Load a machine learning model from the specified path.

    Parameters:
    model_path (str): Path to the model file.

    Returns:
    model: Loaded machine learning model.
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")
    model = joblib.load(model_path)
    return model


def generate_predictions(model, test_data):
    """
    Generate predictions using the loaded model on the test data.

    Parameters:
    model: Loaded machine learning model.
    test_data (pd.DataFrame): Test data for predictions.

    Returns:
    pd.Series: Predictions for the test data.
    """
    predictions = model.predict(test_data)
    return pd.Series(predictions)


if __name__ == "__main__":

    # Setup MLflow
    setup_mlflow()

    # Try to read run_id from file
    try:
        with open('run_id.txt', 'r') as f:
            run_id = f.read().strip()
        mlflow.start_run(run_id=run_id)
    except:
        mlflow.start_run()

    model_uri = f"runs:/{run_id}/model"
    model = mlflow.sklearn.load_model(model_uri)

    logger.info("Model loaded successfully")
    data_to_predict = pd.read_csv("data/test.csv")
    logger.info("Loaded test data")
    x_test = data_to_predict.drop("quality", axis=1)
    predictions = generate_predictions(model, x_test)
    logger.info("Predictions are loaded")