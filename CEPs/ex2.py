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
'''
for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.json'):
        f = open(file)
        txt = f.read()
        lista = json.loads(txt)
        #print lista
        #return lista
'''        
def criaMapa(uf):
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.json'):
            f = open(file)
            txt = f.read()
            lista = json.loads(txt)
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
#mapa = lista
#print 'mapa criado tamanho:',len(mapa)
'''
consulta('77001004')
consulta('69301011')
consulta('69301015')
consulta('69301020')
consulta('69301030')
consulta('13085185')   # CEP não presente nessa UF
'''
