"""
This is a boilerplate pipeline 'eval'
generated using Kedro 0.18.14
"""
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from autogluon.tabular import TabularPredictor

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





def eval_model(model,test):
    X_test = test.iloc[:, :-1]
    y_test = test.iloc[:, -1]
    y_pred = model.predict(X_test)
    y_probas = model.predict_proba(X_test)
    return y_test, y_pred, y_probas


def log_results(y_test, y_pred, y_probas,parameters, model):
    precision = precision_score(y_pred, y_test)
    accuracy = accuracy_score(y_pred, y_test)
    recall = recall_score(y_pred, y_test)
    logger = logging.getLogger(__name__)
    logger.info("Model has a coefficient Accuracy of %.3f on test data.", accuracy)

    # hyperparameters = dict()
    # hyperparameters = model.get_params()
    # print(hyperparameters)
    # run = wandb.init(project="bank_dataset", config=hyperparameters)


    run = wandb.init(project="bank_dataset")


    #wandb.sklearn.plot_roc(y_test, y_probas, y_test.unique())
    wandb.sklearn.plot_feature_importances(model)
    wandb.sklearn.plot_confusion_matrix(y_test, y_pred, y_test.unique())



    wandb.summary["accuracy"] = accuracy
    wandb.summary["recall"] = recall
    wandb.summary["precision"] = precision



    model_artifact = wandb.Artifact(name='classifier', type='model')
    model_artifact.add_file('data/06_models/classifier_1.pkl', name='classifier.pkl')
    encoder_artifact = wandb.Artifact(name='encoder', type='model')
    encoder_artifact.add_file('data/06_models/encoder_1.pkl', name='encoder.pkl')


    raw_data = wandb.Artifact(name='raw_bank_data', type='dataset')
    raw_data.add_file('data/01_raw/bank_raw.pq')

    train_test_data = wandb.Artifact(name='train_test_bank_data', type='dataset')
    if parameters["rebalance"] == "undersampled":
        train_test_data.add_file('data/02_intermediate/preprocessed_undersampled_bank.pq', name='train_test_bank_data.pq')
    else:
        train_test_data.add_file('data/02_intermediate/preprocessed_oversampled_bank.pq', name='train_test_bank_data.pq')

        
    run.log_artifact(raw_data,aliases = ["latest"])
    run.log_artifact(train_test_data,aliases = ["latest"])

    run.log_artifact(model_artifact,aliases = ["latest"])
    run.log_artifact(encoder_artifact,aliases = ["latest"])
