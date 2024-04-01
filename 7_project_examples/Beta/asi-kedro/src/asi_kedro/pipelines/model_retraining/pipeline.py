"""
This is a boilerplate pipeline 'model_retraining'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node
from asi_kedro.pipelines.data_engineering import split_data
from asi_kedro.pipelines.data_science import test_model, train_model

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=split_data,
            inputs="concat_data",
            outputs=["train_data", "test_data"],
            name="split_data_node"
            ),
        node(
            func=train_model,
            inputs="train_data",
            outputs="retrained_predictor",
            name="retrain_model_node"
            ),
        node(
            func=test_model,
            inputs=["retrained_predictor", "test_data"],
            outputs="predictions",
            name="predictions_creation"
        )   
    ])
