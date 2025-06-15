"""Implements the training pipeline for regression models.

It loads data, fits random forest classification model and saves the model.
"""

from pathlib import Path

import joblib
import pandas as pd
import yaml
from loguru import logger
from sklearn.ensemble import RandomForestClassifier

# Load configuration
with Path("config/config.yaml").open() as file:
    config = yaml.safe_load(file)

def train_model() -> None:
    """Trains regression models using grid search for hyperparameter tuning, evaluates the best
    model on the test set, and saves the best model."""
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

    # Initialize the RandomForestClassifier
    rf_clf = RandomForestClassifier(random_state=42)

    # Fit the model on the training data
    model = rf_clf.fit(x_train, y_train)    
    
    # save model 
    joblib.dump(model, "models/model.joblib")
    logger.info("model saved")

if __name__ == "__main__":
    train_model()
