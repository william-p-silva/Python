from datetime import date

maior = 0
menor = 0
ano = date.today().year
for c in range(1, 8):
    nasc = int(input(f"Em que ano a {c}° pessoa nasceu? "))
    
    idade = ano - nasc
    if idade >= 18:
        maior += 1
    elif idade < 18:
        menor += 1
    else:
        print("[ERRO]")
        
print(f"Ao todo temos {maior} pessoa maiores de idade ")
print(f"Ao todo temos {menor} pessoa menores de idade ")
