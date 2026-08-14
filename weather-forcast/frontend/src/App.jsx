import { Search, MapPin, Droplets, Wind, Eye, Gauge } from "lucide-react";
import "./App.css";

function App() {
  return (
    <div className="app">
      <header className="navbar">
        <div className="logo">☁️ Weatherly</div>

        <div className="search-box">
          <Search size={20} />
          <input
            type="text"
            placeholder="Search city..."
          />
        </div>

        <button className="unit-btn">°C</button>
      </header>

      <main className="container">

        <section className="current-weather">

          <div className="location">
            <MapPin size={20} />
            <span>Bhubaneswar, India</span>
          </div>

          <div className="weather-main">
            <div className="weather-icon">☀️</div>

            <div>
              <h1>29°</h1>
              <h2>Partly Cloudy</h2>
              <p>Feels like 31°</p>
            </div>
          </div>

          <div className="high-low">
            <span>H: 32°</span>
            <span>L: 25°</span>
          </div>

        </section>

        <section className="details">

          <div className="detail-card">
            <Droplets />
            <span>Humidity</span>
            <strong>72%</strong>
          </div>

          <div className="detail-card">
            <Wind />
            <span>Wind</span>
            <strong>14 km/h</strong>
          </div>

          <div className="detail-card">
            <Eye />
            <span>Visibility</span>
            <strong>8 km</strong>
          </div>

          <div className="detail-card">
            <Gauge />
            <span>Pressure</span>
            <strong>1012 hPa</strong>
          </div>

        </section>

        <section className="forecast">

          <h2>Hourly Forecast</h2>

          <div className="hourly">

            <div className="hour active">
              <span>Now</span>
              <div>☀️</div>
              <strong>29°</strong>
            </div>

            <div className="hour">
              <span>4 AM</span>
              <div>☀️</div>
              <strong>28°</strong>
            </div>

            <div className="hour">
              <span>5 AM</span>
              <div>☁️</div>
              <strong>28°</strong>
            </div>

            <div className="hour">
              <span>6 AM</span>
              <div>☁️</div>
              <strong>27°</strong>
            </div>

            <div className="hour">
              <span>7 AM</span>
              <div>🌧️</div>
              <strong>27°</strong>
            </div>

            <div className="hour">
              <span>8 AM</span>
              <div>🌧️</div>
              <strong>28°</strong>
            </div>

          </div>

        </section>

        <section className="forecast">

          <h2>7-Day Forecast</h2>

          <div className="weekly">

            <div className="day">
              <span>Today</span>
              <span>☀️</span>
              <strong>32° / 25°</strong>
            </div>

            <div className="day">
              <span>Sunday</span>
              <span>⛅</span>
              <strong>33° / 26°</strong>
            </div>

            <div className="day">
              <span>Monday</span>
              <span>🌧️</span>
              <strong>31° / 25°</strong>
            </div>

            <div className="day">
              <span>Tuesday</span>
              <span>🌧️</span>
              <strong>30° / 24°</strong>
            </div>

          </div>

        </section>

      </main>
    </div>
  );
}

export default App;