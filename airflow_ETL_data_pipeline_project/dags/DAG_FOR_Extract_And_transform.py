from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from transformation_of_data import transformation

from yfinance_input import import_data


default_args={
    'owner': 'ted',
    'retries': 3,
    'retry_delay': timedelta(minutes=3)
}
with DAG(
    dag_id="Extract_and_transformation_DAG",
    default_args=default_args,
    description="This is dag for Extract and Transformation",
    schedule_interval='@daily',
    start_date = datetime(2024,7,1)

)as dag:

    start_task=EmptyOperator(task_id="start_task")
    end_task=EmptyOperator(task_id="end_task")

    extract = PythonOperator(
        task_id="read_data_from_yahoo",
        python_callable=import_data,
        op_kwargs={'start': datetime(2023,5,6).strftime('%Y-%m-%d'), 'end': datetime.today().strftime('%Y-%m-%d')},
        dag=dag)

    transform = PythonOperator(
        task_id="transformation_of_the_data",
        python_callable=transformation,
        dag=dag
    )

    start_task >> extract >> transform >> end_task







