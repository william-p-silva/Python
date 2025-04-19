print("\nPara qual base númerica você dejesa converter? ")
print("Binário [1]")
print("Octal [2]")
print("Hexadecimal [3]")

escolha = int(input("Digite sua escxolha: "))

if escolha == 1:
    conversão = int(input("\nDigite o número para conversão: "))
    print(f"O número {conversão} convertido em binário é {bin(conversão)[2:]}\n")
elif escolha == 2:
    conversão = int(input("\nDigite o número para conversão: "))
    print(f"O número {conversão} convertido em Octal é {oct(conversão)[2:]}\n")
elif escolha == 3:
    conversão = int(input("\nDigite o número para conversão: "))
    print(f"O número {conversão} convertido em Hexadecimal é {hex(conversão)[2:]}\n")
else:
    print("[ERRO] Verifique os dados e tente novamente \n")