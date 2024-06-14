'''
Pacotes e Módulos

Em Python, um módulo é um arquivo (script) que contém código Python e pode ser 
importado em outros arquivos Python. Ele é usado para compartilhar funções, classes 
e variáveis entre arquivos. Já um pacote é uma coleção de módulos organizados em uma 
estrutura de diretórios. Ele permite a divisão de um aplicativo em múltiplos módulos, 
o que facilita a manutenção e o desenvolvimento.

Visite o PyPi, repositório de pacotes da Linguagem Python: https://pypi.org/
'''
#importando um pacote numpy
import numpy

#verificando todos os atributos e metodos disponiveis no pácote
print(dir(numpy))

#usando um dos metodos do pacote numpy
print(numpy.sqrt(25))

#importando apenas um dos metodos do pacote numpy
from numpy import sqrt

#usando o metodo
print(sqrt(9))

# Imprimindo todos os métodos do pacote numpy
print(dir(numpy))

#help do metodo sqrt do pacote numpy
#help(sqrt)

#importando pacote random para trabalhar com randonização
import random

#choice = escolher
print(random.choice(['abacate','banana','maça']))

#sample = amostra
print(random.sample(range(100),10))#gerar uma amostra de dados com range de 100 e extrair 10 valores do range

#importando pacote statistics - permite calcular estatistica
import statistics

dados = [2.75,1.75,1.25,0.25,0.5,1.25,3.5]

#calcula a media do conjunto de dados
print(statistics.mean(dados))

#extrai a mediana do conjunto de dados 
print(statistics.median(dados))

#importanto o pacote OS
import os
print(os.getcwd())#caminho onde esta a ide usada

#visualizar todo conteudo do pacote os
#print(dir(os))

'''     Podemos trabalhar com modelus dos pacotes(quando disponiveis)       '''

#importando o modulo request do pacote urllib, usado para trazer url's
#para dentro do nosso ambiente python
import urllib.request

#variavel resposta armazena o objeto de conexão á url passada como parâmetro
resposta = urllib.request.urlopen('http://python.org')

#objeto resposta
print(resposta)

#chamando o metodo read() do objeto resposta e armazenando o codigo html na variavel html
html = resposta.read()

print(html)