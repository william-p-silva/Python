
# ---------------------------
# Tipos Primitivos
# ---------------------------

#variavel        Valor       Tipo
nome        =   "William"    #str
idade       =    20          #int
userAtivo   =    True        #bool
saldo       =    1.25        #float


# ---------------------------
# Operadores relacionais
# ---------------------------

a = 10
b = 5

print(a == b)  # igualdade → False
print(a != b)  # diferente → True
print(a > b)   # maior que → True
print(a < b)   # menor que → False
print(a >= b)  # maior ou igual → True
print(a <= b)  # menor ou igual → False


# ---------------------------
# Operadores lógicos
# ---------------------------

idade = 20
tem_carteira = True

# 'and' → ambas condições precisam ser verdadeiras
if idade >= 18 and tem_carteira:
    print("Pode dirigir")

# 'not' → inverte o valor lógico
if not tem_carteira:
    print("Não possui carteira")


# ---------------------------
# Estruturas condicionais
# ---------------------------

# 'if' verifica se uma condição é verdadeira
if idade < 16:
    # Se a condição for True, o código dentro do bloco é executado
    print("Você não pode votar")  # 'print' exibe uma mensagem na tela

# 'elif' (else if) testa uma nova condição caso o 'if' seja falso
elif 16 <= idade <= 18 or idade > 70:
    # '16 <= idade <= 18' verifica se a idade está entre 16 e 18
    # 'or' significa "ou", ou seja, basta uma das condições ser verdadeira
    print("Seu voto é facultativo")

# 'else' é executado quando nenhuma das condições anteriores é verdadeira
else:
    print("Seu voto é obrigatório")


# ---------------------------
# Estruturas de repetição
# ---------------------------

# 'for' é usado para repetir um bloco de código um número definido de vezes
for i in range(5):
    # 'i' recebe cada valor da sequência automaticamente a cada repetição
    print(i)  # imprime o valor atual de 'i'

# ---------------------------

# 'while' repete o bloco enquanto a condição for verdadeira
c = 0  # variável de controle iniciando em 0
while c < 5:
    # enquanto 'c' for menor que 5, o loop continua executando
    print(c)  # imprime o valor atual de 'c'

    # 'c += 1' incrementa o valor de 'c' em 1 (mesma coisa que c = c + 1)
    # isso é importante para evitar loop infinito
    c += 1


# ---------------------------
# Estruturas de dados
# ---------------------------

# 'lista' é uma estrutura que armazena vários valores em sequência
# os valores ficam entre colchetes [] e são separados por vírgula
lista = [1, 2, 3]

# cada item da lista possui um índice (posição), começando do 0
# exemplo: lista[0] → 1, lista[1] → 2, lista[2] → 3

# ---------------------------

# 'dicionário' armazena dados no formato chave: valor
# é definido usando chaves {} (não confundir com lista)
pessoa = {
    "nome": "William",  # chave "nome" armazena um valor do tipo string
    "idade": 18         # chave "idade" armazena um valor do tipo inteiro
}

# para acessar um valor no dicionário, usamos a chave
# exemplo: pessoa["nome"] → "William"
# exemplo: pessoa["idade"] → 18



# ---------------------------
# Funções com retorno (return)
# ---------------------------

# 'def' define uma função
# 'return' faz a função devolver um valor ao invés de apenas imprimir
def verificarCondicaoEleitoral(idadeEleitoral):

    # a função analisa a idade e RETORNA uma mensagem
    if idadeEleitoral < 16:
        return "Você não pode votar"

    elif 16 <= idadeEleitoral <= 18 or idadeEleitoral > 70:
        return "Seu voto é facultativo"

    else:
        return "Seu voto é obrigatório"


# ---------------------------
# Chamada de função
# ---------------------------

idade = 16  # valor que será usado como argumento

# chamamos a função e armazenamos o retorno em uma variável
resultado = verificarCondicaoEleitoral(idade)

# usamos o resultado retornado pela função
print(resultado)


# ---------------------------
# Escopo de variáveis
# ---------------------------

# 'escopo' define onde uma variável pode ser acessada

# variável global (fora da função)
idade = 16

def exemplo():
    # variável local (só existe dentro da função)
    x = 10
    print(x)

# print(x)  # daria erro, pois 'x' só existe dentro da função

# dentro da função, conseguimos acessar variáveis globais
def exemplo2():
    print(idade)  # acessa a variável global

exemplo()
exemplo2()


# ---------------------------
# Entrada e saída de dados
# ---------------------------

# 'input()' é usado para receber dados do usuário
# o texto dentro dos parênteses é exibido como mensagem na tela
nome = input("Digite seu nome: ")

# o valor digitado pelo usuário é sempre armazenado como texto (string)

# 'print()' é usado para exibir informações na tela
print(nome)  # mostra o valor que foi digitado pelo usuário


# ---------------------------
# Tratamento de erros (Exception)
# ---------------------------

# 'try' é usado para testar um bloco de código que pode gerar erro
try:
    # 'input' lê um valor digitado pelo usuário (sempre como texto - string)
    numero = int(input("Digite um número: "))
    
    # 'int()' tenta converter o valor digitado para número inteiro
    # se o usuário digitar algo que não seja número, ocorre um erro

# 'except' captura o erro caso ele aconteça no bloco 'try'
except:
    # se ocorrer qualquer erro, esse bloco será executado
    print("Entrada inválida")



# ---------------------------
# Classes e Objetos
# ---------------------------

# 'class' é usado para definir uma classe (modelo/estrutura de um objeto)
class Pessoa:

    # '__init__' é o método construtor
    # ele é executado automaticamente quando um objeto é criado
    # 'self' representa a própria instância (o próprio objeto)
    def __init__(self, nome, idade, sobreNome):
        # atributos (características) do objeto
        self.nome = nome
        self.sobreNome = sobreNome
        self.idade = idade

    # método (função dentro da classe)
    def ApresentarPessoa(self):
        # 'self.nome' acessa o atributo do próprio objeto
        print(f"nome: {self.nome} {self.sobreNome}")
        print(f"idade: {self.idade}")


# ---------------------------
# Criando objetos
# ---------------------------

# criando um objeto da classe Pessoa
# os valores passados são enviados para o método __init__
pessoa1 = Pessoa("Matheus", 19, "Pinheiro")

# chamando um método do objeto
pessoa1.ApresentarPessoa()

# criando outro objeto com valores diferentes
pessoa2 = Pessoa("Luiz", 19, "Alves")

# cada objeto tem seus próprios dados
pessoa2.ApresentarPessoa()





#talvez adicionar:



# ---------------------------
# Importação de módulos
# ---------------------------

# importa o módulo inteiro
import math

print(math.sqrt(16))  # raiz quadrada → 4.0

# importa apenas uma função específica
from math import pow

print(pow(2, 3))  # 2 elevado a 3 → 8.0


# ---------------------------
# Boas práticas de nomenclatura
# ---------------------------

# ❌ ruim (não segue padrão)
def VerificarIdadeUsuario():
    pass

# ✅ bom (snake_case → padrão Python)
def verificar_idade_usuario():
    pass

# variáveis também seguem o mesmo padrão
nome_usuario = "William"
idade_usuario = 20