from twisted.internet import reactor, ssl
from twisted.web import server, resource

class SecureAPI(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        return b"Hello from Secure Twisted API!"

sslContext = ssl.DefaultOpenSSLContextFactory(
    'path/to/server.key', 'path/to/server.crt')

site = server.Site(SecureAPI())
reactor.listenSSL(8443, site, sslContext)
reactor.run()
