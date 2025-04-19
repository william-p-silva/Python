lado1 = float(input("Digite o comprimento segmento: "))
lado2 = float(input("Digite o comprimento segmento: "))
lado3 = float(input("Digite o comprimento segmento: "))
if lado1 < lado2 + lado3 and lado2 < lado3 + lado1 and lado3 < lado2 + lado1:
    print("\nTriângulo valido")
    if lado1 == lado2 and lado2 == lado3: #pode ser feito assim if lado1 == lado2 == lado3
        print(f"O triângulo com lados {lado1}, {lado2} e {lado3} é um triangulo equilátero ")
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print(f"O triângulo com lados {lado1}, {lado2} e {lado3} é um triangulo isóseles ")
    elif lado1 != lado2 and lado3:
        print(f"O triângulo com lados {lado1}, {lado2} e {lado3} é um triangulo escaleno ")
else:
    print("[ERRO] O triângulo não é valido ")