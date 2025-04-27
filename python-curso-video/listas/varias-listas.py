

lista = []
lista_par = []
lista_impar = []
e= ' '
while True:
    n = int(input("Digite um número: "))
    
    
    lista.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    if n % 2 != 0:
        lista_impar.append(n)
    
    e = ' '
    while e not in 'sn':
        e = input("Deseja continuar? [S/N] ").lower().strip()
    if e == 'n':
        break
print(f"\nA lista completa é {lista}")
print(f"Você dogitou esses números pares {lista_par}")
print(f"Você dogitou esses números ímpares {lista_impar}")