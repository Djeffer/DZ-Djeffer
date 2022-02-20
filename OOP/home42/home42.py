import csv
from bs4 import BeautifulSoup
import requests
import re


def get_html(url):
    r = requests.get(url)
    return r.text


def refined(s):
    res = re.sub(r'\D+', '', s)
    return res


def write_csv(data):
    with open('plugins.csv', 'a') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\r')
        writer.writerow((data['name'], data['url'], data['text_block']))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    s = soup.find('div', class_='view-content')
    plugins = s.find_all('article')
    for plugin in plugins:
        name = plugin.find('h2').text
        url = plugin.find('h2').find('a').get('href')
        text_block = plugin.find('p').text

        data = {'name': name, 'url': url, 'text_block': text_block}
        write_csv(data)


def main():
    url = 'https://softobase.com/ru/internet/plaginy'
    get_data(get_html(url))


if __name__ == '__main__':
    main()


