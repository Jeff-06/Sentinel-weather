def interpret_weather(code):
    if code == 0:
        return "Clear sky ☀️"
    elif code in [1, 2, 3]:
        return "Cloudy ☁️"
    elif code in [45, 48]:
        return "Fog 🌫️"
    elif code in [51, 53, 55]:
        return "Drizzle 🌦️"
    elif code in [61, 63, 65]:
        return "Rain 🌧️"
    elif code == 95:
        return "Thunderstorm ⛈️"
    else:
        return "Unknown weather"

def generate_advice(temp, code):
    if code in [61, 63, 65, 95]:
        return "Take an umbrella ☔"
    elif temp > 30:
        return "Very hot today ☀️ Stay hydrated"
    elif temp < 20:
        return "It might be cold ❄️"
    else:
        return "Weather looks good 👍"
