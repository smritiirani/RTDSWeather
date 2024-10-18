Alerting Thresholds and Notifications

from config import TEMP_THRESHOLD, CONSECUTIVE_THRESHOLD
import smtplib
from email.mime.text import MIMEText

class AlertManager:
    def __init__(self):
        self.alert_state = {}

    def check_alerts(self, city, weather_data):
        temp_celsius = weather_data['main']['temp'] - 273.15
        if city not in self.alert_state:
            self.alert_state[city] = {
                'consecutive_count': 0
            }
        
        city_state = self.alert_state[city]
        
        if temp_celsius > TEMP_THRESHOLD:
            city_state['consecutive_count'] += 1
        else:
            city_state['consecutive_count'] = 0

        if city_state['consecutive_count'] >= CONSECUTIVE_THRESHOLD:
            self.trigger_alert(city, temp_celsius)
    
    def trigger_alert(self, city, temp_celsius):
        msg = MIMEText(f"Alert! Temperature in {city} exceeded {TEMP_THRESHOLD} degrees for multiple updates. Current temperature: {temp_celsius:.2f}°C")
        msg['Subject'] = f"Weather Alert for {city}"
        msg['From'] = "alert@weatherapp.com"
        msg['To'] = "user@example.com"

        with smtplib.SMTP('localhost') as server:
            server.send_message(msg)
        print(f"Alert triggered for {city}")
