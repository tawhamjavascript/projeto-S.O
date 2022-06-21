import threading


arquivo = threading.Lock() # atribui a variável um automaticamente
mutex = threading.Lock() # atribui a variável um automaticamente
contador_leitores = 0


def ler_conteudo():
    pass


def processar_dados():
    pass




def leitores():
    global contador_leitores
    while True:
        with mutex:  # dá um down no mutex
            contador_leitores += 1  # soma mais um o número de leitores
            if contador_leitores == 1:  # verifica se quantidade de leitores é igual a um
                arquivo.acquire()   # adquiri o arquivo

        ler_conteudo()  # ler o conteúdo do arquivo
        with mutex:  # dá um down no mutex
            contador_leitores -= 1  # tira um leitor
            if contador_leitores == 0:  # verifica se os leitoes é igual a zero
                arquivo.release()   # se for libera o arquivo

        processar_dados()   # processa os dados do arquivo


def escritores(texto):
    while True:
        with arquivo:
            print("alouu")
            # vai ter código de escrever a aqui


















