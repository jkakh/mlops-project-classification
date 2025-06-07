# Step-by-Step Guide: Refactoring a Data Science Notebook into Python Scripts (with Script-Level Main Functions)

## 1. Review and Understand the Notebook
- Read through the notebook.
- Identify sections for data loading, preprocessing, modeling, evaluation, and visualization.

## 2. Create a Project Structure
```
project/
│
├── src/
│   ├── data.py
│   ├── features.py
│   ├── model.py
│   └── evaluate.py
├── config/
│   └── config.yaml
├── requirements.txt
└── README.md
```

## 3. Move Code into Functions
- For each logical block, create a function in the appropriate script.
- Example:
    ```python
    # src/data.py
    import pandas as pd

    def load_data(path: str) -> pd.DataFrame:
        """Load dataset from a CSV file."""
        return pd.read_csv(path)
    ```

## 4. Add Type Hints and Docstrings
- Use type hints for all function arguments and return types.
- Add docstrings describing each function’s purpose, parameters, and return values.

## 5. Parameterize with Config Files
- Store parameters (file paths, hyperparameters) in a YAML or JSON config file.
- Example `config/config.yaml`:
    ```yaml
    data_path: "data/train.csv"
    model:
      n_estimators: 100
      max_depth: 5
    ```
- Load config in your scripts:
    ```python
    import yaml

    def load_config(config_path: str) -> dict:
        """Load configuration from a YAML file."""
        with open(config_path) as f:
            return yaml.safe_load(f)
    ```

## 6. Add a Main Function in Each Script
- In each script (e.g., `data.py`, `features.py`), add a `main()` function to demonstrate or test the script’s functionality.
- Example:
    ```python
    def main():
        config = load_config("../config/config.yaml")
        df = load_data(config["data_path"])
        print(df.head())

    if __name__ == "__main__":
        main()
    ```

## 7. Test Each Function
- Add simple tests or assertions within the `main()` function or as separate test scripts.

## 8. Remove Notebook-Specific Code
- Remove inline plotting, magic commands, and cell-specific code.

## 9. Document the Refactored Code
- Ensure all functions have clear docstrings.
- Add a README explaining how to run each script.

## 10. Version Control
- Use Git to track changes and collaborate.

---

**Tip:** Refactor incrementally, testing each script’s `main()` function to ensure correctness.