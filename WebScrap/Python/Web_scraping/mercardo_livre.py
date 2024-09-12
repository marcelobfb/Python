#obtendo produtos do mercado livre a partir de uma buscara realizada pelo usuario
import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_produtos=[]

p=str(input('Digite o nome do produto que deseja: '))
url_base='https://lista.mercadolivre.com.br/'
url_produto=url_base+p
response=requests.get(url_produto)
site=BeautifulSoup(response.text,'html.parser')
produtos=site.findAll('div',attrs={'class':'andes-card ui-search-result shops__cardStyles ui-search-result--core andes-card--flat andes-card--padding-16'})
for produto in produtos:
    titulo=produto.find('h2',attrs={'class':'ui-search-item__title shops__item-title'})
    moeda=produto.find('span',attrs={'class':'andes-money-amount__currency-symbol'})
    link=produto.find('a',attrs={'class':'ui-search-link'})
    real=produto.find('span',attrs={'class':'andes-money-amount__fraction'})
    centavos=produto.find('span',attrs={'class':'andes-money-amount__cents'})
    #print(produto.prettify())
    print(f'Titulo do produto: {titulo.text}')
    print('O link do produto é:', link['href'])
    if centavos:
        print(f'{moeda.text}{real.text},{centavos.text}')
        tabela=pd.DataFrame(lista_produtos.append([titulo.text,link['href'],moeda.text,real.text,centavos.text]))
    else:
        print(f'{moeda.text}{real.text},00')
        tabela=pd.DataFrame(lista_produtos.append([titulo.text,link['href'],moeda.text,real.text,'00']))
    print('\n\n')
produtin=pd.DataFrame(lista_produtos,columns=['Título','Link','Moeda','Real','Centavos'])
produtin.to_excel('produtos.xlsx',index=False)