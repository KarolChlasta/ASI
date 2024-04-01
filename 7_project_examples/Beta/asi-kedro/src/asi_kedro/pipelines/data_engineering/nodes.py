"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.14
"""
from pandas import read_csv
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from typing import Tuple
from autogluon.tabular import TabularDataset

def load_data():
    file_name = 'water_potability.csv'
    dataset = read_csv(file_name)
    return dataset


def split_data(data: DataFrame) -> Tuple[DataFrame, DataFrame]:
    train, test = train_test_split(data, test_size=0.2)  # Assuming a 80-20 split
    train = TabularDataset(train)
    test = TabularDataset(test)
    return train, test
    
    