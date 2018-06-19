# -*- coding: cp1252 -*-
import json, os, fnmatch
import BaseHTTPServer

import queryparser

# -*- coding: cp1252 -*-
'''
        Inf 515 - Exemplo
        -- leitura de um arquivo json contendo CEP's de uma UF
           (no exemplo RR)
        -- criação de um dicionário/mapa indexado pelo CEP (associa
           a cada CEP os dados do endereço relativo ao mesmo
        -- consulta ao dicionário/mapa pelo CEP
'''
'''
def resposta(path):
    # os pares (parametro, valor) são colocados no dicionário dict
    parms = queryparser.parse(path)
    return json.dumps(parms)
'''                      
def carrega(cep):
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.json'):
            f = open(file)
            txt = f.read()
            lista = json.loads(txt)
            
            global mapa
            mapa = {}
            for elemento in lista:
                cep = elemento['CEP']
                mapa[cep] = elemento
            print(json.dumps(mapa, indent=8))
            mapa = carrega('cep')
            #return mapa
            if cep in mapa.keys():
                dados = mapa[cep]
            return dados
''' 
def getParms(path):
    parms = queryparser.parse(path)
    res = '<h3> Parâmetros:</h3>\n'
    for k in parms.keys():
        res += '<p>'+k+'="'+parms[k]+'"\n'
    return res
'''                    
class ServidorExemplo(BaseHTTPServer.BaseHTTPRequestHandler):

    # tratamento de uma requisicao GET
    def do_GET(self):
        print self.path
        self.send_response(200)
        self.send_header("Content-type","text/json")
        self.end_headers()
        #self.wfile.write(htmlpage.replace('[parms]',getParms(self.path))
        parms = queryparser.parse(self.path)
        print parms
        if cep in parms:
            cep = parms['CEP']
            if cep == 'CEP':
                if 'cep' in parms:
                    #cep = parms['CEP']
                    result = carrega('cep')
                else:
                    result = { 'erro': 'parametro "cep" ausente' }
        self.wfile.write(carrega(self.path))

    # tratamento de uma requisicao POST
    def do_POST(self):
        self.wfile.write("<HTML><body>Operação POST não permitida.<BR><BR></body></HTML>");

# criação do servidor            
httpserver = BaseHTTPServer.HTTPServer(("",8080), ServidorExemplo)
      
#rodar até ...
httpserver.serve_forever()

'''      
def criaMapa(lista):
    #for file in os.listdir('.'):
    #    if fnmatch.fnmatch(file, '*.json'):
    #        f = open(file)
    #        txt = f.read()
    #        lista = json.loads(txt)
            #print l
        # criação do mapa
            mapa = {}
            for elemento in lista:
                cep = elemento['CEP']
                mapa[cep] = elemento
            return mapa
                
def consulta(cep):
    #print mapa.keys()
    global mapa
    if cep in mapa.keys():
        dados = mapa[cep]
        #python 3: a sintaxe do print é diferente
        print 'CEP:',cep,'Cidade:',dados['Cidade'],'Bairro:',dados['Bairro']
    else:
        print 'CEP', cep, 'nao encontrado'

print 'inicio'
#mapa = criaMapa('RR')
print 'mapa criado tamanho:',len(mapa)
'''
'''
consulta('77001004')
consulta('69301011')
consulta('69301015')
consulta('69301020')
consulta('69301030')
consulta('13085185')   # CEP não presente nessa UF
'''
