import socket


HOST = '127.0.0.1'
PORT = 40000
print('Servidor:', HOST+':'+str(PORT))
serv = (HOST, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(serv)
print('Para sair use CTRL+C\n')
while True:
    try:
        msg = input('Mensagem: ')
    except: break
    sock.send(str.encode(msg))
    msg = sock.recv(1024)
    if not msg: break
    msg = msg.decode()
    print('Recebi:', msg)

sock.close()