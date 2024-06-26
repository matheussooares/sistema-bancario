from scripts import classes


def menu():
    view = """============ MENU =============\n
    [nu] Novo usuário
    [nc] Nova Conta
    [ce] Contas Existentes
    [d] Deposito
    [s] Sacar
    [e] Extrato
    [x] Sair \n==>
    """
    return input(view)

def conta_cliente(cliente):
    # Analisa se o cliente possui uma conta
    if not cliente._contas:
        print('n@@@ Falha no usuário: não possuie conta @@@\n')
        return
    
    # Não pega o numero a conta
    return cliente._contas[0]

# filtra o clientes por cpf
def filtro_cliente(clientes,cpf=None):
    if cpf == None:    
        # Busca o nome do cliente
        cpf = int(input('Informe o CPF do cliente: '))

    cliente_filtrado = None

    for cliente in clientes:
        if cliente._cpf == cpf:
            cliente_filtrado = cliente
            break

    
    if cliente_filtrado:
        return cliente_filtrado
    else:
        return None

def depositar(clientes):
    # Retorna o cliente
    cliente = filtro_cliente(clientes)

    if cliente == None:
        print('\n@@@ Falha no usuário: cpf não encontrado @@@\n')
    else:    
        conta = conta_cliente(cliente)

        if not conta:
            return
        
        valor = float(input('Valor do deposito: '))

        transacao = classes.Deposito(valor)

        cliente.transacao(conta, transacao)
    
    return

def sacar(clientes):
    # Retorna o cliente
    cliente = filtro_cliente(clientes)

    if cliente == None:
        print('n@@@ Falha no usuário: cpf não encontrado @@@\n')
        
    else:
        conta  = conta_cliente(cliente)
        if not conta:
            return
        
        valor = float(input('Valor do saque: '))

        transacao = classes.Saque(valor)

        cliente.transacao(conta, transacao)
    return

def extrato(clientes):
    # Retorna o cliente
    cliente = filtro_cliente(clientes)

    if cliente == None:
        print('\n@@@ Falha no usuário: cpf não encontrado @@@\n')
    else:  
        extrato = "" 
        conta  = conta_cliente(cliente)
        
        if not conta:
            return
        
        transacoes = conta.historico.transacoes
        print('=========== EXTRATO ===========')
        if not transacoes:
            print('Não foi realizado nenhuma movimentação')
        else:
            for transacao in transacoes:
                extrato += f"\n{transacao['data']}\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"
            
            print(extrato)
            print(f"\nSaldo:\t R${conta.saldo:.2f}")
            print('===============================')
    return

def criar_conta(clientes, contas: list, num_conta: int):
   # Retorna o cliente
    cliente = filtro_cliente(clientes)

    if cliente == None:
        print('n@@@ Falha no usuário: cpf não encontrado @@@\n')
    else:
        conta = classes.ContaCorrente.add_conta(numero = num_conta, cliente = cliente)
        contas.append(conta)
        cliente._contas.append(conta)
        print('\n=== Criação de conta realiza com sucesso ===\n')

    return

def criar_cliente(clientes: list):
    # Retorna o cliente
    cpf = int(input('Informe o CPF do cliente: '))
    cliente = filtro_cliente(clientes,cpf)

    if cliente:
        print('n@@@ Falha no usuário: cpf existente @@@\n')
    else:
        nome = input('Nome completo: ')
        data_nascimento = input('Data de nascimento: ')
        endereco = input('Endereço completo: ')

        cliente = classes.Pessoa(cpf = cpf, 
                       nome = nome, 
                       data_nascimento = data_nascimento,
                       endereco = endereco)
        
        
        clientes.append(cliente)

        print('\n=== Criação de usuário realiza com sucesso ===\n')
    return 

def contas(contas):
    if contas:
        for conta in contas:
            print('===============================')
            print(str(conta))
    else:
        print('===============================')
        print('Não existe contas associadas')