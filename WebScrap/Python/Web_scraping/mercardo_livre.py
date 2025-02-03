import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_produtos = []

p = str(input('Digite o nome do produto que deseja: '))
url_base = 'https://lista.mercadolivre.com.br/'
url_produto = url_base + p + '#D[A:{p}]'
response = requests.get(url_produto)
site = BeautifulSoup(response.text, 'html.parser')

# Usando a classe correta para os produtos
produtos = site.find_all('li', attrs={'class': 'ui-search-layout__item'})

for produto in produtos:
    titulo_element = produto.find('a', attrs={'class': 'poly-component__title'})
    moeda_element = produto.find('span', attrs={'class': 'andes-money-amount__currency-symbol'})
    link_element = produto.find('a', attrs={'class': 'poly-component__title'})
    real_element = produto.find('span', attrs={'class': 'andes-money-amount__fraction'})
    centavos_element = produto.find('span', attrs={'class': 'andes-money-amount__cents andes-money-amount__cents--superscript-24'})

    if titulo_element and link_element and moeda_element and real_element:
        titulo = titulo_element.text.strip()
        link = link_element['href']
        moeda = moeda_element.text.strip()
        real = real_element.text.strip()
        centavos = centavos_element.text.strip() if centavos_element else '00'
        lista_produtos.append([titulo, link, moeda, real, centavos])
    else:
        print('Não foi possível encontrar todas as informações do produto.')
    print('\n\n')

tabela = pd.DataFrame(lista_produtos, columns=['Título', 'Link', 'Moeda', 'Real', 'Centavos'])
tabela.to_excel('produtos.xlsx', index=False)
