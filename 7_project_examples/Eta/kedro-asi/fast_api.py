from pathlib import Path

import pandas as pd
from autogluon.tabular import TabularPredictor
from fastapi import FastAPI, HTTPException, Request
from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project
from sdv.lite import SingleTablePreset
from sdv.metadata import SingleTableMetadata

from utils import connect_to_db, get_latest_autogluon_model_path, clear_logs_file, read_logs_file_content

app = FastAPI()
DATABASE_SCHEMA_NAME = 'cwur'
SYNTHETIC_DATA_TABLE_NAME = 'synthetic_cwur'
PRODUCTION_DATA_TABLE_NAME = 'cwur'


@app.get('/run')
async def run_pipeline():
    try:
        project_path = Path.cwd()
        bootstrap_project(project_path)
        clear_logs_file()
        with KedroSession.create(project_path) as session:
            session.run(pipeline_name="__default__")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get('/logs')
async def see_kedro_logs():
    try:
        log_content = read_logs_file_content()
        return {"logs": log_content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post('/predict')
async def make_prediction(request: Request):
    try:
        global predictor
        input_data = await request.json()
        data = pd.DataFrame([input_data])
        predictor = TabularPredictor.load(str(get_latest_autogluon_model_path))
        prediction = predictor.predict(data)
        return {"prediction": prediction.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# TODO: in future maybe let user choose row from synthetic data to make prediction on that.
@app.get('/predictSynthetic')
async def make_prediction_for_synthetic():
    try:
        global predictor
        predictor = TabularPredictor.load(str(get_latest_autogluon_model_path()))
        engine = connect_to_db(str(Path.cwd() / 'conf'))
        synthetic_data = pd.read_sql_table(SYNTHETIC_DATA_TABLE_NAME, engine, DATABASE_SCHEMA_NAME)
        prediction = predictor.predict(synthetic_data)
        return {"prediction": prediction.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post('/synthetic')
async def generate_synthetic_data(request: Request):
    try:
        number_of_rows = await request.json()
        metadata = SingleTableMetadata()
        engine = connect_to_db(str(Path.cwd() / 'conf'))
        real_data = pd.read_sql_table(PRODUCTION_DATA_TABLE_NAME,
                                      engine,
                                      DATABASE_SCHEMA_NAME)
        metadata.detect_from_dataframe(real_data)
        # SDV couldn't automatically recognize institution's column type
        metadata.update_column(column_name='institution', sdtype='categorical')

        synthesizer = SingleTablePreset(metadata, name='FAST_ML')
        synthesizer.fit(data=real_data)
        synthetic_data = synthesizer.sample(num_rows=number_of_rows['number_of_rows'])
        synthetic_data.to_sql(SYNTHETIC_DATA_TABLE_NAME,
                              engine,
                              DATABASE_SCHEMA_NAME,
                              if_exists='append',
                              index=False)

        return {"synthetic": synthetic_data.to_json()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
