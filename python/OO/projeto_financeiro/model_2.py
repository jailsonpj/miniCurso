class ContaBancaria(object):
    __total_contas = 0
    def __init__(self):
        self.agencia = None
        self.numero = None
        self.cliente = None
        self.__saldo = 0.0
        #self.total_contas += 1

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, novo_saldo):
        self.__saldo = novo_saldo

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            return True
        return False