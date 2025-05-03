


estat = {}
gol = []
tot = 0
c = 1
estat["nome"] = input("Nome do jogador: ")
partidas = int(input(f"Quantas partidas {estat['nome']} jogou? "))
for p in range(0, partidas):
    g = int(input(f"Quantos gols {estat['nome']} fez na {p+1}ª partida: "))
    tot += g
    gol.append(g)
    #gol.append(int(input(f"Quantos gols {estat['nome']} fez na {p+1} partida")))

estat["gols"] = gol
estat['total'] = tot
print("-="*30)
print(estat)
print("-="*30)

for k, v in estat.items():
    print(f"O campo {k} tem valor {v}")
print("-="*30)

print(f"O jogador {estat['nome']} jogou {partidas} partidas")
for gl in estat['gols']:
    print(f"   => Na partida {c}, fez {gl} gols")
    c += 1
print(f"Foi um total de {tot} gols")