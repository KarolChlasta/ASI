"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 0.18.14
"""
# Evaluation

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, precision_recall_curve, auc
import wandb


def evaluate_model(predictions_test: pd.DataFrame):
    run = wandb.init(
        project='Kedro-ASI-Test-Autogluon',
        config={
            "learning_rate": 0.01,
            "epochs": 10
        }
    )
    wandb.log({"conf_mat": wandb.plot.confusion_matrix(probs=None,
                                                       y_true=predictions_test['Potability'].values,
                                                       preds=predictions_test['Prediction'].values,
                                                       class_names=['0', '1'])})
