import socket
import sys

HOST = 'localhost'  # Endereço IP do Servidor
PORT = 40000        # Porta em que o cliente escuta
TAM_MSG = 1024

lista_de_erros = {        # Lista de erros possíveis
    "404": "Arquivo não existe",
    "444": "Arquivo já existe",
}

lista_de_sucesso = {     # Lista de sucessos 
    "201": "Arquivo criado com sucesso",
    "203": "Download com sucesso",
    "205": "Alterações salvas"
}

lista_comandos = {      # Lista de comandos que o usuário pode escolher
    "criar": "CREATE",
    "baixar": "DOWNLOAD",
    "escrever": "WRITE",
    "ler": "READ",
    "sair": "EXIT"
}

if len(sys.argv) > 1:  # Pega o endereço IP do servidor digitado pelo cliente
    HOST = sys.argv[1]

serv = (HOST, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Definindo o socket como TCP stream    
sock.connect(serv)  #Conectando com o socket


while True:    # Menu de escolhas do usuário
    print()
    print("*=" * 40, "\n")
    print('Criar arquivo: "criar nome do arquivo"', "\n")
    print("-" * 40, "\n")
    print('Baixar: "baixar nome do arquivo"',"\n")
    print("-" * 40, "\n")
    print('Escrever: "escrever nome do arquivo"', "\n")
    print("-" * 40, "\n")
    print('Ler arquivo: "ler nome do arquivo"', "\n")
    print("-" * 40, "\n")
    print("Encerrar use: 'sair'", "\n")

    print("*=" * 40, "\n")

    cmd_usr = input("Digite algum comando: ").split()
    try:
        comando = lista_comandos.get(cmd_usr[0])   # Ler o comando dado pelo usuário
        assert comando is not None                 # Verifica se o comando existe
        if comando == "CREATE":
            sock.send(str.encode(comando + " " + cmd_usr[1]))     # Vai enviar para o servidor o comando com o nome do arquivo
            dados = sock.recv(TAM_MSG)
            msg_status = dados.decode()
            if lista_de_erros.get(msg_status):        # Se tiver algum erro ele exibe o erro na tela
                print(lista_de_erros.get(msg_status))

            else:
                print(lista_de_sucesso.get(msg_status))   # Se for tudo certo ele exibe a mensagem de sucesso 201
        
        elif comando == "DOWNLOAD":      
            sock.send(str.encode(comando + " " + cmd_usr[1]))  # Envia para o servidor o comando mais o nome do arquivo
            dados = sock.recv(TAM_MSG)
            dados = dados.decode().split() # Decodifica a mensagem e transforma em uma lista
            msg_status = dados[0] # Status da mensagem
            texto = " ".join(dados[1:])  #Pega o texto do arquivo

            if lista_de_erros.get(msg_status) is None:     
                with open(f"{cmd_usr[1]}.txt", "a", encoding="utf-8") as arq: # Cria o arquivo
                    for linha in texto:
                        arq.write(linha) # Escreve no arquivo

                    arq.write("\n")

                print(lista_de_sucesso.get(msg_status))   # Se tudo der certo exibe na tela a mensagem de sucesso 203

            else:
                print(lista_de_erros.get(dados)) # Se acontecer algum erro exibe a mensagem de erro na tela

        elif comando == "READ":
            sock.send(str.encode(comando + " " + cmd_usr[1]))   # Envia para o servidor o comando mais o nome do arquivo
            dados = sock.recv(TAM_MSG).decode()
            if lista_de_erros.get(dados) is None:    # Se não tiver erro exibe na tela o conteúdo do arquivo
                    print(palavra)       

            else:
                print(lista_de_erros.get(dados)) # Se tiver erro exibe a mensagem de erro correspondente


        elif comando == "WRITE":
            nome_arquivo = cmd_usr[1]  # Pega o nome do arquivo 
            texto = " ".join([palavra for palavra in cmd_usr[2:]]) # faz uma interação na lista e transforma em string
            sock.send(str.encode(comando + " " + nome_arquivo + " " + texto)) # Envia ao servidor o comando mais o nome do arquivo mais o texto escrito 
            msg_status = sock.recv(TAM_MSG).decode()
            if lista_de_erros.get(msg_status) is None:    # Se não tiver nenhum erro exibe a mensagem de sucesso 205
                print(lista_de_sucesso.get(msg_status))
            
            else:
                print(lista_de_erros.get(msg_status))    # Se tiver erro exibe uma mensagem de erro

        elif comando == "EXIT" :  # Digite EXIT para sair do cliente
            break

    except AssertionError:   # Se digitar um comando que não existe
        print("Comando não existe")

sock.close()  #Encerra o cliente
