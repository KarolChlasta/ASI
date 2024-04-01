"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.14
"""
from sklearn.model_selection import train_test_split

def prepare_data(all_data):
    return all_data.dropna(axis=0, subset=['RainTomorrow']).drop(columns=['Date'])

def split_data(all_data):
    train_data, test_data = train_test_split(all_data, test_size=0.2, random_state=100)
    return train_data, test_data