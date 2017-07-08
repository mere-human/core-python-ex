from socket import *
from time import ctime

HOST = '192.168.0.98' # use any address that is available
PORT = 9999
ADDR = (HOST, PORT)
BUFFSIZ = 1024

ss = socket(AF_INET, SOCK_STREAM)
ss.bind(ADDR)
ss.listen(5) # max num of incoming requests

while True:
    print('waiting for connection...')
    cs, addr = ss.accept()
    print('...connected from:', addr)
    while True:
        data = cs.recv(BUFFSIZ)
        if not data:
            break
        data = '[%s] %s' % (ctime(), data.decode('utf-8'))
        cs.send(data.encode('utf-8'))
    cs.close()
ss.close()
