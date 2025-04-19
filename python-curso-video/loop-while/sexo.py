
sexo = str(input("Qual seu gênero? [M/F] ")).lower().strip()

while sexo not in 'FmMf': #quando for usar str a validação deve usar in 
    sexo = input("Qual seu gênero? [M/F] ")

print(f"Então seu gênero é {sexo}")