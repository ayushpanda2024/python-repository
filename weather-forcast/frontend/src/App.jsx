import { useEffect, useState } from "react";
import { Search, MapPin, Droplets, Wind } from "lucide-react";
import "./App.css";

function App() {
  const [city, setCity] = useState("Bhubaneswar");
  const [weather, setWeather] = useState(null);

  const fetchWeather = async () => {
    try {
      const response = await fetch(
        `http://127.0.0.1:8000/weather?city=${encodeURIComponent(city)}`
      );
      const data = await response.json();

      if (!response.ok) throw new Error(data.detail || "Weather API failed");

      setWeather(data);
    } catch (error) {
      setWeather(null);
      console.error("Error:", error.message);
    }
  };

  useEffect(() => {
    fetchWeather();
  }, []);

  return (
    <div className="app">
      <div className="search-box">
        <Search size={20} />
        <input
          value={city}
          onChange={(e) => setCity(e.target.value)}
          placeholder="Search city..."
        />
        <button onClick={fetchWeather}>Search</button>
      </div>

      {weather && (
        <div className="weather">
          <div className="location">
            <MapPin />
            <h2>{weather.city}</h2>
          </div>

          <div className="temperature">
            ☀️
            <h1>{weather.current.temperature}°C</h1>
            <p>{weather.current.description}</p>
          </div>

          <div className="details">
            <div>
              <Droplets />
              <p>Humidity</p>
              <strong>{weather.current.humidity}%</strong>
            </div>

            <div>
              <Wind />
              <p>Wind</p>
              <strong>{weather.current.wind_speed} km/h</strong>
            </div>
          </div>
          <div className="forecast">
           {weather.daily.map((day) => (
           <div key={day.date} className="forecast-day">
             <p>{day.date}</p>
             <strong>{day.max_temp}°C</strong>
             <p>Low: {day.min_temp}°C</p>
            </div>
  ))}
</div>
        </div>
      )}
    </div>
  );
}

export default App;