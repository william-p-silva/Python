from random import randint
from time import sleep

print("\n")
print("\033[4;31m-=-\033[m"*26)
print("\033[1;34mEstou pensando em um número de 0 a 10. Você seria capz de adivinhar qual é? ")
print("Você pode parar digitando 99\033[m")
print("\033[4;31m-=-\033[m"*26)
print("\n")

v = 0
d = 0
while True:
    escolha = (input("Digite o número que estou pensando: "))
    print("PROCESSANDO...\033[m")
    sleep(1)
    if escolha.isdigit() and len(escolha) != 0:
        if int(escolha) == 99:
            break
        else:
        
            num = randint(0, 10)
            if num == int(escolha):
                print("\n")
                print("\033[1;32m-=-"*26)
                print("PARABÉNS!!!!!")
                print(f"Isso mesmo estou pensando no número {escolha}")
                print("-=-"*26)
                print("\033[m\n\033[33mvocê pode parar digitando -1")
                v += 1
            
                
            elif int(escolha) < 11 and int(escolha) >= 0:
                print("\n")
                print("\033[31m-=-"*26)
                print(f"infelizmente ({escolha}) não era meu número" )
                print(f"O número que eu estava pensando era {num}")
                print("-=-"*26)
                print("\033[m\n\033[33mvocê pode parar digitando -1")
                d += 1

    else:
        print("\033[1;31m[ERRO] Tente novamente\033[m")
                

print(f"\033[1;34mVocê Ganhou {v} vezes e perdeu {d} vezes\033[m")