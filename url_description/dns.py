#! /user/bin/env python
#!_*_ coding: utf-8 _*_

import dns.resolver

def view(url):	
	consultas=["A","NS","MX","CNAME","AAAA"]
	for c in consultas:
		try:
			solicitud = dns.resolver.query(url,c)
			for req in solicitud:
				print(req)
		except Exception as e:
			print(e)
			print("No se logro la conexion")