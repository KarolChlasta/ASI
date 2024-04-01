"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import split_data, load_data

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=load_data,
            inputs=None,
            outputs="raw_data",
            name="load_csv_file"
        ),
        node(
            func=split_data,
            inputs="raw_data",
            outputs=["train_data", "test_data"],
            name="split_data_node"
            )        
    ])
