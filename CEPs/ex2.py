# -*- coding: cp1252 -*-
import json, os, fnmatch


# -*- coding: cp1252 -*-
'''
        Inf 515 - Exemplo
        -- leitura de um arquivo json contendo CEP's de uma UF
           (no exemplo RR)
        -- criação de um dicionário/mapa indexado pelo CEP (associa
           a cada CEP os dados do endereço relativo ao mesmo
        -- consulta ao dicionário/mapa pelo CEP
'''
def consulta(cep):
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.json'):
            f = open(file)
            txt = f.read()
            lista = json.loads(txt)
                
            mapa = {}
            for elemento in lista:
                cep = elemento['CEP']
                mapa[cep] = elemento

                global mapa
                if cep in mapa.keys():
                    dados = mapa[cep]
                    jsonData = json.dumps(dados, indent=8)
                return jsonData    
                #print 'CEP:',cep,'Estado:',dados['Estado'],'Cidade:',dados['Cidade'],'Bairro:',dados['Bairro']
                #else:
                    #print 'CEP', cep, 'não encontrado'

consulta('69301011')

                    #jsonData = json.dumps(dados, indent=8)
                    #if '49500244' in jsonData:
                    #    print "CEP:", jsonData
                    #    return
                        #return [jsonData]
                    
                    
#print "CEP:",jsonData
       
                #python 3: a sintaxe do print é diferente
                #print 'CEP:',cep,'Estado:',jsonData[3],'Cidade:',jsonData[5],'Bairro:',jsonData[4]
                #print 'CEP:',cep,'Estado:',dados['Estado'],'Cidade:',dados['Cidade'],'Bairro:',dados['Bairro']
            #else:
                #print 'CEP', cep, 'nao encontrado'
'''
class ServidorExemplo(BaseHTTPServer.BaseHTTPRequestHandler):

    # tratamento de uma requisicao GET
    def do_GET(self):
        print self.path
        self.send_response(200)
        self.send_header("Content-type","text/json")
        self.end_headers()
        #self.wfile.write(htmlpage.replace('[parms]',getParms(self.path)))
        self.wfile.write(jsonData(self.path))

    # tratamento de uma requisicao POST
    def do_POST(self):
        self.wfile.write("<HTML><body>Operação POST não permitida.<BR><BR></body></HTML>");
# criação do servidor            
#httpserver = BaseHTTPServer.HTTPServer(("",8080), ServidorExemplo)

'''      
'''
      rodar até ...
httpserver.serve_forever()
      
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
