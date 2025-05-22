


lista = [4, 2 , 5, 1, 3]
organizada = []
menor = lista[0]
i = 0


print(lista)

while i < len(lista):
    
    j = 0
    while j < len(lista):
        if menor > lista[j]:
            menor = lista[j]

        j += 1
    
    organizada.append(menor)
    lista.remove(menor)
    if len(lista) > 0:
        print(lista[0])
        menor = lista[0]


print()
print(organizada)


