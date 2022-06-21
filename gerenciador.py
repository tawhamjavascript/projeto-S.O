import os
from pathlib import Path
from ArquivoError import ArquivoError
from Arquivo import Arquivo


class Gerenciador:
    def __init__(self):
        self.__arquivos = self.__montador_arquivos()
        self.__caminho = "./arquivos/"

    def __montador_arquivos(self):
        arquivosLs = os.listdir("./arquivos")
        arquivos = {}
        for arquivo in arquivosLs:
            arquivos.update({arquivo: Arquivo(arquivo)})

        return arquivos

    def criar_arquivo(self, arquivo):
        caminho = self.__caminho + arquivo
        arquivoExiste = os.path.isfile(caminho)
        try:
            assert not arquivoExiste
            arquivo_caminho = Path(caminho)
            arquivo_caminho.touch()
            self.__arquivos.update({arquivo: Arquivo(arquivo)})

        except AssertionError:
            raise ArquivoError("arquivo inexistente")

    def ler_arquivo(self, arquivo):
        arquivo_objeto = self.__arquivos.get(arquivo)
        try:
            assert arquivo_objeto is not None
            texto = arquivo_objeto.ler_arquivo()
            return texto

        except AssertionError:

            raise ArquivoError("arquivo inexistente")

        # implementar o problema do leitores e escritores

    def escrever_arquivo(self, arquivo, texto):
        arquivo_objeto = self.__arquivos.get(arquivo)
        try:
            assert arquivo_objeto is not None
            arquivo_objeto.escrever_arquivo(texto)

        except AssertionError:
            raise ArquivoError("arquivo inexistente")










