from random import randint
from time import sleep

print("\n")
print("-=-"*26)
print("Estou pensando em um número de 0 a 10. Você seria capz de adivinhar qual é? ")
print("Você pode parar digitando -1")
print("-=-"*26)
print("\n")

escolha = (input("Digite o número que estou pensando: "))
print("PROCESSANDO...")
sleep(1)
while escolha != -1:
    if escolha.isdigit() and len(escolha) != 0 and int(escolha) < 10 and int(escolha) > 0:
        num = randint(0, 10)
        if num == int(escolha):
            print("\n")
            print("-=-"*26)
            print("PARABÉNS!!!!!")
            print(f"Isso mesmo estou pensando no número {escolha}")
            print("você pode parar digitando -1")
            print("-=-"*26)
            escolha = (input("\nDigite o número que estou pensando: "))
            print("\nPROCESSANDO...")
            sleep(1)
            
        else:
            print("\n")
            print("-=-"*26)
            print(f"infelizmente ({escolha}) não era meu número" )
            print(f"O número que eu estava pensando era {num}")
            print("-=-"*26)
            print("\nvocê pode parar digitando -1")
            escolha = (input("Digite o número que estou pensando: "))
            print("\nPROCESSANDO...")
            sleep(1)
    else:
        print("[ERRO] Tente novamente")
        escolha = (input("Digite o número que estou pensando: "))
        print("\nPROCESSANDO...")
        sleep(1)