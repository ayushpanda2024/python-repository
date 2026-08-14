import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os
# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)
def get_weather_data(latitude,longitude):
    start_date = week_ago.strftime("%Y-%m-%d")
    end_date = today.strftime("%Y-%m-%d")
# Get  weather for past week
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
    response = requests.get(url)
    data = response.json()
    url2 = f"https://nominatim.openstreetmap.org/reverse?lat={latitude}&lon={longitude}&format=json"
    response2 = requests.get(
    url2,
    headers={"User-Agent": "MyApp/1.0"}
      )
    data2 = response2.json()
    city_name =data2['address']['city']
    daily_data = data['daily']

# Create a DataFrame
    df = pd.DataFrame({
        'date': daily_data['time'],
        'max_temp': daily_data['temperature_2m_max'],
        'min_temp': daily_data['temperature_2m_min']
    })

# Convert date strings to datetime
    df['date'] = pd.to_datetime(df['date'])
    #______________________________________________________________________________________________
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
    plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

    # Add labels and title
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title(f'{city_name} Weather - Past 7 Days')
    plt.legend()

    # Rotate x-axis labels for readability
    plt.xticks(rotation=40)
    plt.tight_layout()

    # Save the plot
    plt.savefig(f'{city_name}weather_chart.png')
    plt.show()
    

def save_data(data,df,city_name): 
    if not os.path.exists('data'):
        os.makedirs('data')
    df.to_csv(f'data/{city_name}_weather.csv', index=False)

lat =  float(input("Enter the latitude: "))
lon = float(input("Enter the longitude: "))
get_weather_data(latitude=lat, longitude=lon)