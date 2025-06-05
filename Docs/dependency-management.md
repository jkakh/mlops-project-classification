# Dependency Management with `uv` and `pyproject.toml`

This guide explains how to manage Python project dependencies using [`uv`](https://github.com/astral-sh/uv) and `pyproject.toml`.

## 1. Install `uv`

```bash
pip install uv
```

Or, for a global installation:

```bash
pipx install uv
```

## 2. Initialize `pyproject.toml`

If your project doesn't have a `pyproject.toml`, create one:

```bash
uv init
```

Or manually create a minimal file:

```toml
[project]
name = "your-project-name"
version = "0.1.0"
dependencies = []
```

## 3. Add Dependencies

To add a dependency (e.g., `requests`):

```bash
uv add requests
```

This updates `pyproject.toml` and creates/updates `uv.lock`.

## 4. Install All Dependencies

To install all dependencies listed in `pyproject.toml`:

```bash
uv install
```

## 5. Update Dependencies

To update all dependencies to their latest compatible versions:

```bash
uv update
```

Or update a specific package:

```bash
uv update requests
```

## 6. Remove a Dependency

To remove a package:

```bash
uv remove requests
```

## 7. Reproducible Installs

Use the lock file for reproducible environments:

```bash
uv sync
```

## 8. Best Practices

- Commit both `pyproject.toml` and `uv.lock` to version control.
- Use virtual environments for isolation.
- Regularly update dependencies and lock file.

## References

- [uv documentation](https://github.com/astral-sh/uv)
- [PEP 621: pyproject.toml](https://peps.python.org/pep-0621/)