def menu():
    """Função que contém o menu do banco
    """
    
    menu = '''
Qual operação deseja realizar?

    [D] - Deposito
    [S] - Saque
    [E] - Extrato
    [U] - Cadastrar Usuário
    [C] - Criar Conta Corrente
    [L] - Lista de Contas
    [Q] - Sair

-> '''
    return input(menu).upper().strip()[0]

def deposito(saldo, valor, extrato, /):
    """Função chamada para realizar o deposito no banco.

    Args:
        saldo (float): saldo total contido na conta do usuário
        valor (float): valor que o usuário deseja depositar em sua conta
        extrato (string): extrato bancário do usuário, que contém todo seu histórico de operações

    Returns:
        float/string: atualiza o saldo do usuário e seu extrato após o deposito
    """
    if valor <= 0: # verifica se o valor digitado para deposito é positivo ou não.
        print('Por favor, digite um valor positivo.')
    else:
        saldo += valor
        print(f'Deposito efetuado com êxito. Saldo atual: R${saldo:.2f}')
        extrato = f'\nDeposito no valor de R${valor:.2f}' + extrato # adiciona o deposito realizado ao extrato

    return saldo, extrato

def saque(*, saldo, saque, extrato, limite_saque, limite_valor):
    """Função que realiza o saque do valor informado pelo usuário

    Args:
        saldo (float): saldo atual do usuário
        saque (float): valor que o usuário deseja sacar
        extrato (string): extrato bancário do usuário, que contém todo seu histórico de operações
        limite_saque (int): quantidade de saques que o usuário pode realizar por dia
        limite_valor (int): valor máximo permitido ao usuário para saques

    Returns:
        float/string/int: atualiza o valor, o extrato e o limite de saque do usuário após o saque.
    """
    
    if saque > saldo: # verifica se o valor de saque é maior do que o disponível no saldo.
        print('Saldo insuficiente.')

    elif limite_saque == 0: # varifica se o usuário já utilizou todos os 3 saques diários
        print(
            'Infelizmente o limite de saque diário já foi atingido, por favor, tente novamente amanhã!')

    elif saque > limite_valor: # verifica se o valor para saque é maior que o limite
        print('Valor acima do limite diário.')

    elif saque == 0: # verifica se o valor para saque é 0
        print('Valor inválido.')

    else:
        saldo -= saque
        print(f'Saque efetuado com êxito. Saldo atual: R${saldo:.2f}')
        limite_saque -= 1
        extrato = f'\nSaque no valor de R${saque:.2f}' + extrato # adiciona o saque realizado ao extrato

    return saldo, extrato, limite_saque

def consulta_extrato(saldo, /, *, extrato):
    """Função de estilização do extrato

    Args:
        saldo (float): saldo atual do usuário
        extrato (string): extrato bancário do usuário, que contém todo seu histórico de operações.
    """
    print('\n========== EXTRATO ==========\n')
    print(f'Saldo atual: {saldo:.2f}')
    print(extrato)
    print('\n===============================')

def cadastrar_usuario(usuarios):
    """Função que realiza o cadastro de usuário no banco

    Args:
        usuarios (list): lista que contém todos os usuários já cadastrados no banco.
    """
    nome = str(input('Informe seu nome e sobrenome: '))
    cpf = str(input('Informe seu CPF (apenas números): '))
    for pessoas in usuarios: # verifica se já existe um usuário com o mesmo cpf cadastrado
        if pessoas['CPF'] == cpf:
            print('Já existe um usuário com este CPF!')
            return

    print('Me informe sua data de nascimento: ')
    dia = str(input('Dia: '))
    mes = str(input('Mês: '))
    ano = str(input('Ano: '))

    nascimento = f'{dia}/{mes}/{ano}'
    
    print('Me informe o seu endereço: ')
    rua = str(input('Logradouro: '))
    numero = str(input('Número da casa: '))
    bairro = str(input('Bairro: '))
    cidade = str(input('Cidade: '))
    estado = str(input('Sigla do estado: '))
    
    endereco = f'{rua}, {numero} - {bairro} - {cidade}/{estado}' # formata o endereço informado pelo usuário
    
    usuarios.append({'Nome':nome, 'CPF':cpf, 'Data de Nascimento':nascimento, 'Endereço': endereco})
    
    print('Usuário cadastrado com sucesso!')
    
def conta_corrente(agencia, num_conta, usuarios, contas):
    """Função que realiza a criação de conta corrente para os usuários do banco

    Args:
        agencia (int): agência na qual o usuário está cadastrado
        num_conta (int): número da conta que será dado ao usuário
        usuarios (list): lista que contém todos os usuário cadastrados no banco
        contas (list): lista que contém todas as contas dos usuários do banco
    """
    
    cpf = str(input('Me informe seu CPF (apenas números): '))
    existe = 0
    
    for pessoa in usuarios: # verifica se o usuário está cadastrado no banco
        if pessoa['CPF'] == cpf:
            existe += 1
            
    if existe == 0:
        print('Usuário não existe!')
        return
    
    contas.append({'Agencia': agencia, 'Número da Conta': num_conta, 'Usuário': cpf})
    
    print('Conta criada com êxito!')
    
def listar_contas(contas, usuarios):
    for pessoa in contas:
        for user in usuarios: 
            if pessoa['Usuário'] == user['CPF']:
                titular = user['Nome']
        print(f'\nTitular: {titular} \nAgência: 0001 \nConta: {pessoa['Número da Conta']}')
    
def main():
    saldo = 0
    extrato = ''
    limite_valor = 500
    LIMITE_SAQUE = 3
    AGENCIA = '0001'
    usuarios = []
    contas = []

    while True:
        operacao = menu()

        if operacao == 'Q':
            break

        elif operacao == 'D':
            valor = float(input('Qual valor deseja depositar: '))
            saldo, extrato = deposito(saldo, valor, extrato)

        elif operacao == 'S':
            valor_saque = float(input('Qual valor deseja sacar: '))
            saldo, extrato = saque(
                saldo=saldo,
                saque=valor_saque,
                extrato=extrato,
                limite_saque=LIMITE_SAQUE,
                limite_valor=limite_valor
            )

        elif operacao == 'E':
            consulta_extrato(saldo, extrato=extrato)
            
        elif operacao == 'U':
            cadastrar_usuario(usuarios=usuarios)
            
        elif operacao == 'C':
            numero_conta = len(contas) + 1 # cria o número da conta corrente
            conta_corrente(AGENCIA, numero_conta, usuarios, contas)
            
        elif operacao == 'L':
            listar_contas(contas, usuarios)

        else:
            print('Operação inválida. Por favor, tente novamente.')

main()
