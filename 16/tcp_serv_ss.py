from socketserver import (TCPServer as TCP,
    StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 9999
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self): # override, called on incoming msg
        print('...connected from:', self.client_address)
        data = '[%s] %s' % (ctime(), self.rfile.readline().decode('utf-8'))
        self.wfile.write(data.encode('utf-8'))

serv = TCP(ADDR, MyRequestHandler)
print('waiting for connection')
serv.serve_forever()