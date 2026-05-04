
cha = int(input())
suposicao = str(input())
acertos = 0
tentativa = suposicao.split(" ")

for c in range(0, 5):
    if(int(tentativa[c]) == cha):
        acertos += 1

print(acertos)