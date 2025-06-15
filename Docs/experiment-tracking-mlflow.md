# Experiment Tracking with MLflow

## Introduction

[MLflow](https://mlflow.org/) is an open-source platform for managing the end-to-end machine learning lifecycle. It helps track experiments, log parameters, metrics, and artifacts, and organize results for reproducibility. Key concepts:

- **Experiment ID**: Uniquely identifies a group of related runs.
- **Run ID**: Uniquely identifies a single execution of your code.
- **Artifacts**: Files (models, plots, etc.) saved during a run.

## Starting the MLflow Tracking Server

To start the MLflow tracking server locally (using the default file-based backend), run:

```bash
mlflow server --default-artifact-root ./mlruns
```

- `--default-artifact-root`: Directory where artifacts are stored.

Access the MLflow UI at [http://localhost:5000](http://localhost:5000).

## Step-by-Step Guide to Add MLflow Tracking

### 1. Install MLflow

Install MLflow using [uv](https://github.com/astral-sh/uv):

```bash
uv add mlflow
```

### 2. Import MLflow in Your Script

```python
import mlflow
```

### 3. Set Experiment

```python
mlflow.set_experiment("my_experiment")
```

### 4. Start a Run

```python
with mlflow.start_run() as run:
    print("Run ID:", run.info.run_id)
    print("Experiment ID:", run.info.experiment_id)
```

### 5. Log Parameters, Metrics, and Artifacts

```python
with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_metric("accuracy", 0.95)
    mlflow.log_artifact("output/model.pkl")
```

### 6. View Results

Open [http://localhost:5000](http://localhost:5000) to view experiments, runs, parameters, metrics, and artifacts.

## Example Script (`src/train.py`)

```python
import mlflow

mlflow.set_experiment("my_experiment")

with mlflow.start_run() as run:
    mlflow.log_param("param1", 5)
    mlflow.log_metric("score", 0.89)
    with open("output.txt", "w") as f:
        f.write("Sample output")
    mlflow.log_artifact("output.txt")
    print("Run ID:", run.info.run_id)
    print("Experiment ID:", run.info.experiment_id)
```

## Summary

- Start MLflow server.
- Use `mlflow.set_experiment()` and `mlflow.start_run()`.
- Log parameters, metrics, and artifacts.
- View and compare runs in the MLflow UI.

