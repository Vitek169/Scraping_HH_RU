import requests
from bs4 import BeautifulSoup as BS



HEADERS = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 YaBrowser/24.4.0.0 Safari/537.36',
    'accept':'*/*'
}

class Scraping_qa:

    def __init__(self):
        pass

    def qa_junior(self):
        URL = 'https://hh.ru/search/vacancy?text=Qa+engineer+junior&from=suggest_post&salary=&ored_clusters=true&page=0'
        r = requests.get(URL, headers=HEADERS)
        soup = BS(r.content, 'html.parser')
        BASE_URL = 'https://hh.ru/search/vacancy?text=Qa+engineer+junior&from=suggest_post&salary=&ored_clusters=true&page='
        max = soup.find_all('span', {'class':'pager-item-not-in-short-range'})[-1]
        print(f'Максимальное число страниц {max.text}')
        for number_page in range(1, int(max.text) + 1):
            CURRENT_URL = BASE_URL + str(number_page)
            r = requests.get(CURRENT_URL, headers=HEADERS)
            print(f'Страница: {CURRENT_URL}')
            soup = BS(r.content, 'html.parser')
            cards = soup.find_all('div', class_='vacancy-card--H8LvOiOGPll0jZvYpxIF font-inter')
            for card in cards:
                title = card.find('a').text
                print(title)

    def qa_middle(self):
        URL = 'https://hh.ru/search/vacancy?text=Qa+engineer+middle&from=suggest_post&salary=&ored_clusters=true&page=0'
        r = requests.get(URL, headers=HEADERS)
        soup = BS(r.content, 'html.parser')
        BASE_URL = 'https://hh.ru/search/vacancy?text=Qa+engineer+middle&from=suggest_post&salary=&ored_clusters=true&page='
        max = soup.find_all('span', {'class': 'pager-item-not-in-short-range'})[-1]
        print(f'Максимальное число страниц {max.text}')
        for number_page in range(1, int(max.text) + 1):
            CURRENT_URL = BASE_URL + str(number_page)
            r = requests.get(CURRENT_URL, headers=HEADERS)
            print(f'Страница: {CURRENT_URL}')
            soup = BS(r.content, 'html.parser')
            cards = soup.find_all('div', class_='vacancy-card--H8LvOiOGPll0jZvYpxIF font-inter')
            for card in cards:
                title = card.find('a').text
                print(title)





jun = Scraping_qa()
middle = Scraping_qa()
jun.qa_junior()
middle.qa_middle()



