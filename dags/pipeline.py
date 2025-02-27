from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

sys.path.append('/opt/airflow/scripts')  # Adiciona o diretório dos scripts ao path

from generate_files import generate_data
from etl import run_etl  # Importa a função principal do ETL

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 26),
    'retries': 1,
    #'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'xl_etl_pipeline',
    default_args=default_args,
    description='Pipeline ETL para processar arquivos Excel',
    schedule_interval=None,
    catchup=False,
)

generate_files = PythonOperator(
    task_id='gen_data',
    python_callable=generate_data,
    dag=dag,
)

run_etl = PythonOperator(
    task_id='run_etl',
    python_callable=run_etl,
    dag=dag,
)

generate_files >> run_etl
