import pandas as pd

# Read data
df = pd.read_csv('data/data_init.csv')

# Save the data
df.to_csv('data/data_train.csv', index=False)