# =========================================================
# FUNDAMENTOS DE PYTHON - ARQUIVO COMPLETO
# =========================================================


# ---------------------------
# Tipos Primitivos e Variáveis
# ---------------------------

# variáveis armazenam valores na memória
nome = "William"   # str → texto
idade = 20         # int → número inteiro
user_ativo = True  # bool → verdadeiro ou falso
saldo = 1.25       # float → número decimal


# ---------------------------
# Entrada e Saída de Dados
# ---------------------------

# recebe dados do usuário (sempre como string)
nome_usuario = input("Digite seu nome: ")

# exibe informações na tela
print("Olá,", nome_usuario)


# ---------------------------
# Operadores
# ---------------------------

a = 10
b = 5

# operadores matemáticos
print(a + b)  # soma
print(a - b)  # subtração
print(a * b)  # multiplicação
print(a / b)  # divisão

# operadores relacionais
print(a == b)  # igualdade
print(a != b)  # diferente
print(a > b)   # maior que
print(a < b)   # menor que
print(a >= b)  # maior ou igual
print(a <= b)  # menor ou igual

# operadores lógicos
print(a > 5 and b < 10)  # and → ambas verdadeiras
print(not (a == b))      # not → inverte valor


# ---------------------------
# Estruturas Condicionais
# ---------------------------

if idade < 16:
    print("Você não pode votar")

elif 16 <= idade <= 18 or idade > 70:
    print("Seu voto é facultativo")

else:
    print("Seu voto é obrigatório")


# ---------------------------
# Estruturas de Repetição
# ---------------------------

# for → quantidade definida de repetições
for i in range(5):
    print(i)

# while → repete enquanto condição for verdadeira
contador = 0
while contador < 5:
    print(contador)
    contador += 1


# ---------------------------
# Estruturas de Dados
# ---------------------------

# lista (sequência de valores)
lista = [1, 2, 3]
print(lista[0])  # acessa primeiro elemento

# dicionário (chave: valor)
pessoa = {
    "nome": "William",
    "idade": 18
}
print(pessoa["nome"])


# ---------------------------
# Funções (com return)
# ---------------------------

def verificar_condicao_eleitoral(idade_eleitoral):
    if idade_eleitoral < 16:
        return "Você não pode votar"
    elif 16 <= idade_eleitoral <= 18 or idade_eleitoral > 70:
        return "Seu voto é facultativo"
    else:
        return "Seu voto é obrigatório"


# chamada da função
resultado = verificar_condicao_eleitoral(idade)
print(resultado)


# ---------------------------
# Escopo de Variáveis
# ---------------------------

# variável global
numero_global = 10

def exemplo_escopo():
    # variável local (só existe dentro da função)
    numero_local = 5
    print(numero_local)

def acessar_global():
    # acessa variável global
    print(numero_global)

exemplo_escopo()
acessar_global()


# ---------------------------
# Tratamento de Erros
# ---------------------------

try:
    numero = int(input("Digite um número: "))
    print("Número digitado:", numero)
except:
    print("Entrada inválida")


# ---------------------------
# Classes e Objetos
# ---------------------------

class Pessoa:

    def __init__(self, nome, idade, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def apresentar(self):
        print(f"Nome: {self.nome} {self.sobrenome}")
        print(f"Idade: {self.idade}")


# criando objetos
pessoa1 = Pessoa("Matheus", 19, "Pinheiro")
pessoa2 = Pessoa("Luiz", 19, "Alves")

pessoa1.apresentar()
pessoa2.apresentar()


# ---------------------------
# Importação de Módulos
# ---------------------------

import math

# usando função do módulo
print(math.sqrt(16))  # raiz quadrada


# ---------------------------
# Boas Práticas
# ---------------------------

# usar nomes em snake_case
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

media = calcular_media(8, 6)
print("Média:", media)