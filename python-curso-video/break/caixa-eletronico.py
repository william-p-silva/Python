

valor = int(input("Quanto você deseja sacar? R$"))
tot = valor
ced = 200
totced = 0


while True:
    if tot >= ced:
        tot -= ced 
        totced += 1
        
    else:
        if totced > 0:
            print(f"Total de {totced} cédulas de R${ced}")
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2 
        elif ced == 2:
            ced = 1
        totced = 0
        if tot == 0:
            break
