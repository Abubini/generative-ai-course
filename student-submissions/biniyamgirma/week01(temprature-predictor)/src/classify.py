import joblib
import pandas as pd
import numpy as np

class WeatherClassifier:
    def __init__(self):
        self.summary_model = joblib.load("models/classification/random_forest_summary.pkl")
        self.precip_model = joblib.load("models/classification/xgboost_precip.pkl")
        self.le_summary = joblib.load("models/classification/label_encoder_summary.pkl")
        self.le_precip = joblib.load("models/classification/label_encoder_precip.pkl")
    
    def predict_weather(self, features):
        """Predict weather summary and precipitation type"""
        # Convert to DataFrame
        input_df = pd.DataFrame([features])
        
        # Predict
        summary_encoded = self.summary_model.predict(input_df)[0]
        precip_encoded = self.precip_model.predict(input_df)[0]
        
        # Decode
        summary = self.le_summary.inverse_transform([summary_encoded])[0]
        precip = self.le_precip.inverse_transform([precip_encoded])[0]
        
        return {
            'summary': summary,
            'precipitation': precip
        }

if __name__ == "__main__":
    # Example usage
    classifier = WeatherClassifier()
    example_features = {
        'Temperature (C)': 15.5,
        'Humidity': 0.7,
        'Wind Speed (km/h)': 12,
        'Pressure (millibars)': 1015,
        'month': 6,
        'Apparent Temperature (C)': 16.2
    }
    prediction = classifier.predict_weather(example_features)
    print(f"Weather Forecast: {prediction}")