e = 's'
n = 0

c = s = m = 0

while e == 's':
    n = int(input("Digite um número; "))
    e = str(input("Quer continuar? [S/N]: ")).lower().strip()
    c +=1 
    s += n
    if c == 1:
        maior = menor = n
    else:
        if n >= maior:
            maior = n 
        if n <= menor:
            menor = n
m = s / c
    
print(f"Foram digitados {c}. O menor número foi {menor} e o maior foi {maior}. A média foi {m}")