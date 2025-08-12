import joblib
import pandas as pd

class TemperaturePredictor:
    def __init__(self):
        self.models = {
            'linear_regression': joblib.load("models/regression/linear_regression_model.pkl"),
            'decision_tree': joblib.load("models/regression/decision_tree_model.pkl")
        }
    
    def predict_temperature(self, features, model_type='linear_regression'):
        """Predict temperature using specified model"""
        model = self.models.get(model_type)
        if not model:
            raise ValueError(f"Model {model_type} not found")
        
        input_df = pd.DataFrame([features])
        return model.predict(input_df)[0]

if __name__ == "__main__":
    predictor = TemperaturePredictor()
    example_features = {
        'Apparent Temperature (C)': 10.5,
        'Humidity': 0.8,
        'Wind Speed (km/h)': 12,
        'Wind Bearing (degrees)': 180,
        'Visibility (km)': 15,
        'Pressure (millibars)': 1012,
        'month': 6,
        'hour': 14
    }
    
    for model in ['linear_regression', 'decision_tree']:
        temp = predictor.predict_temperature(example_features, model)
        print(f"Predicted Temp ({model}): {temp:.1f}°C")