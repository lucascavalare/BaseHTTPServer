# -*- coding: cp1252 -*-

'''
	Atividade 2 
	-- leitura de um arquivo JSON contendo CEP's de UF
'''

import json
import BaseHTTPServer
#import queryparser
#import glob
import fnmatch
import os

'''
	Lê um arquivo de CEPs no formato JSON e
	retorna um mapa que associa cada CEP aos
	respectivos dados de endereço. 
	parametro: sigla da UF
'''

def criaMapa(uf):

   # 'abre' o arquivo para leitura
   #f = open('ceps_' + uf + '.json', 'r')

   # efetua a leitura do arquivo (dados lidos armazenados em txt)
   #txt = f.read()

   # parsing do JSON (resultado em lista)
   #lista = json.loads(txt)

   # criação do mapa
   #mapa = {}
   #for elemento in lista:
   #    cep = elemento['CEP']
   #    mapa[cep] = elemento
   #return mapa
   for file in os.listdir('.'):
       if fnmatch.fnmatch(file, '*.json'):
           f = open(file)
	   txt = f.read()
	   lista = json.loads(txt)

'''
   Faz a consulta ao CEP passado como parâmetro e
   escreve na saída padrão os dados encontrados.
'''
def consulta(cep):
    global mapa
    if cep in mapa.keys():
        dados = mapa[cep]
        print 'CEP:',cep,'Cidade:',dados['Cidade'],'Bairro:',dados['Bairro']
    else: 
        print 'CEP', cep, 'nao encontrado'

'''
    classe que estende BaseHHTPRequestHandler:
    -- redefine o método do_Get() para que faça o tratamento desejado
    -- os demais métodos da biblioteca são mantidos 'as is'.
'''	
class ServidorExemplo1(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/home/cavalarelucas/atividade2/BaseHTTPServer/CEPs":
            # inicia o envio da resposta c/ código de retorno 200 (OK)
            self.send_response(200)
            
            # define o cabeçalho da resposta (neste caso 'avisa' que o conteúdo será html)
            self.send_header("Content-type","text/html")

            # 'fecha' o cabeçalho
            self.end_headers()

            # 'escreve' o conteudo da resposta
            self.wfile.write(consulta)
	    #return
        else:
            self.send_error(404)
	    return
'''
    Cria o servidor web, usando a classe definida acima,
    atendendo as requisições na porta 8080
'''
httpserver = BaseHTTPServer.HTTPServer(("",8080), ServidorExemplo1)

'''
    Ativa o serviço, 'ad infinitum' 
'''
httpserver.serve_forever()



