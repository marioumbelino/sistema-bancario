from cliente import Cliente
from historico import Historico

class Conta:
    def __init__(self, cliente, numero):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self.saldo
    
    @property
    def numero(self):
        return self.numero
    
    @property
    def agencia(self):
        return self.agencia
    
    @property
    def cliente(self):
        return self.cliente
    
    @property
    def historico(self):
        return self.historico
    
    @classmethod
    def criar_conta(cls, cliente, numero):
        return cls(cliente, numero)
    
    def sacar(self, valor):
        saldo = self.saldo
        
        if valor <= 0:
            print("Valor inválido. Por favor, tente novamente.")

        elif valor > saldo:
            print("Saldo insuficiente!")

        else:
            self._saldo -= valor
            print(f"Saque no valor de R${valor:.2f} realizado com sucesso!")
            return True
        
        return False
    
    def depositar(self, valor):
        saldo = self.saldo
        if valor <= 0:
            print("Valor inválido. Por favor, tente novamente!")
        
        else:
            self._saldo += valor
            print(f"Deposito no valor de R${valor:.2f} realizado com sucesso!")
            return True
        
        return False
            
        
