# Mind Data App Pipeline

Este é um projeto moderno de engenharia de dados que integra Airflow, PySpark, Snowflake e DBT para criar um pipeline de dados robusto e escalável.

## Arquitetura

O projeto segue uma arquitetura moderna de ELT (Extract, Load, Transform) com as seguintes características:

- **Airflow**: Orquestração e agendamento de tasks
- **PySpark**: Processamento distribuído para extração e transformação inicial
- **Snowflake**: Data Warehouse para armazenamento e processamento
- **DBT**: Transformações e modelagem de dados no Snowflake

## Estrutura do Projeto

```
mind-dataApp-pipeline/
├── airflow/                     # Configuração e DAGs do Airflow
├── src/                         # Código fonte do pipeline
├── dbt/                         # Projeto DBT para transformações
├── data/                        # Dados locais e logs
└── tests/                       # Testes unitários e de integração
```

## Pré-requisitos

- Docker e Docker Compose
- Python 3.8+
- Java 8+ (para Spark)
- Conta no Snowflake

Recomendação de gestão de ambiente

Este projeto recomenda usar Conda (Miniconda/Anaconda) para gerir o ambiente de desenvolvimento, pois facilita a instalação de pacotes nativos (como pyarrow e pyspark) no Windows e em ambientes de dados.

Instruções rápidas com Conda:

1. Instale Miniconda/Anaconda (se ainda não tiver).
2. Crie o ambiente a partir do arquivo `environment.yml` no root do projeto:

```powershell
conda env create -f .\environment.yml
conda activate mind-dataapp-pipeline
```

3. Caso precise de pacotes adicionais que não estejam no `environment.yml` (por exemplo DBT), instale-os após ativar o ambiente com `pip` ou `conda` conforme preferir. Exemplo via pip:

```powershell
pip install dbt-core dbt-snowflake
```

Observações:
- O `environment.yml` inclui `pyarrow` e `pyspark` via conda-forge para evitar builds nativos. Isso previne erros de compilação no Windows (ex.: erro CMake ao instalar pyarrow via pip).
- Mantemos uma cópia de backup das dependências antigas em `requirements.txt.bak` caso queira restaurar ou revisar versões específicas.

## Configuração

1. Clone o repositório:
   ```bash
   git clone [URL_DO_REPOSITÓRIO]
   cd mind-dataApp-pipeline
   ```

2. Configure as variáveis de ambiente:
   - Copie `src/config/env.yaml.example` para `src/config/env.yaml`
   - Atualize as configurações conforme seu ambiente

3. Configure as credenciais do Snowflake:
   - Atualize `src/config/snowflake_config.json` com suas credenciais
   - Atualize `dbt/profiles.yml` com suas configurações do Snowflake

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Executando o Pipeline

1. Inicie os serviços com Docker Compose:
   ```bash
   docker-compose up -d
   ```

2. Acesse o Airflow UI:
   - URL: http://localhost:8080
   - Default login: airflow/airflow

3. Ative o DAG `etl_pipeline` no Airflow UI

## Desenvolvimento

- **Extração**: Adicione novos conectores em `src/extract/`
- **Transformação**: Modifique lógicas Spark em `src/transform/`
- **Carregamento**: Ajuste configurações Snowflake em `src/load/`
- **Modelagem**: Desenvolva modelos DBT em `dbt/models/`

## Testes

Execute os testes unitários:
```bash
python -m pytest tests/
```

## Monitoramento

- Logs do pipeline: `data/logs/pipeline.log`
- Airflow UI: http://localhost:8080
- Spark UI: http://localhost:8888

## Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Crie um Pull Request

## Licença

[Sua licença aqui]