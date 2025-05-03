import datetime

trabalhador = {}
ano = datetime.date.today().year
trabalhador["nome"] = input("Nome: ")
nascimento = int(input("Ano de nascimento: "))
trabalhador['idade'] = ano - nascimento
trabalhador["ctps"] = int(input("Carteira de trabalho (0 caso não tenha): "))
if trabalhador["ctps"] != 0:
    trabalhador["contratação"] = int(input("Ano de contratação: "))
    trabalhador["salário"] = float(input("Salário: R$"))
print()
print("-="*30)

trabalhador["aposentadoria"] = trabalhador["contratação"] - nascimento + 35
for k, v in trabalhador.items():
    print(f"{k} tem valor {v}")