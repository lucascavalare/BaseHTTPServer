# -*- coding: cp1252 -*-
import BaseHTTPServer, json
'''
    Exemplo de servidor web
    -- estende  BaseHTTPRequestHandler
    -- trata apenas requisições feitas através do método GET
    -- trata parâmetros passados na URL
    -- retorna um texto JSON gerado com base nos parâmetros
'''
import queryparser

'''
    Retorna um texto json usando os parâmetros passdos em path
'''
def resposta(path):
    # os pares (parametro, valor) são colocados no dicionário dict
    parms = queryparser.parse(path)
    return json.dumps(parms, indent=4)
    

notfound = "GET: resource not found"

# monta uma sequencia de linhas com os parâmetros passados na url
# como parte de um texto HTML
def getParms(path):
    parms = queryparser.parse(path)
    res = '<h3> Parâmetros:</h3>\n'
    for k in parms.keys():
        res += '<p>'+k+'="'+parms[k]+'"\n'
    return res

# o servidor
class ServidorExemplo(BaseHTTPServer.BaseHTTPRequestHandler):

    # tratamento de uma requisicao GET
    def do_GET(self):
        print self.path
        self.send_response(200)
        self.send_header("Content-type","text/json")
        self.end_headers()
        #self.wfile.write(htmlpage.replace('[parms]',getParms(self.path)))
        self.wfile.write(resposta(self.path))

    # tratamento de uma requisicao POST
    def do_POST(self):
        self.wfile.write("<HTML><body>Operação POST não permitida.<BR><BR></body></HTML>");


# criação do servidor            
httpserver = BaseHTTPServer.HTTPServer(("",8080), ServidorExemplo)

# rodar até ...
httpserver.serve_forever()

# testar com: http://localhost:8080//?vulcao=Eyjafallajokull&evento=erupcao&dia=0&hora=0&op=ca
