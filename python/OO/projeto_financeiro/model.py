class ContaBancaria(object):
    def __init__(self):
        self.agencia = None
        self.numero = None
        self.nome_cliente = None
        self.saldo = 0.0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.valor -= valor
            return True
        return False


