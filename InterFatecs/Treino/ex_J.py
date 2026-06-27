def Verificar_Palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()
    return palavra == palavra[::-1]



palavra = str(input(""))

if palavra.strip() == "":
    print("")
else:
    if Verificar_Palindromo(palavra):
        print("SIM")
    else:
        print("NAO")
