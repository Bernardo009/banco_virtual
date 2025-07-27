# 💳 Banco Virtual em Python

Este é um projeto educacional que simula o funcionamento básico de um sistema bancário com contas, cartões, agências e transações.

## 📁 Estrutura do Projeto

- `main.py`: ponto de entrada do sistema. Executa operações com contas, clientes e cartões.
- `agencia.py`: define as classes de agência (Varejo, Exclusive, Virtual) e suas regras.
- `conta.py`: gerencia operações bancárias como depósito, saque, Pix e extrato.
- `cartao.py`: gera cartões com dados aleatórios e associa a uma conta.
- `utilidades.py`: contém função para obter a data atual formatada.

## 🚀 Como Executar

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/banco_virtual.git
cd banco_virtual
```

2. Execute o programa com Python 3.8 ou superior:

```bash
python main.py
```

## 🔧 Requisitos

- Python 3.8+
- Não há bibliotecas externas necessárias (somente `random` e `datetime` da biblioteca padrão).

## ✅ Funcionalidades

- Criação e gerenciamento de contas bancárias
- Criação de cartões de crédito com validade e CVV
- Operações financeiras: saque, depósito e Pix
- Geração de extratos com data e descrição
- Três tipos de agência: Varejo, Exclusive e Virtual
- Validação de patrimônio mínimo para agência Exclusive

## 🧑‍💻 Autor

João Pedro Maximiliano Bernardo
