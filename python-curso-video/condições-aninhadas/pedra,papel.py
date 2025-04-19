from random import randint
from time import sleep

print("\n")
print("\033[35m-=-"*16)
print("Pedra, Papel ou Tesoura?")
print("-=-"*16)

print("=-*"*16)
print("Suas Opções: ")
print("[ 1 ] Pedra")
print("[ 2 ] Papel")
print("[ 3 ] Tesoura")
escolha = int(input("Qual é a sua jogada? "))
print("=-*"*16)
print('\033[m')

while escolha != -1:
    item = ('pedra', 'papel', 'tesoura')
    maquina = randint(0,2)
    maquinatx = item[maquina]
    escolhatx = item[escolha - 1]
    print("\n\033[33mJO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO\033[m")
    sleep(1)
    if maquina == 0:
        if escolha == 1:
            print("\n\033[33mEmpate")
            print(f"O jogador escolheu {escolhatx} e o computador {maquinatx}\n\033[m")
            escolha = int(input("Qual é a sua jogada? "))
        elif escolha == 2:
            print("\n\033[32mVitoria")
            print(f"O jogador escolheu {escolhatx} e o computador {maquinatx}\n\033[m")
            escolha = int(input("Qual é a sua jogada? "))
        elif escolha == 3:
            print("\n\033[31mDerrota")
            print(f"O jogador escolheu {escolhatx} e o computador {maquinatx}\n\033[m")
            escolha = int(input("Qual é a sua jogada? "))


    elif maquina == 1:
        if escolha == 1:
            print("\n\033[31mDerrota")
            print(f"O jogador escolheu {escolhatx} e o computador {maquinatx}\n\033[m")
            escolha = int(input("Qual é a sua jogada? "))
        elif escolha == 2:
            print("\n\033[33mEmpate")
            print(f"O jogador escolheu {escolhatx} e o computador {maquinatx}\n\033[m")
            escolha = int(input("Qual é a sua jogada? "))
        elif escolha == 3:
            print("\n\033[32mVitoria")
            print(f"O jogador escolheu {escolhatx} e o computador {maquinatx}\n\033[m")
            escolha = int(input("Qual é a sua jogada? "))


    elif maquina == 2:
        if escolha == 1:
            print("\n\033[32mVitoria")
            print(f"O jogador escolheu {escolhatx} e o computador {maquinatx}\n\033[m")
            escolha = int(input("Qual é a sua jogada? "))
        elif escolha == 2:
            print("\n\033[31mDerrota")
            print(f"O jogador escolheu {escolhatx} e o computador {maquinatx}\n\033[m")
            escolha = int(input("Qual é a sua jogada? "))
        elif escolha == 3:
            print("\n\033[33mEmpate")
            print(f"O jogador escolheu {escolhatx} e o computador {maquinatx}\n\033[m")
            escolha = int(input("Qual é a sua jogada? "))
    else:
        print("[ERRO] Dados invalidos\n")
        escolha = int(input("Qual é a sua jogada? "))