"""
This is a boilerplate pipeline 'visualize'
generated using Kedro 0.18.14
"""

import wandb
from wandb.sklearn import plot_precision_recall, plot_feature_importances
from wandb.sklearn import plot_class_proportions, plot_learning_curve, plot_roc
from wandb.sklearn import plot_summary_metrics

def initWandb(model, test_data, train_data):
    X_train = train_data.drop(['RainTomorrow'], axis=1)
    X_test = test_data.drop(['RainTomorrow'], axis=1)
    y_train = train_data['RainTomorrow']
    y_test = test_data['RainTomorrow']

    y_pred = model.predict(X_test)
    y_probas = model.predict_proba(X_test)
    
    wandb.login(key="71127b4f2e1d9416554ff923f6f1bcbd94489fca")

    wandb.init(project="ASI_weather", config=model.get_params())
    wandb.config.update(
        {"test_size": 0.15, "train_len": len(X_train), "test_len": len(X_test)}
    )

    labels = X_train.columns

    plot_class_proportions(y_train, y_test, labels=labels)
    plot_learning_curve(model, X_train, y_train)
    plot_roc(y_test, y_probas, labels=labels)
    plot_precision_recall(y_test, y_probas, labels=labels)
    plot_feature_importances(model, feature_names=labels)
    plot_summary_metrics(model=model, X=X_train, y=y_train, X_test=X_test, y_test=y_test)
    

    wandb.finish()

    return model