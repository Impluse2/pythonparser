import re
import requests
from bs4 import BeautifulSoup
from tg_bot.loader import dp, bot

def get_html(url) -> str:
    """
    Получает html-код страницы по заданному URL

    :param url: URL страницы для парсинга
    :return: HTML-код страницы
    """""

    # Дабвляем заголовок User-Agent в запрос для корректной работы парсера
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    r = requests.get(url, headers=headers)
    return r.text


def extract_data(news_html) -> list:
    """""
    Извлекает данные из HTML-кода новостей и возвращает список строк с результатами

    :param news_html: Список HTML-кодов новостей
    :retur: Список строк с результатми
     """""
    results = []
    for news in news_html:
        soup = BeautifulSoup(news, 'lxml')

        # Находим информацию о виде спорта, времени и счета в html-коде новости
        sport = soup.find(class_='p-sport-event__rubric link-holder_over').text
        time = soup.find(class_='p-sport-event__info').text
        score = soup.find(class_='p-sport-event__scores').text

        # Находим названия команд в тексте новости с помощью регулярного выражения
        team_names_match = re.search(r'([А-ЯЁ][а-яё]+)\s*([А-ЯЁ][а-яё]+)', soup.text)
        if team_names_match:
            team_names = team_names_match.groups()
        else:
            team_names = ('Ошибка', 'Ошибка')

        # Формируем строку с результатми и добавляем ее в список результатов
        result = f'{sport}\nВремя: {time}\n{team_names[0]}: {score[0]}\n{team_names[1]}: {score[1]}\n'
        results.append(result)


    return results


def main() -> str:
    """
    Основная функция программы, которая вызывает остальные функции и возвращает результат

    :return: Строка с результатом парсинга
    """

    # Получаем html-код главной страницы спортивного сайта
    url = 'https://sportmail.ru/'
    html = get_html(url)

    # Находим все новости на странице и формируем список HTML-кодов новостей
    soup = BeautifulSoup(html,'lxml')
    news_list = soup.find_all('div', class_='p-sport-event p-sport-event_index js-slider__item')
    news_html_list = [str(news) for news in news_list]

    # Извлекаем данные из HTML-кода новостей и формируем строку с результатами
    return  '\n'.join(extract_data(news_html_list))



