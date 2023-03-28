from abc import ABC, abstractmethod

class Conta(ABC):
    #usando saldo e balance, pois, estava dando erro entre saldo e _saldo
    def __init__(self, Account_id , Saldo):
        self._accout_id = int(Account_id)
        self._balance = float(Saldo)

    @abstractmethod
    def sacar(self, withdraw):
        pass

    @abstractmethod
    def depositar(self, cash_deposit):
        pass

    def get_saldo(self):
        return self._balance

    def set_saldo(self, value):
        if value <= 0:
            raise ValueError("Saldo insuficiente")
        else:
            self._balance = value





    


