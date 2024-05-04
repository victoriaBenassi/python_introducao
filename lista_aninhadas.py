'''
listas de lista - listas aninhadas
listas de listas são matrizes em python
'''

listas = [1,2,3], [4,5,6], [7,8,9] #criando uma lista de listas
print(listas)

a=listas[0] #atribuindo um item da lista a uma variavel
print(a)

b=a[0]#buscando o elemento de indice 0 na lista a
print(b)

list_1 = listas[1]
print(list_1)

valor_1_0 = list_1[0]
print(valor_1_0)

'''
Operações com listas
'''

print(listas)

a = listas[0][0] #atribuindo a variavel a o primeiro valor da primeira lista
print(a)

b = listas[1][2]
print(b)

c = listas[0][2] + 10 #fatiamento da lista
print(c)

d = 10
e = d* listas[2][0]
print(e)

'''
concatenando listas
'''

lista_s1 = [34, 32, 56]
print(lista_s1)

lista_s2 = [21, 90, 51]
print(lista_s2)

lista_total = lista_s1 + lista_s2 #concatenando listas
print(lista_total)

'''
Operador in
'''

#criando uma lista
lista_teste_op=[100, 2, -5, 3.4]
#verificando se o valor 10 pertence a lista
print(10 in lista_teste_op)
#verificando se o valor 100 pertence a lista
print(100 in lista_teste_op)

'''
funções built-in
'''

lista_numeros = [10, 20, 50, -3.4]

#função len() retorna o comprimento da lista
print(len(lista_numeros))

#função max() retorna o valor maximo da lista
print(max(lista_numeros))

#função min() retorna o valor minimo da lista
print(min(lista_numeros))

lista_nomes= ["Ana", "Maria"]
#adicionando um item á lista
lista_nomes.append("Laura")
print(lista_nomes) 
lista_nomes.append("Laura")#o metodo append não verifica se a string ja existe
print(lista_nomes)
#verificando quantas vezes aparece a string na lista
print(lista_nomes.count("Laura"))

#criando uma lista vazia
lista_vazia=[]

print(lista_vazia)
lista_vazia.append(10)#adicionando um item à lista
lista_vazia.append(50)
print(lista_vazia)

old_list = [1,2,3,10]
new_list = []

#copiando os itens de uma lista para outra
for item in old_list:
    new_list.append(item)
print(new_list)

cidades = ['Recife', 'Salvador', 'Bahia']
cidades.extend(['Fortaleza', 'Ceara'])#acrescentando usando o metodo extend
print(cidades)

print(cidades.index('Salvador'))#Qual o indice onde está a string salvador na lista

cidades.insert(2,110) #inserindo no indice 2 o numero 110
print(cidades)

#removendo um item da lista
cidades.remove(110)
print(cidades)

#reverte a ordem da lista
cidades.reverse()
print(cidades)

numeros=[10,599,3,75]
numeros.sort()#ordena a lista
print(numeros)