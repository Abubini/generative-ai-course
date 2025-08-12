import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from datetime import datetime
import os

def preprocess_data():
    # Load raw data
    df = pd.read_csv("./data/weatherHistory.csv")
    
    # Handle missing values
    df = df.dropna(subset=['Precip Type'])  # Critical for classification
    
    # Feature engineering
    df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], utc=True)
    df['month'] = df['Formatted Date'].dt.month
    df['hour'] = df['Formatted Date'].dt.hour
    
    # Create regression dataset
    regression_features = [
        'Apparent Temperature (C)', 'Humidity', 'Wind Speed (km/h)', 
        'Wind Bearing (degrees)', 'Visibility (km)', 'Pressure (millibars)',
        'month', 'hour'
    ]
    regression_df = df[regression_features + ['Temperature (C)']]
    
    # Create classification dataset
    classification_features = [
        'Temperature (C)', 'Humidity', 'Wind Speed (km/h)', 
        'Pressure (millibars)', 'month', 'Apparent Temperature (C)'
    ]
    classification_df = df[classification_features + ['Summary', 'Precip Type']]
    
    # Encode categorical targets
    le_summary = LabelEncoder()
    le_precip = LabelEncoder()
    classification_df['Summary_encoded'] = le_summary.fit_transform(classification_df['Summary'])
    classification_df['Precip_encoded'] = le_precip.fit_transform(classification_df['Precip Type'])
    
    # Save processed data
    os.makedirs("data/processed", exist_ok=True)
    regression_df.to_csv("data/processed/regression_data.csv", index=False)
    classification_df.to_csv("data/processed/classification_data.csv", index=False)
    
    # Save encoders
    os.makedirs("models/classification", exist_ok=True)
    joblib.dump(le_summary, "models/classification/label_encoder_summary.pkl")
    joblib.dump(le_precip, "models/classification/label_encoder_precip.pkl")
    
    return regression_df, classification_df

if __name__ == "__main__":
    preprocess_data()