import streamlit as st

def show_header():
    st.markdown("""
    <style>
        .header {
            background: linear-gradient(90deg, #00d2ff 0%, #3a47d5 100%);
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 20px rgba(0, 210, 255, 0.3);
        }
        .header h1 {
            color: white;
            text-align: center;
            font-size: 2.5rem;
            margin: 0;
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.7);
        }
        .header p {
            color: rgba(255, 255, 255, 0.9);
            text-align: center;
            margin: 0.5rem 0 0;
        }
    </style>
    
    <div class="header">
        <h1>🌡️ WEATHER FORECAST AI</h1>
        <p>Advanced machine learning-powered weather prediction system</p>
    </div>
    """, unsafe_allow_html=True)