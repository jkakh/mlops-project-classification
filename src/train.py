"""Implements the training pipeline for regression models.

It loads data, fits random forest classification model and saves the model.
"""

from pathlib import Path

import joblib
import pandas as pd
import yaml
from loguru import logger
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from utils import setup_mlflow
import mlflow
from mlflow.models.signature import infer_signature

# Load configuration
with Path("config/config.yaml").open() as file:
    config = yaml.safe_load(file)

def train_model() -> None:
    """Trains regression models using grid search for hyperparameter tuning, evaluates the best
    model on the test set, and saves the best model."""

    # Setup MLflow
    setup_mlflow()
    # Try to read run_id from file
    try:
        with open('run_id.txt', 'r') as f:
            run_id = f.read().strip()
        mlflow.start_run(run_id=run_id)
    except:
        mlflow.start_run()

    # Load data
    train_data = pd.read_csv("data/train.csv")
    test_data = pd.read_csv("data/test.csv")
    logger.info("Reading train and test is completed")

    # Separate features and target
    x_train = train_data.drop(
        config["target"], axis=1
    )  # Replace 'target' with your target column name
    y_train = train_data[config["target"]]
    x_test = test_data.drop(config["target"], axis=1)
    y_test = test_data[config["target"]]
    logger.info("Data prep is completed")

            
    # Model parameters
    model_params = {
        'n_estimators': config["rf_hp"]["n_estimators"],
        'max_depth': config["rf_hp"]["max_depth"],
        'random_state': config["rf_hp"]["random_state"],
    }
    # Log training parameters
    mlflow.log_params({
        f'model_{k}': v for k, v in model_params.items()
    })
    mlflow.log_param('model_type', 'RandomForestClassifier')
    
    # Initialize the RandomForestClassifier
    rf_clf = RandomForestClassifier(**model_params)

    # Fit the model on the training data
    model = rf_clf.fit(x_train, y_train)    
    
    # Make predictions
    y_pred_train = model.predict(x_train)
    y_pred_test = model.predict(x_test)
    
    # Calculate metrics
    train_accuracy = accuracy_score(y_train, y_pred_train)
    test_accuracy = accuracy_score(y_test, y_pred_test)
    test_precision = precision_score(y_test, y_pred_test, average='weighted')
    test_recall = recall_score(y_test, y_pred_test, average='weighted')
    test_f1 = f1_score(y_test, y_pred_test, average='weighted')

    training_metrics = {
        'train_accuracy': train_accuracy,
        'test_accuracy': test_accuracy,
        'test_precision': test_precision,
        'test_recall': test_recall,
        'test_f1': test_f1
    }
    mlflow.log_metrics(training_metrics)

    # Prepare input example and model signature for MLflow
    input_example = x_train.head(3)
    signature = infer_signature(x_train, model.predict(x_train))

    mlflow.sklearn.log_model(
        model,
        "model",
        registered_model_name=config["MODEL_NAME"],
        input_example=input_example,
        signature=signature
    )

if __name__ == "__main__":
    train_model()
