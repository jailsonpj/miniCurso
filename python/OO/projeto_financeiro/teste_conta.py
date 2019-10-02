from model import ContaBancaria
import model as md
from model import Cliente


import numpy as np
import pandas as pd
'''
conta = ContaBancaria()
model.ContaBancaria()
conta.agencia = '0233'
conta.numero = '1234-5'
conta.nome_cliente = 'Maria Jose'
conta.saldo = 1500.0

print('Cliente ' + conta.nome_cliente)
print('Agencia %s e Conta %s' % (conta.agencia,conta.numero))
print('Saldo '+ str(conta.saldo))


# Teste dos métodos depositar() e sacar()
conta.depositar(500.0)

if conta.sacar(2500.0):
    print('Saque realizado com sucesso :-)')
else:
    print('Saldo insuficiente :-(')

'''
'''
# Teste do método de transferência
origem = ContaBancaria()
origem.depositar(1200.0)

destino = ContaBancaria()

print('\n Saldo Inicial Origem: ', origem.saldo)
print('Saldo Inicial Destino', destino.saldo)
print('Transferência ===========')
origem.transferir(500.0, destino)
print('Saldo Origem: ', origem.saldo)
print('Saldo destino: ', destino.saldo)

'''

'''
#Teste Cliente
cliente = Cliente()
cliente.nome = 'Luiza'
cliente.cpf = '123456'
cliente.email = 'luiza@gmail.com'

conta = ContaBancaria()
conta.saldo = 1000.0
conta.cliente = cliente

print('Saldo: ', conta.saldo)
print('CPF: ', conta.cliente.cpf)
print('Nome: ', conta.cliente.nome)
print('E-mail: ', conta.cliente.email)
'''