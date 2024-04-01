"""
This is a boilerplate pipeline 'visualize'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import save_data_to_db


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(
            func=save_data_to_db,
            inputs=["params:num_rows", "params:table_name"],
            outputs=None,
            name="save_data_to_db_node"
        ),
    ])
