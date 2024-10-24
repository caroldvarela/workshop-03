from kafka import KafkaProducer, KafkaConsumer
from json import dumps, loads
from src.data_processing.feature_selection import prepare_data
from src.predictions.save_predictions import predict_and_save_score
import time
import logging

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def kafka_producer():
    producer = KafkaProducer(
        value_serializer=lambda m: dumps(m).encode('utf-8'),
        bootstrap_servers=['localhost:9092'],
    )

    df = prepare_data()
    
    for index, row in df.iterrows():
        time.sleep(3)  
        producer.send("kafka_workshop3", value=row.to_dict()) 
        print(f"Message sent: {row.to_dict()}")

    producer.flush() 

def kafka_consumer():
    consumer = KafkaConsumer(
        'kafka_workshop3',
        auto_offset_reset='earliest',
        #enable_auto_commit=True,
        group_id='my-group-1',
        value_deserializer=lambda m: loads(m.decode('utf-8')),
        bootstrap_servers=['localhost:9092']
    )

    logging.info("Iniciando el consumidor...")

    for m in consumer:
        print(f"Message received: {m.value}")
        predict_and_save_score(m.value)

if __name__ == "__main__":
    kafka_producer()
    kafka_consumer()