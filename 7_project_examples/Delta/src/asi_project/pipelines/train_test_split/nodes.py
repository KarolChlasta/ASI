"""
This is a boilerplate pipeline 'train_test_split'
generated using Kedro 0.18.14
"""
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.linear_model import LogisticRegression
import pandas as pd
import logging
import wandb
from sklearn.metrics import (
    confusion_matrix,
    precision_score,
    accuracy_score,
    recall_score,
)
import matplotlib.pyplot as plt



def choose_training_dataset(undersampled_data, oversampled_data,undersampled_data2, oversampled_data2, parameters):
    if parameters["rebalanced"] == "undersampled":
        if undersampled_data is None:
            return undersampled_data2
        else:
            return undersampled_data
    else:
        if oversampled_data is None:
            return oversampled_data2
        else:
            return oversampled_data


def split_train_test(data, parameters):
    y = data[parameters["target_var_name"]]
    X = data.drop([parameters["target_var_name"]], axis=1)



    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        stratify=y,
        test_size=parameters["test_size"],
        random_state=parameters["random_state"],
    )

    train = pd.concat([X_train, y_train], axis=1)
    test = pd.concat([X_test, y_test], axis=1)
 
    return  train, test