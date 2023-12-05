from airflow.hooks.S3_hook import S3Hook

def extract_and_stage_to_s3(**kwargs):
    ti = kwargs['ti']
    output_file = ti.xcom_pull(task_ids='extract_news_info')      
    s3_hook = S3Hook(aws_conn_id='s3_conn')  
    s3_bucket_name = 'newsetldata'