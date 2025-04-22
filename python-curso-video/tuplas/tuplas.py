lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
# c = comida
for c in range(0, len(lanche)):
    #caso eu queira mostrar o dado e a posição do dado 
    print(f"Comi {lanche[c]} na posição {c}")

print('\n')
for c in lanche:
    #caso só precise do dado sem a posição
    print(f"Comi {c}")

print('\n')

for pos, c in enumerate(lanche):
    #caso eu queira mostrar o dado e a posição do dado só que mais dificil 
    print(f"Comi {c} na posição {pos}")
print('\n')

print(sorted(lanche))