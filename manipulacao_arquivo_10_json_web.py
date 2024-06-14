'''
Extração de Arquivo da Web - json
'''
import json

#imprimindo um arquivo json copiado da internet
from urllib.request import urlopen

response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
dados = json.loads(response)[0]

print(dados)

print('Titulo',dados['title'])
print('URL',dados['url'])
print('Duração',dados['duration'])
print('Número de visualizações',dados['stats_number_of_plays'])

#copiando o conteúdo de um arquivo para outro

#Nomes dos arquivos
arquivo_fonte = 'arquivos/dados.json'
arquivo_destino = 'arquivos/dados.txt'

#Método 1
with open(arquivo_fonte,'r') as infile:
    texto = infile.read()
    with open(arquivo_destino,'w') as outfile:
        outfile.write(texto)

#Método 2
open(arquivo_destino,'w').write(open(arquivo_fonte,'r').read())

#leitura do arquivo txt
with open('arquivos/dados.txt','r') as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)

print(dados)