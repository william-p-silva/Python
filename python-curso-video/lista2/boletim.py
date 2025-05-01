boletim = []
notas = []
alunos = []
e = ' '
soma = media = 0

while True:
    nome = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    while e not in 'sn':
        e = input("Quer continuar? [S/N] ").lower().strip()[0]
    boletim.append([nome, [nota1, nota2]])
    
    if e == 'n':
        break
    e = ' '
print("-=-"*35)
print(f"{"n°.":<6}{"nome":<10}{"média":>11}")
for l, n in enumerate(boletim):
    soma = n[1][0] + n[1][1]
    media = soma / 2
    print(f"{l:<6} {n[0]:<10} {media:>8.2f}")
print("-=-"*35)
while True:
    nota_aluno = int(input("Mostrar notas de qual aluno? (999 interrompe) "))
    if nota_aluno >= 0 and nota_aluno <= len(boletim):
        print(f"\nAs notas do aluno {boletim[nota_aluno][0]} são {boletim[nota_aluno][1]}")
    else:
        print("\nAluno não encontrado!!")
    if nota_aluno == 999:
        break
print()
print("-=-"*35)
print("VOLTE SEMPRE")
print("-=-"*35)