"""Project pipelines."""
from __future__ import annotations

from kedro.framework.project import find_pipelines

from kedro.pipeline import Pipeline

from asi_project.pipelines import (
    data_processing as dp,
    data_science as ds,
    automl as at,
    train_test_split as spl,
    eval as ev,
    synthetic_processing as sp
)




def register_pipelines() -> dict[str, Pipeline]:
    data_processing_pipeline = dp.create_pipeline()
    data_science_pipeline = ds.create_pipeline()
    automl_pipeline = at.create_pipeline()
    train_test_split_pipeline = spl.create_pipeline()
    eval_pipeline = ev.create_pipeline()
    synthetic_pipeline = sp.create_pipeline()
    return {
        "dp": data_processing_pipeline,
        "ds": data_science_pipeline,
        "__default__": data_processing_pipeline + train_test_split_pipeline +data_science_pipeline + eval_pipeline,
        "syn": data_processing_pipeline + synthetic_pipeline + train_test_split_pipeline +data_science_pipeline + eval_pipeline

    }
