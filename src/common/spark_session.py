from pyspark.sql import SparkSession

def obter_sessao_spark(nome_aplicacao="Data Pipeline"):
    """
    Cria e retorna um SparkSession com configurações úteis (ex.: conector Snowflake)
    """
    return SparkSession.builder \
        .appName(nome_aplicacao) \
        .config("spark.jars.packages", "net.snowflake:snowflake-jdbc:3.13.23,net.snowflake:spark-snowflake_2.12:2.11.0-spark_3.3") \
        .config("spark.sql.execution.arrow.enabled", "true") \
        .getOrCreate()