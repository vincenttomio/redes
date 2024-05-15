import socket
import sys


# Verificando se a porta foi fornecida como argumento de linha de comando
if len(sys.argv) != 2:
    print("Uso: python3 client.py <porta>")
    sys.exit(1)

# Definindo o endereço do servidor
HOST = '127.0.0.1'

# Definindo a identificação do cliente
NOME_CLIENTE = "Cliente 1"

# Obtendo a porta a partir do argumento de linha de comando
PORT = int(sys.argv[1])

# Criando um socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectando ao servidor
client_socket.connect((HOST, PORT))

# Mensagem de depuração
print(f'Enviando identificação como {NOME_CLIENTE}') 

# Enviando identificação com o prefixo 'IDENTIFY'
client_socket.sendall(f'IDENTIFY {NOME_CLIENTE}'.encode())

# Aguardando confirmação do servidor
server_response = client_socket.recv(1024).decode()
if server_response == 'OK':
    print('Identificação confirmada pelo servidor.')
else:
    print('Erro na identificação com o servidor.')
    client_socket.close()
    sys.exit(1)

print('Cliente conectado ao servidor na porta', PORT)

while True:
    # Menu de opções
    print('\nOpções:')
    print('1. Obter valor do inteiro')
    print('2. Definir valor do inteiro')
    print('3. Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        # Enviando o comando 'get' para obter o valor atual da variável inteira
        client_socket.sendall(b'get')
        # Recebendo e exibindo o valor do inteiro do servidor
        inteiro = client_socket.recv(1024).decode()
        print('Valor do inteiro:', inteiro)
    elif opcao == '2':
        novo_valor = input('Digite o novo valor para o inteiro: ')
        # Enviando o comando 'set' seguido pelo novo valor para definir o valor da variável inteira no servidor
        client_socket.sendall(('set ' + novo_valor).encode())
        # Aguardando confirmação do servidor
        resposta = client_socket.recv(1024).decode()
        if resposta == 'OK':
            print('Valor do inteiro atualizado com sucesso.')
        else:
            print('Erro ao atualizar o valor do inteiro.')
    elif opcao == '3':
        print('Encerrando conexão...')
        break
    else:
        print('Opção inválida. Tente novamente.')

# Fechando o socket do cliente
client_socket.close()

# Lógica do loop principal:
# - O cliente exibe um menu de opções para o usuário.
# - O cliente envia comandos para o servidor com base na escolha do usuário e exibe as respostas recebidas.
