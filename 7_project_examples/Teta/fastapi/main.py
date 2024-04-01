import os
import pickle
import sqlite3

import pandas as pd
from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project
from pydantic import BaseModel
from sdv.metadata import SingleTableMetadata
from sdv.single_table import GaussianCopulaSynthesizer

from fastapi import FastAPI

MODEL_PATH = "../bestmodel/model.pkl"
DATABASE_URI = "../data/mushrooms.db"
DATA_COLUMNS = [
    "cap-shape_b",
    "cap-shape_c",
    "cap-shape_f",
    "cap-shape_k",
    "cap-shape_s",
    "cap-shape_x",
    "cap-surface_f",
    "cap-surface_g",
    "cap-surface_s",
    "cap-surface_y",
    "cap-color_b",
    "cap-color_c",
    "cap-color_e",
    "cap-color_g",
    "cap-color_n",
    "cap-color_p",
    "cap-color_r",
    "cap-color_u",
    "cap-color_w",
    "cap-color_y",
    "bruises_f",
    "bruises_t",
    "odor_a",
    "odor_c",
    "odor_f",
    "odor_l",
    "odor_m",
    "odor_n",
    "odor_p",
    "odor_s",
    "odor_y",
    "gill-attachment_a",
    "gill-attachment_f",
    "gill-spacing_c",
    "gill-spacing_w",
    "gill-size_b",
    "gill-size_n",
    "gill-color_b",
    "gill-color_e",
    "gill-color_g",
    "gill-color_h",
    "gill-color_k",
    "gill-color_n",
    "gill-color_o",
    "gill-color_p",
    "gill-color_r",
    "gill-color_u",
    "gill-color_w",
    "gill-color_y",
    "stalk-shape_e",
    "stalk-shape_t",
    "stalk-root_?",
    "stalk-root_b",
    "stalk-root_c",
    "stalk-root_e",
    "stalk-root_r",
    "stalk-surface-above-ring_f",
    "stalk-surface-above-ring_k",
    "stalk-surface-above-ring_s",
    "stalk-surface-above-ring_y",
    "stalk-surface-below-ring_f",
    "stalk-surface-below-ring_k",
    "stalk-surface-below-ring_s",
    "stalk-surface-below-ring_y",
    "stalk-color-above-ring_b",
    "stalk-color-above-ring_c",
    "stalk-color-above-ring_e",
    "stalk-color-above-ring_g",
    "stalk-color-above-ring_n",
    "stalk-color-above-ring_o",
    "stalk-color-above-ring_p",
    "stalk-color-above-ring_w",
    "stalk-color-above-ring_y",
    "stalk-color-below-ring_b",
    "stalk-color-below-ring_c",
    "stalk-color-below-ring_e",
    "stalk-color-below-ring_g",
    "stalk-color-below-ring_n",
    "stalk-color-below-ring_o",
    "stalk-color-below-ring_p",
    "stalk-color-below-ring_w",
    "stalk-color-below-ring_y",
    "veil-type_p",
    "veil-color_n",
    "veil-color_o",
    "veil-color_w",
    "veil-color_y",
    "ring-number_n",
    "ring-number_o",
    "ring-number_t",
    "ring-type_e",
    "ring-type_f",
    "ring-type_l",
    "ring-type_n",
    "ring-type_p",
    "spore-print-color_b",
    "spore-print-color_h",
    "spore-print-color_k",
    "spore-print-color_n",
    "spore-print-color_o",
    "spore-print-color_r",
    "spore-print-color_u",
    "spore-print-color_w",
    "spore-print-color_y",
    "population_a",
    "population_c",
    "population_n",
    "population_s",
    "population_v",
    "population_y",
    "habitat_d",
    "habitat_g",
    "habitat_l",
    "habitat_m",
    "habitat_p",
    "habitat_u",
    "habitat_w",
]


app = FastAPI()


class MushroomInput(BaseModel):
    cap_shape: str
    cap_surface: str
    cap_color: str
    bruises: str
    odor: str
    gill_attachment: str
    gill_spacing: str
    gill_size: str
    gill_color: str
    stalk_shape: str
    stalk_root: str
    stalk_surface_above_ring: str
    stalk_surface_below_ring: str
    stalk_color_above_ring: str
    stalk_color_below_ring: str
    veil_type: str
    veil_color: str
    ring_number: str
    ring_type: str
    spore_print_color: str
    population: str
    habitat: str


def run_kerdo_pipeline(**kwargs):
    os.chdir("../mushrooms")
    bootstrap_project(os.getcwd())
    params = {"model_params": kwargs}
    session = KedroSession.create(extra_params=params)
    session.run()
    session.close()
    os.chdir("../fastapi")


@app.post("/predict")
def predict_mushroom(mushroom: MushroomInput):
    with open(MODEL_PATH, "rb") as file:
        loaded_model = pickle.load(file)
    input_data = pd.DataFrame([mushroom.dict()])
    onehot = pd.get_dummies(input_data, dtype=int)
    onehot = onehot.reindex(columns=DATA_COLUMNS, fill_value=0)
    prediction = loaded_model.predict(onehot)
    return {"prediction": prediction[0]}


@app.get("/generate/{ammount}")
def generate_data(ammount: int):
    connection = sqlite3.connect(DATABASE_URI)
    df = pd.read_sql("SELECT * FROM mushrooms", connection)
    metadata = SingleTableMetadata()
    metadata.detect_from_dataframe(df)
    synthesizer = GaussianCopulaSynthesizer(metadata)
    synthesizer.fit(df)
    sample = synthesizer.sample(num_rows=ammount)
    sample.to_sql("mushrooms", connection, if_exists="append", index=False)
    json = sample.head(10).to_json()
    return json


@app.get("/run_pipeline")
def run_pipeline(hyperparameters: str, presets: str, eval_metric: str, time_limit: int):
    params = {
        "hyperparameters": hyperparameters,
        "presets": presets,
        "eval_metric": eval_metric,
        "time_limit": time_limit,
    }
    run_kerdo_pipeline(**params)
