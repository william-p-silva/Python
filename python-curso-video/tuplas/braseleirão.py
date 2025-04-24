




classificacao = ("Palmeiras", "Flamengo", "Fluminense", "Bragantino","Ceará SC", "Corinthians", "Cruzeiro", "Vasco da Gama","Juventude", "Sã Paulo", "Mirassol", "Internacional","Bahia", "Fortaleza", "Botafogo", "EC Vitória","Atlético-MG", "Santos", "Grêmio", "Sport Recife")  

print(f"\nClassificação atualizada do Brasileirão 2025\n{classificacao}")
print(f"\nOs 5 primeiros colocados\n{classificacao[0:5]}")
print(f"\nOs 4 ultimos colocados\n{classificacao[-4:]}")
print(f"\nOrdem alfabetica\n{sorted(classificacao)}")
print(f"\nO Corinthians está na {classificacao.index("Corinthians") +1}ª posição")