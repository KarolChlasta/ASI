"""
This is a boilerplate pipeline 'load_data'
generated using Kedro 0.18.14
"""

from autogluon.tabular import TabularDataset
import pandas as pd
import sqlite3

# def load_data(weatherAUS):
#     # plain_data = catalog.load("weatherAUS")
#     all_data = TabularDataset(weatherAUS)
#     return all_data

def load_data():
    # df = pd.read_csv("https://raw.githubusercontent.com/michaljn2/ASI_Projekt/main/weatherAUS.csv")
    conn = sqlite3.connect("asi.db")
    # df.to_sql('weather', conn, if_exists='replace', index=False)
    all_data = pd.read_sql_query("SELECT * FROM weather", conn, index_col=None, coerce_float=True, params=None, parse_dates=None, chunksize=None)
    # all_data = TabularDataset(sqlData)
    return all_data