from pars import get_dynamic_links, parse_website, a
from mysqlbd import setup_database, insert_parsed_data
from neiron import process_file

def main():
    urli = 'https://аэронет2035.рф/'

    # Парсинг данных
    get_dynamic_links(urli)
    parse_website(a, urli)

    # Установка базы данных и вставка данных
    setup_database()

    with open('text.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()

    insert_parsed_data(data)

    # Классификация текста нейронной сетью
    results = process_file('text.txt')

    # Обработка и вывод результатов классификации
    for idx, prob in enumerate(results):
        print(
            f"Текст {idx + 1} вероятность принадлежности к классу 'термины из категории беспилотных авиационных систем и их контекст': {prob[1]:.4f}")


if __name__ == '__main__':
    main()

