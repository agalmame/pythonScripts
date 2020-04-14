import requests
from bs4 import BeautifulSoup as bf
from pprint import PrettyPrinter as Pretty

href=''
al= []

def scrapeBook (url):
    url = f"http://books.toscrape.com/catalogue/{url}"
    html = requests.get(url)

    control = bf(html.content,'html.parser')
    title = control.select(".product_main h1")[0].get_text()
    price = control.select(".product_main p.price_color")[0].get_text()
    stock = control.select(".product_main .instock")[0].get_text().strip().split(' ')[2].split('(')[1]
    dic = {'title':title,'price':price,'stock':stock}
    return dic

for i in range(1,51):
    print(f"this is {i}\n")
    URl = f'http://books.toscrape.com/catalogue/page-{i}.html'
    page = requests.get(URl)
    soup = bf(page.content, 'html.parser')
    results = soup.select("ol.row li h3 a")

    for result in results:
        href= result.get('href')
        info = scrapeBook(href).items()
        al.append(info)
        print(al)


