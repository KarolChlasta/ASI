"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 0.18.14
"""
from kedro.pipeline import Pipeline, pipeline, node
from .nodes import evaluate_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=evaluate_model,
            inputs="predictions",
            outputs=None,
            name="autogluon_evaluation"
        )
    ])
