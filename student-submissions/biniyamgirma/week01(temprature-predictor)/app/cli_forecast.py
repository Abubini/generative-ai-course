from src.predict import TemperaturePredictor
from src.classify import WeatherClassifier
import pandas as pd

def main():
    print("Weather Forecasting System")
    print("1. Predict Temperature")
    print("2. Full Weather Forecast")
    choice = input("Select option (1 or 2): ")
    
    # Common features
    features = {
        'Apparent Temperature (C)': float(input("Apparent Temperature (C): ")),
        'Humidity': float(input("Humidity (0-1): ")),
        'Wind Speed (km/h)': float(input("Wind Speed (km/h): ")),
        'Wind Bearing (degrees)': float(input("Wind Bearing (degrees): ")),
        'Visibility (km)': float(input("Visibility (km): ")),
        'Pressure (millibars)': float(input("Pressure (millibars): ")),
        'month': int(input("Month (1-12): ")),
        'hour': int(input("Hour (0-23): "))
    }
    
    if choice == '1':
        # Temperature prediction only
        model = input("Model (linear/decision): ").lower()
        model_type = 'linear_regression' if model.startswith('l') else 'decision_tree'
        
        predictor = TemperaturePredictor()
        temp = predictor.predict_temperature(features, model_type)
        print(f"\nPredicted Temperature: {temp:.1f}°C")
    
    else:
        # Full forecast
        model = input("Temperature model (linear/decision): ").lower()
        model_type = 'linear_regression' if model.startswith('l') else 'decision_tree'
        
        # Predict temperature
        predictor = TemperaturePredictor()
        temp = predictor.predict_temperature(features, model_type)
        
        # Prepare features for classification
        classifier = WeatherClassifier()
        weather_features = {
            'Temperature (C)': temp,
            'Humidity': features['Humidity'],
            'Wind Speed (km/h)': features['Wind Speed (km/h)'],
            'Pressure (millibars)': features['Pressure (millibars)'],
            'month': features['month'],
            'Apparent Temperature (C)': features['Apparent Temperature (C)']
        }
        
        # Predict weather
        forecast = classifier.predict_weather(weather_features)
        
        print("\n=== Weather Forecast ===")
        print(f"Temperature: {temp:.1f}°C")
        print(f"Weather: {forecast['summary']}")
        print(f"Precipitation: {forecast['precipitation']}")

if __name__ == "__main__":
    main()