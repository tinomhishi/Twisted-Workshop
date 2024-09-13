from twisted.internet import reactor, task

def print_time():
    print("Current time:", reactor.seconds())

lc = task.LoopingCall(print_time)
lc.start(2.0)  # Call every 2 seconds

reactor.run()
