import requests
def get_weather_data(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m"
    response = requests.get(url)
    data = response.json()
    return data['current']['temperature_2m'], data['current']['time']
get_weather_data(40.7128, -74.0060)  
get_weather_data(34.0522, -118.2437)
get_weather_data(77.5937, 2.9719)