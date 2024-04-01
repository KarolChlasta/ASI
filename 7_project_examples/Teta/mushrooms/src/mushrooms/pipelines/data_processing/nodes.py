import pandas as pd
import sqlite3


def load_mushrooms() -> pd.DataFrame:
    database_file_path = "../data/mushrooms.db"
    connection = sqlite3.connect(database_file_path)
    df = pd.read_sql("SELECT * FROM mushrooms", connection)
    connection.close()
    return df


def preprocess_mushrooms(mushrooms: pd.DataFrame) -> pd.DataFrame:
    onehot = pd.get_dummies(mushrooms, dtype=int)
    return onehot


def create_model_input_table(mushrooms: pd.DataFrame) -> pd.DataFrame:

    model_input_table = mushrooms
    model_input_table = model_input_table.dropna()
    return model_input_table
