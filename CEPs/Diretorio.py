# -*- coding: cp1252 -*-
# dicionario contendo pares da forma (estado:(url,id))
import BaseHTTPServer
import queryparser
import json

# dicionário c/ os pares na forma { estado: (url, id) }
dic = {}

#número sequencial único, usado para gerar os id´s dos servidores registrados
nsu = 0

def printDic():
    print "----------------------------"
    for k in dic.keys():
        print "estado:",k,"-->",dic[k]
    print "- - - - - - - - - - - - - - "

# registra um servidor de ddd´s no Diretório
# parâmetros:
#   url: url do servidor
#   estado: sigla do estado atendido pelo servidor (ex. SP, RJ, MG)
#  retorna o id único sob o qual o servidor é registrado ou "??" se
#  o registro não for possível (já existe outro servidor atendendo ao mesmo estado)
def registraServidor(estado, url):
    print "==> registraServidor(",url,",",estado,")"
    global nsu
    if dic.has_key(estado):
        print"--> ?? estado já registrado:"+estado
        return { 'erro': 'estado ja registrado:'+estado }
    nsu += 1
    id= "S_"+str(nsu)
    dic[estado] = (url,id)
    printDic()
    return { 'id': id, 'sucesso': True }

# remove um servidor de DDD´s do Diretório
# parâmetro:
#   url: url do servidor
#   id:  id sob o qual o servidor foi registrado no Diretório (esse é o valor
#        retornado por registraServidor(url,estado)
#   retorna True ou False, indicando sucesso ou falha da operação
def removeServidor(url,id):
    print "==> removeServidor(",url,",",id,")"
    for k in dic.keys():
        if dic[k] == (url,id):
            dic.pop(k)
            printDic()
            return { 'sucesso':True }
    print "--> ??"
    return { 'erro': 'url ou id invalida' }

# consulta pelo servidor de DDD´s que atende a um estado
# parâmetro:
#     estado: sigla do estado
#     retorna a url do servidor(se registrado no Diretório) ou
#     "??" caso o servidor não seja encontrado
def consultaServidor(estado):
    print "consultaServidor(",estado,")"
    if dic.has_key(estado):
        return { 'url': dic[estado][0] }
    return { 'erro': 'estado desconhecido:'+estado }

# consulta pelos estados atendidos pelos servidores registrados no Diretório.
# retorna a lista com a sigla dos estados atendidos.
def consultaEstados():
    print "consultaEstados()"
    return { 'estados' : dic.keys() }


# teste das funções de apoio, na linha de comando
def test1():
    d = {"SP":"souza:8080", "RJ":"rodrigues:8080","RN": "silva:8080", "RO":"oliveira:8080", "MG":"pereira:8080"}
    r = {}
    for s in d.keys():
        r[registraServidor(s,d[s])] = d[s]
    print r
    print consultaEstados()
    for s in d.keys():
        print consultaServidor(s)
    print consultaServidor('kk')
    print consultaServidor('pp')
    for k in r.keys():
        print removeServidor(r[k],k)
        
    
# mostra relação das funções oferecedidas pelo servidor.
def help():
    return "Press F1 for help :>) "


# servidor HTTP
# o servidor
class Diretorio(BaseHTTPServer.BaseHTTPRequestHandler):

    # tratamento de uma requisicao GET
    def do_GET(self):
        print self.path
        self.send_response(200)
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, , PUT, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Authorization")
        self.send_header("Content-type","text/json")
        self.end_headers()
        parms = queryparser.parse(self.path)
        print parms
        if 'op' in parms:
            op = parms['op']
            if op == 'consulta':
                if 'estado' in parms:
                    estado = parms['estado']
                    result = consultaServidor(estado)
                else:
                    result = { 'erro': 'parametro "estado" ausente' }
            elif op == 'registro':
                if 'estado' in parms and 'url' in parms:
                    estado = parms['estado']
                    url = parms['url']
                    result = registraServidor(estado, url)
                else:
                    result = {'erro': 'parametros incompletos' }
            elif op == 'estados':
                result = consultaEstados() 
            elif op == 'remove':
                if 'url' in parms and 'id' in parms:
                    url = parms['url']
                    id = parms['id']
                    result = removeServidor(url,id)
                else:
                    result = {'erro': 'parametros incompletos' }
            else:
                result = { 'erro': 'operacao desconhecida:'+op }
        else:
            result = { 'erro': 'parametro "op" ausente' }
        self.wfile.write(json.dumps(result))

    # tratamento de uma requisicao POST
    def do_POST(self):
        self.wfile.write("POST: operação inválida");


def criaDiretorio():
    print 'inicio'
    httpServer = BaseHTTPServer.HTTPServer(("",8080), Diretorio)
    httpServer.serve_forever()


criaDiretorio()


       






