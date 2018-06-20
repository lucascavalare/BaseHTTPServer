# -*- coding: cp1252 -*-



import json


def criaMapa(uf):
    
    #'abre' o arquivo para leitura
    f = open('ceps_' + uf + '.json', 'r')

    # efetua a leitura do arquivo (dados lidos armazenados em txt)
    txt = f.read()

    # parsing do json (resultado em lista)
    lista = json.loads(txt)

    # criação do mapa
    mapa = {}
    for elemento in lista:
        cep = elemento['CEP']
        mapa[cep] = elemento    
    return mapa

mapa = criaMapa('RR')
#print(criaMapa(uf))

criaMapa('69301011')
