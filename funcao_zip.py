'''
Função Zip

A função zip() em Python é uma função que agrupa elementos de múltiplas estruturas de dados 
iteráveis (como listas, tuplas ou outros objetos iteráveis) juntos em pares. A função zip() 
retorna um objeto zip, que pode ser convertido em outra estrutura de dados, como uma lista ou 
dicionário, se necessário.
'''

# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())

#criando duas listas
lista_1 = [1,2,3]
lista_2 = [4,5,6]

#unindo as listas, em python3 retorna um interator
zip(lista_1,lista_2)

print(list(zip(lista_1,lista_2)))

#atenção quando as sequencias tiverem numero diferente de elementos
print(list(zip('abcd','XY')))
#a função zip retorna a combinação, descarta os elementos que nao combinam

#criando 2 dicionario
dicionario_1 = {'a':1,'b':2}
dicionario_2 = {'c':3,'d':4}

#a função zip combina as chaves dos dicionarios
#zip vai unir as chaves
print(list(zip(dicionario_1,dicionario_2)))

#zip para unir os valores (itens)
print(list(zip(dicionario_1,dicionario_2.values())))

#criando uma função para trocar os valores entre 2 dicionarios
def trocaValores (d1,d2):

    dicTemp = {}

    for d1key, d2val in zip(d1, d2.values()):
        dicTemp[d1key] = d2val

    return dicTemp

print(trocaValores(dicionario_1,dicionario_2))
