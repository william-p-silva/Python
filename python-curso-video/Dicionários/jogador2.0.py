


clube = []
gol = []
jogador = {}
c = 0

while True:
    jogador['nome'] = str(input("Nome: ")).title()
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    for g in range(0, partidas):
        gol.append(int(input(f"\tQuantos gols na {g+1}ª partida? ")))
    jogador['gols'] = gol[:]
    jogador['totalGols'] = sum(gol[:])
    gol.clear()
    while True:
        res = str(input("Quer continuar? [S/N] ")).lower().strip()[0]
        if res in 'sn':
            break
    
    clube.append(jogador.copy())
    jogador.clear()
    if res == 'n':
        break


print('-='*35)
print(f"{'cod':>4}{'nome':<15}{'gols':<15}{'total de gols':<15}")

for k, v in enumerate(clube):
    print(f"{k:>4} ", end='')
    for d in v.values():
        print(f"{str(d):<15}", end='')
    print()
print('--'*35)
while True:
    res_jog = int(input("Mostrar dados de qual jogador? (-1 para parar)"))
    if res_jog == -1:
        break
    if res_jog >= len(clube):
        print("[ERRO] Jogador nã encontrado")
    else:
        print(f"\nLevantamento do jogador {clube[res_jog]['nome']}")
        for i, g in enumerate(clube[res_jog]["gols"]):
            print(f"\tNa partida {i+1} ele fez {g} gols")
print('--'*35)


print("<==ACABOU==>")
