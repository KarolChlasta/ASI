"""
This is a boilerplate pipeline 'train_test_split'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import split_train_test, choose_training_dataset

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
         node(
                func=choose_training_dataset,
                inputs=["preprocessed_undersampled_bank","preprocessed_oversampled_bank","preprocessed_oversampled_bank2","preprocessed_undersampled_bank2","params:dataset_choice"],
                outputs='data',
                name="choose_dataset",
            ),

         node(
                func=split_train_test,
                inputs=["data","params:dataset_choice"],
                outputs=['train_dataset', 'test_dataset'],
                name="split_data_node",
            )

    ])
