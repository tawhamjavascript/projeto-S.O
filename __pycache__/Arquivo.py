import threading


class Arquivo:
    def __init__(self, nome_arquivo):
        self.__arquivo = threading.Lock()  # atribui a variável um automaticamente
        self.__mutex = threading.Lock()  # atribui a variável um automaticamente
        self.__contador_leitores = 0
        self.__nome_arquivo = nome_arquivo

    def ler_arquivo(self):
        while True:
            with self.__mutex:  # dá um down no mutex
                self.__contador_leitores += 1  # soma mais um o número de leitores
                if self.__contador_leitores == 1:  # verifica se quantidade de leitores é igual a um
                    self.__arquivo.acquire()  # adquiri o arquivo

            conteudo = self.ler_conteudo()  # ler o conteúdo do arquivo
            with self.__mutex:  # dá um down no mutex
                self.__contador_leitores -= 1  # tira um leitor
                if self.__contador_leitores == 0:  # verifica se os leitoes é igual a zero
                    self.__arquivo.release()  # se for libera o arquivo

            return conteudo

    def ler_conteudo(self):
        linhas = None  
        with open(f"./arquivos/{self.__nome_arquivo}", 'r', encoding='utf-8') as arquivo:  # abre o arquivo, no modo leitura, com a codificação utf-8
            linhas = arquivo.readlines()  # vai ler todas as linhas do arquivo
            linhas = " ".join([linha for linha in linhas])  # percorre todas as linhas dividindo os índices por um espaço em branco

        return linhas # retorna as linhas em modo de string

    def escrever_arquivo(self, dado):
        with self.__arquivo:  # dá um down no semafáro
            with open(f"./arquivos/{self.__nome_arquivo}", 'a', encoding='utf-8') as arquivo:  # abre o arquivo, e manda adicionar na última posição
                arquivo.write(dado + "\n")  # escreve o texto no arquivo e dá uma quebra de página no final
