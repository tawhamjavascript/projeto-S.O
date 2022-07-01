import os
from pathlib import Path
from ArquivoError import ArquivoError
from Arquivo import Arquivo


class Gerenciador:
    def __init__(self):
        self.__arquivos = self.__montador_arquivos()  # guarda um dict com todos objetos Arquivos
        self.__caminho = "./arquivos/"  # variável que vai guardar o caminho dos arquivos

    def __montador_arquivos(self):
        arquivosLs = os.listdir("./arquivos")  # guarda todos os arquivos presente no diretório arquivos
        arquivos = {}  
        for arquivo in arquivosLs:  
            arquivos.update({arquivo: Arquivo(arquivo)}) # adiciona a cada interação o objeto arquivo no dicionário

        return arquivos  # retorna o dict de objetos

    def criar_arquivo(self, arquivo):
        caminho = self.__caminho + arquivo  # guarda o caminho onde vai ser criado o arquivo
        arquivoExiste = os.path.isfile(caminho)  # verifica se o arquivo existe
        try:
            assert not arquivoExiste  # se o arquivo existir emite um erro
            arquivo_caminho = Path(caminho)  # Cria um objeto do tipo path 
            arquivo_caminho.touch()  # cria o arquivo 
            self.__arquivos.update({arquivo: Arquivo(arquivo)})  # adiciona o arquivo no dict

        except AssertionError:
            raise ArquivoError("arquivo inexistente")  # propaga um arquivoError

    def ler_arquivo(self, arquivo):
        arquivo_objeto = self.__arquivos.get(arquivo)  # pegar no dict o arquivo 
        try:
            assert arquivo_objeto is not None  # se o arquivo não existir solta um AssertionError
            texto = arquivo_objeto.ler_arquivo()  # ler o conteúdo do arquivo
            return texto  # retorna o conteúdo do arquivo

        except AssertionError:

            raise ArquivoError("arquivo inexistente")  # se tiver um error do tipo assertion propaga um erro arquivo Error


    def escrever_arquivo(self, arquivo, texto):
        arquivo_objeto = self.__arquivos.get(arquivo)  # pega o arquivo no dicionáro
        try:
            assert arquivo_objeto is not None  # se o arquivo não existir solta um AssertionError
            arquivo_objeto.escrever_arquivo(texto)  # escreve o texto no arquivo

        except AssertionError:
            raise ArquivoError("arquivo inexistente")  # se tiver um error do tipo assertion propaga um erro arquivo Error










