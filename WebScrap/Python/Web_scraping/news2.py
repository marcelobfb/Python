import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias=[]

resp=requests.get('https://g1.globo.com')

content=resp.content

site=BeautifulSoup(content,'html.parser')
#html da noticia
noticias=site.findAll('div',attrs={'class':'feed-post-body'})
for noticia in noticias:
    #titulo
    titulo=noticia.find('a',attrs={'class':'feed-post-link'})
    #print(noticia.prettify())
    #print(titulo.text)#o .text vai pegar somente o texto escrito no link 
    #print(titulo['href'])#link da noticia
    subtitulo=noticia.find('div',attrs={'class':"feed-post-body-resumo"})#achei o subtitulo na noticia e botei pra procurar
    if (subtitulo):#se tiver subtitulo vai mostrar se n, n vai
        print(subtitulo.text)
        lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
    else:
        lista_noticias.append([titulo.text,'',titulo['href']])
news=pd.DataFrame(lista_noticias,columns=['Título','Subtitulo','Link'])#cria uma tabela
news.to_excel('noticias.xlsx',index=False)#o index é a numeração do lado esquerdo do titulo q salva por padrao se vc colocar false n vai salvar
#print(news)