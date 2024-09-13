from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver

class RealTimeProcessor(LineReceiver):
    def lineReceived(self, line):
        print(f"Received: {line}")
        self.sendLine(f"Processed: {line}")

class RealTimeFactory(Factory):
    def buildProtocol(self, addr):
        return RealTimeProcessor()

reactor.listenTCP(8000, RealTimeFactory())
reactor.run()
