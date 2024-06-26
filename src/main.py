from scripts import utils

def main():
    clientes = []
    contas = []
    

    while True:
        opc = utils.menu()

        if opc == 'd':
            utils.depositar(clientes)
        elif opc == 's':
            utils.sacar(clientes)
        elif opc == 'e':
            utils.extrato(clientes)
        elif opc =='nc':
            num_conta = len(contas)+1
            utils.criar_conta(clientes, contas, num_conta)
        elif opc == 'x':
            break
        elif opc == 'nu':
            utils.criar_cliente(clientes)
        elif opc == 'ce':
            utils.contas(contas)
        else:
            print('\n@@@ Falha na operação: digite um valor válido @@@\n')


main()


