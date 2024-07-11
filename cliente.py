class Cliente:
    def __init__(self, endereco=None):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self):
        pass
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)
