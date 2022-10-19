import requests
from bs4 import BeautifulSoup

items = []

for i in range(7):
    url = f'https://scrapingclub.com/exercise/list_basic/?page={i + 1}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")

    urls = soup.find_all('h4', class_='card-title')
    for i in range(len(urls)):
        urls[i] = urls[i].find('a', href=True)
        urls[i] = urls[i]['href']

    for i in range(len(urls)):
        url = f'https://scrapingclub.com/{urls[i]}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, features="html.parser")

        name = soup.find('h3').text
        price = soup.find('div', class_='card-body').find('h4').text
        description = soup.find('p', class_='card-text').text
        
        items.append([name, price, description])

for i in range(len(items)):
    item = items[i]
    print(f'*************\n{item[0]}\n{item[1]}\n{item[2]}\n*************')