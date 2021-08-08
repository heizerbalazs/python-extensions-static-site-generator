import sys
import importlib

from pathlib import Path


def load_module(directory: str, name: str):
    sys.path.insert(0, directory)
