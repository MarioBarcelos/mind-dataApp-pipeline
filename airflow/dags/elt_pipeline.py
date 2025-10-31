from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from datetime import datetime, timedelta
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from src.extract.ingest import ingerir_dados
from src.transform.transform import transformar_dados
from src.load.load import carregar_para_snowflake

argumentos_padrao = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag_elt = DAG(
    'elt_pipeline',
    default_args=argumentos_padrao,
    description='Pipelina ELT',
    schedule_interval='@daily',
    catchup=False
)

#tarefa de extração
tarefa_extracao = PythonOperator(
    task_id='extracao',
    python_callable=ingerir_dados,
    dag=dag_elt
)

#tarefa de carga
tarefa_carga = PythonOperator(
    task_id='cargaDL',
    python_callable=carregar_para_snowflake,
    dag=dag_elt
)

#tarefa de transformação
tarefa_transformacao = PythonOperator(
    task_id='transformacao',
    python_callable=transformar_dados,
    dag=dag_elt
)


#tarefa DBT
tarefa_dbt = SnowflakeOperator(
    task_id='',
    snowflake_conn_id='',
    sql='',
    warehouse='',
    database='',
    dag=dag_elt
)

#dependências
tarefa_extracao >> tarefa_carga >> tarefa_transformacao >> tarefa_dbt