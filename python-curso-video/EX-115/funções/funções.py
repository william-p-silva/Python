from funções import decoração
from time import sleep



def escolha(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não continuar.\033[m')
            return 0
        else:


            if 0 < valor < 4:
                return valor
            else:
                print('\033[31mERRO! Digite um número entre 1 e 3.\033[m')
                sleep(1)
                decoração.menu()
                continue
        

def leiaInt(n):
    while True:
        try:
            valor = int(input(n))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não continuar.\033[m')
            return -1
        else:
            return valor
