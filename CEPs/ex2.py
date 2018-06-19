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
            #print(lista)
        
            global mapa
            mapa = {}
            for elemento in lista:
                cep = elemento['CEP']
                mapa[cep] = elemento
            return mapa

print(carrega('49000001')  
            #mapa = carrega('cep')
            #return mapa
            #if cep in mapa.keys():
            #    dados = mapa[cep]
            #return dados
