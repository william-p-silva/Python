

tupla = ('Lapis', 1.55, 
         'borracha', 2,
         'apontador', 5,
         'Tesoura', 15,
         'Caderno', 65,
         'Muchila', 88)




print(f"\n{"=-="*15}")
print(f"{"Lista de preços":^40}")
print(f"{"=-="*15}\n")
for pos in range(len(tupla)):
    if pos % 2 == 0:
        print(f"{tupla[pos]:.<30}", end=' ')
    else:
        print(f"R$ {tupla[pos]:>5.2f}")
print(f"\n{"=-="*15}\n")