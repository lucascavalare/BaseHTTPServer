# -*- coding: cp1252 -*-
'''
    Exemplo básico de servidor web
    -- trata apenas o método GET
    -- responde com um texto html fixo (htmlpage)
'''

import BaseHTTPServer, json, os, fnmatch
import queryparser
import Diretorio

### texto fixo retornado como resposta ao get
#def resposta(cep):
#    parms = queryparser.parse(cep)
 #   return parms

def test1():
    d = {"SP":"souza:8080", "RJ":"rodrigues:8080","RN": "silva:8080", "RO":"oliveira:8080", "MG":"pereira:8080"}
    r = {}
    for s in d.keys():
        r[registraServidor(s,d[s])] = d[s]
    print r
    print consultaEstados()
    for s in d.keys():
        print consultaServidor(s)
    print consultaServidor('SC')
    print consultaServidor('RJ')
    for k in r.keys():
        print removeServidor(r[k],k)
'''
def consulta(path):
    file = 0
    print path
  #  while file != consulta:
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.json'):
            f = open(file)
            txt = f.read()
            lista = json.loads(txt)
            for d in lista:
                for value in d.values():
                    if value==path:
                        return d
                        #print 'CEP:',d['CEP'],'Cidade:',d['Cidade'],'Bairro:',d['Bairro'],'Estado:',d['Estado']

### em caso de url inválida 
notfound = "File not found"

def resposta(path):
  a = consulta(queryparser.parse(path))
  return json.dumps(a, indent=8)

def getParms(path):
    d = queryparser.parse(path)
    res = '<h3> Parâmetros:</h3>\n'
    for k in d.keys():
        res += '<p>'+k+'="'+d[k]+'"\n'
    return res
'''
'''
    classe que estende BaseHHTPRequestHandler:
    -- redefine o método do_Get() para que faça o tratamento desejado
    -- os demais métodos da biblioteca são mantidos 'as is'.
'''
'''
class ServidorExemplo1(BaseHTTPServer.BaseHTTPRequestHandler):

        def do_GET(self):
                # inicia o envio da resposta c/ código de retorno 200 (OK)
                self.send_response(200)
                # define o cabeçalho da resposta (neste caso 'avisa' que o conteúdo será html)
                self.send_header("Content-type","text/json")
                # 'fecha' o cabeçalho
                self.end_headers()
                # 'escreve' o conteudo da resposta
                self.wfile.write(resposta(self.path))
'''
'''
    Cria o servidor web, usando a classe definida acima,
    atendendo as requisições na porta 8080
'''
'''
httpserver = BaseHTTPServer.HTTPServer(("",8080), ServidorExemplo1)
'''
'''
    Ativa o serviço, 'ad infinitum' 
httpserver.serve_forever()
'''
