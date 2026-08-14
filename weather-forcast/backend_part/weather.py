from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import requests
from datetime import datetime, timedelta
from geopy.geocoders import Nominatim


app = FastAPI()

# Allow React to communicate with Python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Geocoder
geolocator = Nominatim(user_agent="weather_app")


@app.get("/")
def home():
    return {
        "message": "Weather API is running"
    }


@app.get("/weather")
def get_weather(city: str):

    # -----------------------------
    # 1. Find city coordinates
    # -----------------------------

    location = geolocator.geocode(city)

    if not location:
        raise HTTPException(
            status_code=404,
            detail="City not found"
        )

    latitude = location.latitude
    longitude = location.longitude


    today = datetime.now()
    week_ago = today - timedelta(days=7)

    start_date = week_ago.strftime("%Y-%m-%d")
    end_date = today.strftime("%Y-%m-%d")

    url = (
        f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code&timezone=auto"
    )

    response = requests.get(url)

    if response.status_code != 200:
        raise HTTPException(
            status_code=500,
            detail="Weather API failed"
        )

    data = response.json()

    daily = data["daily"]

    daily_weather = []

    for i in range(len(daily["time"])):

        daily_weather.append({
            "date": daily["time"][i],
            "max_temp": daily["temperature_2m_max"][i],
            "min_temp": daily["temperature_2m_min"][i]
        })

    current = data.get("current", {})

    current_weather = {
        "temperature": current.get("temperature_2m"),
        "humidity": current.get("relative_humidity_2m"),
        "wind_speed": current.get("wind_speed_10m"),
        "weather_code": current.get("weather_code")
    }



    return {
        "city": location.address,
        "latitude": latitude,
        "longitude": longitude,
        "current": current_weather,
        "daily": daily_weather
    }