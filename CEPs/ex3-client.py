# -*- coding: cp1252 -*-
'''
    Exemplo básico de servidor web
    -- trata apenas o método GET
    -- responde com um texto html fixo (htmlpage)
'''

#import BaseHTTPServer, json, os, fnmatch
#import queryparser
#import Diretorio

import httplib
import sys

conn = httplib.HTTPConnection('35.237.56.163', 8080)
conn.request("GET", "/?op=estados")
r1 = conn.getresponse()
print r1.status, r1.reason
