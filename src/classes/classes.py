import datetime
from abc import ABC, abstractmethod
class Conta:
    def __init__(self, numero: int, cliente):
        self._agencia = '0001'
        self._saldo = 0
        self._numero = numero
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def conta(cls, cliente, numero):
        return cls(numero, cliente)
    
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
            print('\n@@@ Falha na operação: saldo insuficiente @@@\n')
        elif valor > 0:
            self._saldo -= valor
            print('\n=== Operação saque realiza com sucesso ===\n')
            return True
        else:
            print('\n@@@ Falha na operação: valor inválido @@@\n')
        
        return False
    
    def depositar(self,valor):
        if valor>0:
            self._saldo += valor
            print('\n=== Operação de deposito realiza com sucesso ===')
            return True
        else:
            print('\n@@@ Falha na operação: valor inválido @@@\n')
            return False

class ContaCorrente(Conta):
    def __init__(self, LIMITE=500.00, LIMITE_SAQUES=3, **arg):
        self._LIMITE = LIMITE
        self._LIMITE_SAQUES = LIMITE_SAQUES
        super().__init__(**arg)
    
    def sacar(self, valor):

        # Fução que conta o número de saques
        def saques(historico):
            num_saque = 0
            for transacao in historico:
                if transacao['tipo'] == "Saque":
                    num_saque +=1
            return num_saque
        

        num_saques = saques(self._historico)

        if valor > self._saldo:
            print('\n@@@ Falha na operação: saldo insuficiente @@@\n')

        elif num_saques >= self._LIMITE_SAQUES:
            print('\n@@@ Falha na operação: excedeu número máximos de saque @@@\n')
    
        elif valor > 0 and  valor <= self._LIMITE:
           return super().sacar(valor)
    
        else:
            print('\n@@@ Falha na operação: valor inválido @@@\n')

        
        return False
    
    def __str__(self):
        return f"""Agência:\t {self._agencia}\nC\C:\t {self._numero}\nTitular:\t {self._cliente._nome}"""

class Historico:
    def __init__(self):
        self.transacoes = []

    def transacao(self,transacao):
        self.transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "Valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s")
            }
        )

class Cliente:
    def __init__(self, endereco: str):
        self._endereco = endereco
        self._contas = []

    def transacao(self, conta, transacao):
        transacao.registrar(conta)

    def conta(self, conta: Conta):
        self._contas.append(conta)
    
class Pessoa(Cliente):
    def __init__(self, cpf: str, nome: str, data_nascimento: str, **kw):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
        super().__init__(**kw)

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self,_valor):
        self._valor = _valor
    
    @property
    def valor(self):
        return self._valor
    
    

pessoa = Pessoa(cpf="07871",
                nome="jose matheus",
                data_nascimento="10/06",
                endereco = "Rua natal")

conta = ContaCorrente(numero = 1,cliente = pessoa)

conta.depositar(100)
conta.sacar(1000)