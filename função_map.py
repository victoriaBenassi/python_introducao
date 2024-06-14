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

numeros_ao_quadrado = list(map(potencia, numeros))

print(numeros_ao_quadrado) 