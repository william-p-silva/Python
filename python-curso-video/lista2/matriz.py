matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma_par = soma_col = 0



for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um valor: [{l}][{c}] "))


print("-=-"*30)
for l in range(0,3):
    for c in range(0,3):
        print(f" [{matriz[l][c]: ^6}] ", end=' ')
    print()
       # if c == 2:
            #print() essa foi minha tentativa paia
print("-=-"*30)
for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
            
        if c == 2:
            soma_col += matriz[l][c]
            
    if l == 1:
        maior = max(matriz[l])
print("-=-"*30)
print(f"A soma dos números pares é {soma_par}")
print(f"A soma dos números da terceira coluna é {soma_col}")
"""Outra opção para soma da coluna 2
for l in range(0,3):
        soma_col += matriz[l][2]"""
print(f"O maior valor da linha dois é {maior}")

