from random import randint

print("\nPedra, Papel ou Tesoura?\n")
print("Suas Opções: ")
print("[ 1 ] Pedra")
print("[ 2 ] Papel")
print("[ 3 ] Tesoura")
escolha = int(input("Qual é a sua jogada? "))


while escolha != -1:
    item = ('pedra', 'papel', 'tesoura')
    maquina = randint(0,2)
    maquinatx = item[maquina]
    escolhatx = item[escolha - 1]
    if maquina == 0:
        if escolha == 1:
            print(f"vc {escolhatx} maquina {maquinatx}")
            print("empate 0")
            escolha = int(input("Qual é a sua jogada? "))

        elif escolha == 2:
            print(f"vc {escolhatx} maquina {maquinatx}")
            print("derrota 0")
            escolha = int(input("Qual é a sua jogada? "))

        elif escolha == 3:
            print(f"vc {escolhatx} maquina {maquinatx}")
            print("Vitoria 0")
            escolha = int(input("Qual é a sua jogada? "))

    if maquina == 1:
        if escolha == 1:
            print(f"vc {escolhatx} maquina {maquinatx}")
            print("Derrota 1")
            escolha = int(input("Qual é a sua jogada? "))

        elif escolha == 2:
            print(f"vc {escolhatx} maquina {maquinatx}")
            print("Empate 1")
            escolha = int(input("Qual é a sua jogada? "))

        elif escolha == 3:
            print(f"vc {escolhatx} maquina {maquinatx}")
            print("Vitoria 1")
            escolha = int(input("Qual é a sua jogada? "))
                
    if maquina == 2:
        if escolha == 1:
            print(f"vc {escolhatx} maquina {maquinatx}")
            print("Vitoria 2")
            escolha = int(input("Qual é a sua jogada? "))

        elif escolha == 2:
            print(f"vc {escolhatx} maquina {maquinatx}")
            print("Derrota 2")
            escolha = int(input("Qual é a sua jogada? "))

        elif escolha == 3:
            print(f"vc {escolhatx} maquina {maquinatx}")
            print("Empate 2")
            escolha = int(input("Qual é a sua jogada? "))