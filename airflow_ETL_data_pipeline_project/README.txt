
This is a project building ETL data pipeline using Apache airflow.


ETL data pipeline structure:

Extraction:     Extract the stock data of APPL from yahoo finance
     |
     V
Transformation: Extract the "Close price" and "Volume" column in the data
                Append a new column called SMA3 which is the simple moving average (3 days) of the "Close price"
     |
     V
Load:           Load the data to the Amazon S3 where a bucket is created and send a data copy to the email



Mainly package and application used:
yfinance (download the stock data from yahoo finance)
Airflow (building the dag and performing scheduled execution)
Amazon S3 (where the extracted data is loaded to)



Code file:

DAG_FOR_Extract_And_transform.py: Code defining the dag which is responsible for extracting and transforming section

yfinance_input.py:                Code for extracting the stock data of "APPL" from yahoo finance

transformation_of_data.py:        Code for extracting the "Close price" and "Volume" from data and append the SMA3
                                  column to the data

DAG_FOR_LOAD.py:                  Code defining the dag which is responsible for loading the transformed data to
                                  amazon S3 and send email

LOAD_TO_AMAZON_S3:                 Code for loading the transformed data to amazon S3



Airflow related file:.env
                      airflow.cfg


Docker related file: docker-compose.yaml
                     Dockerfile
                     requirement.txt




