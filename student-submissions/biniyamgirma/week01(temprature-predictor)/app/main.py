import streamlit as st
import pandas as pd
from datetime import datetime
from components.header import show_header
from components.inputs import show_inputs
from components.results import show_results
from components.styles import apply_custom_styles
from utils.load_models import load_models
from utils.weather_icons import get_weather_icon

def main():
    # Apply custom styles
    apply_custom_styles()
    
    # Load ML models
    models = load_models()
    
    # Show header
    show_header()
    
    # Initialize session state
    if 'prediction' not in st.session_state:
        st.session_state.prediction = None
    
    # Main landscape layout container
    st.markdown("""
    <style>
        .main-container {
            display: flex;
            flex-direction: row;
            gap: 2rem;
            margin-top: 1.5rem;
        }
        .input-section {
            width: 35%;
            padding-right: 2rem;
        }
        .output-section {
            width: 65%;
            padding-left: 1rem;
        }
        @media (max-width: 1200px) {
            .main-container {
                flex-direction: column;
            }
            .input-section, .output-section {
                width: 100%;
                padding: 0;
            }
        }
    </style>
    <div class="main-container">
    """, unsafe_allow_html=True)
    
    # Left Column - Input Section
    st.markdown('<div class="input-section">', unsafe_allow_html=True)
    user_inputs = show_inputs()
    
    # Prediction button with cool effect
    if st.button('**PREDICT WEATHER**', 
                use_container_width=True,
                type="primary",
                help="Analyze current conditions and predict weather"):
        with st.spinner('Analyzing atmospheric data...'):
            try:
                # Prepare input data with feature names for regression
                reg_input = pd.DataFrame([[
                    user_inputs['apparent_temp'],
                    user_inputs['humidity'],
                    user_inputs['wind_speed'],
                    user_inputs['wind_bearing'],
                    user_inputs['visibility'],
                    user_inputs['pressure'],
                    user_inputs['month'],
                    user_inputs['hour']
                ]], columns=[
                    'Apparent Temperature (C)',
                    'Humidity',
                    'Wind Speed (km/h)',
                    'Wind Bearing (degrees)',
                    'Visibility (km)',
                    'Pressure (millibars)',
                    'month',
                    'hour'
                ])
                
                # Make temperature prediction
                temp_pred = models['regression']['decision_tree'].predict(reg_input)[0]
                
                # Prepare input data for classification
                classif_input = pd.DataFrame([[
                    temp_pred,
                    user_inputs['humidity'],
                    user_inputs['wind_speed'],
                    user_inputs['pressure'],
                    user_inputs['month'],
                    user_inputs['apparent_temp']
                ]], columns=[
                    'Temperature (C)',
                    'Humidity',
                    'Wind Speed (km/h)',
                    'Pressure (millibars)',
                    'month',
                    'Apparent Temperature (C)'
                ])
                
                # Get weather predictions
                weather_code = models['classification']['summary'].predict(classif_input)[0]
                precip_code = models['classification']['precip'].predict(classif_input)[0]
                
                # Decode to text labels
                weather_label = models['classification']['summary_encoder'].inverse_transform([weather_code])[0]
                precip_label = models['classification']['precip_encoder'].inverse_transform([precip_code])[0]
                
                # Store prediction results
                st.session_state.prediction = {
                    'temperature': round(temp_pred, 1),
                    'weather': weather_label,
                    'precipitation': precip_label,
                    'icon': get_weather_icon(weather_label, precip_label),
                    'humidity': user_inputs['humidity'],
                    'pressure': user_inputs['pressure'],
                    'wind_speed': user_inputs['wind_speed'],
                    'apparent_temp': user_inputs['apparent_temp'],
                    'location': {
                        'lat': user_inputs['lat'],
                        'lon': user_inputs['lon']
                    },
                    'time': {
                        'month': user_inputs['month'],
                        'hour': user_inputs['hour']
                    }
                }
                
            except Exception as e:
                st.error(f"Prediction failed: {str(e)}")
                st.session_state.prediction = None
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close input section
    
    # Right Column - Output Section
    st.markdown('<div class="output-section">', unsafe_allow_html=True)
    if st.session_state.prediction:
        show_results(st.session_state.prediction)
    else:
        st.markdown("""
        <div class="placeholder-card">
            <h3>Weather Forecast</h3>
            <p>Enter parameters and click PREDICT to see results</p>
            <div class="scanning-animation"></div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)  # Close output section
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close main container

if __name__ == "__main__":
    main()