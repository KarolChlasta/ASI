from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle


def lgr_model(X_train, X_test, y_train, y_test, X_val, y_val):
    logmodel = LogisticRegression(max_iter=500)
    logmodel.fit(X_train, y_train)
    y_pred_val = logmodel.predict(X_val)
    y_pred = logmodel.predict(X_test)
    print(classification_report(y_test, y_pred))
    print(classification_report(y_val, y_pred_val))
    pickle.dump(logmodel, open("./models/lgr.pkl", "wb"))


def knn_model(X_train, X_test, y_train, y_test, X_val, y_val):
    knn_model = KNeighborsClassifier(n_neighbors=8)
    knn_model.fit(X_train, y_train)
    y_pred_knn_val = knn_model.predict(X_val)
    y_pred_knn = knn_model.predict(X_test)
    print(accuracy_score(y_test, y_pred_knn))
    print(accuracy_score(y_val, y_pred_knn_val))
    pickle.dump(knn_model, open("./models/knn.pkl", "wb"))
