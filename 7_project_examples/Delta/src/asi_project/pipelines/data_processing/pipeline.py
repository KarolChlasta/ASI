"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import preprocess_data,load_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
          node(
                func=load_data,
                inputs=None,
                outputs="bank_raw",
                name="load_dataset",
            ),
         node(
                func=preprocess_data,
                inputs=["bank_raw"],
                outputs=["preprocessed_oversampled_bank","preprocessed_undersampled_bank", "data_encoder","syndata"],
                name="bank_processed_node",
            )

    ])
