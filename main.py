def menu():

    menu = """

    ======== Menu - Sistema bancário ======
    -------------- Operações --------------
    [d] Depositar
    [s] Sacar
    [e] Extrato

    ---------- Contas e Usuarios ----------
    [nu] Novo Usuario
    [nc] Nova Conta
    [lu] Listar Usuarios
    [lc] Listar conta

    ---------------------------------------
    [q] Sair
    
    ==> """
    
    return menu

def deposito(valor, saldo, count, extrato, /):
    if valor <= 0:
        print('[ERRO]: O valor de depósito digitado é invalido!\n Operação cancelada!')
    else:
        saldo += valor
        count += 1
        extrato += f"{count} - [Depósito]: R$ {valor}\n"
        print(f'\n\n    Valor do saldo atual: R$ {saldo:.2f}')
    return saldo, extrato, count

def sacar(*, saldo, limite, numero_saques, count, extrato):
    saque = float(input("Digite o valor para saque: R$"))

    excedeu_limite = saque > limite
    excedeu_saldo = saque > saldo

    if excedeu_saldo:
        print(f'\n[ERRO]: O valor do saque é maior que o valor do saldo.\nOperação cancelada!')
        print(f'Valor do saldo atual: R$ {saldo:.2f}')

    elif excedeu_limite:
        print(f'\n[ERRO]: O limite da operação de saque são de R$ {float(limite):.2f}.\nOperação cancelada!')
        print(f'Valor do saldo atual: R$ {saldo:.2f}')

    elif saque > 0:
        saldo = saldo - saque
        numero_saques += 1
        count += 1
        extrato += f"{count} - [Saque]: R$ {saque}\n"
        print(f'Valor do saldo atual: R$ {saldo:.2f}')

    else:
        print('[ERRO]: Valor de saque invalidado!\nOperação cancelada. ')
    return saldo, numero_saques, extrato, count

def imprimir_extrato(saldo, /, *,extrato):
    impressao = f"""
   \n=============== Extrato Bancário =============== \n
    {extrato if extrato else 'Nenhuma Movimentação realizada hoje!'}
    \n\nSaldo: R$ {saldo:.2f})
    \n======================================================="""
    
    print(impressao)

def criar_usuario(usuarios):
    cpf = input("Informe o cpf (somente numeros): ")    
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n Atenção! Já existe usuário com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/uf): ")
    
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
            })
    
    print("### Usuário criado com sucesso! ####")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtratodos = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtratodos[0] if usuarios_filtratodos else None

def listar_usuarios(usuarios):
    seq = 1
    for i, usuario in enumerate(usuarios):
        print(f"{seq} - {usuario['nome']} - cpf: {usuario['cpf']}")
        seq += 1
        
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuario (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n #### Conta criada com sucesso ###")
        conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        return conta
    
    print(" Atenção! Usuario não encontrado. Encerrando opção.")

def listar_contas(contas):
    for conta in contas:
        registro = f"""
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("#" * 60)
        print(registro)
        

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    count = 0
    AGENCIA = "0001"
    
    usuarios = []
    contas = []

    while True:

        opcao = input(menu())

        if opcao == 'd':
            valor = float(input('Digite um valor para deposito: R$ '))
            saldo, extrato, count = deposito(valor, saldo, count, extrato)

        elif opcao == 's':
            excedeu_saque = numero_saques >= LIMITE_SAQUES

            if excedeu_saque:
                print(f'[ERRO]: O limite de saques diarios chegou ao limite.\nOperação cancelada!')
                print(f'Quantidade de saques realizadas: {numero_saques}.')
            else:
                saldo, numero_saques, extrato, count = sacar(saldo=saldo, limite=limite, numero_saques=numero_saques, count=count, extrato=extrato)

        elif opcao == 'e':
            imprimir_extrato(saldo, extrato=extrato)
            
        elif opcao == 'q':
            break
        
        elif opcao == 'nu':
            criar_usuario(usuarios)
            
        elif opcao == 'lu':
            listar_usuarios(usuarios)
            
        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                
        elif opcao == 'lc':
            listar_contas(contas)
        else:
            print('A opção selecionada é invalida!\n\nSelecione outra opção!')
            
            
main()