from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory
from twisted.internet import reactor

class MyWebSocketProtocol(WebSocketServerProtocol):
    def onMessage(self, payload, isBinary):
        self.sendMessage(payload, isBinary)

factory = WebSocketServerFactory("ws://localhost:9000")
factory.protocol = MyWebSocketProtocol

reactor.listenTCP(9000, factory)
reactor.run()
