import urlparse

# Separa os pares (nome,valor) contidos numa url contendo os
# dados de um formulario devolvidos pelo pelo navegador (usando GET).
# Limitacao: esta versao nao trata listas de selecao multipla.

def parse(url):
    query = urlparse.urlparse(url)[4]
    print query
