from random import randint
from time import sleep

print("\n")
print("\033[4;31m-=-\033[m"*26)
print("\033[1;34mEstou pensando em um número de 0 a 10. Você seria capz de adivinhar qual é? ")
print("Você pode parar digitando -1\033[m")
print("\033[4;31m-=-\033[m"*26)
print("\n")

escolha = (input("\033[33mDigite o número que estou pensando: "))
print("PROCESSANDO...\033[m")
sleep(1)
while escolha != "-1":
    if escolha.isdigit() and len(escolha) != 0 and int(escolha) < 11 and int(escolha) >= 0:
        num = randint(0, 10)
        if num == int(escolha):
            print("\n")
            print("\033[1;32m-=-"*26)
            print("PARABÉNS!!!!!")
            print(f"Isso mesmo estou pensando no número {escolha}")
            print("-=-"*26)
            print("\033[m\n\033[33mvocê pode parar digitando -1")
            escolha = (input("Digite o número que estou pensando: "))
            print("PROCESSANDO...\033[m")
            sleep(1)
            
        else:
            print("\n")
            print("\033[31m-=-"*26)
            print(f"infelizmente ({escolha}) não era meu número" )
            print(f"O número que eu estava pensando era {num}")
            print("-=-"*26)
            print("\033[m\n\033[33mvocê pode parar digitando -1")
            escolha = (input("Digite o número que estou pensando: "))
            print("PROCESSANDO...\033[m")
            sleep(1)
    else:
        print("\033[1;31m[ERRO] Tente novamente\033[m")
        escolha = (input("\033[33mDigite o número que estou pensando: "))
        print("PROCESSANDO...\033[m")
        sleep(1)