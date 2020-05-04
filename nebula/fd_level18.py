#!/usr/bin/python


OPEN_MAX = 1024
res = ''
for i in range(OPEN_MAX - 4): # OPEN_MAX - stdin - stdout - stderr
    res += '-d fd_{} '.format(str(i))
print res
