import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
import time

a = []


def add_domain(url, domain):
    if 'facebook' in url or 'instagram' in url:
        return domain

    if not url.startswith('http'):
        if url.startswith('/'):
            return domain + url
        else:
            return domain + '/' + url
    return url


def get_dynamic_links(url):
    ua = UserAgent()
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={ua.random}")

    # Указываем путь к драйверу браузера
    service = Service(ChromeDriverManager().install())

    # Создаем экземпляр драйвера браузера
    driver = webdriver.Chrome(service=service, options=options)

    # Загружаем страницу
    driver.get(url)
    time.sleep(2)

    # Получаем содержимое страницы
    page_source = driver.page_source

    driver.quit()

    soup = BeautifulSoup(page_source, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        a.append(link.get('href'))


def parse_website(url, domain):
    k = 0
    # Отправляем GET-запрос к веб-сайту
    global links
    url.pop(0)
    url.pop(7)
    with open('text.txt', 'w', encoding='utf-8') as file:
        for i in url:
            if i is not None:
                k += 1
                ua = UserAgent()
                headers = {
                    'User-Agent': str(ua.random)
                }
                # Получаем содержимое страницы
                domain1 = add_domain(i, domain)
                page = requests.get(domain1, headers=headers)
                soup = BeautifulSoup(page.text, 'html.parser')

                # Находим все теги <a>, которые содержат ссылки
                links = soup.find_all('div')
                for link in links:
                    cleaned_text = link.text.strip()
                    if cleaned_text:
                        file.write(cleaned_text + ' ')
                        break


if __name__ == '__main__':
    urli = input('Введите ссылку на сайт:')

    get_dynamic_links(urli)
    print(a)
    print(len(a))
    parse_website(a, urli)
