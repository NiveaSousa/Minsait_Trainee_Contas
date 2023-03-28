from Conta import Conta

class ContaCorrente(Conta):

    def __init__(self,account_id, balance, limite) -> Conta:
        super().__init__(account_id, balance)
        self.limite = limite

    def sacar(self, withdraw):
        try:
            limite_maximo = self.balance + self.limite
            limite_maximo -= withdraw
            self.set_saldo(limite_maximo)
        except ValueError as ve:
            print(ve)
                

    def depositar(self, cash_deposit):
        self.balance = self.get_saldo()
        self.balance += cash_deposit
        self.set_saldo(self.balance)


