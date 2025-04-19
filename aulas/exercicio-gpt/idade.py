# o programa vai descobrir a idade e classificar ela em uma faixa etaria
ano_nascimento = int(input("Digite o seu ano de nascimento: "))
idade = 2025 - ano_nascimento
if idade >=0 and idade < 12:
    print(f"Você tem {idade} anos e é considerado criança ")
elif idade >= 12 and idade < 18:
    print(f"Você tem {idade} anos e é considerado adolecente ")
elif idade >= 18 and idade < 60:
    print(f"Você tem {idade} anos e é considerado adulto ")
else:
    print(f"Você tem {idade} anos e é considerado idoso ")