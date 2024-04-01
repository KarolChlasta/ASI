import os
import pandas as pd
from pathlib import Path
from kedro.framework.startup import bootstrap_project
from kedro.framework.session import KedroSession
from enum import Enum
from fastapi import FastAPI, Request, Header, HTTPException, Body
from fastapi.responses import RedirectResponse
from typing import Iterable, Tuple, Optional
from itertools import chain

project_path = Path.cwd()
metadata = bootstrap_project(project_path)
session = KedroSession.create(metadata.package_name, project_path)
context = session.load_context()

app = FastAPI(
    title="FastAPI",
    version="0.1.0",
    description="""
        
    """,
    openapi_tags=[]
)

@app.get('/')
async def docs_redirect():
    return RedirectResponse(url='/docs')

MLPredictor = context.catalog.load("MLPredictor")

@app.get("/my_model", tags=['weather'])
def predict_my_model(
    Location:str, 
    MinTemp:float, 
    MaxTemp:float, 
    Rainfall:float, 
    Evaporation:float, 
    Sunshine:float, 
    WindGustDir:str, 
    WindGustSpeed:float, 
    WindDir9am:str, 
    WindDir3pm:str, 
    WindSpeed9am:float, 
    WindSpeed3pm:float, 
    Humidity9am:float, 
    Humidity3pm:float, 
    Pressure9am:float, 
    Pressure3pm:float, 
    Cloud9am:float, 
    Cloud3pm:float, 
    Temp9am:float, 
    Temp3pm:float, 
    RainToday:str
    ):
    args={
    "Location": Location,
    "MinTemp": MinTemp,
    "MaxTemp": MaxTemp,
    "Rainfall": Rainfall,
    "Evaporation": Evaporation,
    "Sunshine": Sunshine,
    "WindGustDir": WindGustDir,
    "WindGustSpeed": WindGustSpeed,
    "WindDir9am": WindDir9am,
    "WindDir3pm": WindDir3pm,
    "WindSpeed9am": WindSpeed9am,
    "WindSpeed3pm": WindSpeed3pm,
    "Humidity9am": Humidity9am,
    "Humidity3pm": Humidity3pm,
    "Pressure9am": Pressure9am,
    "Pressure3pm": Pressure3pm,
    "Cloud9am": Cloud9am,
    "Cloud3pm": Cloud3pm,
    "Temp9am": Temp9am,
    "Temp3pm": Temp3pm,
    "RainToday": RainToday,
    }
    df = pd.DataFrame({k: [v] for k, v in args.items()})
    result = MLPredictor.predict(df)
    
    if result.get('error'):
        raise HTTPException(
            status_code=int(result.get('error').get('status_code')), 
            detail=result.get('error').get('detail')
        )

    return result
def _get_values_as_tuple(values: Iterable[str]) -> Tuple[str, ...]:
    return tuple(chain.from_iterable(value.split(",") for value in values))


@app.post("/kedro")
def kedro(
    request: dict = Body(..., example={
        "pipeline_name": "",
        "tag": [],
        "node_names": [],
        "from_nodes": [],
        "to_nodes": [],
        "from_inputs": [],
        "to_outputs": [],
        "params": {}
    })
):
    pipeline_name = request.get("pipeline_name")
    tag = request.get("tag")
    node_names = request.get("node_names")
    from_nodes = request.get("from_nodes")
    to_nodes = request.get("to_nodes")
    from_inputs = request.get("from_inputs")
    to_outputs = request.get("to_outputs")
    params = request.get("params")

    tag = _get_values_as_tuple(tag) if tag else tag
    node_names = _get_values_as_tuple(node_names) if node_names else node_names
    package_name = str(Path(__file__).resolve().parent.name)
    try:
        with KedroSession.create(package_name, env=None, extra_params=params) as session:
            return session.run(
                    tags=tag,
                    node_names=node_names,
                    from_nodes=from_nodes,
                    to_nodes=to_nodes,
                    from_inputs=from_inputs,
                    to_outputs=to_outputs,
                    pipeline_name=pipeline_name,
                )
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@app.get("/catalog")
def catalog(
    name: str
):
    try:
        file = context.catalog.load(name)
        return file.to_json(force_ascii=False)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))