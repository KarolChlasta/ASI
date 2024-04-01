"""
This is a boilerplate pipeline 'automl'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import automlflow



def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([

         node(
                func=automlflow,
                inputs=["train_dataset", "params:dataset_choice"],
                outputs="classifier",
                name="automl_node",
            )

    ])
