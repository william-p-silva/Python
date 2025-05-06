def inicio():
    print('Iniciando o programa de cálculo de área...')
    print('-='*30)


def calcular_area(base, altura):
    area = base * altura
    print('-='*30)
    print(f'A área do retângulo é {area} m²')
    print()


inicio()
b = float(input('Digite a base do retângulo: '))
a = float(input('Digite a altura do retângulo: '))
# Chama a função para calcular a área
calcular_area(b, a)