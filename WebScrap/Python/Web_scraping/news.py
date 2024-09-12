import requests
from bs4 import BeautifulSoup

resp=requests.get('https://g1.globo.com')

content=resp.content

site=BeautifulSoup(content,'html.parser')
#html da noticia
noticia=site.find('div',attrs={'class':'feed-post-body'})
#titulo
titulo=noticia.find('a',attrs={'class':'feed-post-link'})
#print(noticia.prettify())
print(titulo.text)#o .text vai pegar somente o texto escrito no link 

subtitulo=noticia.find('div',attrs={'class':"feed-post-body-resumo"})#achei o subtitulo na noticia e botei pra procurar
print(subtitulo.text)