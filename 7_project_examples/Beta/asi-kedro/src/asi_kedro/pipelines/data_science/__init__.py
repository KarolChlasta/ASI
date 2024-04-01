"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.14
"""

from .pipeline import create_pipeline
from .nodes import test_model, train_model

__all__ = ["create_pipeline"]

__version__ = "0.1"
