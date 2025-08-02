import requests
from tabulate import tabulate
import requests
from tabulate import tabulate
from datetime import datetime
# weather_ap.py
API_KEY = "1594ad55bd499522469e020917105921"  # Your key
# OpenWeatherMap API endpoint
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# Function to format UNIX timestamp to a readable time
def format_unix_time(timestamp):
    """Convert UNIX timestamp to readable time."""
    return datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')


# Function to fetch weather data for a given city

def get_weather(city):   
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        # Make the API request
        response = requests.get(BASE_URL, params=params, timeout=10)
    except requests.exceptions.RequestException as e:
        print("Network error:", e)
        return

    if response.status_code == 200:
        data = response.json()

        table = [
            ["City", f"{data['name']}, {data['sys']['country']}"],
            ["Temperature (°C)", data['main']['temp']],
            ["Feels Like (°C)", data['main']['feels_like']],
            ["Min Temp (°C)", data['main']['temp_min']],
            ["Max Temp (°C)", data['main']['temp_max']],
            ["Humidity (%)", data['main']['humidity']],
            ["Condition", data['weather'][0]['description']],
            ["Wind Speed (m/s)", data['wind']['speed']],
            ["Sunrise", format_unix_time(data['sys']['sunrise'])],
            ["Sunset", format_unix_time(data['sys']['sunset'])]
        ]

        print(tabulate(table, headers=["Parameter", "Value"], tablefmt="fancy_grid"))
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
    print("Fetching weather data...")
    print("Done.")  