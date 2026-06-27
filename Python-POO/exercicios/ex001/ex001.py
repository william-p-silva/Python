
class pessoa:
    """teste de help"""
    def __init__(self):
        self.nome = ""
        self.idade = -1
        self.sobreNome = ""

    def ExibriInfos(self):
        return f"Nome: {self.nome} {self.sobreNome} || idade: {self.idade}"

    def Aniversario(self):
        self.idade += 1



people = pessoa()

people.nome = "william"
people.sobreNome = "silva"
people.idade = 20

print(people.ExibriInfos())

people.Aniversario()

print(people.ExibriInfos())

