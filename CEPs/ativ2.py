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
   f = open('ceps_' + uf + '.json', 'r')

   # efetua a leitura do arquivo (dados lidos armazenados em txt)
   txt = f.read()

   # parsing do JSON (resultado em lista)
   lista = json.loads(txt)

   # criação do mapa
   mapa = {}
   for elemento in lista:
       cep = elemento['CEP']
       mapa[cep] = elemento
   return mapa


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
        print 'CEP', cep, 'Not Found'

#print 'inicio'
#for file in os.listdir('.'):
#    if fnmatch.fnmatch(file, '*.json'):
#        #print file
#        with open(file) as json_data:
#	    mapa = json.load(json_data)
#print 'mapa criado tamanho:',len(mapa)


