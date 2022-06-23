import socket
import sys

HOST = 'localhost'  # Endereço IP do Servidor
PORT = 40000
TAM_MSG = 1024

lista_de_erros = {
    "404": "Arquivo não existe",
    "444": "Arquivo já existe",
}

lista_comandos = {
    "criar": "CREATE",
    "baixar": "DOWNLOAD",
    "escrever": "WRITE",
    "ler": "READ",
}

if len(sys.argv) > 1:
    HOST = sys.argv[1]

serv = (HOST, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(serv)
print("Para encerrar use EXIT")

while True:
    print('Para criar o arquivo digite "criar nome do arquivo "', 'Para baixar digite "baixar nome do arquivo"',
          'Para escrever digite "escrever nome do arquivo"', 'Para ler o arquivo digite "ler nome do arquivo"',
          sep="\n")
    cmd_usr = input("Digite algum comando: ").split()
    try:
        comando = lista_comandos.get(cmd_usr[0])
        assert comando is not None
        if comando == "CREATE":
            sock.send(str.encode(comando))
            dados = sock.recv(TAM_MSG)
            msg_status = dados.decode().split("\n")[0]
            if lista_de_erros.get(msg_status):
                print(lista_de_erros.get(msg_status))

            else:
                print(msg_status)






    except AssertionError:
        print("Comando não existe")

# Porta em que o Servidor está


tcp = socket.socket()  # Socket tcp

destino = (HOST, PORT)

tcp.connect(destino)

print('\nDigite suas mensagens')

print('Para sair use CTRL+X\n')

mensagem = input()  # Recebendo a mensagem

while mensagem != '\x18':
    tcp.send(str(mensagem).encode())

    mensagem = input()

tcp.close()  # Fechando o Socket
