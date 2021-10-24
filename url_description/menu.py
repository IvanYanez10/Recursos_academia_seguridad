#!/user/bin/env python
#!_*_ coding: utf-8 _*_

import whois
import ip_reverse
import dns

def main():
	print("Menu")

	print("1. DNS")
	print("2. ip reverse")
	print("3. whois")

	nb = input('> ')
	url = input('Direccion: http://www.')

	if nb=='1':
		dns.view(url)
	elif nb=='2':
		ip_reverse.rev(url)
	elif nb=='3':
		whois.who(url)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()
