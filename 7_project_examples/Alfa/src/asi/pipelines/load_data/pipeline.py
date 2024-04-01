"""
This is a boilerplate pipeline 'load_data'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import load_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        # node(
        #     func=load_data,
        #     inputs="weatherAUS",
        #     outputs="all_data",
        #     name="load_data"
        # )
         node(
            func=load_data,
            inputs=None,
            outputs="all_data",
            name="load_data"
        )
    ])
