from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import HistGradientBoostingClassifier

def drop_nan(df):
    columns_to_drop = df.columns[df.isna().iloc[row_index]]
    return df.drop(columns=columns_to_drop)

def analyze_factors(data, target_column='Potability'):
    # Assume all other columns are features
    data = data.dropna()
    X = data.drop(target_column, axis=1)
    y = data[target_column]
    # Fit a random forest classifier
    model = RandomForestClassifier()
    model.fit(X, y)

    # Get feature importances
    importances = model.feature_importances_
    feature_names = X.columns
    feature_importances = pd.Series(importances, index=feature_names)

    return feature_importances.sort_values(ascending=False)


def get_model_insights(data, target_column='Potability'):
    X = data.drop(target_column, axis=1)
    y = data[target_column]

    # Fit a decision tree classifier
    model = DecisionTreeClassifier(max_depth=3)  # Limiting depth for simplicity
    model.fit(X, y)

    # Visualize the decision tree
    plt.figure(figsize=(20, 10))
    plot_tree(model, feature_names=X.columns, class_names=['Non-Potable', 'Potable'], filled=True)
    plt.show()
