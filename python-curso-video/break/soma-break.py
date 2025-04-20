s = c = 0
while True:
    n = int(input("Digite um número (digite -1 para parar): "))
    if n == -1:
        break
    c += 1
    s += n 
print(f"Você digitou {c} números")
print(f"A soma dos números foi {s}")