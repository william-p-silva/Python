
lista = []
dados = []
e = ' '
maior = menor = 0
while True:
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Peso: ")))
     
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    while e not in 'sn':
        e = input("Deseja continuar? [S/N] ").lower().strip()
    if e == 'n':
        break
    e = ' '   
print("=-="*30)
print(f"Ao todo foram cadastradas {len(lista)} pessoas ")
print(f"\nO maior peso foi {maior}Kg. De", end=' ')
for p in lista:
    if p[1] == maior:
        print(f"[{p[0]}]", end=' ')
print(f"\nO menor peso foi {menor}Kg. De", end=' ')
for p in lista:
    if p[1] == menor:
        print(f"[{p[0]}]", end=' ')
print('\n')
print('-=-'*30)
