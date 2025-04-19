#esse programa deve descobrir se um número é par ou ímpar
print("digite -1 para parar")
num = int(input("Digite um número inteiro: "))

#o loop vai pedir sempre um número novo
# o -1 é para parar 
while num != -1:
    if num % 2 != 0:
        print(f"O número {num} é ímpar ")
    elif num % 2 == 0:
        print(f"O número {num} é par ")
    else:
        print("[ERRO] Verifique os dados e tente novamente")
    num = int(input("Digite um número inteiro: "))