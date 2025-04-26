valor = []
while True:
    #você pode inverter a variavel qu vai mudar n = input
    # valor.append(n)
    valor.append(int(input("Digite um número: ")))
    n = valor[-1]
    if valor.count(n) >= 2:
        print(f"O número {n} já foi cadastrado por isso foi desconsiderado ")
        valor.pop()
    else:
        print("Valor adicionado com sucesso ")
    esc = input("Deseja continuar? [S/N] ").lower().strip()
    if esc == 'n':
        break
print(f"Esses foram os números cadastrados {valor.sort()}")