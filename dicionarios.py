'''

dentro de um dicionario coloca pares de chave e valor, esses 
pares são separados por virgulas
chaves{}
'''
#crindo um dicionario
estudantes_dict = {'Pedro':24, 'Ana':22, 'Ronaldo':26, 'Janaina':25}
print(estudantes_dict)
print(estudantes_dict['Pedro'])#retorna o valor associado a chave Pedro
estudantes_dict['Victoria'] = 18 #adicionando um par ao dicionario
print(estudantes_dict['Victoria'])

estudantes_dict.clear()#esvaziando o dicionario
print(estudantes_dict)

del estudantes_dict #deletando o dicionario

estudantes = {'Pedro':24, 'Ana':22, 'Victoria':19, 'Maria':25}
print(estudantes)
print(len(estudantes))#verifica o tamanho do dicionario
print(estudantes.keys())#retorna somente as chaves
print(estudantes.values())#retorna somente os valores
print(estudantes.items())#retorna somente os itens que são os elementos

estudantes_2 = {'Camila':27, 'Adiana':28, 'Roberta':26}
print(estudantes_2)
estudantes.update(estudantes_2)#atualiza o primeiro dicionario com os itens do segundo
print(estudantes)

#criando dicionario vazio
dicionario_1 = {}
print(dicionario_1)
dicionario_1['nome']='Victoria' #adicionado elementos ao dicionario
dicionario_1['sobrenome']='Benassi'
dicionario_1['idade']=18
print(dicionario_1)

#extraindo cada valor das chaves e colocar em variaveis

nome = dicionario_1['nome']
sobrenome = dicionario_1['sobrenome']
idade = dicionario_1['idade']

print(nome, sobrenome, idade ) 

'''
Dicionario de listas
'''

dict_3 = {'chave1':1230, 'chave2':[22,453,73.4], 'chave3':['pichanha', 'fraldinha', 'alcatra']}
print(dict_3)

#acessando um item da lista, dentro do dicionario
print(dict_3['chave3'][0].upper())#buscar o valor que esta na lista dentro do dicionario e
#retornar em letra maiuscula 

#operações com itens da lista, dentro do dicionario
variavel_1 = dict_3['chave2'][0]-2 #busca o valor na lista e subtrai 
print(variavel_1)

#duas operações no mesmo comando, para atualizar um item dentro da lista
dict_3['chave2'][0]-=2
print(dict_3)

'''
Criando dicionarios aninhados
permite estruturar dados de forma hierárquica, útil para representar
informações que têm uma relação de "pai-filho" ou "contêiner-contido".
'''

dict_aninhado = {'key1':{'key2_aninhada':{'key3_aninhada':'Dict aninhado em python'}}}
print(dict_aninhado)
print(dict_aninhado['key1']['key2_aninhada']['key3_aninhada'])




