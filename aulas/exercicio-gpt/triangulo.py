lado_a = float(input("Digite o tamanho de um lado do triângulo: "))
lado_b = float(input("Digite o tamanho de um lado do triângulo: "))
lado_c = float(input("Digite o tamanho de um lado do triângulo: "))
if (lado_a + lado_b > lado_c) and (lado_b + lado_c > lado_a) and (lado_a + lado_c > lado_b):
    print("O triangulo é valido ")
else:
    print("O triangulo é invalido ")