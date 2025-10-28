from pyspark.sql import SparkSession
from src.common.spark_session import obter_sessao_spark
from src.common.logger import obter_logger
import os

logger = obter_logger(__name__)

def ingerir_dados():
    """
    Ingerir dados das fontes para o data lake
    """
    try:
        # Obtém sessão Spark
        spark = obter_sessao_spark()

        # Caminho fonte (editar conforme fonte real)
        caminho_origem = os.path.join('data', 'raw')

        # Leitura (exemplo CSV)
        df = spark.read.csv(
            caminho_origem,
            header=True,
            inferSchema=True
        )

        # Salva como parquet na zona processed
        caminho_processado = os.path.join('data', 'processed', 'raw_data')
        df.write.mode('overwrite').parquet(caminho_processado)

        logger.info(f"Ingestão concluída em {caminho_processado}")

    except Exception as e:
        logger.error(f"Erro na ingestão: {str(e)}")
        raise e

if __name__ == "__main__":
    ingerir_dados()