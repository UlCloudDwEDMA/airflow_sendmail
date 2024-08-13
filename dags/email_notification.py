from airflow import DAG
#from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
 
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 3, 20), 
    'retry_delay' : timedelta(seconds=5),
    'email': ['ramesh.babuv@ul.com'], 
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1
}

with DAG(
    dag_id='rb_email_test_failure',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
) as dag:
    task_failure = BashOperator(
        task_id='task_failure',
        bash_command="cd non_exist_folder"
    )
