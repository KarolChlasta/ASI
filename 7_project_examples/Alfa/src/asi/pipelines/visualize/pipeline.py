"""
This is a boilerplate pipeline 'visualize'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import initWandb


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=initWandb,
            inputs=["MLPredictor", "test_data", "train_data"],
            outputs=["model"],
            name="initWandb"
        )
    ])
