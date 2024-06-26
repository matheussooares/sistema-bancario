from datetime import datetime

def log_transacao(funcao):
    
    def transacoes(*args):
        funcao(*args)
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"\n{data}")
        print('===============================')
    
    return transacoes

class contaIterado:
    def __init__(self) -> None:
        pass
    def __iter__(self):
        pass
    def __next__(self):
        pass