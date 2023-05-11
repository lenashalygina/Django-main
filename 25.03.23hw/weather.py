import requests
from bs4 import BeautifulSoup
from django.core.cache import cache


def fetch_weather_data():
    url = "https://www.gismeteo.kz/weather-almaty-5205/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        temperature = soup.find('span', {'class': 'temperature'}).text
        weather_description = soup.find('div', {'class': 'weather-description'}).text

        return {
            'temperature': temperature,
            'weather_description': weather_description
        }
    else:
        return None


def get_weather_data():
    weather_data = cache.get('weather_data')

    if weather_data is None:
        weather_data = fetch_weather_data()
        cache.set('weather_data', weather_data, timeout=60)

    return weather_data


# Usage
weather_data = get_weather_data()
if weather_data:
    print("Temperature: ", weather_data['temperature'])
    print("Weather Description: ", weather_data['weather_description'])
else:
    print("Failed to fetch weather data.")
