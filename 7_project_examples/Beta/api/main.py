# from endpoint.parametrs_point import router as parameters_router
# from endpoint.wandb_point import router as wandb_router
# from endpoint.home_point import router as home_router
# from fastapi import FastAPI
# from services.cli import *
#
# app = FastAPI()
#
# app.include_router(parameters_router)
# app.include_router(wandb_router)
# app.include_router(home_router)
from fastapi import FastAPI
from api.endpoint.dataset_endpoint import router as db_router

app = FastAPI()

app.include_router(db_router)