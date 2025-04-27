

n = []
e = ' '
while True:
    n.append(int(input("Digite um número: ")))
    while e not in 'sn':
        e = input("Deseja continuar? [S/N] ").lower().strip()[0]

    if e == 'n':
        break

    e = ' '
n.sort(reverse=True)
print("=="*25)
print(f"Você digitou {len(n)} elementos")
print(f"Os valores em ordem decrescente são {n}")
if n.count(5) != 0: #if 5 in n: outra opção
    print("O valor 5 faz parte da lista")
else:
    print("O valor 5 não faz parte da lista")