def menu():
    view = """============ MENU =============\n
    [nu] Novo usuário
    [d] Deposito
    [s] Sacar
    [e] Extrato
    [x] Sair \n==>
    """
    return input(view)

def extrato(saldo, /,*,extratos):
    print('=========== EXTRATO ===========')
    if not extratos:
        print('Não foi realizado nenhuma movimentação')
    else:
        print(extratos)
    print(f'\nsaldo: {saldo:.2f}')
    print('===============================')


def deposito(saldo,extratos,/):

    valor = float(input('Valor do deposito: '))

    if valor>0:
        saldo += valor
        extratos += f'Depósito: R$ {valor:.2f}\n'
        print('\n=== Operação de deposito realiza com sucesso ===')
    else:
        print('\n@@@ Falha na operação: valor inválido @@@\n')

    return saldo,extratos
    
def saque(*,saldo, extratos, num_saques):
    LIMITE_SAQUES = 3
    LIMITE = 500.00

    valor = float(input('Valor do saque: '))

    if valor > saldo:
        print('\n@@@ Falha na operação: saldo insuficiente @@@\n')

    elif num_saques >= LIMITE_SAQUES:
        print('\n@@@ Falha na operação: excedeu número máximos de saque @@@\n')
    
    elif valor > 0 and  valor <= LIMITE:
        saldo -= valor
        extratos += f'Saque: R$ {valor:.2f}\n'
        num_saques +=1
        print('\n=== Operação saque realiza com sucesso ===\n')
    
    else:
        print('\n@@@ Falha na operação: valor inválido @@@\n')
    
    return saldo,extratos,num_saques

def usuario(usuarios):
    cpf = input('Digite seu CPF: ')
    user = filtro_usuario(cpf,usuarios)

    if user == False:
        print('n@@@ Falha no usuário: cpf existente @@@\n')
    else:
        nome = input('Nome completo: ')
        dt_nascimento = input('Data de nascimento: ')
        endereco = input('Endereço completo: ')

        usuarios.append({'nome': nome,
                         'data nascimento': dt_nascimento,
                         'cpf': cpf,
                         'endereco': endereco
                         })
        print('\n=== Criação de usuário realiza com sucesso ===\n')
    
    return usuarios

def conta(usuarios,contas,numero_conta):
    AGENCIA = '0001'
    cpf = input('Digite seu CPF: ')
    user = filtro_usuario(cpf,usuarios)

    if user == False:
        print('n@@@ Falha no usuário: cpf não encontrado @@@\n')
    
    else:
        contas.append({'agencia':AGENCIA,
                       'numero conta': numero_conta
                       })
    
    return usuarios, contas



def filtro_usuario(cpf,usuarios):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return False

def main():
    saldo = 0
    extratos = ''
    num_saques = 0
    usuarios = []
    contas = []
    LIMITE = 500.00

    while True:
        opc = menu()
        if opc == 'd':
            saldo, extratos = deposito(saldo,extratos)
        elif opc == 's':
            saldo, extratos, num_saques = saque(
                                                saldo = saldo,
                                                extratos = extratos, 
                                                num_saques = num_saques)
        elif opc == 'e':
            extrato(saldo, extratos = extratos)
        elif opc == 'x':
            break
        elif opc == 'nu':
            usuarios = usuario(usuarios)
        else:
            print('\n@@@ Falha na operação: digite um valor válido @@@\n')

main()