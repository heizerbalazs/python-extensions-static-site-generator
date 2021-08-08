import sys
import importlib

from pathlib import Path


def load_module(directory: str, name: str) -> None:
    sys.path.insert(0, directory)
    importlib.import_module(name)
    sys.path.pop(0)


def load_directory(directory: Path) -> None:
    for path in directory.rglob("*.py"):
        load_module(directory.as_posix(), path.stem)
