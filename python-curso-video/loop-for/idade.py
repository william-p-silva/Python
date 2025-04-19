import datetime


ano_atual = datetime.date.today().year
menor = 0
maior = 0
for c in range(1, 7):
    ano_nasc = int(input(f"Digite o ano de nascimento da pessoa {c}: "))
    idade = ano_atual - ano_nasc
    if idade < 18:
        menor += 1
    else:
        maior += 1
print(f"Foram detctadas {menor} pessoas menores de idade e {maior} pessoas maiores de idade")