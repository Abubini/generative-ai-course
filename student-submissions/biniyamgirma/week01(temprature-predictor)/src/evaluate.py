import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_absolute_error, classification_report
from sklearn.model_selection import train_test_split
import os

def evaluate_models():
    # Regression evaluation
    reg_df = pd.read_csv("data/processed/regression_data.csv")
    X_reg = reg_df.drop('Temperature (C)', axis=1)
    y_reg = reg_df['Temperature (C)']
    X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
        X_reg, y_reg, test_size=0.2, random_state=42
    )
    
    os.makedirs("visuals/regression", exist_ok=True)
    
    for model_name in ['linear_regression_model', 'decision_tree_model']:
        model = joblib.load(f"models/regression/{model_name}.pkl")
        y_pred = model.predict(X_test_reg)
        
        # Plot
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=y_test_reg, y=y_pred)
        plt.title(f'Actual vs Predicted ({model_name})')
        plt.savefig(f"visuals/regression/{model_name}_eval.png")
        plt.close()
        
        print(f"\n{model_name} Evaluation:")
        print(f"MAE: {mean_absolute_error(y_test_reg, y_pred):.2f}°C")
    
    # Classification evaluation
    clf_df = pd.read_csv("data/processed/classification_data.csv")
    X_clf = clf_df.drop(['Summary', 'Precip Type', 'Summary_encoded', 'Precip_encoded'], axis=1)
    y_clf_summary = clf_df['Summary_encoded']
    y_clf_precip = clf_df['Precip_encoded']
    X_train_clf, X_test_clf, y_train_summary, y_test_summary, y_train_precip, y_test_precip = train_test_split(
        X_clf, y_clf_summary, y_clf_precip, test_size=0.2, random_state=42
    )
    
    os.makedirs("visuals/classification", exist_ok=True)
    le_summary = joblib.load("models/classification/label_encoder_summary.pkl")
    le_precip = joblib.load("models/classification/label_encoder_precip.pkl")
    
    # Summary evaluation - Handle potential missing classes
    rf_summary = joblib.load("models/classification/random_forest_summary.pkl")
    y_pred_summary = rf_summary.predict(X_test_clf)
    
    # Get all possible classes from the label encoder
    all_summary_classes = le_summary.classes_
    
    print("\nWeather Summary Classification Report:")
    print(classification_report(
        y_test_summary,
        y_pred_summary,
        labels=range(len(all_summary_classes)),
        target_names=all_summary_classes,
        zero_division=0
    ))
    
    # Precipitation evaluation
    xgb_precip = joblib.load("models/classification/xgboost_precip.pkl")
    y_pred_precip = xgb_precip.predict(X_test_clf)
    
    print("\nPrecipitation Type Classification Report:")
    print(classification_report(
        y_test_precip,
        y_pred_precip,
        target_names=le_precip.classes_,
        zero_division=0
    ))

if __name__ == "__main__":
    evaluate_models()