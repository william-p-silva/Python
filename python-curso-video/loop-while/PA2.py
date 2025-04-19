i = int(input("Digite um número: "))
r = int(input("Digite um número: "))

c = 1
f = i
tot = 0
esc = 10
while esc != 0:
    tot = esc + tot
    while c <= tot:
        print(f)
        f = f + r
        c += 1
    esc = int(input("Quantos termos a mais? "))
        