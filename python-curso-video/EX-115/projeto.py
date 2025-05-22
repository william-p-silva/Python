from funções import decoração
from funções import funções
from time import sleep
from arquivo import *


arq = 'pessoas.txt'
if not arquivoExiste(arq):
    print('Arquivo não encontrado, criando arquivo...')
    criarArquivo(arq)
while True:
    decoração.cabeça("MENU PRINCIPAL")
    decoração.menu(['Ver pessoas Cadastradas', 'Cadastrar Pessoas', 'SAIR DO SISTEMA'])
    n = funções.escolha("Sua opção: ")
    if n == 0 or n == 3:
        decoração.cabeça('\033[31mSaindo do sistema...\033[m')
        sleep(2)
        break
    else:
        if n == 1:
            lerArquivo(arq)
            sleep(2)
        elif n == 2:
            decoração.cabeça("CADASTRAR PESSOA")
            nome = str(input('Nome: '))
            idade = funções.leiaInt('Idade: ')

            if idade == -1:
                print('\033[31mERRO! Não foi possível cadastrar a pessoa.\033[m')
    
            cadastrar(arq, nome, idade)
            sleep(2)


