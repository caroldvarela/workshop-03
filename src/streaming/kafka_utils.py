from kafka import KafkaProducer, KafkaConsumer
from json import dumps, loads
from src.data_processing.feature_selection import prepare_data
from src.predictions.save_predictions import predict_and_save_score
import time
from database.db_utils import load_data
import pandas as pd

def kafka_producer():
    producer = KafkaProducer(
        value_serializer=lambda m: dumps(m).encode('utf-8'),
        bootstrap_servers=['localhost:9092'],
    )

    X_test, y_test = prepare_data()
    
    for index in range(len(X_test)):
        time.sleep(5)  
        row = X_test.iloc[index].to_dict()
        row['score'] = float(y_test.iloc[index])
        producer.send("kafka_workshop3", value=row)  
        print(f"Message sent: {row}")

    producer.flush() 

def kafka_consumer():
    consumer = KafkaConsumer(
        'kafka_workshop3',
        #auto_offset_reset='lastest',
        enable_auto_commit=True,
        group_id='my-group-1',
        value_deserializer=lambda m: loads(m.decode('utf-8')),
        bootstrap_servers=['localhost:9092']
    )

    try:
        for m in consumer:
            print(f"Message received: {m.value}")
            data = m.value
            original_score = data.pop('score', None)
            df = predict_and_save_score(data)
            df['score'] = original_score
            load_data(df)
    except Exception as e:
        print(f"Error: {e}")
