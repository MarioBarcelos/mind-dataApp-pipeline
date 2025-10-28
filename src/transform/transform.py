from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from src.common.spark_session import obter_sessao_spark
from src.common.logger import obter_logger
import os

logger = obter_logger(__name__)

def transformar_dados():
    """
    Transformar dados usando Spark
    """
    try:
        # Obtém sessão Spark
        spark = obter_sessao_spark()

        # Lê dados da zona processed
        caminho_entrada = os.path.join('data', 'processed', 'raw_data')
        df = spark.read.parquet(caminho_entrada)

        # Exemplo de transformação: adiciona timestamp de processamento
        df_transformado = df.withColumn(
            'processed_timestamp',
            current_timestamp()
        )

        # Salva dados transformados
        caminho_saida = os.path.join('data', 'processed', 'transformed_data')
        df_transformado.write.mode('overwrite').parquet(caminho_saida)

        logger.info(f"Transformação concluída e salva em {caminho_saida}")

    except Exception as e:
        logger.error(f"Erro na transformação: {str(e)}")
        raise e

if __name__ == "__main__":
    transformar_dados()