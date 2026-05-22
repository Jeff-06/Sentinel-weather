from flask import Flask, render_template
from weather import get_weather
from logic import *
import os
import psutil
app = Flask(__name__)

@app.route('/')
def home():
    temp, wind, code = get_weather()
    temp = os.popen("vcgencmd measure_temp").read()
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
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
    advice=advice,
    cpu=cpu,
    memory=memory,
    temp=temp
)

    


app.run(host='0.0.0.0', port=5000)