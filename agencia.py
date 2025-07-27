from random import randint

class Agencia:
    def __init__(self, cnpj, telefone, numero=None):
        self.cnpj = cnpj
        self.telefone = telefone
        self.numero = numero or randint(1001, 9999)
        self.caixa = 0
        self.clientes = []

    def ver_caixa(self):
        status = "abaixo" if self.caixa < 1_000_000 else "acima"
        print(f"Caixa {status} do ideal: R$ {self.caixa:,.2f}")

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append({"nome": nome, "CPF": cpf, "Patrimonio": patrimonio})

class Varejo(Agencia):
    def __init__(self, cnpj, telefone):
        super().__init__(cnpj, telefone)
        self.caixa = 1_000_000_000

class Exclusive(Agencia):
    def __init__(self, cnpj, telefone):
        super().__init__(cnpj, telefone)
        self.caixa = 1_000_000_000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        
        if patrimonio >= 1_000_000:
            super().adicionar_cliente(nome, cpf, patrimonio)

        else:
            print("Cliente não tem patrimonio suficiente para a conta Exclusive")


class Virtual(Agencia):
    def __init__(self, cnpj, telefone, site):
        super().__init__(cnpj, telefone, numero=3925)
        self.site = site
        self.caixa_pp = 0

    def movimentar_pp(self, valor, tipo):
        if tipo == "deposito":
            self.caixa -= valor
            self.caixa_pp += valor
        elif tipo == "saque":
            self.caixa_pp -= valor
            self.caixa += valor