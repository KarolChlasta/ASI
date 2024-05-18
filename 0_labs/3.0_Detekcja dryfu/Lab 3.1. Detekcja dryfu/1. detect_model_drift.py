from pickle import TRUE
import numpy as np
import pandas as pd
from datetime import date, datetime
import os.path

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)

# Read model evaluation results
eval_results = pd.read_csv('evaluation/model_eval.csv', parse_dates=['time_stamp'], dayfirst=True)

last_run = eval_results['time_stamp'].max()

# Prepare data for tests
RMSE_logs = eval_results[eval_results['metric']=='RMSE']
r2_logs = eval_results[eval_results['metric']=='r2']

last_RMSE = RMSE_logs[RMSE_logs['time_stamp']==last_run]['score'].values[0]
all_other_RMSE = RMSE_logs[RMSE_logs['time_stamp']!=last_run]['score'].values

last_r2 = r2_logs[r2_logs['time_stamp']==last_run]['score'].values[0]
all_other_r2 = r2_logs[r2_logs['time_stamp']!=last_run]['score'].values


### Hard test ###

# For RMSE, we identify drift (print TRUE) if the new RMSE is larger than the mean of all the past RMSE
hard_test_RMSE = last_RMSE > np.mean(all_other_RMSE)
# it obviously may be set as a fixed value, like
# hard_test_RMSE = last_RMSE > 1.0

# For r2, we identify drift (print TRUE) if the new R2 is smaller than the mean of all the past r2
hard_test_r2 = last_r2 < np.mean(all_other_r2)
# it obviously may be set as a fixed value, like
# hard_test_r2 = last_r2 < 0.7

print('\nLegend: \nTRUE means the model has drifted. FALSE means the model has not.')

print('\n.. Hard test ..')
print('RMSE: ', hard_test_RMSE, '  R2: ', hard_test_r2)


### Parametric test ###
# For RMSE, we identify drift (print TRUE) if the new RMSE is larger than the mean of all the past RMSE + 2*std of all the past RMSE
param_test_RMSE = last_RMSE > np.mean(all_other_RMSE) + 2*np.std(all_other_RMSE)

# For r2, we identify drift (print TRUE) if the new R2 is smaller than the mean of all the past r2 - 2*std of all the past r2
param_test_r2 = last_r2 < np.mean(all_other_r2) - 2*np.std(all_other_r2)

print('\n.. Parametric test ..')
print('RMSE: ', param_test_RMSE, '  R2: ', param_test_r2)


### Non-parametric (IQR) test ###
# For RMSE, we identify drift (print TRUE) if the new RMSE is larger than the 3rd quantile + 1.5 IQR
# ... YOUR CODE HERE - start ...
iqr_RMSE = np.quantile(all_other_RMSE, 0.75) - np.quantile(all_other_RMSE, 0.25)
iqr_test_RMSE = last_RMSE > np.quantile(all_other_RMSE, 0.75) + iqr_RMSE*1.5
# ... YOUR CODE HERE - end ...

# For r2, we identify drift (print TRUE) if the new R2 is smaller than than the 1st quantile - 1.5 IQR
# ... YOUR CODE HERE - start ...
iqr_r2 = np.quantile(all_other_r2, 0.75) - np.quantile(all_other_r2, 0.25)
iqr_test_r2 = last_r2 < np.quantile(all_other_r2, 0.25) - iqr_r2*1.5

# Print test results

# ... YOUR CODE HERE - end ...


# Re-training signal
print('\n  --- DRIFT DETECTION ---')
# ... YOUR CODE HERE - start ...

# create a set of drift detection signals
actual_tests = {...}

a_set = set(actual_tests.values())
if True in set(actual_tests.values()):
    drift_detected = TRUE

# in case of drift_detected is TRUE:
# print the drift detection signal on the screen



# save the drift detection signal to a file



# ... YOUR CODE HERE - end ...



