#!/user/bin/env python
#!_*_ coding: utf-8 _*_

import requests
from bs4 import BeautifulSoup

def who(url):
	print("Whois")
	solicitud = requests.get("https://who.is/whois/{}".format(url))
	soup = BeautifulSoup(solicitud.text, 'html5lib')
	print(soup)
	for l in soup.find_all("div",{"class":"rawWhois"}):
		print(l.get_text())