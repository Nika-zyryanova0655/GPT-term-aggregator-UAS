import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def getlinks(url):
    ua = UserAgent()
    headers = {
        'User-Agent': str(ua.random)
    }

    # Получаем содержимое страницы
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')

    # Находим все теги <div>
    div_tags = soup.find_all('div')

    # Выводим текст из каждого найденного тега <div>
    for div_tag in div_tags:
        print(div_tag.text)
        break


if __name__ == '__main__':
    # Пример ссылки
    url = 'https://аэронет2035.рф/catalog/tproduct/607938184-455698780031-geoskan-lite'

    # Парсим данные по ссылке
    getlinks(url)