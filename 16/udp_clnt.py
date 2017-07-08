from socket import *
from time import ctime

HOST = '192.168.0.98'
PORT = 9999
ADDR = (HOST, PORT)
BUFFSIZ = 1024

cs = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('> ')
    if not data:
        break
    cs.sendto(data.encode('utf-8'), ADDR)
    data, addr = cs.recvfrom(BUFFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))
cs.close()
