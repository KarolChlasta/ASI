"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import synthetic,preprocess_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
         node(
                func=preprocess_data,
                inputs=["syndata","params:info"],
                outputs=["preprocessed_oversampled_bank2","preprocessed_undersampled_bank2", "data_encoder2", "syntheticdataset"],
                name="synned_node",
            )

    ])
