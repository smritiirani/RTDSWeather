Configuration File

API_KEY = 'your_openweathermap_api_key'
INTERVAL = 300  # API call every 5 minutes
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

# Thresholds for alerts
TEMP_THRESHOLD = 35  # Degrees Celsius
CONSECUTIVE_THRESHOLD = 2  # Trigger alert after 2 consecutive updates

# Database settings
DATABASE = {
    'host': 'db',
    'user': 'postgres',
    'password': 'password',
    'dbname': 'weather_monitor'
}
