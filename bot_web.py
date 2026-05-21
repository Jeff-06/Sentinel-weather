from flask import Flask
from weather import get_weather
from logic import *
import os
app = Flask(__name__)

@app.route('/')
def home():
    temp, wind, code = get_weather()
    if temp is None:
        return """
<html>
<body>
    <h1>Sentinel Weather — Error</h1>
    <p>Unable to fetch weather data right now. Please try again later.</p>
</body>
</html>
"""

    condition = interpret_weather(code)
    advice = generate_advice(temp, code)

    return f"""
<html>
<head>
    <title>Sentinel Weather</title>

    <meta http-equiv="refresh" content="10">

    <style>
        body {{
            background-color: #0f172a;
            color: white;
            font-family: Arial;
            padding: 40px;
        }}

        .card {{
            background-color: #1e293b;
            padding: 20px;
            border-radius: 15px;
            width: 300px;
            box-shadow: 0 0 10px rgba(0,0,0,0.3);
        }}

        h1 {{
            color: #38bdf8;
        }}

        p {{
            font-size: 18px;
        }}
    </style>
</head>

<body>

    <div class="card">
        <h1>🌤 Sentinel Weather</h1>

        <p>🌡 Temperature: {temp}°C</p>
        <p>💨 Wind: {wind} km/h</p>
        <p>☁ Condition: {condition}</p>

        <hr>

        <p>👉 {advice}</p>
    </div>

</body>
</html>
"""

@app.route('/pi')
def pi():
    temp = os.popen("vcgencmd measure_temp").read()
    uptime = os.popen("uptime -p").read()
    memory = os.popen("free -h").read()

    return f"""
    <h1>Pi System Info</h1>
    <p><b>CPU Temp:</b> {temp}</p>
    <p><b>Uptime:</b> {uptime}</p>
    <pre>{memory}</pre>
    """
app.run(host='0.0.0.0', port=5000)