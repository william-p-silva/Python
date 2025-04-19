def numero(x, y):
    try:
        float(x)
        float(y)
        return True
    except ValueError:
        return False
    
n1 = float(input("\nDigite um número; "))
n2 = float(input("Digite um número; "))
sair = True

while sair:
    print("\n[1] somar")
    print("[2] multiplicar")
    print("[3] maior")
    print("[4] novos números")
    print("[5] sair")
    esco = int(input("\nDIgite sua escolha: "))
    if esco == 1:
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}')
    elif esco == 2:
        mul = n1 * n2
        print(f'{n1} X {n2} = {mul}')
    elif esco == 3:
        if n1 > n2:
            print(f"O maior número é {n1}")
        elif n2 > n1:
            print(f"O maior número é {n2}")
        elif n1 == n2:
            print("Os números são iguais")
    elif esco == 4:
        n1 = float(input("\nDigite um número; "))
        n2 = float(input("Digite um número; "))
    elif esco == 5:
        sair = False
    else:
        n1 = float(input("\nDigite um número; "))
        n2 = float(input("Digite um número; "))
