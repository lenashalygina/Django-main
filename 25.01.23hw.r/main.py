from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.http import HttpResponse
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_weather():
    url = 'https://www.gismeteo.kz/weather-almaty-5205/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    weather_data = {
        'temperature': soup.find('span', class_='temperature').text,
        'description': soup.find('div', class_='description').text
    }
    return weather_data


@cache_page(60 * 5)
def weather_view(request):
    weather_data = cache.get('weather_data')
    if not weather_data:
        weather_data = get_weather()
        cache.set('weather_data', weather_data)
    return HttpResponse(f"Weather: {weather_data}")


def get_currency():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://example.com/currency')   #не нашла открытый
    currency_data = {
        'usd': driver.find_element_by_id('usd').text,
        'eur': driver.find_element_by_id('eur').text
    }
    driver.quit()
    return currency_data


@cache_page(60 * 5)
def currency_view(request):
    currency_data = cache.get('currency_data')
    if not currency_data:
        currency_data = get_currency()
        cache.set('currency_data', currency_data)
    return HttpResponse(f"Currency: {currency_data}")
