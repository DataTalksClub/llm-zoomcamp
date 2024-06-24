# Local Setup (Win10)

1. Environment

    ```bash
    pyenv global 3.11.9
    python -m venv venv  # removed via: sudo rm -rf venv
    .\venv\Scripts\Activate # alias venv
    pip install -U pip wheel setuptools
    pip install -r requirements.txt
    ```

2. pre-commit

    ```bash
    pip install pre-commit
    pre-commit install
    pre-commit autoupdate
    # pre-commit run # test
    ```

3. Extras
   - Docker
    - https://community.chocolatey.org/packages/docker-desktop#individual
    - test: `docker version`

# Homework

## Module 1: Introduction to LLMs and RAG

- [Homework](cohorts\2024\01-intro\homework.md)

-
