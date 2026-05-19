from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
'rag_pipeline',
start_date=datetime(2025,1,1),
schedule='@daily',
catchup=False
) as dag:

    ingest=BashOperator(
    task_id='load_docs',
    bash_command='python ingestion/load_documents.py'
    )

    embedding=BashOperator(
    task_id='create_embeddings',
    bash_command='python processing/create_embeddings.py'
    )

    retrieve=BashOperator(
    task_id='query_pipeline',
    bash_command='python retrieval/rag_query.py'
    )

ingest>>embedding>>retrieve
