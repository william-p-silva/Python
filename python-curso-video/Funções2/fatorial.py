

def fatorial(n, show=False):
    """
    Função para calcular o fatorial de um número.
    :param n: número inteiro
    :return: retorna o fatorial do número
    """
    if n == 0 or n == 1:
        return 1
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(f"{c}", end=' ')
            if c > 1:
                print(f" X ", end=' ')
            else:
                print(f" = ", end=' ')
    return f"{f}"
    

print(fatorial(5, show=True))  # Saída: 120