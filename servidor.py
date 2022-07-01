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



def processa_mensagem(mensagem, coneccao, cliente): # Metodo que faz o processamento da mensagem
    mensagem_decodificada = mensagem.decode() #Decodifica a mensagem e coloca dentro da variável, mensagem_decodificada
    mensagem_decodificada = mensagem_decodificada.split() # Dividi a mensagem decodificada em pequenos pedaços

    if mensagem_decodificada[0] == "READ": #Vai comparar a mensagem que está no índice da posição 0, se é igual a READ
        nome_arquivo = "".join(mensagem_decodificada[1:]) #Se for igual a READ, vai pegar o valor que está na posição 1 
        
        try: #Se existir
            conteudo_arquivo = gerenciador_arquivo.ler_arquivo(nome_arquivo + ".txt") #Vai ler o conteudo do arquivo.txt e colocalo na variável conteudo do arquivo
            coneccao.send(str.encode(conteudo_arquivo)) # Vai ser enviado o conteudo do arquivo codificado para o cliente

        except ArquivoError as error: #Caso não exista, vai enviar uma mensagem de erro 404 codificada para o cliente  
            coneccao.send(str.encode("404")) 

    elif mensagem_decodificada[0] == "DOWNLOAD": # Caso a mensagem que está na posição 0, seja igual DOWNLOAD
        nome_arquivo = "".join(mensagem_decodificada[1:]) #Percorre o que está no índicie 1 em diante e coloca na variável nome_arquivo
        try:
            conteudo_arquivo = gerenciador_arquivo.ler_arquivo(nome_arquivo + ".txt") # Ler o arquivo.txt e coloca seu conteudo na variável conteudo_arquivo
   
            coneccao.send(str.encode(f"203 {conteudo_arquivo}"))# Envia uma mensagem codificada, relatando que deu tudo certo, mais o conteudo do arquivo para o cliente

        except ArquivoError as error: #Caso ocorra um erro, vai enviar uma mensagem de erro 404 codificada para o cliente  
            coneccao.send(str.encode("404"))

    elif mensagem_decodificada[0] == "WRITE":  # Caso a mensagem que está no índice 0, seja igual WRITE
        nome_arquivo = "".join(mensagem_decodificada[1]) #Pega a mensagem que está no índice 1 e coloca na variável nome_arquivo
        dados = " ".join(mensagem_decodificada[2:]) # Percorre os índices que estão na posição 2 em diante, separando por um espaço e coloca na variável dados
    
        try:
            gerenciador_arquivo.escrever_arquivo(nome_arquivo + ".txt", dados) # Escreve no arquivo.txt
            coneccao.send(str.encode("205")) #Envia uma mensagem codificada de sucesso para o cliente
            

        except ArquivoError as error:
            coneccao.send(str.encode("404")) #Caso ocorra um erro, envia uma mensagem codificada de erro para o cliente

    elif mensagem_decodificada[0] == "CREATE": # Caso a mensagem que está no índice 0, seja igual CREATE
        nome_arquivo = ''.join(mensagem_decodificada[1]) # Pega o que está no íncide 1 e coloca na variável
        try:
            gerenciador_arquivo.criar_arquivo(nome_arquivo + ".txt") #Vai criar um arquivo.txt
            coneccao.send(str.encode("201")) #Envia uma mensagem de sucesso para o cliente

        except ArquivoError as error:
            coneccao.send(str.encode("444")) #Caso de errado, retorna uma mensagem de erro para o cliente


def processa_cliente(con, cliente): #Metodo para processar mensagem do cliente
    while True: #Enquanto for verdadeiro
        msg = con.recv(TAMANHO_MENSAGEM) #Ler o tamanho da mensagem do cliente
        if not msg or processa_mensagem(msg, con, cliente): break

    con.close() #Fecha a conexão e informa qual cliente foi desconecatado
    print("Cliente desconectado:", cliente)


while True:
    try:
        con, cliente = sock.accept() #Inicia uma conexão com o cliente

    except: break
    thread = Thread(target=processa_cliente, args=(con, cliente)) 

    thread.start() #Dá início a uma thread, para cada cliente criado


sock.close()