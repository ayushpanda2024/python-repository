from datetime import date, timedelta

import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from geopy.geocoders import Nominatim

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

geolocator = Nominatim(user_agent="weather_app")


@app.get("/")
def home():
    return {"message": "Weather API is running"}


@app.get("/weather")
def get_weather(city: str):
    location = geolocator.geocode(city)
    if not location:
        raise HTTPException(404, "City not found")

    today = date.today()
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": location.latitude,
            "longitude": location.longitude,
            "start_date": today - timedelta(days=6),
            "end_date": today,
            "daily": "temperature_2m_max,temperature_2m_min",
            "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
            "timezone": "auto",
        },
        timeout=10,
    )

    if not response.ok:
        raise HTTPException(500, "Weather API failed")

    data = response.json()
    daily = data["daily"]
    current = data.get("current", {})

    return {
        "city": location.address,
        "latitude": location.latitude,
        "longitude": location.longitude,
        "current": {
            "temperature": current.get("temperature_2m"),
            "humidity": current.get("relative_humidity_2m"),
            "wind_speed": current.get("wind_speed_10m"),
            "weather_code": current.get("weather_code"),
        },
        "daily": [
            {"date": day, "max_temp": high, "min_temp": low}
            for day, high, low in zip(
                daily["time"],
                daily["temperature_2m_max"],
                daily["temperature_2m_min"],
            )
        ],
    }