import requests

LAT = 9.93
LON = 76.26

def get_weather():
    url = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&current_weather=true&timezone=auto"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        cw = data.get("current_weather")
        if not cw:
            return None, None, None

        temp = cw.get("temperature")
        wind = cw.get("windspeed")
        code = cw.get("weathercode")

        return temp, wind, code
    except Exception:
        return None, None, None
