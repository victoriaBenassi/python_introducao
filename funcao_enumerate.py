'''
Função Enumerate

A função enumerate() em Python é uma função que permite iterar sobre uma estrutura de dados 
(como uma lista, tupla ou outro objeto iterável). A função enumerate() retorna um objeto enumerado, 
que pode ser usado em loops para percorrer a estrutura de dados e acessar o contador e o valor de 
cada elemento.
'''

# Criando uma lista
sequencia = ['a','b','c']

#a função enumerate retorna um interator
enumerate(sequencia)

#convertento para retornar uma lista
print(list(enumerate(sequencia)))#retorna o indice de cada caracter

#imprimindo os valores de uma lista com a função enumerate () e seus respectivos indices
for indice,valor in enumerate(sequencia):
    print(indice,valor)


#loop para indice e valor
for indice,valor in enumerate(sequencia):
    if indice >= 2 :
        break
    else:
        print(valor)

#criando uma lista
lista = ['Marketing', 'Tecnologia', 'Business']

#fazendo enumerate() da lista
for indice,valor in enumerate(lista):
    print(indice,valor)

#usando uma string no enumerate()
for indice,letras in enumerate('data science academy'):
    print(indice,letras)

#usando um range de valor
for i,item in enumerate(range(10)):
    print(i,item)