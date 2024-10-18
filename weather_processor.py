Processing, Conversion, and Aggregates

import requests
from config import API_KEY, DATABASE
from database import save_daily_summary
import json

class WeatherProcessor:
    def __init__(self):
        self.daily_data = {}  # Store rollups for cities

    def fetch_weather_data(self, city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        response = requests.get(url)
        return response.json()

    def process_weather_data(self, city, weather_data):
        # Extract relevant fields
        temp_kelvin = weather_data['main']['temp']
        weather_main = weather_data['weather'][0]['main']
        timestamp = weather_data['dt']
        
        temp_celsius = temp_kelvin - 273.15
        self.update_daily_rollups(city, temp_celsius, weather_main, timestamp)

    def update_daily_rollups(self, city, temp_celsius, weather_main, timestamp):
        if city not in self.daily_data:
            self.daily_data[city] = {
                'temp_sum': 0,
                'temp_count': 0,
                'max_temp': float('-inf'),
                'min_temp': float('inf'),
                'weather_conditions': {},
                'last_timestamp': timestamp
            }
        
        city_data = self.daily_data[city]
        city_data['temp_sum'] += temp_celsius
        city_data['temp_count'] += 1
        city_data['max_temp'] = max(city_data['max_temp'], temp_celsius)
        city_data['min_temp'] = min(city_data['min_temp'], temp_celsius)

        # Count dominant weather condition
        if weather_main in city_data['weather_conditions']:
            city_data['weather_conditions'][weather_main] += 1
        else:
            city_data['weather_conditions'][weather_main] = 1

        # Save daily summary at midnight
        if self.is_end_of_day(timestamp, city_data['last_timestamp']):
            self.save_daily_summary(city)
            self.reset_city_data(city)
        
        city_data['last_timestamp'] = timestamp

    def is_end_of_day(self, timestamp, last_timestamp):
        # Compare date from timestamps (midnight logic)
        return time.strftime("%d", time.gmtime(timestamp)) != time.strftime("%d", time.gmtime(last_timestamp))

    def save_daily_summary(self, city):
        city_data = self.daily_data[city]
        avg_temp = city_data['temp_sum'] / city_data['temp_count']
        max_temp = city_data['max_temp']
        min_temp = city_data['min_temp']
        dominant_condition = max(city_data['weather_conditions'], key=city_data['weather_conditions'].get)

        summary = {
            'city': city,
            'avg_temp': avg_temp,
            'max_temp': max_temp,
            'min_temp': min_temp,
            'dominant_condition': dominant_condition
        }

        save_daily_summary(summary)

    def reset_city_data(self, city):
        self.daily_data[city] = {
            'temp_sum': 0,
            'temp_count': 0,
            'max_temp': float('-inf'),
            'min_temp': float('inf'),
            'weather_conditions': {},
            'last_timestamp': None
        }
