import os
import subprocess
from typing import List
from api.model.DataSetModel import KedroDataSet
import sqlite3


def run(env_name: str, wandb_key: str):
    print('run', env_name, wandb_key)
    cwd = os.getcwd() + "\\asi-kedro"
    res = subprocess.run(f"cd {cwd} & conda activate {env_name} & wandb login {wandb_key} & kedro run", shell=True)
    print(res)


def wrapping_sqlite(raw_data: List) -> List[KedroDataSet]:
    res = []

    for row in raw_data:
        i=0
        res.append(KedroDataSet(
            ph=None if row[0] is None else float(row[0]),
            Hardness=None if row[1] is None else float(row[1]),
            Solids=None if row[2] is None else float(row[2]),
            Chloramines=None if row[3] is None else float(row[3]),
            Sulfate=None if row[4] is None else float(row[4]),
            Conductivity=None if row[5] is None else float(row[5]),
            Organic_carbon=None if row[6] is None else float(row[6]),
            Trihalomethanes=None if row[7] is None else float(row[7]),
            Turbidity=None if row[8] is None else float(row[8]),
            Potability=None if row[9] is None else float(row[9])
        ))

    return res


def get_data_from_sqlite(table_name: str) -> List:
    sql = f"SELECT * FROM {table_name};"
    if os.getenv('test', 'False') == 'True':
        sql = sql.replace(';', ' LIMIT 100;')

    conn = sqlite3.connect('./asi-kedro/sqlite/database.db')
    cursor = conn.cursor().execute(sql)
    data = cursor.fetchall()

    conn.close()
    return data


def get_raw_data() -> List[KedroDataSet]:
    raw_data = get_data_from_sqlite('raw_data')

    return wrapping_sqlite(raw_data)


def get_test_data() -> List[KedroDataSet]:
    raw_data = get_data_from_sqlite('test_data')

    return wrapping_sqlite(raw_data)

def get_train_data() -> List[KedroDataSet]:
    raw_date = get_data_from_sqlite('train_data')

    return wrapping_sqlite(raw_date)

def get_synth_data() -> List[KedroDataSet]:
    synth_data = get_data_from_sqlite('synth_data')

    return wrapping_sqlite(synth_data)
