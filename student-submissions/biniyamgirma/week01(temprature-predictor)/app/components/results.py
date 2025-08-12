import streamlit as st
import plotly.express as px
import pandas as pd

def show_results(prediction):
    st.markdown(f"""
    <style>
        .result-card {{
            background: rgba(30, 30, 50, 0.7);
            border-radius: 15px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            border-left: 5px solid #00d2ff;
            box-shadow: 0 4px 20px rgba(0, 210, 255, 0.2);
            transition: all 0.3s ease;
        }}
        .result-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0, 210, 255, 0.3);
        }}
        .result-title {{
            color: #00d2ff;
            font-size: 1.2rem;
            margin-bottom: 0.5rem;
        }}
        .result-value {{
            font-size: 2rem;
            font-weight: bold;
            color: white;
            margin: 0.5rem 0;
        }}
        .weather-icon {{
            font-size: 3rem;
            text-align: center;
            margin: 1rem 0;
        }}
    </style>
    
    <div class="result-card">
        <div class="weather-icon">{prediction['icon']}</div>
        <div class="result-title">Current Conditions</div>
        <div class="result-value">{prediction['weather']}</div>
    </div>
    
    <div class="result-card">
        <div class="result-title">Temperature</div>
        <div class="result-value">{prediction['temperature']}°C</div>
    </div>
    
    <div class="result-card">
        <div class="result-title">Precipitation</div>
        <div class="result-value">{prediction['precipitation']}</div>
    </div>
    
    <div class="result-card">
        <div class="result-title">Humidity</div>
        <div class="result-value">{round(prediction['humidity'] * 100, 1)}%</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Historical trend visualization
    st.markdown("### 📈 Historical Trend")
    data = pd.DataFrame({
        'Hour': range(24),
        'Temperature': [prediction['temperature'] - 5 + i * 0.5 for i in range(24)],
        'Humidity': [prediction['humidity'] * 100 - 10 + i for i in range(24)],
        'Wind Speed': [prediction['wind_speed'] - 5 + i * 0.5 for i in range(24)]
    })
    
    fig = px.line(data, x='Hour', y=['Temperature', 'Humidity', 'Wind Speed'],
                 title="24-hour Forecast Trend",
                 labels={'value': 'Measurement', 'variable': 'Metric'},
                 color_discrete_map={
                     'Temperature': '#00d2ff',
                     'Humidity': '#3a47d5',
                     'Wind Speed': '#ff6b6b'
                 })
    
    fig.update_layout(
        plot_bgcolor='rgba(20, 20, 40, 0.8)',
        paper_bgcolor='rgba(20, 20, 40, 0.5)',
        font_color='white',
        xaxis=dict(showgrid=True, gridcolor='rgba(100, 100, 150, 0.2)'),
        yaxis=dict(showgrid=True, gridcolor='rgba(100, 100, 150, 0.2)'),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)