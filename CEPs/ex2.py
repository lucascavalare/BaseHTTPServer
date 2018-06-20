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
                     
def criaMapa(cep):
        # 'list' for files in directory
        for file in os.listdir('.'):
                # 'test' if filenames match the pattern
                if fnmatch.fnmatch(file, '*.json'):
                        # 'open' files that match
                        f = open(file)
                        # do read file (stored in txt)
                        txt = f.read()
                        # parsing JSON (result in lista)
                        lista = json.loads(txt)
                # print the list
                #return lista 
                        #global mapa
                        mapa = {}
                        for elemento in lista:
                                cep = elemento['CEP']
                                mapa[cep] = elemento
                        print mapa


            #return lista                
            #global mapa
            #mapa = {}
            #for elemento in lista:
            #    cep = elemento['CEP']
            #    mapa[cep] = elemento
            #print mapa    
                #if cep in mapa.keys():
                #    dados = mapa[cep]
                #return dados
#print(criaMapa('69397000'))
