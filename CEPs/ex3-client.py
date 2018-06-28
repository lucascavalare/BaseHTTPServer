# -*- coding: cp1252 -*-
'''
    Exemplo básico de servidor web
    -- trata apenas o método GET
    -- responde com um texto html fixo (htmlpage)
'''

#import BaseHTTPServer, json, os, fnmatch
#import queryparser
#import Diretorio

import urlparse
#import httplib
#import sys
import httplib2
import json, os



url = 'http://35.229.35.219:8080/?'
parsed = urlparse.urlparse(url) 
print urlparse.parse_qs(parsed.query)['op'] 


'''
conn = httplib.HTTPConnection('35.196.162.70', 8080)
conn.request("GET", "/?op=estados")
r1 = conn.getresponse()
print r1.status, r1.reason

h = httplib2.Http(".cache")
resp, content = h.request("http://35.196.162.70:8080/?op=registro&estado=MG&url=http://mg.gov.br:8080", "PUT", headers={'content-type':'text/json'})
print json.dumps(resp, indent=5)
'''
'''
def test1(cep, url):
    #d = {"SP":"souza:8080", "RJ":"rodrigues:8080","RN": "silva:8080", "RO":"oliveira:8080", "MG":"pereira:8080"}
    d = {"MG":"mg.gov.br:8080"}
    r = {}
    #for s in d.keys():
    #    r[registraServidor(s,d[s])] = d[s]
    #print r
    #print consultaEstados()
    for s in d.keys():
        print consultaServidor(s)
    #print consultaServidor('kk')
    #print consultaServidor('pp')
    #for k in r.keys():
    #    print removeServidor(r[k],k)
'''
