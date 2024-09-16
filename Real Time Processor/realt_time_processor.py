from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver

# LineReceiver, which is used to handle data one line at a time
class RealTimeProcessor(LineReceiver):
    def lineReceived(self, line):
        print(f"Received: {line}")
        response = f"Processed: {line.decode('utf-8')}"
        self.sendLine(response.encode('utf-8'))

class RealTimeFactory(Factory):
    def buildProtocol(self, addr):
        return RealTimeProcessor()

reactor.listenTCP(8888, RealTimeFactory())
reactor.run()
