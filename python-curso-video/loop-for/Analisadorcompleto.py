


soma = 0
velho = 0


mulher_menor = 0 
mulher_maior = 0 
homem_menor = 0 
homem_maior = 0 


for c in range(1,5):
    print(f"======= {c}° pessoa =======")
    nome = str(input("Qual seu nome? ")).upper().strip()
    idade = int(input('Qual sua idade? '))
    sexo = str(input("Qual seu sexo [M/F] ")).upper().strip()

    soma += idade
    
    if sexo == 'F' and idade <= 21:
        mulher_menor += 1
    elif sexo == 'F' and idade > 21:
        mulher_maior += 1
    elif sexo == 'M' and idade <= 21:
        homem_menor += 1
    elif sexo == 'M' and idade > 21:
        homem_maior += 1
    if idade >= velho and sexo == "M":
        velho = idade
        nome_res = nome
print(f"A média das idades é {soma / c}")
print(f"O homem mais velho tem {velho} e seu nome é {nome_res}")
print(f"Na lista existem {mulher_menor} mulheres menores de 21 anos")