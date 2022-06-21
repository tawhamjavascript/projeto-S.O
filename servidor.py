import socket
from ArquivoError import ArquivoError
from gerenciador import Gerenciador
from threading import Thread


TAMANHO_MENSAGEM = 1024
HOST = "0.0.0.0"
PORT = 40000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv = (HOST, PORT)
sock.bind(serv)
sock.listen(50)
gerenciador_arquivo = Gerenciador()


def processa_mensagem(mensagem, coneccao, cliente):
    mensagem_decodificada = mensagem.decode()
    mensagem_decodificada = mensagem_decodificada.split()
    if mensagem_decodificada[0] == "download" or mensagem_decodificada[0] == "read":
        nome_arquivo = "".join(mensagem_decodificada[1:])
        try:
            conteudo_arquivo = gerenciador_arquivo.ler_arquivo(nome_arquivo)
            coneccao.send(str.encode(conteudo_arquivo))

        except ArquivoError as error:
            coneccao.send(str.encode("404"))

    elif mensagem_decodificada[0] == "write":
        nome_arquivo = "".join(mensagem_decodificada[1])
        dados = " ".join(mensagem_decodificada[2:])
        try:
            gerenciador_arquivo.escrever_arquivo(nome_arquivo, dados)
            coneccao.send(str.encode("404"))

        except ArquivoError as error:
            coneccao.send(str.encode(error))

    elif mensagem_decodificada[0] == "create":
        nome_arquivo = ''.join(mensagem_decodificada[1])
        try:
            gerenciador_arquivo.criar_arquivo(nome_arquivo)
            coneccao.send(str.encode("ARQUIVO_CRIADO " + nome_arquivo))

        except ArquivoError as error:
            coneccao.send(str.encode("301"))


def processa_cliente(con, cliente):
    while True:
        msg = con.recv(TAMANHO_MENSAGEM)
        if not msg or processa_mensagem(msg, con, cliente): break

    con.close()
    print("Cliente desconectado:", cliente)


while True:
    try:
        con, cliente = sock.accept()

    except: break
    thread = Thread(target=processa_cliente, args=(con, cliente))

    thread.start()


sock.close()


