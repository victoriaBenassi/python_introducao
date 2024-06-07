'''
list comprehension e dict comprehension
loop dentro de uma lista
'''

# [expressão for item in coleção de valores if condição == true]

#list comprehension que imprime os numeros ate 10
#para cada valor de x na lista de elemento retorne x
# ou retorne x para cada valor de x na lista de elementos
print([x for x in range(11)])

#list comprehension que imprime os numeros até 10 e grava em uma lista python
lista_numeros = [x for x in range(11)]
print(lista_numeros)

#list comprehension que imprime os numeros menores que 5 em um intervalo de 1 a 10
numeros_menores = [x for x in range(10) if x < 5]
print(numeros_menores)

#lista de frutas
frutas = ['mamao', 'maca', 'pera', 'uva']
#nova lista
novas_frutas = []

#loop tradicional para buscar as palavas com a letra 'm'

for palavra in frutas:
    if 'm' in palavra:
        novas_frutas.append(palavra)

print(novas_frutas)

#mesmo resultado anterior mas com list comprehension

novas_frutas = [palavra for palavra in frutas if 'm' in palavra]
print(novas_frutas)

#dict comprehension

#dicionario de alunos e notas 
dict_alunos = {'Bob': 68,'Michael': 84,'Ana': 93, 'Zico': 57}

#criamos um novo dicionarios imprimindo os pares de chave:valor
#retorna chave : valor para cada chave e cada valor, retornados dos itens do dicionario
dict_alunos_status = {k:v for (k,v) in dict_alunos.items()}

print(dict_alunos_status)

#criamos um novo dicionario com o status : nota maior que 70, aprovado, senão, reprovado
dict_alunos_status = {k: ('aprovado' if v > 70 else 'reprovado') for (k, v) in dict_alunos.items()}
print(dict_alunos_status)
#retornar chave : se por acaso valor de v for maior que 70 retorna aprovado senão reprovado
#para cada combinação de chave e valor no dicionario