
lis = []
for c in range(0, 5):
    n = int(input("Digite um número: "))

    if c == 0 or n > lis[-1]:
        lis.append(n)
        print("Adicionado no final da lista")
    else:
        pos = 0 
        while pos < len(lis):
            if n <= lis[pos]:
                lis.insert(pos, n)
                print(f"Voê adicionou um número na posição {pos} ")
                break
            pos += 1
print("Voê digitou esses valores: ", lis)