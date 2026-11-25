import requests

LATITUDE = 1
LONGITUDE = 38
# these locations are for Kenya

URL = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": LATITUDE,
    "longitude": LONGITUDE,
    "daily": "temperature_2m_max,temperature_2m_min,sunrise,sunset,rain_sum,showers_sum",
    "timezone": "auto",
    "forecast_days": 7,
}

try:
    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Could not fetch weather data: {e}")
    raise SystemExit(1)

data = response.json()
daily = data["daily"]
units = data["daily_units"]

print(f"{'Date':<12}{'Min':>8}{'Max':>8}{'Sunrise':>9}{'Sunset':>8}{'Rain':>9}{'Showers':>9}")

for day, t_min, t_max, srise, sset, rain, showers in zip(
    daily["time"],
    daily["temperature_2m_min"],
    daily["temperature_2m_max"],
    daily["sunrise"],
    daily["sunset"],
    daily["rain_sum"],
    daily["showers_sum"],
):
    # sunrise/sunset look like "2026-11-25T06:20"; keep only the time part
    print(
        f"{day:<12}"
        f"{t_min:>6}{units['temperature_2m_min']:<2}"
        f"{t_max:>6}{units['temperature_2m_max']:<2}"
        f"{srise.split('T')[1]:>9}"
        f"{sset.split('T')[1]:>8}"
        f"{rain:>7}{units['rain_sum']:<2}"
        f"{showers:>7}{units['showers_sum']:<2}"
    )