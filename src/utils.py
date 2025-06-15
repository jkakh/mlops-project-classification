import mlflow
import mlflow.sklearn
import pickle
import json
from datetime import datetime
from pathlib import Path
import yaml


# Load configuration
with Path("config/config.yaml").open() as file:
    config = yaml.safe_load(file)

def setup_mlflow():
    """Initialize MLflow tracking"""
    mlflow.set_tracking_uri(config["MLFLOW_TRACKING_URI"])
    mlflow.set_experiment(config["EXPERIMENT_NAME"])

def get_or_create_run(run_name=None):
    """Get existing run or create new one"""
    if run_name is None:
        run_name = f"pipeline_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    # Check if there's an active run
    active_run = mlflow.active_run()
    if active_run is None:
        run = mlflow.start_run(run_name=run_name)
        return run
    return active_run

def log_pipeline_stage(stage_name, parameters=None, metrics=None, artifacts=None):
    """Log information for a specific pipeline stage"""
    with mlflow.start_run(nested=True, run_name=f"{stage_name}_stage"):
        if parameters:
            mlflow.log_params(parameters)
        if metrics:
            mlflow.log_metrics(metrics)
        if artifacts:
            for artifact_path, artifact_data in artifacts.items():
                mlflow.log_dict(artifact_data, artifact_path)