"""
This is a boilerplate pipeline 'synthetic_data_creation'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import create_synth_data

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=create_synth_data,
            inputs="raw_data",
            outputs=["synth_data", "concat_data"],
            name="synth_data_node"
            )
    ])
