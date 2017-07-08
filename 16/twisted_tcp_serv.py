from twisted.internet import protocol, reactor
from time import ctime

PORT = 9999

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        self.clnt = self.transport.getPeer().host
        print('...connected from:', self.clnt)
    def dataReceived(self, data):
        d = '[%s] %s' % (ctime(), data.decode('utf-8'))
        self.transport.write(d.encode('utf-8'))

factory = protocol.Factory()
factory.protocol = TSServProtocol
print('waiting for connection...')
reactor.listenTCP(PORT, factory)
reactor.run()