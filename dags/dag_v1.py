from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from coinmarketcap_fetch_data import fetch_data
from transform_pandas import transform




with DAG(
    dag_id= 'dag_crypto_ETL',
    description= 'Fetching data and loading to a SQL server',
    start_date= datetime(2024, 2, 5, 14),
    schedule_interval='@daily', # CRON expression
    catchup=False
) as dag:

    api_task = PythonOperator(
    task_id='coinmarketcap_fetch_data',
    python_callable= fetch_data
    )

    transform_task = PythonOperator(
    task_id='transform_to_pandas',
    python_callable= transform
    )
    
    api_task >> transform_task


