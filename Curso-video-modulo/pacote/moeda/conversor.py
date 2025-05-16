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
    print(f"Subtraindo {d}% de {moeda(n)} é igual: {diminuir(n,d,f):<10}")
    print(f"Aumentando {p}% de {moeda(n)} é igual: {aumentar(n,p,f):<10}")
    print(f"O dobro de {moeda(n)} é igual: {dobro(n,f):<10}")
    print(f"A metade de {moeda(n)} é igual: {metade(n,f):<10}")
    
    footer()

def cabeça(n):
    print("==" * 30)
    print(f"{'RESUMO DO VALOR':^50}")
    print("==" * 30)
    print(f"ANALISANDO O VALOR {moeda(n)}")
    print("==" * 30)


def footer():
    print("==" * 30)
    print("==" * 30)