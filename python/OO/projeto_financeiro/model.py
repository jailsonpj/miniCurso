class ContaBancaria(object):
    def __init__(self):
        self.agencia = None
        self.numero = None
        self.cliente = None
        self.saldo = 0.0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        return False

    def transferir(self, valor, destino):
        if self.sacar(valor):
            destino.depositar(valor)
            return True
        return False

class Cliente(object):
    def __init__(self):
        self.nome = None
        self.cpf = None
        self.rg = None
        self.email = None