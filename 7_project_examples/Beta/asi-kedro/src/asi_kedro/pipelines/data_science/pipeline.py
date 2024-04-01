"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import train_model, test_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=train_model,
            inputs="train_data",
            outputs="predictor",
            name="predictor_creation"
            ),
        node(
            func=test_model,
            inputs=["predictor", "test_data"],
            outputs="predictions",
            name="predictions_creation"
        )
    ])
