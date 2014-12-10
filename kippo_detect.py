#!/usr/bin/python

import socket
import sys

if len(sys.argv) != 2:
	print '[+] Usage: python %s 1.1.1.1' % sys.argv[0]
	exit()

host = sys.argv[1]
port = 22

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
banner = s.recv(1024)
s.send('\n\n\n\n\n\n\n\n')
response = s.recv(1024)
s.close()

if "168430090" in response:
	print '[!] Kippo honeypot detected!'
