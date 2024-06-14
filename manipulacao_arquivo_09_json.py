'''
Manipulando Arquivos JSON (Java Script Object Notation )

JSON (JavaScript Object Notation) é um formato de dados de texto simples
e leve que é utilizado para transmitir informações em aplicações web. É baseado 
em uma estrutura de objetos JavaScript e usa pares de chave-valor para representar
dados. JSON é facilmente lido e escrito por máquinas e é amplamente utilizado 
como formato de intercâmbio de dados em aplicações web modernas.
'''

#criando um dicionario
dict_victoria = {'nome':'Victoria Benassi',
                 'linguagem':'python',
                 'similar':'c,c#,java',
                 'users':'100000'}

for k,v in dict_victoria.items():
    print(k,v)

#importando json
import json

#convertendo dicionario para um objeto json
json.dumps(dict_victoria)#dumps= converte o dicionario para formato arquivo json

#criando um arquivo json
with open('arquivos/dados.json','w') as arquivo:
    arquivo.write(json.dumps(dict_victoria))#converte o dicionario para o formato json

#leitura do arquivo json
with open('arquivos/dados.json','r') as arquivo:
    texto = arquivo.read()
    #carregar o conetudo do texto,no formato json
    dados = json.loads(texto)#loads= carregar

print(dados)
print(dados['nome'])