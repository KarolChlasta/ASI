from download import download
from preprocess import preprocess
from model import lgr_model, knn_model


if __name__ == "__main__":
    dataset_dataframe = download()
    X_train, X_test, y_train, y_test, X_val, y_val = preprocess(dataset_dataframe)
    lgr_model(X_train, X_test, y_train, y_test, X_val, y_val)
    knn_model(X_train, X_test, y_train, y_test, X_val, y_val)
