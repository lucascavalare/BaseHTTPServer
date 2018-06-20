# -*- coding: cp1252 -*-



import json
import os
import fnmatch

#def consulta(cep):
for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.json'):
            f = open(file)
            txt = f.read()
            lista = json.loads(txt)
        
            mapa = {}
            for elemento in lista:
                cep = elemento['CEP']
                mapa[cep] = elemento
                #return mapa
                if cep in mapa.keys():
                    dados = mapa[cep]
                    jsonData = json.dumps(dados, indent=8)
                    if '30001970' in jsonData:
                        print(jsonData)
                        #return jsonData
#print(consulta('49000001')) 
quit()
