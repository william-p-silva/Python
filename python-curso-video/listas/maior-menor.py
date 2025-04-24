

valores = []
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input("Digite um número: ")))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print(valores)
print(f"O menor valor foi {menor} nas posições: ", end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f" {i}... ",end='')
print(f"\nO maior valor foi {maior}nas posições: ", end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f" {i}...", end='')