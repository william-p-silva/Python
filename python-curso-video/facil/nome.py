nome = str(input("Digite seu nome: ")).strip().lower()
print(f"\nA letra A aparece {nome.count('a')} vezes")
print(f"A primeira letra A está em {nome.find('a')+1}")
print(f"A ultima letra A está em {nome.rfind('a')}")