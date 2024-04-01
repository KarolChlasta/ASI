import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from autogluon.tabular import TabularDataset, TabularPredictor
import psycopg2
import wandb
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

def download(host, database, user, password):
    conn = psycopg2.connect(host=host, database=database, user=user, password=password, port=5433)
    sql_query = 'SELECT * FROM health_data'
    df = pd.read_sql(sql_query, conn)
    conn.close()   
    return df

def init_wandb(configg):
    wandb.init(
    project="asi-2",
    config=configg)
    
    
def preprocess(df , random_state:int, constring):   
    #X = df.drop("diabetes", axis=1)  # Replace "target_column_name" with the actual name of your target column.
    y = df["diabetes"]
    X = df
    label_encoders = {}
    for column in X.select_dtypes(include=["object"]).columns: # replace "object" with "category"
        label_encoders[column] = LabelEncoder()
        X[column] = label_encoders[column].fit_transform(X[column])
    X_train, X_split, y_train, y_split = train_test_split(X, y, test_size=0.3, random_state=random_state)
    X_test, X_validate, y_test, y_validate = train_test_split(X_split, y_split, test_size=0.5, random_state=random_state)
    
    db = create_engine(constring) 
    
    X_train.to_sql('train', db, if_exists='replace', index=False)
    X_test.to_sql('test', db, if_exists='replace', index=False)
    X_validate.to_sql('validate', db, if_exists='replace', index=False)
    
    
    X_test = X_test.drop("diabetes", axis=1)
    X_validate = X_validate.drop('diabetes', axis=1)
    
    return X_train, X_test, X_validate, y_train, y_test, y_validate
