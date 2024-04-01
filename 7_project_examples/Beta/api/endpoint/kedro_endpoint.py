from typing import List, Optional

from pydantic import BaseModel

from api.model.DataSetModel import KedroDataSet
from api.services import kedro
from fastapi import APIRouter, HTTPException
import subprocess

router = APIRouter()


@router.get("/raw_data", response_model=List[KedroDataSet])
async def get_raw_data():
    return kedro.get_raw_data()

@router.get("/test_data", response_model=List[KedroDataSet])
async def get_test_data():
    return kedro.get_test_data()

@router.get("/train_data", response_model=List[KedroDataSet])
async def get_train_data():
    return kedro.get_train_data()

@router.get("/synth_data", response_model=List[KedroDataSet])
async def get_synth_data():
    return kedro.get_synth_data()