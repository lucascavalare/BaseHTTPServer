# -*- coding: cp1252 -*-
'''
    Exemplo básico de servidor web
    -- trata apenas o método GET
    -- responde com um texto html fixo (htmlpage)
'''
import BaseHTTPServer

### texto fixo retornado como resposta ao get
htmlpage = """
<html><head><title>Inf 515 - Aplicacões Distribuídas - 2013</title></head>
<body>Exemplo de Servidor Web em Python (Inf 515 - 2014)</body>
</html>"""

### em caso de url inválida 
notfound = "File not found"

'''
    classe que estende BaseHHTPRequestHandler:
    -- redefine o método do_Get() para que faça o tratamento desejado
    -- os demais métodos da biblioteca são mantidos 'as is'.
'''
class ServidorExemplo1(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            # inicia o envio da resposta c/ código de retorno 200 (OK)
            self.send_response(200)
            
            # define o cabeçalho da resposta (neste caso 'avisa' que o conteúdo será html)
            self.send_header("Content-type","text/html")

            # 'fecha' o cabeçalho
            self.end_headers()

            # 'escreve' o conteudo da resposta
            self.wfile.write(htmlpage)
        else:
            self.send_error(404, notfound)

'''
    Cria o servidor web, usando a classe definida acima,
    atendendo as requisições na porta 8080
'''
httpserver = BaseHTTPServer.HTTPServer(("",8080), ServidorExemplo1)

'''
    Ativa o serviço, 'ad infinitum' 
'''
httpserver.serve_forever()

