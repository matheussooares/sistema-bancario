from datetime import datetime

def log_transacao(funcao):
    
    def envelope(*args,**kw):
        print('===============================')
        resultado = funcao(*args,**kw)
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        from pathlib import Path
        ROOT_PATH = Path().resolve()
        with open(ROOT_PATH/'src'/'data'/"log.txt","a", encoding='utf-8') as arquivo:
            arquivo.write(
                f"[{data}] função '{funcao.__name__.upper()}' executada com argumentos {args} e {kw}."
                f"Retornou {resultado}\n"
            )
        print('===============================')
        return resultado
    
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