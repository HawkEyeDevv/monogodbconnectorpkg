import os.path
from pathlib import Path

list_of_files = [
    ".github/workflows/ci.yml",
    ".github/workflows/python-publish.yaml",
    "src/__init__.py",
    "src/mongodb-connect.py",
    "experiment/__init__.py",
    "experiment/experiments.ipynb",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/unit/test_unit.py",
    "tests/integration/__init__.py",
    "tests/integration/test_int.py",
    "requirements.txt",
    "requirements_dev.txt",
    "tox.ini",
    "pyproject.toml",
    "setup.cfg",
    "setup.py",
]

for file_path in list_of_files:
    file_path = Path(file_path)
    dir_name, file_name = os.path.split(file_path)
    if dir_name != "":
        os.makedirs(dir_name, exist_ok=True)

    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        with open(file_path, "w") as f:
            pass