from sklearn.model_selection import train_test_split
from autogluon.tabular import TabularPredictor
from sklearn.metrics import accuracy_score, recall_score, precision_score
import numpy as np
import pandas as pd
import wandb


def autogluonTraining(data):
    train_X, test_X = train_test_split(pd.DataFrame(data))

    predictor = TabularPredictor(label='planet_type').fit(pd.DataFrame(train_X))
    predictions = predictor.predict(pd.DataFrame(test_X))
    
    run = wandb.init(project='asi-project', job_type='train')
    true_labels = test_X['planet_type']
    accuracy = accuracy_score(true_labels, predictions)
    recall = recall_score(true_labels, predictions, average='weighted')
    precision = precision_score(true_labels, predictions, average='weighted')
    wandb.log({
        "accuracy": accuracy,
        "recall": recall,
        "precision": precision
    })
    

    run.finish()

    return predictor
