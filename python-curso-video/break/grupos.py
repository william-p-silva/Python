

maior_idade = menor_idade = feminino = masculino = f_maior = f_menor = c = 0
e = 's'
while True:
    if e == 's':
    
        print("Cadastre uma pessoa")
        idade = int(input("Digite a idade: "))
        genero = ' '
        e = ' '
        while genero not in 'mf':
            genero = str(input("[M/F] ")).lower().strip()[0]
            if genero in "mf" and idade  > 0 and idade < 200 :
                if idade >= 18:
                    maior_idade += 1
                elif idade < 18:
                    menor_idade += 1
                if genero == 'm':
                    masculino += 1
                if genero == 'f':
                    feminino += 1
                if genero == 'f' and idade > 17:
                    f_maior += 1
                elif genero == 'f' and idade < 17:
                    f_menor += 1
            else:
                print("[ERRO]")
                
                c += 1
        while e not in 'sn':
            e = str(input("Quer continuar? ")).lower().strip()[0]
        
    else:
        print("Acabou")
        break
print(f"\nForam cadastradas {c} pessoas")
print(f"Sendo {masculino} Homens e {feminino} Mulheres")
print(f"A {maior_idade} pessoas maiores de 18 anos e {menor_idade} menores de 18 anos")
print(f"Sendo {f_maior} Mulheres maiores de idade e {f_menor} menores de idade")