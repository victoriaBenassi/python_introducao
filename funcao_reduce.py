'''
Função Reduce - pacote functools

A função reduce() em Python é uma função da biblioteca functools que aplica 
uma determinada função binária a pares consecutivos de elementos em uma estrutura 
de dados iterável (como uma lista, tupla ou outro objeto iterável), reduzindo-a a 
um único valor.
'''

#importando a função reduce do modulo functools
from functools import reduce

from IPython.display import Image
Image('arquivos/reduce.png')

## Criando uma lista
lista = [47, 11 , 42, 13]

print(lista)

def soma(a,b):
    x = a+b
    return x

#usando reduce com uma função e uma lista. a função vai retornar o valor maximo
print(reduce(soma, lista))

#usando a função reduce() com lambda

print(reduce(lambda x,y : x+y, lista))

#podemos atribuir a expressão lambda a uma variavel
max_valor = lambda num1,num2 : num1 if(num1>num2) else num2

#reduzindo a lista até o valor maximo, atravez da função criada com a expressão lambda 
print(reduce(max_valor,lista))