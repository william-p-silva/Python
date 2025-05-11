def leiaInt(msg):
    f = False
    numero = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            numero = int(n)
            f = True
            
        else:
            print("Erro! Digite um número inteiro válido.")
        if f:
            break
    return numero
n = leiaInt("Digite um número inteiro: ")
print(f"Você digitou o número {n}")