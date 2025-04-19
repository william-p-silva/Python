print("Digite dois números e o programa dira qual é o maior")
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
if num1 > num2:
    maior_num = num1
    print(f"O maior número entre {num1} e {num2} é o número {maior_num}")
elif num2 > num1:
    maior_num = num2 
    print(f"O maior número entre {num1} e {num2} é o número {maior_num}")
elif num1 == num2:
    print(f"Os números {num1} e {num2} são iguais")
else:
    print("[ERRO] dados invalidos")
