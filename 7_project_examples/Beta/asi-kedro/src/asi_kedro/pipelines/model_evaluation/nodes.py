# """
# This is a boilerplate pipeline 'model_evaluation'
# generated using Kedro 0.18.14
# """
# # Evaluation
#
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.metrics import roc_curve, precision_recall_curve, auc
# import wandb
#
#
# def evaluate_model(predictions_test: pd.DataFrame):
#     run = wandb.init(
#         project='Kedro-ASI-Test-Autogluon',
#         config={
#             "learning_rate": 0.01,
#             "epochs": 10
#         }
#     )
#     wandb.log({"conf_mat": wandb.plot.confusion_matrix(probs=None,
#                                                        y_true=predictions_test['Potability'].values,
#                                                        preds=predictions_test['Prediction'].values,
#                                                        class_names=['0', '1'])})

import pandas as pd
import wandb
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score


class Metrics:
    pass


def evaluate_model(
        predictions_test: pd.DataFrame,
        project_name='Kedro-ASI-Test-Autogluon',
        learning_rate=0.01,
        epochs=10,
        log_additional_info=False
) -> [pd.DataFrame, pd.DataFrame]:
    # Initialize WandB run
    run = wandb.init(project=project_name, config={"learning_rate": learning_rate, "epochs": epochs})

    try:
        # Calculating metrics
        accuracy = accuracy_score(predictions_test['Potability'], predictions_test['Prediction'])
        precision = precision_score(predictions_test['Potability'], predictions_test['Prediction'])
        recall = recall_score(predictions_test['Potability'], predictions_test['Prediction'])
        f1 = f1_score(predictions_test['Potability'], predictions_test['Prediction'])
        confusion_matrix = pd.crosstab(
            predictions_test['Potability'],
            predictions_test['Prediction'],
            rownames=['Actual'],
            colnames=['Predicted']
        )

        # Log metrics
        wandb.log({"conf_mat": wandb.plot.confusion_matrix(probs=None, y_true=predictions_test['Potability'].values,
                                                           preds=predictions_test['Prediction'].values,
                                                           class_names=['0', '1']),
                   "accuracy": accuracy,
                   "precision": precision,
                   "recall": recall,
                   "f1_score": f1})

        return pd.DataFrame({
            'accuracy': [accuracy],
            'precision': [precision],
            'recall': [recall],
            'f1_score': [f1]
        }), confusion_matrix

    except KeyError as e:
        print(f"KeyError: {e}. Ensure 'Potability' and 'Prediction' are in predictions_test.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        run.finish()
