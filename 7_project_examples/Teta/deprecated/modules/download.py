import pandas as pd


def download():
    url = "https://raw.githubusercontent.com/karolpj/asi_group1/main/data/mushrooms.csv"
    df = pd.read_csv(url)
    return df
