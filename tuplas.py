'''
Tupla - é uma estrutura de dados semelhante a uma lista, mas
imutável, o que significa que não pode ser alterada após a sua criação.
As tuplas são definidas usando parênteses ()
'''

# Criando uma tupla
tupla1 = ("Geografia", 23, "Elefantes", 9.8, 'Python')

# Imprimindo a tupla
print(tupla1)

# Tuplas não suportam append()
#tupla1.append("Chocolate")

# Tuplas não suportam delete de um item específico
#del tupla1["Elefantes"]  

# Tuplas podem ter um único item
tupla1 = ("Chocolate")
print(tupla1)

#acessando item da tupla
tupla1 = ("Geografia", 23, "Elefantes", 9.8, 'Python')
print(tupla1[0])

# Verificando o comprimento da tupla
len(tupla1)

# Slicing, da mesma forma que se faz com listas
tupla1[1:]

#indice onde esta o elemento
print(tupla1.index('Elefantes'))

# Tuplas não suportam atribuição de item
#tupla1[1] = 21

# Deletando a tupla
del tupla1

# Criando uma tupla
t2 = ('A', 'B', 'C')

print(t2)

# Tuplas não suportam atribuição de item
#t2[0] = 'D'

# Usando a função list() para converter uma tupla para lista
# adicionando mais um item a tupla fazendo conversão 
# para lista e depois voltando para tup´la
lista_t2 = list(t2)
print(type(t2))
print(type(lista_t2))

print(lista_t2)

print(lista_t2.append('D'))#adicionando um item a lista
print(lista_t2)

# Usando a função tuple() para converter uma lista para tupla
t2 = tuple(lista_t2)

print(t2)