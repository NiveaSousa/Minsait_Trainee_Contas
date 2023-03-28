from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

opcao_escolhida = 0

conta_poupanca = ContaPoupanca(123, 300)
conta_corrente = ContaCorrente(321, 500, 200)

#testando deposito e verificando rendimento sem determinar medida de tempo
conta_poupanca.depositar(100)
conta_poupanca.verificar_rendimento_ao_ano(5)
print(conta_poupanca.taxa_de_rendimento)
print(conta_poupanca.get_saldo())

#testando saque acima do valor
conta_poupanca.sacar(600)

#testando saque dentro do valor
conta_poupanca.sacar(10.0)
print(conta_poupanca.get_saldo())

#teste deposito conta corrente
conta_corrente.depositar(200)
print(conta_corrente.get_saldo())

#teste saque que da erro
conta_corrente.sacar(1000)

#teste saque que funciona
conta_corrente.sacar(200)
print(conta_corrente.get_saldo())