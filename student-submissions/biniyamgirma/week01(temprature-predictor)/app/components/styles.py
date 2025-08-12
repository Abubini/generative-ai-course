import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
        /* Main landscape layout */
        .stApp {
            background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
            color: white;
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        /* Input section */
        .input-section {
            background: rgba(20, 20, 40, 0.7);
            padding: 1.5rem;
            border-radius: 15px;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);
            backdrop-filter: blur(5px);
        }
        
        /* Output section */
        .output-section {
            padding: 0 1.5rem;
        }
        
        /* Cards */
        .result-card {
            background: rgba(30, 30, 50, 0.7);
            border-radius: 15px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            border-left: 5px solid #00d2ff;
            box-shadow: 0 4px 20px rgba(0, 210, 255, 0.2);
            transition: all 0.3s ease;
            width: 100%;
        }
        
        /* Header */
        .header {
            background: linear-gradient(90deg, #00d2ff 0%, #3a47d5 100%);
            padding: 1.5rem;
            border-radius: 15px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 20px rgba(0, 210, 255, 0.3);
            text-align: center;
        }
        
        /* Sliders */
        .stSlider {
            background: rgba(30, 30, 50, 0.7) !important;
            border-radius: 10px !important;
            padding: 15px !important;
            margin-bottom: 1rem !important;
        }
        
        /* Button */
        .stButton>button {
            background: linear-gradient(90deg, #00d2ff 0%, #3a47d5 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 12px 24px !important;
            font-size: 1rem !important;
            transition: all 0.3s ease !important;
            margin-top: 1.5rem !important;
        }
    </style>
    """, unsafe_allow_html=True)