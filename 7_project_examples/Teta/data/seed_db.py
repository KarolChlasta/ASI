import pandas as pd
import sqlite3

csv_file_path = "./mushrooms.csv"
database_file_path = "./mushrooms.db"
df = pd.read_csv(csv_file_path)
connection = sqlite3.connect(database_file_path)
df.to_sql("mushrooms", connection, index=False, if_exists="replace")
connection.commit()
connection.close()
