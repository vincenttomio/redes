import socket
import sys
import time


# Verificando se a porta do servidor foi fornecida como argumento de linha de comando
if len(sys.argv) != 2:
    print("Uso: python3 proxy.py <porta_servidor>")
    sys.exit(1)

# Obtendo a porta do servidor a partir do argumento de linha de comando
PORT_SERVIDOR = int(sys.argv[1])

# Definindo o endereço e porta do servidor
HOST_SERVIDOR = '127.0.0.1'
HOST_PROXY = '127.0.0.1'

# Porta fixa da proxy
PORT_PROXY = 1501  

# Definindo a identificação
TAG_PROXY = "Proxy"

# Função para obter o valor inteiro do servidor
def obter_valor_inteiro():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Conectando-se ao servidor
        server_socket.connect((HOST_SERVIDOR, PORT_SERVIDOR))
        
        # Enviando identificação como Proxy
        server_socket.sendall(f'IDENTIFY {TAG_PROXY}'.encode())
        
        # Aguardando confirmação do servidor antes de enviar o comando 'get'
        server_response = server_socket.recv(1024).decode()
        print(f'Resposta do servidor: {server_response}')  # Mensagem de depuração
        if server_response == 'OK':
            # Enviando o comando 'get'
            server_socket.sendall(b'get')
            
            # Recebendo o valor do inteiro do servidor
            inteiro = server_socket.recv(1024).decode()
            return inteiro
        else:
            print('Erro ao identificar o proxy no servidor.')
            return None

# Função para lidar com a conexão do cliente
def handle_client(client_connection, client_address):
    # Recebendo a identificação do cliente
    identification = client_connection.recv(1024).decode()
    print(f'Mensagem de identificação recebida: {identification}')
    
    if identification.startswith('IDENTIFY'):
        # Enviando resposta 'OK' após a identificação
        client_connection.sendall(b'OK')
        
        # Enviando o valor inteiro do servidor para o cliente
        inteiro = obter_valor_inteiro()
        if inteiro is not None:
            client_connection.sendall(inteiro.encode())
    else:
        # Se a identificação não for recebida corretamente, envia uma mensagem de erro
        client_connection.sendall(b'Erro de identificacao')


# Criando um socket TCP/IP para o proxy
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_socket:
    # Vinculando o socket da proxy com o endereço e porta especificados
    proxy_socket.bind((HOST_PROXY, PORT_PROXY))

    # Colocando a proxy para escutar por conexões
    proxy_socket.listen(1)
    print('Proxy escutando na porta', PORT_PROXY)

    while True:
        # Aguardando uma conexão do cliente
        print('Aguardando conexão do cliente...')
        client_connection, client_address = proxy_socket.accept()
        with client_connection:
            handle_client(client_connection, client_address)
        
        # Pausa antes de aceitar a próxima conexão
        time.sleep(5)  # Intervalo de tempo entre as requisições ao servidor

# Propósito da pausa entre as conexões:
# - A pausa permite que a proxy não sobrecarregue o servidor com conexões muito frequentes,
#   garantindo um intervalo de tempo entre as requisições ao servidor.
