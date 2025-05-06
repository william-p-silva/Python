from random import randint
def sorteio():
    print('\nSorteando 5 valores da lista: ', end='')
    sorteados = []
    for i in range(5):
        n = randint(1, 10)
        print(f'{n} ', end='', flush=True)
        sorteados.append(n)
    return sorteados
def somaPar(numeros):
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'\nSomando os valores pares de {numeros}, temos {soma}')
valores = sorteio()

somaPar(valores)