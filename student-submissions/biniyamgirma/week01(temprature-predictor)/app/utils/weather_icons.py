def get_weather_icon(weather_label, precip_label):
    """Get weather icon based on decoded text labels"""
    weather_label = str(weather_label).lower()
    precip_label = str(precip_label).lower()
    
    if "rain" in precip_label:
        return "🌧️"
    elif "snow" in precip_label:
        return "❄️"
    elif "clear" in weather_label:
        return "☀️"
    elif "cloud" in weather_label:
        return "☁️"
    elif "fog" in weather_label:
        return "🌫️"
    elif "partly" in weather_label:
        return "⛅"
    else:
        return "🌈"