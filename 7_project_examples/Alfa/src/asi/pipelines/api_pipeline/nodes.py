import pandas as pd


class MLPredictor:
    def __init__(self, model):
        self.model = model

    def predict(self, args_API: pd.DataFrame):
        df_args = args_API
        prediction = self.model.predict(df_args)
        return {"prediction": prediction}


def save_predictor(model):
    predictor = MLPredictor(model)
    return predictor
