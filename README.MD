# Sistema Bancário em Python

Este é um sistema bancário básico implementado em Python, oferecendo funcionalidades como depósito, saque, criação de usuários e contas, além da visualização de extratos.

## Funcionalidades

- **Menu Principal**: O programa apresenta um menu com várias opções de operações, incluindo depósito, saque, criação de usuários e contas, além da visualização de extratos.

- **Depósito**: Permite ao usuário fazer depósitos em sua conta, com validação do valor inserido.

- **Saque**: O usuário pode sacar dinheiro de sua conta, com verificações de saldo e limite de saques diários.

- **Extrato**: Exibe o extrato das transações realizadas, incluindo depósitos e saques, bem como o saldo final.

- **Criação de Usuários e Contas**: Permite ao usuário criar novos usuários e associar contas a esses usuários.

- **Listagem de Usuários e Contas**: Oferece a funcionalidade de listar todos os usuários e suas contas associadas.

## Funções Implementadas

- `menu()`: Exibe o menu principal do sistema.
- `deposito()`: Realiza a operação de depósito na conta do usuário.
- `sacar()`: Realiza a operação de saque da conta do usuário.
- `imprimir_extrato()`: Exibe o extrato bancário na tela.
- `criar_usuario()`: Cria um novo usuário no sistema.
- `filtrar_usuario()`: Filtra um usuário com base no CPF.
- `listar_usuarios()`: Lista todos os usuários cadastrados.
- `criar_conta()`: Cria uma nova conta associada a um usuário.
- `listar_contas()`: Lista todas as contas cadastradas no sistema.

## Execução

Para executar o programa, basta rodar o script `main()`.

```bash
python nome_do_arquivo.py
