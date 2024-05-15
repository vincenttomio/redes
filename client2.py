import socket


# Definindo o endereço da proxy
HOST_PROXY = '127.0.0.1'
PORT_PROXY = 1501

# Definindo a identificação do cliente
NOME_CLIENTE = "Cliente 2"

# Criando um socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectando à proxy
client_socket.connect((HOST_PROXY, PORT_PROXY))

# Mensagem de depuração
print(f'Enviando identificação como {NOME_CLIENTE}') 

# Enviando identificação com o prefixo 'IDENTIFY'
client_socket.sendall(f'IDENTIFY {NOME_CLIENTE}'.encode())

# Aguardando confirmação da proxy antes de receber o valor do inteiro
proxy_response = client_socket.recv(1024).decode()
if proxy_response == 'OK':
    # Recebendo e exibindo o valor do inteiro da proxy
    inteiro = client_socket.recv(1024).decode()
    print('Identificação confirmada pelo servidor.')
    print('Valor do inteiro:', inteiro)
else:
    print('Erro ao identificar o cliente na proxy.')

# Fechando o socket do cliente
client_socket.close()

# Lógica do cliente:
# - O cliente envia uma identificação para a proxy usando o prefixo 'IDENTIFY'.
# - Após a confirmação da identificação, o cliente recebe o valor atual do inteiro da proxy.
# - O valor do inteiro é então exibido.
