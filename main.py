menu = """
Menu - Sistema bancário
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

digite uma opção: 
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
count = 0

while True:
    
    opcao = input(menu)
    
    if opcao == 'd':
        deposito = float(input('Digite um valor para deposito: R$ '))
        if deposito <= 0:
            print('[ERRO]: O valor de depósito digitado é invalido!\n Operação cancelada!')
        else:
            saldo += deposito
            count += 1
            extrato += f"{count} - [Deposito]: R$ {deposito}\n"
            print(f'Valor do saldo atual: R$ {saldo:.2f}')
            
    elif opcao == 's':
        excedeu_saque = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saque:
            print(f'[ERRO]: O limite de saques diarios chegou ao limite.\nOperação cancelada!')
            print(f'Quantidade de saques realizadas: {numero_saques}.')
        else:
            saque = float(input("Digite o valor para saque: R$"))
            
            excedeu_limite = saque > limite
            excedeu_saldo = saque > saldo
            
            if excedeu_saldo:
                print(f'[ERRO]: O valor do saque é maior que o valor do saldo.\nOperação cancelada!')
                print(f'Valor do saldo atual: R$ {saldo:.2f}')

            elif excedeu_limite:
                print(f'[ERRO]: O limite da operação de saque são de R$ {float(limite):.2f}.\nOperação cancelada!')
                print(f'Valor do saldo atual: R$ {saldo:.2f}')
            
            elif saque > 0:
                saldo = saldo - saque
                numero_saques += 1
                count += 1
                extrato += f"{count} - [Saque]: R$ {saque}\n"
                print(f'Valor do saldo atual: R$ {saldo:.2f}')
                
            else:
                print('[ERRO]: Valor de saque invalidado!\nOperação cancelada. ')
                
                
    elif opcao == 'e':
        print("\n===============", 'Extrato Bancário', "===============",)
        print('Movimentações realizadas:')
        print(extrato if extrato else 'Nenhuma Movimentação realizada hoje!')
        print(f'\n\nSaldo final: R$ {saldo:.2f}')
        print("\n=======================================================",)
    elif opcao == 'q':
        break
    else:
        print('A opção selecionada é invalida!\n\nSelecione outra opção!')