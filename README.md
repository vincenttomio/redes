# Projeto de Redes: Sistema de Proxy e Servidor

Este projeto consiste na implementação de um sistema de proxy e servidor em Python, desenvolvido como parte de um trabalho prático da disciplina de Redes de Computadores.

## Descrição

A comunicação eficiente entre clientes e servidores é essencial em muitas aplicações de rede. Neste trabalho prático, foi proposta a construção de uma proxy para facilitar essa comunicação. A proxy atua como uma entidade intermediária entre o cliente e o servidor, simplificando o processo de acesso aos dados.

## Funcionalidades Principais

- A proxy facilita a comunicação entre clientes e servidor, permitindo uma implementação mais flexível e modular do sistema de rede.
- A proxy é capaz de obter dados do servidor sem sobrecarregá-lo e encaminhar os dados aos clientes, mantendo a integridade dos dados do servidor.

## Componentes do Projeto

- **server.py:** Script do servidor que responde às solicitações dos clientes e mantém o estado do sistema.
- **proxy.py:** Script da proxy que gerencia as conexões entre clientes e servidor, atuando como intermediário.
- **client1.py:** Cliente que se conecta diretamente ao servidor para obter e modificar os dados.
- **client2.py:** Cliente que se conecta à proxy para obter os dados do servidor.

## Execução do Projeto

1. Inicie o servidor: `python3 server.py 1500`
2. Inicie a proxy: `python3 proxy.py 1500`
3. Execute o Cliente 2: `python3 client2.py`
4. Execute o Cliente 1: `python3 client1.py 1500`

## Relatório e Contato

Há um relatório na pagina institucional [www.inf.ufpr.br/vvsbt20/redes](www.inf.ufpr.br/vvsbt20/redes).


## Contribuição

Contribuições são bem-vindas!

## Contato

Para mais informações, entre em contato com [vincent.tomio@ufpr.br](vincent.tomio@ufpr.br).


