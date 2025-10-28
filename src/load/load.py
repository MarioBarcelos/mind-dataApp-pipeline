from src.common.snowflake_connection import obter_conexao_snowflake
from src.common.spark_session import obter_sessao_spark
from src.common.logger import obter_logger
import os

logger = obter_logger(__name__)

def carregar_para_snowflake():
    """
    Carrega os dados transformados para o Snowflake
    """
    try:
        # Obtém sessão Spark
        spark = obter_sessao_spark()

        # Lê dados transformados
        caminho_entrada = os.path.join('data', 'processed', 'transformed_data')
        df = spark.read.parquet(caminho_entrada)

        # Obtém opções de conexão
        opcoes_snowflake = obter_conexao_snowflake()

        # Grava no Snowflake
        df.write \
            .format('snowflake') \
            .options(**opcoes_snowflake) \
            .option('dbtable', 'transformed_data') \
            .mode('overwrite') \
            .save()

        logger.info('Carga para Snowflake concluída')

    except Exception as e:
        logger.error(f"Erro na carga para Snowflake: {str(e)}")
        raise e

if __name__ == "__main__":
    carregar_para_snowflake()