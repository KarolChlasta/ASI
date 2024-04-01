from sdv.single_table import GaussianCopulaSynthesizer
from sdv.metadata import SingleTableMetadata
import psycopg2
from sqlalchemy import create_engine
import pandas as pd

def generate_synthetic_data(host, database, user, password, constring):
    conn = psycopg2.connect(host=host, database=database, user=user, password=password, port=5433)
    sql_query = 'SELECT * FROM health_data'
    df = pd.read_sql(sql_query, conn)
    conn.close()

    metadata = SingleTableMetadata()
    metadata.detect_from_dataframe(df)
    model = GaussianCopulaSynthesizer(metadata)
    model.fit(df)
    synthetic_data = model.sample(len(df))

    conn = create_engine(constring)
    synthetic_data.to_sql('health_data', conn, if_exists='replace', index=False)