from kedro.pipeline import Pipeline, node
from .loading import loadData
from .training import autogluonTraining

load_node = node(
    loadData,
    inputs=[],
    outputs="data",
    name="load_node"
)


train_node = node(
    autogluonTraining,
    inputs="data",
    outputs="predictor_output",
    name="train_node"
)

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            load_node,
            train_node
        ]
    )