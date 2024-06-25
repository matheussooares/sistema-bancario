from scripts import classes

def menu():
    view = """============ MENU =============\n
    [nu] Novo usuário
    [nc] Nova Conta
    [d] Deposito
    [s] Sacar
    [e] Extrato
    [x] Sair \n==>
    """
    return input(view)

def conta_cliente(cliente):
    # Analisa se o cliente possui uma conta
    if not cliente.contas:
        print('n@@@ Falha no usuário: não possuie conta @@@\n')
        return
    
    # Não pega o numero a conta
    return cliente.contas[0]

# filtra o clientes por cpf
def filtro_cliente(cpf,clientes):
    cliente_filtrado = None

    for cliente in clientes:
        if cliente.cpf == cpf:
            cliente_filtrado = cliente
            break

    
    if cliente_filtrado:
        return cliente_filtrado
    else:
        return None

def depositar(clientes):
    # Busca o nome do cliente
    cpf = int(input('Informe o CPF do cliente: '))
    
    # Retorna o cliente
    cliente = filtro_cliente(cpf,clientes)

    if cliente == None:
        print('n@@@ Falha no usuário: cpf não encontrado @@@\n')
    else:    
        valor = float(input('Valor do deposito: '))

        transacao = classes.Deposito(valor)

        conta = conta_cliente(cliente)
        
        if not conta:
            return

        cliente.transacao(conta, transacao)
    
    return
