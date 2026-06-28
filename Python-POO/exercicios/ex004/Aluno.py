from Pessoa import Pessoa

class Aluno(Pessoa):
    def __ini__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma
