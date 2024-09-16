import os
from twisted.internet import reactor, ssl
from twisted.web import server, resource

class SecureAPI(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        return b"Hello from Secure Twisted API!"

    if not os.path.exists('keys/server.key') or not os.path.exists('keys/server.crt'):
        Exception('Certs not found')

sslContext = ssl.DefaultOpenSSLContextFactory(
    'keys/server.key', 'keys/server.crt')

site = server.Site(SecureAPI())
reactor.listenSSL(8443, site, sslContext)
reactor.run()

# curl --insecure https://localhost:8443

'''
Add-Type @"
    using System.Net;
    using System.Security.Cryptography.X509Certificates;
    public class TrustAllCertsPolicy : ICertificatePolicy {
        public bool CheckValidationResult(
            ServicePoint srvPoint, X509Certificate certificate,
            WebRequest request, int certificateProblem) {
            return true;
        }
    }
"@
[System.Net.ServicePointManager]::CertificatePolicy = New-Object TrustAllCertsPolicy

# Now run your web request without worrying about SSL certificate validation
Invoke-WebRequest -Uri "https://localhost:8443"

'''