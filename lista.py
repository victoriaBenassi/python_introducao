'''
Estruturas de dados em python - listas
armazenar varios tipos de dados em uma lista
colchetes[]
'''

#criando uma lista
lista_1= ["arroz, frango , feijão, açucar"] #lista como string
print(lista_1)

lista_2= ["arroz", "frango", "feijão", "açucar"] #lista de string
print(lista_2)

lista_3=[23, 100, "Cientista de dados"]#armazenando diferentes elementos em uma lista
print(lista_3)

#atribuindo cada valor da lista a uma variavel
item_1= lista_3[0]
item_2= lista_3[1]
item_3= lista_3[2]

#imprimindo as variaveis
print(item_1)
print(item_2)
print(item_3)

#imprimindo um item da lista
print(lista_2[3])
#atualizando um item da lista
lista_2[3] = "chocolate"
print(lista_2[3])

#deletando um item da lista
del lista_2[3]
print(lista_2)
#não é possivell deletar um item que não existe na lista