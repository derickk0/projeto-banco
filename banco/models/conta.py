class Conta:
    def __init__(self, numero: int, agencia: int) -> None:
        self.numero = numero
        self.agencia = agencia
        self.saldo = 0

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor