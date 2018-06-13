# -*- coding cp1252 -*-
import BaseHTTPServer, json
'''
    Servidor Web
        -- estende BaseHTTPRequestHandler
        -- trata apenas requisições feitas através do método GET
        -- trata parâmetros passados na URL
        -- retorna um texto sJSON gerado com base nos parâmetros
'''
import queryparser
'''
    retorna um texto JSON usando os parâmetros passados em path
'''
def resposta(path):
    # os pares (parametro, valor) são colocados no dicionário dict
    params = queryparser.parse(path)
    return json.dumps(params)
notfound = "GET: resource not found"
'''
    Lê um arquivo de CEPs no formato JSON e
    retorna um mapa que associa cada CEP aos
    respectivos dados de endereço.
    parâmetro: sigla da UF
'''
def criaMapa(uf):
    # 'abre' o arquivo para leitura
    f = open('ceps_' + uf + '.json', 'r')
    # efetua a leitura do arquivo(dados lidos armazenados em txt)
    txt = f.read()
    # parsing do JSON (resultado em lista)
    lista = json.loads(txt)
    # criação do mapa
    mapa = {}
    #for elemento in lista:
    #    cep = elemento['CEP']
    #    mapa[cep] = elemento
    #return mapa
    print 'inicio'
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.json'):
            print file

'''
    faz a consulta ao CEP passado como parâmetro e
    escreve na saída padrão os dados encontrados.
'''
