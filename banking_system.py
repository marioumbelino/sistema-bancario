from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, endereco):
        pass

    def realizar_transacao(self):
        pass

    def adcionar_conta(self):
        pass

class PessoaFisica(Cliente):
    def __init__(self, endereco, nome, data_nascimento, cpf):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        if valor > saldo:
            print("Não foi possível realizar o saque, valor insuficiente.")

        elif valor > 0:
            self.saldo -= valor
            print("Saque efetuado com sucesso!")
            return True
        
        else:
            print("Falha no saque! Por favor, tente novamente!")
        
        return False
    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saque=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])
        
        if valor > self.limite:
            print("Falha no saque! O valor limite foi excedido.")

        elif numero_saques >= self.limite_saque:
            print("Falha no saque! Número máximo de saques excedido")

        else:
            return super().sacar(valor)

        return False
    
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    def registrar(self, conta):
        pass

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adcionar_transacao(self, transacao):
        self.transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
            }
        )
        
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)

