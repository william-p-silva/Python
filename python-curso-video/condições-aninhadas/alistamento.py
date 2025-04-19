import datetime



ano_nas = int(input("Digite seu ano de nascimento: "))
ano_atual = datetime.date.today().year 

idade = ano_atual - ano_nas

if idade > 18 and idade <= 19:
    print(f"Você deveria ter se alistado a {idade - 18} ano")
elif idade > 18:
    print(f"Você deveria ter se alistado a {idade - 18} anos")
elif idade < 18 and idade >= 17:
    print(f"Você ainda vai se alistar \nFalta {18 - idade} ano")
elif idade < 18:
    print(f"Você ainda vai se alistar \n Faltam {18 - idade} anos")
else:
    print("Você deve se alistar imediatamente ")