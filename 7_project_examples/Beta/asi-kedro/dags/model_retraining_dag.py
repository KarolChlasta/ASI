# model_retraining_dag.py
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from kedro.config import ConfigLoader

conf_loader = ConfigLoader(conf_source="conf/local")
paths_conf = conf_loader.get("paths*")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

kedro_project_path = paths_conf["kedro_project_path"]
kedro_virtualenv_path = paths_conf["kedro_virtualenv_path"]

dag = DAG(
    'model_retraining',
    default_args=default_args,
    description='DAG for running Kedro model retraining pipeline',
    schedule_interval=timedelta(days=7),  # Adjust the interval as needed
)

run_retrain_pipeline_task = BashOperator(
    task_id='run_kedro_pipeline',
    bash_command=f'source {kedro_virtualenv_path}/bin/activate && '
                 f'cd {kedro_project_path} && '
                 f'kedro run --pipeline=model_retraining_pipeline',
    dag=dag,
)

# You can add more tasks and dependencies here if needed

run_retrain_pipeline_task  # Define the task as the end of the DAG
