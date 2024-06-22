class Conta:

    def __init__(self, numero, cliente):
        self._agencia = '0001'
        self._saldo = 0
        self._numero = numero
        self._cliente = cliente
        self._historico = Historico()
    
    def saldo(self):
        return self.saldo

    def nova_conta(self):
        pass

class ContaCorrente(Conta):
    def __init__(self, limite: float, limite_saque: float, **arg):
        self.limite = limite
        self.limite_saque = limite_saque
        super().__init__(**arg)


class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def conta(self, conta: Conta):
        self._contas.append(conta)
    

class Pessoa(Cliente):
    def __init__(self, cpf: str, nome: str, data_nascimento: str, **kw):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
        super().__init__(**kw)



pessoa = Pessoa(cpf="07871",
                nome="jose matheus",
                data_nascimento="10/06",
                endereco = "Rua natal")

print(pessoa)