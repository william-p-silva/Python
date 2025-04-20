import math
import re

#Teorema de Pitágoras
print("\nSou Capaz de realizar o Teorema de Pitágoras")
print("Para isso preciso que você escolha o que deseja calcular:")
print("Se for calcular a hipotenusa digite [1] se for calcular um dos catetos digite [2]")



while True:
    escolha = (input("Digite sua escolha. Apenas números inteiros: "))
    if escolha == 1 or 2:
        if escolha.isdigit():#isdigit só aceita números inteiros e positivos
        #verifica se o valor diditado é um número
            if int(escolha) == 1 :
            #vai calcular a hipotenusa
                lado1 = float(input("\nDigite o comprimento do cateto A: "))
                lado2 = float(input("Digite o comprimento do cateto B: "))

                hipotenusa = math.hypot(lado1, lado2) #calculo bruto
                #hipotenusa = math.sqrt(hipotenusa)#retorna com a raiz calculada

                print(f"\nDado o cateto A {lado1} e cateto B {lado2} o comprimento da hipotenusa é {hipotenusa:.2f} \n")
                break
            elif int(escolha) == 2 :
            #vai calcular o cateto
                lado1 = float(input("\nDigite o comprimento do cateto A: "))
                lado2 = float(input("Digite o comprimento da hipotenusa: "))

                if lado1 < lado2 :
                #se os dados forem corretos
                    cateto = (lado2 ** 2 ) - (lado1 ** 2)#calculo bruto
                    cateto = math.sqrt(cateto)#retorna com a raiz calculada

                    print(f"Dado o cateto A {lado1} e a hipotenusa {lado2} o comprimento do cateto B é {cateto:.2f} ")

                elif lado1 > lado2:
                #casos os dados possam executar o teorema mas estejam em ordem errada
                    print("\n[ERRO] ")
                    print(f"Os valore digitados são: cateto A: {lado1} e hipotenusa: {lado2} \nIsso está incorreto pois um cateto não pode ser maior que a hipotenusa")
                    print("O calculo foi feito, porem foi considerado que o cateto A é na verdade a hipotenusa \nRecomendo revisar os dados \n ")

                    cateto = (lado1 ** 2 ) - (lado2 ** 2) #calculo bruto
                    cateto = math.sqrt(cateto)#retorna com a raiz calculada

                    print(f"Dado o cateto A {lado1}  e a hipotenusa {lado2} (originalmente inserido como o cateto) o comprimento do cateto B é {cateto:.2f}\n ")
                    print("O calculo foi feito, porem foi considerado que o cateto A é na verdade a hipotenusa \nRecomendo revisar os dados \n ")

                elif lado2 == lado1 :
                #caso seja impossivel executar o teorema
                    print(f"\n[ERRO]")
                    print(f"O Cateto A {lado1} não pode ser igual a hipotenusa {lado2}")
                else:
                    print("\n[ERRO]\nVerifique os dados e tente novamente")
                    
                break
            else:
                print("\n[ERRO]\nVerifique os dados e tente novamente")
                
        else:
            print("\n[ERRO]\nVerifique os dados e tente novamente")
           