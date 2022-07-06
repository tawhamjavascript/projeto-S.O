import ascii
import time

professores = ["https://anuncie-ja-1.tawham2.repl.co/imgs/gustavo.png", "https://anuncie-ja-1.tawham2.repl.co/imgs/leonidas.jpg"]
alunos = ["https://anuncie-ja-1.tawham2.repl.co/imgs/mellaine.png", "https://anuncie-ja-1.tawham2.repl.co/imgs/gabriel.jpeg", "https://anuncie-ja-1.tawham2.repl.co/imgs/tawham.jpeg"]

def exibir_professores():
    with open("./professores.txt", "r") as f:
        print(f.read())

    time.sleep(3)
    for foto in professores:
        output = ascii.loadFromUrl(foto)
        print(output)
        time.sleep(3)


def exibir_alunos():
    with open("./alunos.txt", "r") as f:
        print(f.read())

    time.sleep(3)

    for foto in alunos:
        output = ascii.loadFromUrl(foto)
        print(output)
        time.sleep(3)

