# -*- coding: cp1252 -*-
'''
    Exemplo básico de servidor web
    -- trata apenas o método GET
    -- responde com um texto html fixo (htmlpage)
'''

#import BaseHTTPServer, json, os, fnmatch
#import queryparser
#import Diretorio

#import urlparse
#import httplib
#import sys
#import httplib2
import json, os
#import socket 
import requests 


url = "http://35.229.35.219:8080/?op=estados"
headers = {'cache-control': "no-cache"}
response = requests.request("GET", url, headers=headers)

print json.dumps(json.loads(response.text), indent=2)


'''
HOST = '35.229.35.219'  # The remote host
PORT = 8080             # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.bind((HOST, PORT))
s.connect((HOST, PORT))
s.listen(5)
conn, addr = s.accept()
print 'Connected by', addr

#def constultaCEP('69301015', 'RR')
'''    
