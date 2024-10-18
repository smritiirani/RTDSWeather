Visualizations for Weather Trends and Alerts

import matplotlib.pyplot as plt

def plot_daily_summaries(summaries):
    cities = [summary['city'] for summary in summaries]
    avg_temps = [summary['avg_temp'] for summary in summaries]
    max_temps = [summary['max_temp'] for summary in summaries]
    min_temps = [summary['min_temp'] for summary in summaries]

    plt.figure(figsize=(10, 6))
    plt.plot(cities, avg_temps, label='Average Temp')
    plt.plot(cities, max_temps, label='Max Temp', linestyle='--')
    plt.plot(cities, min_temps, label='Min Temp', linestyle=':')
    plt.title('Daily Weather Summary')
    plt.xlabel('City')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.show()
