def numInt(msg):
    while True:
        try:
            n = int(input(msg))
            
        except (ValueError, TypeError):
            print('Número inválido, digite novamente.')
            continue
        except (KeyboardInterrupt):
            print('\nEntrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n

def numReal(msg):
    while True:
        try:
            n = float(input(msg))
            
        except (ValueError, TypeError):
            print('Número inválido, digite novamente.')
            continue
        except KeyboardInterrupt:
            print('\nEntrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n
    

num1 = numInt('Digite um número inteiro: ')
num2 = numReal('Digite um número real: ')

print(f"O número inteiro digitado foi {num1} e o número real foi {num2}.")