from time import sleep

def valor(*num):
    """
    Função que recebe vários números e retorna o maior deles.
    :param num: números a serem analisados
    :return: maior número
    """
    
    print('-=' * 30)
    sleep(1)
    print('Analisando os valores passados...')
    if len(num) == 0:
        print('Nenhum valor foi informado.')
    elif len(num) == 1:
        print('Apenas um valor foi informado.')
        print(f'{num[0]} ', end='', flush=True)
        print()
        sleep(0.3)
    else:
        for n in num:
            print(f'{n} ', end='', flush=True)
            sleep(0.3)
        maior = max(num)
        sleep(1)
        print(f'\nO maior valor informado foi {maior}')
    sleep(1)
    print("fim")
    
    print('-=' * 30)
valor(5,3,6,88)
valor(1, 2, 3)
valor(4, 5)
valor(2)
valor(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)