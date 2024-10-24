import joblib
import pandas as pd
from database.db_utils import load_data

model = joblib.load('models/best_model_Random_Forest.pkl')

def predict_and_save_score(data):
    """
    Perform the prediction and save the score in the database.

    Args:
        data (dict): Data received from the Kafka consumer.
    """
    df = pd.DataFrame([data])  

    score = model.predict(df) 

    df['score_predicted'] = score


    load_data(df)