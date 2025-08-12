import streamlit as st
from datetime import datetime

def show_inputs():
    st.markdown("### 🌍 Location Data")
    col1, col2 = st.columns(2)
    with col1:
        lat = st.slider("Latitude", -90.0, 90.0, 37.7749, 0.1)
    with col2:
        lon = st.slider("Longitude", -180.0, 180.0, -122.4194, 0.1)
    
    st.markdown("### ⏳ Time Parameters")
    date_col, hour_col = st.columns(2)
    with date_col:
        date = st.date_input("Date", datetime.now())
    with hour_col:
        hour = st.slider("Hour", 0, 23, 12)
    
    st.markdown("### 🌡️ Weather Parameters")
    tab1, tab2 = st.tabs(["Basic", "Advanced"])
    
    with tab1:
        apparent_temp = st.slider("Apparent Temperature (C)", -20.0, 50.0, 20.0, 0.1)
        humidity = st.slider("Humidity (%)", 0.0, 100.0, 50.0, 0.1)
    
    with tab2:
        wind_speed = st.slider("Wind Speed (km/h)", 0.0, 100.0, 10.0, 0.1)
        wind_bearing = st.slider("Wind Direction", 0, 359, 180)
        visibility = st.slider("Visibility (km)", 0.0, 20.0, 10.0, 0.1)
        pressure = st.slider("Pressure (hPa)", 800.0, 1100.0, 1013.0, 0.1)
    
    return {
        'lat': lat,
        'lon': lon,
        'month': date.month,
        'hour': hour,
        'apparent_temp': apparent_temp,
        'humidity': humidity / 100,
        'wind_speed': wind_speed,
        'wind_bearing': wind_bearing,
        'visibility': visibility,
        'pressure': pressure
    }