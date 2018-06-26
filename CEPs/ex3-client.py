# -*- coding: cp1252 -*-
'''
    Exemplo básico de servidor web
    -- trata apenas o método GET
    -- responde com um texto html fixo (htmlpage)
'''

#import BaseHTTPServer, json, os, fnmatch
#import queryparser
#import Diretorio

#import httplib
#import sys
import httplib2
import json
'''
conn = httplib.HTTPConnection('35.196.162.70', 8080)
conn.request("GET", "/?op=estados")
r1 = conn.getresponse()
print r1.status, r1.reason
'''
h = httplib2.Http(".cache")
resp, content = h.request("http://35.196.162.70:8080", "GET", data=json.dumps(payload))
print resp
