import socket

HOST = 'localhost'     # Endereço IP do Servidor

PORT = 5000            # Porta em que o Servidor está


tcp = socket.socket()    # Socket tcp

destino = (HOST, PORT)

tcp.connect(destino)

print('\nDigite suas mensagens')

print('Para sair use CTRL+X\n')


mensagem = input()       # Recebendo a mensagem 

while mensagem != '\x18':       

   tcp.send(str(mensagem).encode()) 

   mensagem = input()


tcp.close()     # Fechando o Socket