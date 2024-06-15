def menu():
    view = """============ MENU =============\n
    [d] Deposito
    [s] Sacar
    [e] Extrato
    [x] Sair\n===============================
    """
    return view

def extrato(extratos,saldo):
    print('=========== EXTRATO ===========')
    if not extratos:
        print('Não foi realizado nenhuma movimentação')
    else:
        print(extratos)
    print(f'\nsaldo: {saldo:.2f}')
    print('===============================')


def deposito(saldo,extratos):

    valor = float(input('Valor do deposito: '))

    if valor>0:
        saldo += valor
        extratos += f'Depósito: R$ {valor:.2f}\n'
        print('Operação de deposito realiza com sucesso')
    else:
        print('Falha na operação: valor inválido')

    return saldo,extratos
    
def saque(saldo, extratos, num_saques):
    LIMITE_SAQUES = 3
    valor = float(input('Valor do saque: '))

    if valor > saldo:
        print('Falha na operação: saldo insuficiente')

    elif num_saques >= LIMITE_SAQUES:
        print('Falha na operação: excedeu número máximos de saque')
    
    elif valor > 0:
        saldo -= valor
        extratos += f'Saque: R$ {valor:.2f}\n'
        num_saques +=1
        print('Operação saque realiza com sucesso')
    
    else:
        print('Falha na operação: valor inválido')
    
    return saldo,extratos,num_saques



def main():
    saldo = 0
    extratos = ''
    num_saques = 0

    while True:
        opc = input(menu())

        if opc == 'd':
            saldo, extratos = deposito(saldo,extratos)
        elif opc == 's':
            saldo, extratos, num_saques = saque(saldo, extratos, num_saques)
        elif opc == 'e':
            extrato(extratos,saldo)
        elif opc == 'x':
            break
        else:
            print('Digite um valor válido')

main()