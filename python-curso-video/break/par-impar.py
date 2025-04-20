from random import randint
f = c = v = d = 0 #f = resultado(pc + user) c = variavel de controle v=vitoria d=derrota
print("\nVamos jogar par ou ímpar")
while True:
    if c < 4:
        n = int(input("\nDigite um número: "))
        e = str(input("Qual sua escolha [P/I]? ")).lower().strip()
        a = randint(1, 10)
        while e not in "pi":
            e = str(input("Qual sua escolha [P/I]? ")).lower().strip()[0]
        if e == 'i':
            f = a + n
            if f % 2 == 0:
                print("Você perdeu :(")
                d += 1
                print(f"O computador escolheu {a} e você {n} a soma foi {f}\n")
                #variante com {break} caso o jogador perca o jogo acaba
            elif f % 2 != 0:
                print("Você ganhou :)")
                v += 1
                print(f"O computador escolheu {a} e você {n} a soma foi {f}\n")
        elif e == 'p':
            f = a + n
            if f % 2 != 0:
                print("Você perdeu :(")
                d += 1
                print(f"O computador escolheu {a} e você {n} a soma foi {f}\n")
                #variante com {break} caso o jogador perca o jogo acaba 
            elif f % 2 == 0:
                print("Você ganhou :)")
                v += 1
                print(f"O computador escolheu {a} e você {n} a soma foi {f}\n")
        
    else:
        break
    c += 1
print(f"\nVocê ganhou {v} e perdeu {d} \nAcabou\n")