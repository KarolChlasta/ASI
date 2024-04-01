from typing import Dict
from kedro.pipeline import Pipeline
from .pipelines.data_pipeline import create_pipeline

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipeline.
    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    return {
        "data_pipeline": create_pipeline(),
        "__default__": create_pipeline(),
    }