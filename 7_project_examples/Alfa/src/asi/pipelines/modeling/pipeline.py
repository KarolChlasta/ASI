"""
This is a boilerplate pipeline 'modeling'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import train_model, evaluate_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
         node(
            func=train_model,
            inputs=["train_data", "params:autogluon.hyperparameters"],
            outputs="MLPredictor",
            name="train_model"
        ),
        node(
            func=evaluate_model,
            inputs=["MLPredictor", "test_data"],
            outputs=None,
            name="evaluate_model"
        ),
    ])
