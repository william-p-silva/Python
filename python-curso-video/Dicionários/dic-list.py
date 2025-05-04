

cadastro = {}
cadastrados = []
sexo = continuar = ' '
soma = 0
while True:
    cadastro['nome'] = str(input("Nome: ")).title()
    while sexo not in 'MF':
        sexo = str(input("Sexo: [M/F] ")).upper().strip()[0]
        if sexo in 'MF':
            cadastro['sexo'] = sexo
        else:
            print("[ERRO] Por favor, digite apenas M ou F")
    cadastro['idade'] = int(input("Idade: "))
    sexo = ' '
    while continuar not in 'sn':
        continuar = str(input("Deseja continuar? [S/N] ")).lower().strip()[0]
        if continuar in 'sn':
            break
        else:
            print("[ERRO] Por favor, digite S ou N")
    
    
    cadastrados.append(cadastro.copy())
    cadastro.clear()
    if continuar == 'n':
        break
    continuar= ' '


print("-="*30)

print(f"Ao todo foram cadastradas {len(cadastrados)} pessoas")
for i,v in enumerate(cadastrados):
    soma += cadastrados[i]['idade']
media = soma / len(cadastrados)
print(f"A média de idade é de {media:.2f} anos")

print("As mulheres cadastradas foram:", end=' ')
for i,v in enumerate(cadastrados):
    if cadastrados[i]["sexo"] == 'F':
        print(f"{cadastrados[i]["nome"]}.", end=' ')
print("\nLista de pessoas acima da média:")
for i,v in enumerate(cadastrados):
    if cadastrados[i]['idade'] > media:
        print(f"\tNome = {cadastrados[i]['nome']}; Sexo = {cadastrados[i]['sexo']}; {cadastrados[i]['idade']} anos")

print("<< ENCERRADO >>")
print()