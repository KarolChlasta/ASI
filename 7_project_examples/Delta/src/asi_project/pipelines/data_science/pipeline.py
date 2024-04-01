"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import train_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
         node(
                func=train_model,
                inputs=['train_dataset',"params:model_options"],
                outputs="classifier",
                name="train_model_node",
            )


    ])
