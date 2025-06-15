"""Script for data preparation."""

import sys
from pathlib import Path

import pandas as pd
from loguru import logger
from sklearn import model_selection
import yaml
from utils import setup_mlflow, get_or_create_run
import mlflow

# Load configuration
with Path("config/config.yaml").open() as file:
    config = yaml.safe_load(file)


def prepare_data(config) -> None:
    """Prepare train and test raw red wine data.

    :param config_path: Path to configuration file.
    :param in_path: Path where raw data is read from.
    :param out_train: Path where prepared train data is stored.
    :param out_test: Path where prepared test data is stored.
    """

    # Setup MLflow
    setup_mlflow()

    with get_or_create_run("ml_pipeline_main") as main_run:
        try:
            logger.info("Cleaning data")

            data = pd.read_csv(config["data"]["data_dir"] + "/winequality-red.csv")
            logger.info(
                "Raw data read from {} file",
            )

            # Log preprocessing parameters and metrics
            preprocessing_params = {
                'test_size': config["data"]["test_size"],
                'random_state': config["data"]["random_state"],
            }
            mlflow.log_params(preprocessing_params)

            train, test = model_selection.train_test_split(
                data, test_size=preprocessing_params["test_size"], random_state=preprocessing_params["random_state"]
            )
            logger.debug("Train and test data split")

            train.to_csv(config["data"]["data_dir"] + "/train.csv")
            logger.info("Train data saved to {} file", config["data"]["data_dir"] + "/train.csv")

            test.to_csv(config["data"]["data_dir"] + "/test.csv")
            logger.info("Test data saved to {} file", config["data"]["data_dir"] + "/test.csv")



        except Exception as exc:
            logger.error("Unexpected error")
            logger.error(exc.with_traceback())
            sys.exit(1)
        
                # Store run ID for other scripts
        run_id = main_run.info.run_id
        with open('run_id.txt', 'w') as f:
            f.write(run_id)
        


if __name__ == "__main__":
    prepare_data(config=config)