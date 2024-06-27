from datetime import datetime

def log_transacao(funcao):
    
    def envelope(*args,**kw):
        print('===============================')
        funcao(*args,**kw)
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"{data}: {funcao.__name__.upper()}")
        print('===============================')
    
    return envelope

class contaIterado:
    def __init__(self, contas):
        self.contas = contas
        self._index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            conta = self.contas[self._index]
            return  f"""Agência:\t{conta._agencia}\nNúmero da conta:\t{conta._numero}\nTitular:\t {conta._cliente._nome}\nSaldo:\tR${conta._saldo:.2f}"""
        except IndexError:
            raise StopIteration
        finally:
            self._index += 1