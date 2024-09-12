from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq='cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resp == 1:
        #opção de listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resp == 2:
        #opção de cadastrar uma pessoa
        cabeçalho('NOVO CADASTRO')
        nome=str(input('Nome: ')).capitalize()
        idade=leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        #opção de sair do sistema
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        #digitou um opção errada no menu
        print('\033[31mERRO! Digite uma opção válida!\033[m')

