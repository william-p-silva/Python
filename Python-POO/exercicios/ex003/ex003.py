

class Conta_bancaria:
    def __init__(self, id, titular, saldo = 0):
        self.id = id
        self.titular = titular
        self.saldo = saldo


    def saque(self, valor):
        if (valor > self.saldo): return "Erro vc não tem saldo"
        if valor <= 0: return "Você não pode sacar zero"
        self.saldo -= valor
        return f"Saldo atual é de {self.saldo:,.2f}"
    

    def depositar(self, valor):
        if valor <= 0: return "Erro você não pode depositar zero reais"
        self.saldo += valor
        return f"Saldo atual é de {self.saldo:,.2f}"


    def __str__(self):
        return f"A conta de {self.titular} tem {self.saldo:,.2f} de saldo"


c1 = Conta_bancaria(112, "William", 3000)
print(c1)
print(c1.saque(4000))
print(c1.depositar(10000))