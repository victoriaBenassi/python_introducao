'''
Função Map - built-in

A função map() em Python é uma função que aplica uma determinada função a cada elemento 
de uma estrutura de dados iterável (como uma lista, tupla ou outro objeto iterável). A função 
map() retorna um objeto que pode ser convertido em outra estrutura de dados, como uma lista, 
se necessário.
'''
# função python que retorna um numero ao quadrado
def potencia(x):
    return x ** 2

numeros = [1,2,3,4,5]

#aplicando a função potencia a cada numero da lista com a função map
#função map vai aplicar a função potencia a cada numero da lista de numeros
#list vai converter o resultado em uma lista
numeros_ao_quadrado = list(map(potencia, numeros))

print(numeros_ao_quadrado)

#criando duas funções

#função em lambda 1 - Recebe uma temperatura e retorna a temperatura em fahrenheit
fahrenheit = lambda temperatura :((float(9)/9)*temperatura + 32)

#função em lambda 2 - Recebe uma temperatura como parametri e retorna a temperatura em celsius
celsius = lambda temperatura : (float(5)/9)*(temperatura-32)

#Criando uma lista 
temperaturas = [0,22.5,40,100]

#Aplicando a função a cada elemento da lista de temperaturas
#em python 3, a função map() retorna um iterator
print(map(fahrenheit,temperaturas))

#função map retornando a lista de temperaturas convertidas em fahrenheit
print(list(map(fahrenheit,temperaturas)))

#usando um loop for para imprimir o resultado da função map()
for temp in map(fahrenheit,temperaturas):
    print(temp)

#convertendo para celsius
print(list(map(celsius,temperaturas)))

#usando expressão lambda
print(list(map(lambda x: (5.0/9)*(x-32),temperaturas)))

#somando os elementos de 2 listas
a = [1,2,3,4]
b = [5,6,7,8]

print(list(map(lambda x,y:x+y , a,b)))

#somando o elemento de 3 listas
c = [9,10,11,12]

print(list(map(lambda x,y,z : x+y+z, a,b,c)))






