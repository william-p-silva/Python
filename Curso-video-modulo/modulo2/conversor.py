def dobro(n=0, formt=False):
    """
    Função que retorna o dobro de um número.
    :param n: número a ser dobrado
    :return: dobro do número
    """
    res = n * 2
    return res if not formt else moeda(res)


def metade(n=0, formt=False):
    res = n / 2
    
    return res if formt is False else moeda(res)


def aumentar(n=0, p=0, formt=False):
    res = n + (n * p/100)
    return res if formt is False else moeda(res)


def diminuir(n=0, d=0, formt=False):
    res = n - (n * d/100)
    return res if not formt else moeda(res)


def moeda(n=0, moeda='R$'):
    return f"{moeda}{n:.2f}".replace('.',',')



def tudo(n=0, d=10, p=20, f=False):
    cabeça(n)
    print("\n",diminuir(n,d,f),"\n", aumentar(n,p,f),"\n", dobro(n,f),"\n", metade(n,f))
    footer()

def cabeça(n):
    print("==" * 30)
    print(f"{'RESUMO DO VALOR':^50}")
    print("==" * 30)
    print(f"ANALISANDO O VALOR {n}")
    print("==" * 30)


def footer():
    print("==" * 30)
    print("==" * 30)