class Conta:
    def __init__(self, numConta):
        self.numero = numConta
        self.saldo = 0

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.contas = []

    def getNome(self):
        return self.nome
