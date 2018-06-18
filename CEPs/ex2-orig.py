# -*- coding: cp1252 -*-
'''
        Inf 515 - Exemplo
        -- leitura de um arquivo json contendo CEP's de uma UF
           (no exemplo RR)
        -- criação de um dicionário/mapa indexado pelo CEP (associa
           a cada CEP os dados do endereço relativo ao mesmo
        -- consulta ao dicionário/mapa pelo CEP
'''

import json

'''
    Le um arquivo de CEPs no formato json e
    retorna um mapa que associa cada CEP aos
    respectivos dados de endereço.
    parâmetro: sigla da uf
'''
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


'''
    Faz a consulta ao CEP passado como parâmetro e
    escreve na saida padrão os dados encontrados.
'''
def consulta(cep):
    global mapa
    if cep in mapa.keys():
        dados = mapa[cep]
        #python 3: a sintaxe do print é diferente
        print 'CEP:',cep,'Cidade:',dados['Cidade'],'Bairro:',dados['Bairro']
    else:
        print 'CEP', cep, 'nao encontrado'

'''
    'Corpo do programa': teste de alguns CEPS
'''
print 'inicio'
mapa = criaMapa('RR')
print 'mapa criado tamanho:',len(mapa)

consulta('69301000')
consulta('69301011')
consulta('69301015')
consulta('69301020')
consulta('69301030')
consulta('13085185')   # CEP não presente nessa UF


        
