from scripts import utils

def main():
    clientes = []
    contas = []
    

    while True:
        opc = utils.menu()

        if opc == 'd':
            utils.depositar(saldo,extratos)
        elif opc == 's':
            saldo, extratos, num_saques = saque(
                                                saldo = saldo,
                                                extratos = extratos, 
                                                num_saques = num_saques)
        elif opc == 'e':
            extrato(saldo, extratos = extratos)
        elif opc =='nc':
            usuarios, contas = conta(usuarios, contas)
            listar_contas(contas)
        elif opc == 'x':
            break
        elif opc == 'nu':
            usuarios = usuario(usuarios)
        else:
            print('\n@@@ Falha na operação: digite um valor válido @@@\n')

# joao = classes.Pessoa(cpf="07871",
#                 nome="jose matheus",
#                 data_nascimento="10/06",
#                 endereco = "Rua natal")

# conta = classes.Conta(numero = 1, cliente = joao)

# conta_corrente = classes.ContaCorrente(numero = 1,cliente = joao)



# print(conta_corrente)


# valor = float(input("Quando deseja depositar: "))

# conta_corrente.depositar(valor)
# conta.depositar(valor)




# valor = float(input("Quando deseja depositar: "))
# conta.sacar(valor)