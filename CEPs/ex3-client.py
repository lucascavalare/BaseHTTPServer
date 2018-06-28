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
#import json, os
import socket 


HOST = '10.142.0.4'  # The remote host
PORT = 8080             # The same port as used by the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr

#def constultaCEP('69301015', 'RR')
    
