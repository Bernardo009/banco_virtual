from random import randint
from datetime import date


class Cartao:
    def __init__(self, titular, conta):
        self.numero = randint(1_0000_0000_0000_0000, 9_9999_9999_9999_9999)
        self.nome = titular
        self.validade = f"{date.today().month}/{date.today().year + 5}"
        self.cvv = f"{randint(100, 999)}"
        self.conta = conta
        conta.cartoes.append(self)

    def exibir(self):
        print(f"Número: {self.numero} | CVV: {self.cvv} | Validade: {self.validade}")
