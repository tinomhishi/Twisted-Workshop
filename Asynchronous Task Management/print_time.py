import datetime
from twisted.internet import reactor, task


def get_datetime_string_from_timestamp(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def print_time():
    print("Current time:", get_datetime_string_from_timestamp(reactor.seconds()))

lc = task.LoopingCall(print_time)
lc.start(2.0)  # Call every 2 seconds

reactor.run()
