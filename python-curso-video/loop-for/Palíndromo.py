#descobrindo se uma frase é igual ao seu inverso :)

frase = str(input("Digite uma frase: ")).strip().lower()
separada = frase.split()
junta = "".join(separada)
#inv = '' pode ser feito com for 
inv = junta[::-1]
'''for letra in range(len(junta) -1, -1, -1):
    inv += junta[letra]'''#feito com for 
if inv == junta:
    print(f"A frase {junta} é um Palíndromo pois seu inverso é {inv}")
else:
    print(f"A frase {frase} não é um Palíndromo pois seu inverso fica {inv}")