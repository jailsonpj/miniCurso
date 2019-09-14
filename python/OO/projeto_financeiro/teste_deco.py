# -*- coding: utf-8 -*-
from model_2 import ContaBancaria

conta = ContaBancaria()

print('Saldo inicial: ', conta.saldo)

conta.depositar(1000)
print('Saldo apos deposito: ', conta.saldo)

conta.sacar(200.0)
print('Saldo apos saque: ', conta.saldo)

