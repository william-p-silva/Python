
menor = 0 
maior = 0
for c in range(1, 6):
    peso = float(input(f"Qual o peso da {c}° pessoa? "))
    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso < menor:
            menor = peso 
        elif peso > maior :
            maior = peso
        else:
            print("[ERRO]")
print(f"O maior peso foi {maior} ")
print(f'O menor peso foi {menor} ')
