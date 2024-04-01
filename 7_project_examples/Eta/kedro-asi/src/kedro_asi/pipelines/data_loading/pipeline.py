from kedro.pipeline import Pipeline, node, pipeline

from .nodes import load_data_from_postgresql


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=load_data_from_postgresql,
                inputs=None,
                outputs="universities",
                name="load_data_from_postgresql"
            )
        ]
    )
