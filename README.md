# mlops-project-classification
Classification example mlops project

## Essential Software Installation
* Python Installation Download Python from python.org (get the latest stable version, currently 3.11 or 3.12). During installation, make sure to check "Add Python to PATH" - this is crucial for command line access.
* Git Installation
Download Git from git-scm.com. Use the default installation settings, but pay attention to the default editor selection (you can choose VS Code if you prefer).
* Visual Studio Code
Download VS Code from code.visualstudio.com. It's lightweight yet powerful, perfect for Python development and AI projects.
* Install VS Code Extensions**
    - Open VS Code and go to the Extensions view (`Ctrl+Shift+X`).
    - Search for and install the following extensions:
        - **Python** (by Microsoft) – Provides rich support for Python development.
        - **Jupyter** (by Microsoft) – Enables working with Jupyter Notebooks inside VS Code.

## Clone Git repository
### Prerequisite: Create a GitHub OAuth Classic Token

1. Go to [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens).
2. Click **Generate new token** > **Generate new token (classic)**.
3. Set a name, expiration, and select the `repo` scope.
4. Click **Generate token** and copy the token. Store it securely.

### Steps to Clone the Repository

1. Open a terminal or command prompt.
2. Navigate to the directory where you want to clone the project.
3. Run the following command:

    ```bash
    git clone https://github.com/jkakh/mlops-project-classification.git
    ```

4. When prompted for a username and password, use your GitHub username and paste the OAuth token as the password.

## Download Dataset and Prepare Data Folder

### Steps to Download `winequality-red.csv` from Kaggle

1. Create a free Kaggle account at [kaggle.com](https://www.kaggle.com/).
2. Go to the [Wine Quality Data Set page](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009).
3. Download the `winequality-red.csv` file to your local machine.

### Organize the Data Folder

1. In your project root, create a folder named `data` if it doesn't exist:
    ```bash
    mkdir -p data
    ```
2. Move the downloaded `winequality-red.csv` file into the `data` folder.

3. (Optional but recommended) Add a `.gitkeep` file to ensure the `data` folder is tracked by git, even if empty:
    ```bash
    touch data/.gitkeep
    ```
   > Note: Do **not** commit the actual dataset file (`winequality-red.csv`) to version control. Only commit the `.gitkeep` file.



## Steps to Create a Python Virtual Environment
Before creating a virtual environment, it's important to understand why it's needed:

A **virtual environment** allows you to create an isolated space for your project's Python dependencies. This ensures that packages required for this project do not interfere with packages from other projects or the global Python installation. Using `venv` helps maintain reproducibility and avoids version conflicts between dependencies.

1. Open a terminal in your project root directory.
2. Run the following command to create a virtual environment named `venv`:
    ```bash
    python3 -m venv venv
    ```
3. Activate the virtual environment:
    - **On Windows:**
        ```bash
        venv\Scripts\activate
        ```
    - **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
4. Your terminal prompt should now show `(venv)` indicating the environment is active.
5. To deactivate the environment, simply run:
    ```bash
    deactivate
    ```