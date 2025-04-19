import random
computador = random.randint(1, 10)
tentativas = 0
acertou = False
while not acertou:
    escolha = int(input("Digite um número entre 1 e 10: "))
    tentativas += 1
    if escolha > computador:
        print("Quase. Tente um número menor")
    elif escolha < computador:
        print("Quase. Tente um número maior")
    elif escolha == computador:
        print(f"Isso mesmo o meu número é {computador}")
        print(f"Você conseguiu com {tentativas} tentativas")
        acertou = True
    
