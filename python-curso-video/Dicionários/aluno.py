aluno = {}

aluno["Nome"] = str(input("Nome: "))
aluno["Média"] = float(input("Média: "))
if 0 <= aluno["Média"] <= 5:
    situação = "Reprovado"
elif 5 < aluno["Média"] < 7:
    situação = "Recuperação"
elif 7 < aluno["Média"] < 10:
    situação = "Aprovado"
elif aluno["Média"] == 10:
    situação = "Aprovado com Honra"
else:
    print("[ERRO]")

aluno["Situação"] = situação
for c, v in aluno.items():
    print(f"-- {c} é igual a {v}")