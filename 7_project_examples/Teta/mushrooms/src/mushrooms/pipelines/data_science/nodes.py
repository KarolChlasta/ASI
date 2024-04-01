from typing import Tuple
import shutil


import pandas as pd
from sklearn.model_selection import train_test_split
import wandb
from autogluon.tabular import TabularDataset, TabularPredictor

path = "../models"


def split_data(data: pd.DataFrame) -> Tuple:
    """Splits data into features and targets training and test sets.

    Args:
        data: Data containing features and target.
        parameters: Parameters defined in parameters/data_science.yml.
    Returns:
        Split data.
    """
    data.dropna(inplace=True)
    X = data.drop(columns=["class_e", "class_p"])
    y = data["class_e"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, shuffle=True
    )

    return X_train, X_test, y_train, y_test


def train_model(
    X_train: pd.DataFrame, y_train: pd.DataFrame, model_params
) -> TabularPredictor:
    """Trains the linear regression model.

    Args:
        X_train: Training data of independent features.
        y_train: Training data for price.

    Returns:
        Trained model.
    """
    print("Model params: ", model_params)
    label = "label"
    y_train = pd.DataFrame({"label": y_train})
    data = pd.concat([X_train, y_train], axis=1)
    train_data = TabularDataset(data)
    predictor = TabularPredictor(
        label=label, eval_metric=model_params["eval_metric"], path=path
    ).fit(
        train_data,
        time_limit=model_params["time_limit"],
        presets=model_params["presets"],
        hyperparameters=model_params["hyperparameters"],
    )
    return predictor


def evaluate_model(
    predictor: TabularPredictor, X_test: pd.DataFrame, y_test: pd.Series, model_params
):
    """Calculates and logs the coefficient of determination.

    Args:
        regressor: Trained model.
        X_test: Testing data of independent features.
        y_test: Testing data for price.
    """
    y_test = pd.DataFrame({"label": y_test})
    data = TabularDataset(pd.concat([X_test, y_test], axis=1))

    evaluation = predictor.evaluate(data)

    predictor.leaderboard(data)
    leaderboard = predictor.leaderboard(silent=True)
    best_model = leaderboard.iloc[0]["model"]
    shutil.move(f"{path}/models/{best_model}/model.pkl", "../bestmodel/model.pkl")

    wandb.init(project="mushrooms")
    wandb.log({"best model": leaderboard.iloc[0]["model"]})
    wandb.log(evaluation)
    wandb.log(model_params)

    wandb.finish()
