import logging
import os

def obter_logger(nome):
    """
    Cria e retorna um logger com configuração padrão
    """
    # Diretório de logs
    dir_logs = os.path.join('data', 'logs')
    os.makedirs(dir_logs, exist_ok=True)

    # Criar logger
    logger = logging.getLogger(nome)
    logger.setLevel(logging.INFO)

    # Formatação
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Handler de arquivo
    handler_arquivo = logging.FileHandler(
        os.path.join(dir_logs, 'pipeline.log')
    )
    handler_arquivo.setLevel(logging.INFO)
    handler_arquivo.setFormatter(formatter)

    # Handler de console
    handler_console = logging.StreamHandler()
    handler_console.setLevel(logging.INFO)
    handler_console.setFormatter(formatter)

    # Adiciona handlers (cuidado para não duplicar em execuções repetidas)
    logger.addHandler(handler_arquivo)
    logger.addHandler(handler_console)

    return logger