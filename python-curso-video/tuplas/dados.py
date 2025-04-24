num = (int(input("Digite um número: ")), int(input("Digite um número: ")),
       int(input("Digite um número: ")), int(input("Digite um número: ")),)

par = 0
print(f"Foram digitados os valores:", end='')
for i in num:
    print(f" {i} ", end=' ')
    if i % 2 ==0:
        par +=1

print(f"\nForam digitados {num.count(9)} números 9")
if num.count(3) != 0:

    print(f"O 3 apareceu pela primeira vez na posição {num.index(3)+1}")
else:
    print(f"O 3 não apareceu")
print(f"E tivemos {par} números pares")