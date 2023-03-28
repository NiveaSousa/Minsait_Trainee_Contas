from Conta import Conta
import requests

class ContaPoupanca(Conta):
    def __init__(self,account_id, balance):
        super().__init__(account_id, balance)
        self.taxa_de_rendimento = self.obter_taxa_rendimento()


    def obter_taxa_rendimento(self):
        url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados/ultimos/1?formato=json'
        response = requests.get(url)
        dados = response.json()
        taxa = float(dados[0]['valor'])/10
        return taxa

        

    def sacar(self, withdraw):
        try:
            self.balance = self.get_saldo()
            self.balance -= withdraw
            self.set_saldo(self.balance)
        except ValueError as ve:
            print(ve)
            

    def depositar(self, cash_deposit):
        self.balance = self.get_saldo()
        self.balance += cash_deposit
        self.set_saldo(self.balance)

    def verificar_rendimento_ao_ano(self, tempo, medida_de_tempo='anos'):
        if medida_de_tempo == 'anos':
            tempo = tempo
        elif medida_de_tempo == 'meses':
            tempo = tempo/12
        elif medida_de_tempo == 'dias':
            tempo = tempo/365
        elif medida_de_tempo == 'horas':
            tempo = tempo/8766
        elif medida_de_tempo == 'minutos':
            tempo = tempo/525600
        elif medida_de_tempo == 'segundos':
            tempo = tempo/31536000
        else:
            raise ValueError('Unidade de tempo inválida')
        
        rendimento = self.balance * (self.taxa_de_rendimento*12) * tempo
        novo_saldo = self.balance + rendimento
        self.set_saldo(novo_saldo)
        return rendimento
    


