"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.14
"""
import pandas
import pandas as pd
from sdv.metadata import SingleTableMetadata
from sklearn.preprocessing import OrdinalEncoder
from sklearn.impute import SimpleImputer
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler
import numpy as np
from sdv.single_table import GaussianCopulaSynthesizer
import pandas
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.impute import SimpleImputer
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler
import numpy as np




def load_data():
    return pd.read_csv("https://archive.ics.uci.edu/static/public/222/data.csv")


def drop_impute_missing_data(data):
    columns_to_drop = data.columns[data.isnull().mean() > 0.5]

    data = data.drop(columns=columns_to_drop)
    data[data == "NaN"] = np.nan
    remaining_columns = data.columns[data.isnull().any()]
    # Separate categorical and numerical columns
    categorical_columns = data[remaining_columns].select_dtypes(include='object').columns
    numerical_columns = data[remaining_columns].select_dtypes(exclude='object').columns
    print(categorical_columns)
    print(numerical_columns)
    # Impute categorical columns
    if not categorical_columns.empty:
        categorical_imputer = SimpleImputer(strategy='most_frequent')
        data[categorical_columns] = categorical_imputer.fit_transform(data[categorical_columns])

    # Impute numerical columns
    if not numerical_columns.empty:
        numerical_imputer = SimpleImputer(strategy='mean')
        data[numerical_columns] = numerical_imputer.fit_transform(data[numerical_columns])

    return data


def rebalance_data(data):
    rus = RandomUnderSampler(random_state=0)
    X_resampled, y_resampled = rus.fit_resample(data.drop(['y'], axis=1), data[['y']])
    data_undersampled = pd.concat([X_resampled, y_resampled], axis="columns")

    rus = RandomOverSampler(random_state=0)
    X_resampled, y_resampled = rus.fit_resample(data.drop(['y'], axis=1), data[['y']])
    data_oversampled = pd.concat([X_resampled, y_resampled], axis="columns")
    return data_oversampled, data_undersampled


def encode_data(data):
    enc = OrdinalEncoder()
    data[data.select_dtypes(include=['object']).columns] = enc.fit_transform(data.select_dtypes(include=['object']))
    return data, enc


def preprocess_data(data, parameters):
    dataChanged = drop_impute_missing_data(data)
    synthetic_data = synthetic(dataChanged, 1000)

    print("DATA CHANGED ///////////////////////")
    print(dataChanged)
    print("DATA CHANGED ///////////////////////")
    print(synthetic_data)

    # dataframe = pandas.DataFrame.join(dataChanged, synthetic_data)

    dataChanged, enc = encode_data(dataChanged)
    oversampled, undersampled = rebalance_data(dataChanged)


    # dataframe = pandas.DataFrame.join(dataChanged, synthetic_data)

    # print(dataframe)

    return oversampled, undersampled, enc, dataChanged


def synthetic(data, rows):
    metadata = SingleTableMetadata()
    metadata.detect_from_dataframe(data)
    synthesizer = GaussianCopulaSynthesizer(metadata)
    synthesizer.fit(data)
    synthetic_data = synthesizer.sample(num_rows=rows)
    return synthetic_data


