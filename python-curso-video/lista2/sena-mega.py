from random import randint
from time import sleep



jogos = int(input("Quantos jogos você deseja que eu sorteie? "))
for j in range(1,jogos+1):
    bilhete = []
    while len(bilhete) < 6:
        
        n = randint(1,60)
        if n not in bilhete:
            bilhete.append(n)
    bilhete.sort()
    print(f"O {j}° jogo é {bilhete}")
    sleep(0.5)
    print()