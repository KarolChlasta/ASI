from pathlib import Path

from kedro.config import ConfigLoader
from sqlalchemy import Engine, create_engine

# Should be loaded from logging.yml as KEDRO_LOGGING_CONFIG or default as its hardcoded now
log_file_path = Path.cwd() / 'info.log'


def connect_to_db(conf_path: str) -> Engine:
    conf_loader = ConfigLoader(conf_source=conf_path)
    credentials = conf_loader.get("local/credentials", "credentials.yml")
    db_username = credentials["postgres"]["username"]
    db_password = credentials["postgres"]["password"]
    db_host = credentials["postgres"]["host"]
    db_port = credentials["postgres"]["port"]
    database_name = credentials["postgres"]["database"]
    user = db_username
    password = db_password
    host = db_host
    database = database_name
    connection_string = f"postgresql://{user}:{password}@{host}:{db_port}/{database}"
    return create_engine(connection_string)


def get_latest_autogluon_model_path() -> Path:
    model_directory = Path('AutogluonModels')
    if not model_directory.exists():
        raise FileNotFoundError(f"Could not find directory with Autogluon Models: {model_directory}")
    latest_model_path = max(model_directory.iterdir(), key=lambda x: x.stat().st_mtime)
    if not latest_model_path.is_dir():
        raise FileNotFoundError(f"Nie znaleziono modelu: {latest_model_path}")
    return latest_model_path


def read_logs_file_content() -> str:
    with open(log_file_path, 'r') as log_file:
        return log_file.read()


def clear_logs_file():
    open(log_file_path, 'w').close()
