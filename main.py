import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math

url = 'https://www.kabum.com.br/espaco-gamer/cadeiras-gamer'

headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.85"}

site = requests.get(url, headers=headers)
Soup = BeautifulSoup(site.content,'html.parser')

qtd_itens = Soup.find('div', id='listingCount').get_text().strip()

index = qtd_itens.find(' ')
qtd = qtd_itens[:index]

ultima_pag = math.ceil(int(qtd)/ 10)

dic_produtos = {'marca':[], 'preco':[]}

for i in range(1, ultima_pag+1):
    url_pag = f'https://www.kabum.com.br/espaco-gamer/cadeiras-gamer?page_number={i}&page_size=20&facet_filters=&sort=most_searched'
    site = requests.get(url_pag, headers=headers)
    Soup = BeautifulSoup(site.content,'html.parser')
    produtos = Soup.find_all('div', class_=re.compile('productCard'))

    for produto in produtos:
        marca = produto.find('span', class_= re.compile('nameCard')).get_text().strip()
        preco = produto.find('span', class_= re.compile('priceCard')).get_text().strip()

    print(marca, preco)

    dic_produtos['marca'].append(marca)
    dic_produtos['preco'].append(preco)

    print(url_pag)

    df = pd.DataFrame(dic_produtos)
    df.to_csv('mydesktop/docks/webscraping.csv', encoding='uyf-8', sep= ';')





