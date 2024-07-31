from datetime import timedelta
#from airflow import DAG
#from airflow.operators.python_operator import PythonOperator
#from airflow.utils.dates import days_ago
from datetime import datetime
from producer import producer_etl

default_args = {
    'owner': 'chisom',
    'depends_on_past': False,
    'start_date': datetime(2024, 7, 31),
    'email': ['chisomnwokwu09@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'producer_dag',
    default_args=default_args,
    description='Dag to run producer script',
    schedule_interval='@once'
)

run_etl = PythonOperator(
    task_id='run_producer_etl',
    python_callable=producer_etl,
    dag=dag, 
)

run_etl