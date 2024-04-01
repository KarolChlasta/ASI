from kedro.pipeline import Pipeline, node, pipeline

from .nodes import evaluate_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=evaluate_model,
                inputs="universities",
                outputs=None,
                name="evaluate_model"
            )
        ]
    )
