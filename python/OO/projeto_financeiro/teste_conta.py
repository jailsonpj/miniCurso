from model import ContaBancaria

conta = ContaBancaria()

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