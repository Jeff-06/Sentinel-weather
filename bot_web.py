from flask import Flask, render_template
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

    return render_template(
    "index.html",
    temp=temp,
    wind=wind,
    condition=condition,
    advice=advice
)

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