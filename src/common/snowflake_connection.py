import json
import os

def obter_conexao_snowflake():
    """
    Lê as credenciais de `src/config/snowflake_config.json` e retorna um dicionário
    com as opções esperadas pelo conector Spark->Snowflake.
    """
    cfg_path = os.path.join('src', 'config', 'snowflake_config.json')
    if not os.path.exists(cfg_path):
        raise FileNotFoundError(f"Arquivo de configuração Snowflake não encontrado: {cfg_path}")

    with open(cfg_path, 'r', encoding='utf-8') as f:
        cfg = json.load(f)

    # Mapeia para as chaves usadas pelo conector Snowflake para Spark
    return {
        'sfURL': cfg.get('url'),
        'sfUser': cfg.get('user'),
        'sfPassword': cfg.get('password'),
        'sfDatabase': cfg.get('database'),
        'sfSchema': cfg.get('schema'),
        'sfWarehouse': cfg.get('warehouse'),
        'sfRole': cfg.get('role')
    }
