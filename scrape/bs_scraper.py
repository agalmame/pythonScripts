from bs4 import BeautifulSoup
import requests


page = requests.get('https://www.sainsburys.co.uk/shop/gb/groceries/meat-fish').text 
soup = BeautifulSoup(page, 'html.parser')


fjsljf

def extract_department_links(url):
    links = []

    ul = soup.find('ul', class_='categories departments')
    if ul:
        for li in ul.find_all('li'):
            a = li.find('a',href=True)
            if a:
                links.append(a['href'])


