# Descrição da Implementação - Sistema Bancário em Python

Esta implementação em Python é de um sistema bancário básico que permite ao usuário realizar operações como depósito, saque, visualização de extrato e sair do sistema.
Este projeto foi proposto no Bootcamp: Python AI Backend Developer - Vivo.

## Funcionalidades

- **Menu Principal**: O programa exibe um menu com opções para o usuário, onde ele pode escolher entre:
    - [d] Depositar
    - [s] Sacar
    - [e] Extrato
    - [q] Sair

- **Variáveis de Controle**:
   - `saldo`: Armazena o saldo da conta do usuário.
   - `limite`: Define o limite máximo de saque por transação.
   - `extrato`: Armazena o histórico das transações realizadas.
   - `numero_saques`: Registra o número de saques realizados em um dia.
   - `LIMITE_SAQUES`: Define o limite máximo de saques por dia.
   - `count`: Contador utilizado para numerar as transações no extrato.

- **Estrutura de Repetição**:
   O programa executa em um loop infinito (`while True`), permitindo que o usuário realize várias operações consecutivas até optar por sair do sistema.

- **Condições de Operações**:
   - **Depósito (`d`)**: Solicita ao usuário o valor a ser depositado e adiciona esse valor ao saldo. Se o valor for inválido (negativo ou zero), exibe uma mensagem de erro.
   - **Saque (`s`)**: Verifica se o número de saques diários ultrapassou o limite. Se não, solicita ao usuário o valor do saque. Verifica se o saque excede o saldo ou o limite de saque. Se for inválido, exibe uma mensagem de erro. Caso contrário, realiza o saque, atualiza o saldo e registra a transação no extrato.
   - **Extrato (`e`)**: Exibe o extrato das transações realizadas até o momento, incluindo depósitos e saques, bem como o saldo final.
   - **Sair (`q`)**: Encerra o programa.

- **Validação de Entradas**:
   O programa valida as entradas do usuário, garantindo que apenas opções válidas sejam selecionadas e que os valores inseridos sejam numéricos e positivos, quando necessário.

- **Exibição de Mensagens**:
   O programa fornece feedback ao usuário após cada operação, informando sobre o resultado da operação ou qualquer erro que ocorra.

Esta é uma implementação simples, mas funcional, de um sistema bancário em Python. É uma base sólida que pode ser expandida com recursos adicionais, como autenticação de usuário, persistência de dados e interface gráfica.

