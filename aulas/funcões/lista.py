
def maior(l):
    maior = l[0]
    for c in l:
        if c > maior:
            maior = c
    return maior



lista = [5, 6, 9, 55, 12, 33, 99]
print(maior(lista))