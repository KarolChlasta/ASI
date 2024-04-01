"""Project pipelines."""
from __future__ import annotations
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline

from asi_kedro.pipelines import (
    data_engineering as de,
    data_science as ds,
    model_evaluation as me
)

def register_pipelines() -> Dict[str, Pipeline]:
    data_engineering_pipeline = de.create_pipeline()
    data_science_pipeline = ds.create_pipeline()
    model_evaluation_pipeline = me.create_pipeline()

    return {
        "de": data_engineering_pipeline,
        "ds": data_science_pipeline,
        "me": model_evaluation_pipeline,
        "__default__": data_engineering_pipeline + data_science_pipeline + model_evaluation_pipeline
    }
