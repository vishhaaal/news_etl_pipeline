import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from news_fetcher import runner
from s3_store import extract_and_stage_to_s3

default_args = {
    'owner' : 'vishal',
    'depends_on_past' : False,
    'start_date' : datetime(2023,12,5),
    'retries' : 5,
    'retry_delay' : timedelta(minutes = 2)
}
with DAG(
    dag_id = 'weather_api',
    default_args = default_args,
    schedule_interval = '@daily',
    catchup = False
)as dag:
    extract_news_info = PythonOperator(
        task_id = 'extract_news_info',
        python_callable = runner,
        dag = dag
    )

    stage_to_s3_task = PythonOperator(
        task_id='stage_to_s3_task',
        python_callable=extract_and_stage_to_s3
    )

    snowflake_create_table = SnowflakeOperator(
        task_id = 'snowflake_create_table',
        sql ="""create table if not exists parquetdata using template(select ARRAY_AGG(OBJECT_CONSTRUCT(*)) from TABLE(INFER_SCHEMA (LOCATION=>'@PIPELINE.PUBLIC.stage_area',FILE_FORMAT=>'parquet_format')))""",
        snowflake_conn_id = 'snowflake_conn'
    )

    snowflake_copy = SnowflakeOperator(
        task_id = 'snowflake_copy',
        sql = """copy into PIPELINE.PUBLIC.parquetdata from @PIPELINE.PUBLIC.stage_area MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE FILE_FORMAT = parquet_format""",
        snowflake_conn_id = 'snowflake_conn'
    )

extract_news_info >> stage_to_s3_task >> snowflake_create_table >> snowflake_copy