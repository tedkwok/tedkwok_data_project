from airflow import DAG
from airflow.operators.email import EmailOperator
from airflow.operators.python import PythonOperator
from airflow.sensors.external_task import ExternalTaskSensor
from airflow.operators.empty import EmptyOperator
from datetime import timedelta, datetime
from LOAD_TO_AMAZON_S3 import load_to_s3


default_args={
    'owner': 'ted',
    'retries': 3,
    'retry_delay': timedelta(minutes=3)
}
with DAG(
    dag_id = "DAG_FOR_LOAD",
    default_args=default_args,
    description="This is dag for Loading",
    schedule="@once",
    start_date=datetime(2024,7,1)
)as dag:
    start_task = EmptyOperator(task_id="start_task")
    end_task = EmptyOperator(task_id="end_task")



    Send_Email = EmailOperator(
        task_id = "email",
        to= "receivedairflow@myyahoo.com",
        conn_id="email",
        subject= "AAPL stock data",
        html_content="The APPL stock data file is attached below",
        files = ["Input_File/APPL.csv"],
        dag=dag
    )

    Load_file_to_s3 = PythonOperator(
        task_id = "load_s3",
        python_callable = load_to_s3,
        op_kwargs= {"filename":"Input_File/APPL.csv" , "key":"APPL_data_airflow_project", "bucket_name":"python-airflow-project"},
        dag=dag
    )



    start_task >> Load_file_to_s3 >>Send_Email >> end_task


