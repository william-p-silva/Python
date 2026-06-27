abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
       "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
       "u", "v", "w", "x", "y", "z"]

entrada = input("").split(" ")

numRep = int(entrada[0])
minOuMai = entrada[1]

# transforma em maiúsculo se precisar
if minOuMai == "maiusculas":
    for i in range(len(abc)):
        abc[i] = abc[i].upper()

for l in range(numRep):

    listFinal = []

    # cria 26 pontos
    for c in range(26):
        listFinal.append(".")

    # coloca as letras no final
    inicio = 26 - (l + 1)

    for a in range(l + 1):
        listFinal[inicio + a] = abc[a]

    # imprime linha
    for item in listFinal:
        print(item, end="")

    print("")