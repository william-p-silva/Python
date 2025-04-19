frutas = ('maça', 'banana', 'laranja', 'uva')
if 'banana' in frutas:
    print('Eatá em frutas')
frutas_copia = list(frutas)
frutas_copia.append('abacaxi')
frutas = tuple(frutas_copia)
print(frutas)