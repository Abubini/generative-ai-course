import joblib

def load_models():
    return {
        'regression': {
            'linear_regression': joblib.load('models/regression/linear_regression_model.pkl'),
            'decision_tree': joblib.load('models/regression/decision_tree_model.pkl')
        },
        'classification': {
            'summary': joblib.load('models/classification/random_forest_summary.pkl'),
            'precip': joblib.load('models/classification/xgboost_precip.pkl'),
            'summary_encoder': joblib.load('models/classification/label_encoder_summary.pkl'),
            'precip_encoder': joblib.load('models/classification/label_encoder_precip.pkl')
        }
    }