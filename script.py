import requests
from bs4 import BeautifulSoup
import datetime

def url_parser(url):
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' }
    
    page=requests.get(url, headers=headers)
    soup=BeautifulSoup(page.content, 'html.parser')
    price=soup.find(id='priceblock_ourprice')
    print(price)
    if price==None:
        product='default'
        price=1
        date=datetime.datetime.now()
        return (product, date, price)
    else:
        price=price.text
        price=price[0:-2]
        price=price.replace(u'\xa0', u' ')
        price=price.replace(',', '.')
        price=price.replace(' ', '')
        price=float(price)
        brut_product=soup.find(id='productTitle').text
        product=" ".join(brut_product.split())
        date=datetime.datetime.now()
        return(product, date, price)

#url='https://www.amazon.fr/Nouveau-Apple-13-pouces-Processeur-10e-génération/dp/B0863V6RNQ/ref=sr_1_8?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=macbook+pro&qid=1590674621&sr=8-8'

#print(url_parser(url))


    