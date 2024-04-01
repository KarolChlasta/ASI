from fastapi import FastAPI, HTTPException, Request
from autogluon.tabular import TabularPredictor
from kedro.framework.startup import bootstrap_project
from kedro.framework.session import KedroSession
from kedro.config import ConfigLoader
import pandas as pd
from datetime import datetime
from pathlib import Path
import psycopg2
from sqlalchemy import create_engine
from sdv.lite import SingleTablePreset
from sdv.metadata import SingleTableMetadata
from sdv.metadata import SingleTableMetadata


app = FastAPI()

# @app.on_event("startup")
# async def on_startup():


@app.post("/predict")
async def predict(request: Request):
    try:
        global predictor

        model_directory = Path('AutogluonModels')
        if not model_directory.exists():
            raise FileNotFoundError(f"Nie znaleziono katalogu modelu: {model_directory}")

        # Znajdowanie najnowszego modelu
        latest_model_path = max(model_directory.iterdir(), key=lambda x: x.stat().st_mtime)

        if not latest_model_path.is_dir():
            raise FileNotFoundError(f"Nie znaleziono modelu: {latest_model_path}")
    
        print(latest_model_path)

        predictor = TabularPredictor.load(str(latest_model_path))
        input_data = await request.json()
        data = pd.DataFrame([input_data])
        prediction = predictor.predict(data)
        return {"prediction": prediction.tolist()}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/run")
async def run(request: Request):
    try:
        project_path = Path.cwd()
        bootstrap_project(project_path)
        with KedroSession.create(project_path) as session:
            session.run(pipeline_name="__default__")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.get("/synthetic")
async def synthetic(request: Request):
    try:
        metadata = SingleTableMetadata()
        conf_loader = ConfigLoader(conf_source=str(Path.cwd() / 'conf'))
        credentials = conf_loader.get("local/credentials", "credentials.yml")
        # Parametry połączenia z bazą danych
        db_username = credentials["postgres"]["username"]
        db_password = credentials["postgres"]["password"]
        db_host = credentials["postgres"]["host"]
        db_port = credentials["postgres"]["port"]
        db_name = credentials["postgres"]["name"]

        # Łączenie z bazą danych
        user = db_username
        password = db_password
        host = db_host
        dbname = db_name
        connection_string = f"postgresql://{user}:{password}@{host}:{db_port}/{dbname}"
        print("Problem is here")
        engine = create_engine(connection_string)
        print("Problem is after")

        # Wczytywanie danych z bazy danych do DataFrame
        real_data = pd.read_sql_table('exoplanets', engine)

        metadata.detect_from_dataframe(real_data)
        metadata.update_column(
                column_name='eccentricity',
                sdtype='numerical')

        synthesizer = SingleTablePreset(metadata, name='FAST_ML')
        synthesizer.fit(data=real_data)

        synthetic_data = synthesizer.sample(num_rows=100)

        with engine.connect() as connection:
            sql = """CREATE TABLE IF NOT EXISTS synthetic_exoplanets (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255),
                        distance DECIMAL,
                        stellar_magnitude DECIMAL,
                        planet_type VARCHAR(100),
                        discovery_year INTEGER,
                        mass_multiplier DECIMAL,
                        mass_wrt VARCHAR(50),
                        radius_multiplier DECIMAL,
                        radius_wrt VARCHAR(50),
                        orbital_radius DECIMAL,
                        orbital_period DECIMAL,
                        eccentricity DECIMAL,
                        detection_method VARCHAR(100)
                    );"""
            connection.execute(sql)

        synthetic_data.to_sql('synthetic_exoplanets', engine, if_exists='append', index=False)

        return {"synthetic": synthetic_data.to_json()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
