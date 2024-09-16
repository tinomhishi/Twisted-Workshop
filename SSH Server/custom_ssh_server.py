from twisted.conch.ssh import factory, keys, userauth, connection, transport
from twisted.cred import portal, checkers
from twisted.internet import reactor
from twisted.python import log
import sys

# Enable logging to stdout
log.startLogging(sys.stdout)

# Avatar representing an authenticated user
class ExampleAvatar:
    pass

# Realm for the SSH service
class ExampleRealm:
    def requestAvatar(self, avatarId, mind, *interfaces):
        return interfaces[0], ExampleAvatar(), lambda: None

# Setting up the SSH server factory
class ExampleSSHFactory(factory.SSHFactory):
    def __init__(self, privateKeyPath, publicKeyPath, passphrase=None):
        # If the key is encrypted, provide the passphrase
        self.privateKey = keys.Key.fromFile(privateKeyPath, passphrase=passphrase)
        self.publicKey = keys.Key.fromFile(publicKeyPath)
    
    def getPublicKeys(self):
        return {b'ssh-rsa': self.publicKey}
    
    def getPrivateKeys(self):
        return {b'ssh-rsa': self.privateKey}

# Path to your RSA key files
privateKeyPath = "keys/ssh_host_rsa_key"
publicKeyPath = "keys/ssh_host_rsa_key.pub"
passphrase = b"tino"  # Replace with your passphrase

# Create an instance of the custom SSH factory
sshFactory = ExampleSSHFactory(privateKeyPath, publicKeyPath, passphrase)

# Use a realm and portal for authentication
realm = ExampleRealm()
sshFactory.portal = portal.Portal(realm)

# Register a simple username/password checker (In-memory)
checker = checkers.InMemoryUsernamePasswordDatabaseDontUse()

# Adding users and passwords
checker.addUser(b"user1", b"password1")  # Add user "user1" with password "password1"
checker.addUser(b"user2", b"password2")  # Add another user "user2" with password "password2"

# Register the checker to the portal
sshFactory.portal.registerChecker(checker)

# Listen for SSH connections on port 2222
reactor.listenTCP(2222, sshFactory)
reactor.run()
