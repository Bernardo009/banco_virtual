from utilidades import data_atual


class Conta:
    def __init__(self, nome, cpf, agencia, numero):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = -7000
        self.agencia = agencia
        self.numero = numero
        self.transacoes = []
        self.cartoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append(
            {"tipo": "Deposito", "Valor": valor, "data": data_atual()}
        )

    def sacar(self, valor):
        if self.saldo - valor >= self.limite:
            self.saldo -= valor
            self.transacoes.append(
                {"tipo": "Saque", "Valor": -valor, "data": data_atual()}
            )

        else:
            print("Saldo insuficiente!")
    
    def pix(self, valor, destino):
        if self.saldo - valor >= self.limite:
            self.saldo -= valor
            self.transacoes.append({"tipo": "PIX", "Valor" : -valor, "data" : data_atual() })
            destino.saldo += valor
            destino.transacoes.append({"tipo": "PIX", "Valor" : valor, "data" : data_atual() })
        
        else:
            print("Saldo insuficiente!")


    def extrato(self):
        print(f"Extrato - conta {self.numero} | Titular: {self.nome}")
        for i in self.transacoes:
            print(f"{i["data"]} - {i["tipo"]}: R$ {i["Valor"]:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")