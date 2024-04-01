import pandas as pd
from sklearn.model_selection import train_test_split


def preprocess(df):
    if df.duplicated().sum() > 0:
        df.drop_duplicates()
    df = df.apply(lambda x: pd.factorize(x)[0])
    X = df.drop(columns="class")
    y = df["class"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, shuffle=True
    )
    X_test, X_val, y_test, y_val = train_test_split(
        X_test, y_test, test_size=0.25, random_state=31, shuffle=True
    )
    return X_train, X_test, y_train, y_test, X_val, y_val
