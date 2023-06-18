import requests
from bs4 import BeautifulSoup


def get_crypto_price(coin):
    url = f'https://coinmarketcap.com/currencies/{coin}/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price_element = soup.find('span', class_='cmc-details-panel-price__price')
    if price_element:
        price = price_element.text.strip()
    else:
        price = 'Цена не доступна'
    return price


cryptos = ['bitcoin', 'ethereum', 'litecoin']

for crypto in cryptos:
    price = get_crypto_price(crypto)
    print(f'Цена {crypto.capitalize()}: {price}')
