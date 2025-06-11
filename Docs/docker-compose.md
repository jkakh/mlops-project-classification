
This document provides a step-by-step guide for containerizing and orchestrating a machine learning workflow using Docker and Docker Compose. It covers:

**Dockerfile**: Packages your code and dependencies into an image.

**mlflow service**: Runs the MLflow tracking server for experiment tracking.

**data_prep, train, inference services**: Each runs a specific workflow step as a container, depending on the previous step and MLflow.

1. **Creating a Dockerfile**:  
    - Explains how to build a custom Docker image for your ML project.
        - The Dockerfile uses an official Ubuntu base image, installs Python on top of it, and sets up a working directory.
        - Project dependencies are managed using `pyproject.toml` and installed with [uv](https://github.com/astral-sh/uv), a fast Python package manager.
        - The Dockerfile copies your project files, installs dependencies with `uv sync` (or directly from `pyproject.toml`), and specifies a default command to run your main script.

2. **Creating a Docker Compose File**:  
    - Shows how to define and manage multiple services required for the ML workflow.
    - The `docker-compose.yml` file includes:
      - An `mlflow` service to run the MLflow tracking server in a container, exposing the UI on port 5000 and persisting artifacts.
      - Separate services for `data_prep`, `train`, and `inference`, each running a specific script as a workflow step.
      - Service dependencies are defined to ensure correct execution order (e.g., `train` waits for `data_prep` and `mlflow`).

3. **Workflow Execution**:  
    - Instructions for building and starting all services with `docker-compose up --build`.
    - Describes how the workflow is orchestrated: MLflow server starts first, followed by data preparation, training, and inference steps in sequence.
    - Guidance on accessing the MLflow UI and viewing logs.

4. **Running the Workflow**:

    1. **Build and start all services:**
     ```sh
     docker-compose up --build
     ```
     This will:
     - Start MLflow server.
     - Run data preparation.
     - Train the model.
     - Run inference.

    2. **Access MLflow UI:**
     - Open [http://localhost:5000](http://localhost:5000) in your browser.

    3. **Logs and Results:**
     - Check logs in the terminal or use `docker-compose logs <service>`.

5. **Customizing**

- Edit `command` in each service to match your script locations.
- Add volumes if you want to persist data or models.
