Main Application
from weather_processor import WeatherProcessor
from alert_manager import AlertManager
from config import INTERVAL, CITIES
import time

if __name__ == '__main__':
    weather_processor = WeatherProcessor()
    alert_manager = AlertManager()

    while True:
        for city in CITIES:
            weather_data = weather_processor.fetch_weather_data(city)
            weather_processor.process_weather_data(city, weather_data)
            alert_manager.check_alerts(city, weather_data)
        time.sleep(INTERVAL)
