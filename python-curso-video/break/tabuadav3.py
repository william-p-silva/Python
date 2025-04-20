c = t = 0

while True:
    n = int(input("Digite o número que deseja ver a tabuada: "))
    if n < 0:
        break
    else:
        if n >= 0:
            for c in range(1, 11): #while c <= 10: primeira tentativa foi com while ma scom for é melhor
                t = n * c
                print(f" {n} X {c} = {t}")
                c += 1
        #c = 0 é preciso caso use o while
print("Você terminou")