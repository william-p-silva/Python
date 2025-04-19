import math

#esse programa vai trazer alguns dados  de números
print("Para parar basta digitar -1")
num = (input('Digite um número: '))


#loop para não precisas ficar iniciando o codigo varias vezes
while num != "-1":
    #se não for digitado nada ele indica erro e pede outro numero
    if len(num) == 0:
        print("\n[ERRO]")
        num = (input('Digite um número: '))
    #caso tenha um digito (não é feita a verificação sobre caracteres)
    else:
        n = int(num)
        #indica a tabuada até onúmero 10 padrão
        print(f"\nAqui está a tabuada do número {num} \n")
        #loop da tabuada
        for s in range(10):
            v =' '
            print(f"| {n} X {v}{s} = {n*s} ")
            s += 1
        print(f"| {n} X {s} = {n*s} ")
        print(f"{v}____________")
        #esses prints são apenas para estetica
        #o print abaixo é para indicar o antecessor e o sucessor sem variaveis
        print(f"\nAnalisando o número {num} chegamos a conclusão que seu antecessor é {int(num)-1} e seu sucessor é {int(num)+1}")
        #par ou impar
        if int(num) % 2 == 0:
            print(f"O Número {num} é par")
        else:
            print(f"O Número {num} é impar")
        #quadrado raiz quadrada e o dobro 
        print(f"O número {num} elevado ao quadrado é igual a {int(num) ** 2}")
        print(f"A raiz quadrada do número {num} é igual a {math.sqrt(int(num)):.2f}")
        #pede outro numero e refaz o codigo
        print(f"O dobro do número {num} é igua á {n*2}")
        num = (input('\nDigite um número: '))
        s = 1
