import socket
import sys


# Verificando se a porta foi fornecida como argumento de linha de comando
if len(sys.argv) != 2:
    print("Uso: python3 server.py <porta>")
    sys.exit(1)

# Definindo o endereço do servidor
HOST = '127.0.0.1'

# Obtendo a porta a partir do argumento de linha de comando
PORT = int(sys.argv[1])

# Criando um socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vinculando o socket com o endereço e porta especificados
server_socket.bind((HOST, PORT))

# Colocando o servidor para escutar por conexões
server_socket.listen(1)

print('Servidor escutando na porta', PORT)

# Inicializando a variável inteira
inteiro = 0

while True:
    # Aguardando uma conexão
    print('Aguardando conexão...')
    connection, client_address = server_socket.accept()

    # Tentando receber a identificação do cliente
    try:
        identification = connection.recv(1024).decode()
        
        # Mensagem de depuração
        print(f'Mensagem de identificação recebida: {identification}')
        
        # Enviando resposta 'OK' após a identificação
        connection.sendall(b'OK')
    except Exception as e:
        print(f'Erro ao receber identificação: {e}')  # Mensagem de depuração

    try:
        while True:
            # Recebendo os dados do cliente
            data = connection.recv(1024).decode()
            if data:
                print('Mensagem recebida:', data)
                if data == 'get':
                    # Enviando o valor atual da variável inteira para o cliente
                    connection.sendall(str(inteiro).encode())
                elif data.startswith('set'):
                    # Atualizando o valor da variável inteira com o valor recebido do cliente
                    inteiro = int(data.split()[1])
                    print('Variável inteira atualizada para', inteiro)
                    connection.sendall(b'OK')
                else:
                    connection.sendall(b'Comando invalido')
            else:
                break
    finally:
        # Fechando a conexão
        connection.close()

# Protocolo de comunicação esperado:
# O cliente deve enviar uma identificação inicial para o servidor, usando o prefixo "IDENTIFY".
# Após a identificação bem-sucedida, o cliente pode enviar comandos "get" para obter o valor atual do inteiro,
# ou comandos "set <valor>" para definir o valor do inteiro no servidor.
