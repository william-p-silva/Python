from funções import decoração
from funções import funções
from time import sleep


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
            decoração.cabeça("OPÇÃO 1")
            sleep(2)
        elif n == 2:
            decoração.cabeça("OPÇÃO 2")
            sleep(2)


