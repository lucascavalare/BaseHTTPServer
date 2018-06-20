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
                     
def criaMapa(uf):
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.json'):
            f = open(file)
            txt = f.read()
            lista = json.loads(txt)
            print lista
'''                
            global mapa
            mapa = {}
            for elemento in lista:
                cep = elemento['CEP']
                mapa[cep] = elemento
            return mapa

def consulta(cep):
    global mapa
#    mapa = carrega('cep')
            #print(mapa)
    if cep in mapa.keys():
        dados = mapa[cep]
        print 'CEP:',cep
    else:
        print 'CEP:', cep, 'nao encontrado'
        
print 'inicio'
mapa = criaMapa('RR')
print 'mapa criado:',len(mapa)

consulta('69301000')
consulta('69399000')
