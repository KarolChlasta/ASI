import numpy as np
import pandas as pd
import pickle
from sklearn.metrics import mean_squared_error, r2_score
from datetime import date, datetime
import os.path

import argparse

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)

def go(args):

    # Load model
    model_name = "model/" + args.model
    model = pickle.load(open(model_name, 'rb'))

    # Read test data
    batch_no = args.batch
    test_data = pd.read_csv("data/batch " + str(batch_no) + ".csv")

    X = test_data['x'].values.reshape(-1,1)
    y = test_data['y'].values.reshape(-1,1)

    # Predict
    predictions = model.predict(X)

    # Evaluate
    RMSE = np.sqrt(mean_squared_error(y, predictions))
    r2 = r2_score(y, predictions)
    print('RMSE on test data: ', RMSE)
    print('r2 on test data: ', r2)

    # Create the evaluation dataframe
    eval_df = pd.DataFrame()

    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    eval_df = eval_df.append({'time_stamp':now, 'version': '1.0', 'batch': batch_no, 'metric': 'RMSE', 'score': RMSE}, ignore_index=True)
    eval_df = eval_df.append({'time_stamp':now, 'version': '1.0', 'batch': batch_no, 'metric': 'r2', 'score': r2}, ignore_index=True)

    # Save evaluation to file
    evaluation_file_name = 'evaluation/model_eval.csv'

    if os.path.isfile(evaluation_file_name):
        eval_df.to_csv('evaluation/model_eval.csv', mode='a', index=False, header=False)
    else:
        eval_df.to_csv('evaluation/model_eval.csv', index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Model evaluation')
    parser.add_argument('--batch', type=int, default=1, help='Test batch number')
    parser.add_argument('--model', type=str, default='model_1.0.pkl', help='Model name')
    args = parser.parse_args()
    go(args)

# to call from CLI type e.g.: $ python 1.\ evaluate.py --batch 3 --model model_1.1.pkl