# 🌡️ Temperature Predictor Capstone Project

Welcome to the **Temperature Predictor** project, a comprehensive machine learning pipeline for weather prediction. This repository demonstrates the full workflow: from data preprocessing and exploratory analysis, through model training and evaluation, to interactive and command-line prediction interfaces.

---

## 📁 Project Structure

```
week01(temprature-predictor)/
│
├── README.md                  # Project documentation (this file)
├── requirements.txt           # Python dependencies
│
├── app/                       # Application interfaces (CLI & Streamlit)
│   ├── __init.py
│   ├── cli_forecast.py        # CLI for forecasting
│   ├── cli_predict.py         # CLI for single predictions
│   ├── main.py                # Streamlit web app
│   ├── components/            # Streamlit UI components
│   └── utils/                 # App-specific utilities
│
├── assets/                    # Static assets for the app
│   ├── styles.css             # Custom CSS styles
│   └── icons/                 # Weather icons
│
├── data/                      # Data files
│   ├── weatherHistory.csv     # Raw weather data
│   ├── processed_temperatures.csv # Cleaned data
│   ├── processed/             # Intermediate processed data
│
├── models/                    # Trained models
│   ├── classification/        # Classification models & encoders
│   └── regression/            # Regression models
│
├── notebooks/                 # Jupyter notebooks for EDA & modeling
│   ├── eda.ipynb
│   └── model_training.ipynb
│
├── src/                       # Core source code
│   ├── __init__.py
│   ├── classify.py            # Classification logic
│   ├── evaluate.py            # Model evaluation & visualization
│   ├── predict.py             # Prediction utilities
│   ├── preprocess.py          # Data cleaning & feature engineering
│   └── train.py               # Model training scripts
│
└── visuals/                   # Generated plots and figures
    ├── actual_vs_predicted_decision_tree.png
    ├── actual_vs_predicted_linear_regression.png
    └── ...
```

---

## 📝 Features

- **Data Preprocessing:** Cleans, transforms, and engineers features from raw weather data.
- **Exploratory Data Analysis:** Interactive Jupyter notebooks for data exploration and visualization.
- **Model Training:** Supports both regression (temperature prediction) and classification (weather summary, precipitation).
- **Model Evaluation:** Generates performance metrics and visualizations.
- **Interactive Web App:** User-friendly Streamlit interface for real-time predictions.
- **Command-Line Tools:** CLI scripts for batch and single predictions.
- **Reusable Modules:** Modular codebase for easy extension and maintenance.
- **Rich Visualizations:** Output plots for model diagnostics and results.

---

## ⚙️ Requirements

- **Python:** 3.8 or higher (tested on 3.10)
- **Core Libraries:**  
  - pandas, numpy, scikit-learn, matplotlib, seaborn, streamlit, joblib, click, etc.
- See [`requirements.txt`](requirements.txt) for the full list.

---

## 🚀 Setup & Installation

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd generative-ai-course/student-submissions/biniyamgirma/week01(temprature-predictor)
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🛠️ Usage Guide

### 1. **Data Preprocessing**
Preprocess raw data for modeling:
```bash
python src/preprocess.py
```

### 2. **Model Training**
Train regression and classification models:
```bash
python src/train.py
```

### 3. **Model Evaluation**
Generate evaluation metrics and plots:
```bash
python src/evaluate.py
```

### 4. **Interactive Web App**
Launch the Streamlit app for interactive predictions:
```bash
streamlit run app/main.py
```

### 5. **Command-Line Prediction**
Make predictions directly from the terminal:
```bash
python -m app.cli_predict
```

### 6. **Batch Forecasting**
For batch or time-series forecasting:
```bash
python -m app.cli_forecast
```

### 7. **Jupyter Notebooks**
Explore data and models interactively:
```bash
jupyter notebook notebooks/eda.ipynb
jupyter notebook notebooks/model_training.ipynb
```

---

## 📊 Visual Results

Sample outputs from the `visuals/` directory:

### Actual vs Predicted (Linear Regression)
![Linear Regression](visuals/actual_vs_predicted_linear_regression.png)

### Actual vs Predicted (Decision Tree)
![Decision Tree](visuals/actual_vs_predicted_decision_tree.png)

---

## 📂 File & Module Details

- **app/**: All user interfaces (CLI and Streamlit), UI components, and app utilities.
- **assets/**: Custom styles and icons for the web app.
- **data/**: Raw and processed datasets.
- **models/**: Serialized models and encoders for both regression and classification.
- **notebooks/**: Step-by-step EDA and model development.
- **src/**: Core logic for preprocessing, training, prediction, and evaluation.
- **visuals/**: Diagnostic and result plots.

---

## 🧩 Extending the Project

- Add new features by creating modules in `src/` and updating the app interfaces.
- Train and evaluate new models by modifying `train.py` and `evaluate.py`.
- Add new CLI commands in `app/cli_predict.py` or `app/cli_forecast.py`.

---

## 📝 Notes

- Always activate your virtual environment before running scripts.
- Ensure all dependencies are installed.
- For custom predictions, use the CLI or Streamlit app.
- Visualizations are auto-generated after evaluation.

---

## 🏆 Learning Outcomes

- Data cleaning and feature engineering
- Regression and classification modeling
- Model evaluation and visualization
- Interactive and CLI-based prediction interfaces
- Modular and maintainable codebase

---

## 🤝 Contributing

Pull requests are welcome! Please follow the PR template and ensure all code follows style guidelines.

---

## 📧 Support

For questions or issues, please contact the course instructors or open a GitHub issue.

---