from socket import *

HOST = 'localhost'
PORT = 9999
ADDR = (HOST, PORT)
BUFFSIZ = 1024


while True:
    cs = socket(AF_INET, SOCK_STREAM)
    cs.connect(ADDR)
    data = input('> ')
    if not data:
        break
    cs.send((data + '\n').encode('utf-8'))
    data = cs.recv(BUFFSIZ)
    if not data:
        break
    print(data.decode('utf-8').strip())
    cs.close() # connection is closed after request is handled
