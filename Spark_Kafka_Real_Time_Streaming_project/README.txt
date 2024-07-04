

This is project of building a real-time spark streaming.



Streaming structure:
extract real time stock data from yahoo finance --> pass to kafka topic --> pass to pyspark readstream --> pyspark writestream to file and console



Mainly Package used:
Beautiful Soup (for webscraping infomration from yahoo finance)
kafka          (passing the real time extracted data to kafka topic)
pyspark        (act as consumer of the topic and write the streaming data to console and data folder with format parquet)




Code file:

Extract_Stockdata_toKafka.ipynb: the code performing webscraping the real time data of price, Volume and TrailingPE of AAPL from yahoo finance and use kafka producer to pass     
                                 real time data to topic called streaming
                                 
Pyspark_handling_StreamData_from_kafka:the code performing the readstream from the topic streaming and save the data to data/streaming.parquet/ in parquet format
                                       
                                     

Docker file:

docker-compose.yml: This is a file for creating three container:
                     ed-kafka
                     ed-zookeeper
                     ed-pyspark-jupyter
                     
                     
