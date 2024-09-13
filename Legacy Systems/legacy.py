from twisted.conch.ssh import factory, keys, userauth, connection, transport
from twisted.cred import portal, checkers
from twisted.internet import reactor

class ExampleAvatar:
    pass

class ExampleRealm:
    def requestAvatar(self, avatarId, mind, *interfaces):
        return interfaces[0], ExampleAvatar(), lambda: None

sshFactory = factory.SSHFactory()
sshFactory.portal = portal.Portal(ExampleRealm())
sshFactory.portal.registerChecker(checkers.InMemoryUsernamePasswordDatabaseDontUse(user="password"))

reactor.listenTCP(2222, sshFactory)
reactor.run()
