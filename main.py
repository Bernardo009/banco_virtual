from conta import Conta
from agencia import Exclusive
from cartao import Cartao

ag = Exclusive("20.648.594/0001-20", "(12)99999-9999")

ag.adicionar_cliente("Pedro", "123.456.789-80", 2_000_000)

cc = Conta("Pedro", "123.456.789-80", ag.numero, "0023")
cc.depositar(3400)
cc.sacar(350)

cartao = Cartao(cc.nome, cc)
cartao.exibir()

outra = Conta("Maria", "444.222.555-77", ag.numero, "0045")
cc.pix(1000, outra)

cc.extrato()
outra.extrato()
