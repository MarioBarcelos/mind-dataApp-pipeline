dbt_run = SnowflakeOperator(
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from datetime import datetime, timedelta
import sys
import os

# Adiciona o root do projeto ao path
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

dag_etl = DAG(
    'etl_pipeline',
    default_args=argumentos_padrao,
    description='Pipelina ETL usando Spark e DBT',
    schedule_interval='@daily',
    catchup=False
)

# Tarefa de extração
tarefa_extracao = PythonOperator(
    task_id='extracao',
    python_callable=ingerir_dados,
    dag=dag_etl
)

# Tarefa de transformação
tarefa_transformacao = PythonOperator(
    task_id='transformacao',
    python_callable=transformar_dados,
    dag=dag_etl
)

# Tarefa de carga
tarefa_carga = PythonOperator(
    task_id='carga',
    python_callable=carregar_para_snowflake,
    dag=dag_etl
)

# Tarefa DBT (exemplo usando operator Snowflake - ajuste conforme necessário)
tarefa_dbt = SnowflakeOperator(
    task_id='dbt_run',
    snowflake_conn_id='snowflake_conn',
    sql='dbt run',
    warehouse='COMPUTE_WH',
    database='YOUR_DATABASE',
    dag=dag_etl
)

# Dependências
tarefa_extracao >> tarefa_transformacao >> tarefa_carga >> tarefa_dbt