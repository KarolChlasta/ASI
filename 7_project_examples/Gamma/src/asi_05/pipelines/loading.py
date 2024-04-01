import pandas as pd
from kedro.config import ConfigLoader
from pathlib import Path
import psycopg2

def loadData():
    # odczytanie credentials
    conf_loader = ConfigLoader(conf_source=str(Path.cwd() / 'conf'))
    credentials = conf_loader.get("local/credentials", "credentials.yml")
    # Parametry połączenia z bazą danych
    db_username = credentials["postgres"]["username"]
    db_password = credentials["postgres"]["password"]
    db_host = credentials["postgres"]["host"]
    db_port = credentials["postgres"]["port"]
    db_name = credentials["postgres"]["name"]

    # Łączenie z bazą danych
    connection = psycopg2.connect(
        dbname=db_name,
        user=db_username,
        password=db_password,
        host=db_host,
        port=db_port
    )

    # Wczytywanie danych z bazy danych do DataFrame
    query = "SELECT * FROM exoplanets"
    data = pd.read_sql(query, connection)
    
    # Zamykanie połączenia
    connection.close()
    return data