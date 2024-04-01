"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.14
"""
from pandas import DataFrame, concat
from autogluon.tabular import TabularPredictor
from autogluon.tabular import TabularDataset

def train_model(train_data: TabularDataset) -> TabularPredictor:
    # Assuming the last column of df is 'target' and rest are features
    predictor = TabularPredictor(label='Potability', eval_metric='balanced_accuracy').fit(train_data=train_data)
    return predictor

def test_model(predictor: TabularPredictor, test_data: DataFrame) -> DataFrame:
    predictions = DataFrame(predictor.predict(data=test_data, as_pandas=True))
    predictions.rename(columns={"Potability": "Prediction"}, inplace=True)
    predictions = concat([predictions, test_data["Potability"]], axis=1)
    return predictions

