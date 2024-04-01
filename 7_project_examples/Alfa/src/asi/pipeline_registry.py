"""Project pipelines."""
from __future__ import annotations

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from asi.pipelines.generate_data.pipeline import create_pipeline as generate_data_pipeline



def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines()
    pipelines["generate_data"] = generate_data_pipeline()  # Manually adding your pipeline
    pipelines["__default__"] = sum(pipelines.values())
    return pipelines
