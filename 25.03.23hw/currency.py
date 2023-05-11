from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from django.core.cache import cache


def fetch_currency_data():
    chrome_path = '/path/to/chromedriver'
    driver = webdriver.Chrome(service=ChromeService(executable_path=chrome_path))

    driver.get('https://www.example.com/currency')

    currency_data = {}
    currency_elements = driver.find_elements(By.XPATH, '//div[@class="currency-data"]')
    for element in currency_elements:
        currency_name = element.find_element(By.XPATH, './span[@class="currency-name"]').text
        currency_value = element.find_element(By.XPATH, './span[@class="currency-value"]').text
        currency_data[currency_name] = currency_value

    driver.quit()
    return currency_data


def get_currency_data():
    currency_data = cache.get('currency_data')

    if currency_data is None:
        currency_data = fetch_currency_data()
        cache.set('currency_data', currency_data, timeout=60)

    return currency_data


currency_data = get_currency_data()
if currency_data:
    for currency_name, currency_value in currency_data.items():
        print(f"{currency_name}: {currency_value}")
else:
    print("Failed to fetch currency data.")
