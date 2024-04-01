from typing import Union
from fastapi import FastAPI
import wandb
import pickle
from bank_client import Bank_Client
import pyarrow.parquet as pq
import uvicorn
import pandas as pd
from autogluon.tabular import TabularPredictor
from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project
import os
import yaml
from fastapi import FastAPI, HTTPException, Request

class ModelHandler:
    def __init__(self):
        self.loaded_model = None
        self.loaded_encoder = None
        self.model_artifact =  None

    def load_models(self):
        api = wandb.Api()
        self.model_artifact = api.artifact("asi_grupa_3/bank_dataset/classifier:latest")
        encoder_artifact = api.artifact("asi_grupa_3/bank_dataset/encoder:latest")

        model_path = self.model_artifact.download()
        self.loaded_model = pickle.load(open(f'{model_path}\classifier.pkl', 'rb'))

        encoder_path = encoder_artifact.download()
        self.loaded_encoder = pickle.load(open(f'{encoder_path}\encoder.pkl', 'rb'))

app = FastAPI()
model_handler = ModelHandler()

@app.on_event("startup")
def load_models():
    model_handler.load_models()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/downloadmodels")
def read_root():
    model_handler.load_models()
    return {"message": "Models downloaded successfully."}

@app.get("/modelinfo")
def show_model_info():
    return {"model_type": type(model_handler.loaded_model).__name__,
            "model_name": model_handler.model_artifact.name,
            "model_meta": model_handler.model_artifact.metadata}



@app.post("/runpipeline")
def receive_parameters(data: dict):
    bootstrap_project( os.getcwd())
    session = KedroSession.create()
 
    data_science_params = data.get("data_science_params")
    split_params = data.get("split_params")
    pipeline = data.get("pipeline")
        # Process the received parameters and write to YAML files
    write_data_science_params(data_science_params)
    write_split_params(split_params)

    answer = session.run(pipeline)
    session.load_context()
        
    return {"message": "Parameters received and YAML files written successfully!"}
    
def write_data_science_params(params):
    data_science_file_path = "conf/base/parameters_data_science.yml"
    with open(data_science_file_path, "w") as f:
        yaml.dump({
            "model_options": {
                "random_state": params["random_state"],
                "features": "all",
                "kernel": params["kernel"],
                "rebalance": params["rebalance"],
                "model_type": params["model_type"],
                "n_estimators": params["n_estimators"]
            }
        }, f)

def write_split_params(params):
    split_file_path = "conf/base/parameters_train_test_split.yml"
    with open(split_file_path, "w") as f:
        yaml.dump({
            "dataset_choice": {
                "rebalanced": params["rebalance_split"],
                "target_var_name": "y",
                "test_size": params["test_size"],
                "val_size": params["val_size"],
                "random_state": params["random_state_split"]
            }
        }, f)


@app.post("/predict/client")
def predict_client(data: Bank_Client):
    data = data.dict()
    dframe = pd.DataFrame(data, index=[0])
    dframe['y'] = 'no'
    dframe[dframe.select_dtypes(include=['object']).columns] = model_handler.loaded_encoder.transform(dframe.select_dtypes(include=['object']))

    prediction = model_handler.loaded_model.predict(dframe.iloc[:, :-1])
    prob = model_handler.loaded_model.predict_proba(dframe.iloc[:, :-1])

    prediction = 'Will take credit' if prediction[0] == 1.0  else "Will not take credit"
    return {
        'prediction': prediction,
        'probabilityA': f"Probability A: { prob[0][0] * 100:.2f}%",
        'probabilityB': f"Probability B: { prob[0][1] * 100:.2f}%"
    }

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8001)
