menu = '''

Qual operação deseja realizar?

    [D] - Deposito
    [S] - Saque
    [E] - Extrato
    [Q] - Sair
    
-> '''


saldo = 0
extrato = ''
limite_valor = 500
limite_saque = 3

while True:
    operacao = str(input(menu)).upper().strip()[0]

    if operacao == 'Q':
        break

    elif operacao == 'D':
        while True:
            deposito = float(input('Qual valor deseja depositar: '))
            if deposito <= 0:
                print('Por favor, digite um valor positivo.')
            else:
                saldo += deposito
                print(f'Deposito efetuado com êxito. Saldo atual: R${saldo:.2f}')
                extrato = f'\nDeposito no valor de R${deposito:.2f}' + extrato
                break

    elif operacao == 'S':
        while True:
            saque = float(input('Qual valor deseja sacar: '))

            if saque > saldo:
                print('Saldo insuficiente.')
                while True:
                    outro_valor = str(
                        input('Deseja seguir para o saque de outro valor: [S/N]\n')).upper().strip()[0]
                    if outro_valor not in 'SN':
                        print('Input inválido')
                    else:
                        break

            elif saque > 500:
                print('Valor acima do limite diário.')
                while True:
                    outro_valor = str(
                        input('Deseja seguir para o saque de outro valor: [S/N]\n')).upper().strip()[0]
                    if outro_valor not in 'SN':
                        print('Input inválido')
                    else:
                        break

            elif limite_saque == 0:
                print(
                    'Infelizmente o limite de saque diário já foi atingido, por favor, tente novamente amanhã!')
                break

            elif saque == 0:
                print('Valor inválido.')
                while True:
                    outro_valor = str(
                        input('Deseja seguir para o saque de outro valor: [S/N]\n')).upper().strip()[0]
                    if outro_valor not in 'SN':
                        print('Input inválido')
                    else:
                        break

            else:
                saldo -= saque
                limite_saque -= 1
                print(f'Saque efetuado com êxito. Saldo atual: R${saldo:.2f}')
                extrato = f'\nSaque no valor de R${saque:.2f}' + extrato
                break

    elif operacao == 'E':
        print('\n========== EXTRATO ==========\n')
        print(f'Saldo atual: {saldo:.2f}')
        print(extrato)
        print('\n===============================')

    else:
        print('Operação inválida. Por favor, tente novamente.')
