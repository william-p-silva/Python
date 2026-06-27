

velocidade = int(input(""))

if velocidade <= 107:
    velocidadeMaxima = velocidade + 7
else:
    velocidadeMaxima = velocidade * 1.07

print(f"{velocidadeMaxima:.0f}")