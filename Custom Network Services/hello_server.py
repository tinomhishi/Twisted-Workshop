from twisted.web import server, resource
from twisted.internet import reactor

class SimpleAPI(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        return b"Hello from Twisted API!"

site = server.Site(SimpleAPI())
reactor.listenTCP(8080, site)
reactor.run()