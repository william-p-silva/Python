
class pessoa():
    """teste de help"""
    carro = ""
    def __init__(self, nome ="", sobre_nome ="", idade = 0):
        self.nome = nome
        self.idade = idade
        self.sobreNome = sobre_nome

    def carro(self, nome_marca):
        self.carro = nome_marca

    def ExibriInfos(self):
        return f"Nome: {self.nome} {self.sobreNome} || idade: {self.idade}"

    def Aniversario(self):
        self.idade += 1

    def __str__(self):
        return "Voou lhe mostrar algo..."


people = pessoa("William", "Sialva", 20)


print(people.ExibriInfos())

people.Aniversario()

print(people.ExibriInfos())
people.carro("Fiat")
print(people.carro)

