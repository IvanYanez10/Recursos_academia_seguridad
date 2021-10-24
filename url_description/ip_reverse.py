#!/user/bin/env python
#!_*_ coding: utf-8 _*_

import requests
from bs4 import BeautifulSoup

def rev(url):
	print("ip-reverse")
	agente = {'User-Agent':'Firefox'}
	print(url)	
	a = requests.get("https://viewdns.info/reverseip/?host={}&t=1".format(url), headers=agente)
	b = BeautifulSoup(a.text, 'html5lib')
	c = b.find(id="null")
	d = c.find(border="1")
	for l in d.find_all("tr"):
		print("sitio encontrado: " + l.td.string)