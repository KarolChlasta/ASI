"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import prepare_data, split_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=prepare_data,
            inputs="all_data",
            outputs="all_data_prepared",
            name="prepare_data"
        ),
         node(
            func=split_data,
            inputs="all_data_prepared",
            outputs=["train_data", "test_data"],
            name="split_data"
        ),
    ])
