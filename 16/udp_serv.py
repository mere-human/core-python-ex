from socket import *
from time import ctime

HOST = '192.168.0.98' # use any address that is available
PORT = 9999
ADDR = (HOST, PORT)
BUFFSIZ = 1024

ss = socket(AF_INET, SOCK_DGRAM)
ss.bind(ADDR)

while True:
    print('waiting for connection...')
    data, addr = ss.recvfrom(BUFFSIZ)
    data = '[%s] %s' % (ctime(), data.decode('utf-8'))
    ss.sendto(data.encode('utf-8'), addr)
    print('...received from and returned to:', addr)
ss.close()
