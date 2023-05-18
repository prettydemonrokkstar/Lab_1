from bs4 import BeautifulSoup
import requests

def parse():
    url = 'https://www.citilink.ru/catalog/smartfony/APPLE'
    try:
        page = requests.get(url)
        print('Status code: ' + str(page.status_code))
        soup = BeautifulSoup(page.text, 'html.parser')
    except:
        print('An error occured while connecting to the site...')
        return -1

    blocks = soup.findAll('span',
                          class_='ProductCardHorizontal__price_current-price js--ProductCardHorizontal__price_current-price')
    prices = []
    for data in blocks:
        prices.append(int(str(data.text).replace(' ', '').replace('\n', '')))
    print('iPhones found: ' + str(len(prices)))

    print('---')
    print('Max price: ' + str(max(prices)))
    print('Min price: ' + str(min(prices)))
    print('Average: ' + str(sum(prices) / len(prices)))