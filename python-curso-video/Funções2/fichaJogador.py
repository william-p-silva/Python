

def ficha(n=0, g=0):
    """
    Função para mostrar a ficha do jogador.
    :param n: nome do jogador
    :param g: número de gols
    :return: retorna a ficha do jogador
    """
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
    if len(n) == 0:
        n = "<desconhecido>"
    if g == 0:
        g = 0
    print(f"O jogador {n} fez {g} gols")


n = str(input("Nome do jogador: "))
p = input("Número de gols: ")

ficha(n,p)