"""
This is a boilerplate pipeline 'data_science'
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


def train_model(train, parameters):
    model_type = parameters["model_type"]
    clf = None

    if model_type == "svc":
        clf = svm.SVC(
            kernel=parameters["kernel"], random_state=parameters["random_state"], probability=True
        )
    elif model_type == "logistic":
        clf = LogisticRegression(random_state=parameters["random_state"], max_iter=10000)
    elif model_type == "random_forest":
        clf = RandomForestClassifier(
            n_estimators=parameters["n_estimators"],
            random_state=parameters["random_state"],
        )

    X_train = train.iloc[:, :-1]
    y_train = train.iloc[:, -1]

    clf.fit(X_train, y_train.values.ravel())
    print("DATA_SCIENCE")
    X_train.info()
    return clf
