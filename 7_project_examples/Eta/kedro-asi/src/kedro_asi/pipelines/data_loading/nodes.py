import pandas as pd
from sqlalchemy import create_engine
from kedro.config import ConfigLoader


def load_data_from_postgresql() -> pd.DataFrame:
    conf_loader = ConfigLoader("conf")
    credentials = conf_loader.get("local*", "credentials*", "credentials*/**")
    db_credentials = credentials['my_postgres_db']

    engine = create_engine(
        f'postgresql://{db_credentials["username"]}:{db_credentials["password"]}@{db_credentials["host"]}:{db_credentials["port"]}/{db_credentials["database"]}')

    sql_query = 'SELECT * FROM cwur.cwur'

    universities = pd.read_sql_query(sql_query, engine)

    return universities
