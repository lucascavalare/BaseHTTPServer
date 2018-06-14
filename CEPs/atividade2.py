# -*- coding: cp1252 -*-
import BaseHTTPServer, json, os
'''
Servidor Web
-estende BaseHTTPRequestHandler
-trata apenas requisições feitas através do método GET
-trata parâmetros passados na URL
-retorna um texto sJSON gerado com base nos parâmetros
'''
import queryparser
'''
    retorna um texto JSON usando os parâmetros passados em path
'''
def resposta(path):
#    # os pares (parametro, valor) são colocados no dicionário dict
    params = queryparser.parse(path)
    return json.dumps(params)
notfound = "GET: resource not found"


'''
    Lê um arquivo de CEPs no formato JSON e
    retorna um mapa que associa cada CEP aos
    respectivos dados de endereço.
    parâmetro: sigla da UF
'''
def criaMapa(uf):
    # 'abre' o arquivo para leitura
    f = open('ceps_' + uf + '.json', 'r')
    # efetua a leitura do arquivo(dados lidos armazenados em txt)
    txt = f.read()
    # parsing do JSON (resultado em lista)
    lista = json.loads(txt)
    # criação do mapa
    mapa = {}
    #for elemento in lista:
    #    cep = elemento['CEP']
    #    mapa[cep] = elemento
    #return mapa
print 'inicio'
for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.json'):
        print file
    

'''
    faz a consulta ao CEP passado como parâmetro e
    escreve na saída padrão os dados encontrados.

def consulta(cep):
    global mapa
    if cep in mapa.keys():
        dados = mapa[cep]
        print 'CEP:',cep,'Cidade:',dados['Cidade'],'Bairro:',dados['Bairro']
    else:
        print 'CEP', cep, 'NOT FOUND'

class ServidorExemplo(BaseHTTPServer.BaseHTTPRequestHandler):
    
    # tratamento de uma requisição GET
    def do_GET(self):
        print self.path
        self.send_response(200)
        self.send_header("Content-type","text/json")
        self.end_headers()
        self.wfile.write(resposta(self.path))
        
     # tratamento de uma requisição POST   
    def do_POST(self):
        self.wfile.write("<HTML><body>Operação POST não permitida.<BR><BR></body></HTML>");
            
# Criação do Servidor
httpserver = BaseHTTPServer.HTTPServer(("",8080), ServidorExemplo)

# Run forever
httpserver.serve_forever()
'''
