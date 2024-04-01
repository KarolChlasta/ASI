"""
This is a boilerplate pipeline 'automl'
generated using Kedro 0.18.14
"""

from autogluon.tabular import TabularDataset, TabularPredictor
from sklearn.model_selection import train_test_split
import pickle
def automlflow(data, parameters):
    data = TabularDataset(data)

    label_column = parameters["target_var_name"]



    predictor = TabularPredictor(label=label_column).fit(train_data=data, presets="optimize_for_deployment")
   

    model =  pickle.load(open( f"{predictor.path}\models\{predictor.get_model_best()}\model.pkl", 'rb'))
    return model

