'''
 For aninhado- um loop for dentro de outro loop for
 Isso é útil quando você precisa iterar sobre múltiplas
 sequências ou criar uma estrutura de repetição complexa
'''
#loops aninhados
lista1 = [0,1,2,3,4]
lista2 = [1,2,3] 

# Loop externo
for elemento_lista1 in lista1:
    
    # Loop interno
    for elemento_lista2 in lista2:
        
        print('\n', elemento_lista1 * elemento_lista2)
        
    print('----')

# O número 47 aparece nas duas listas?

lista1 = [10,16,24,39,47]
lista2 = [32,89,47,76,12]

# Loop externo
for elemento_lista1 in lista1:
    
    # Loop interno
    for elemento_lista2 in lista2:
        
        # Condicional
        if elemento_lista1 == 47 and elemento_lista2 == 47:
            
            print("O número 47 foi encontrado nas duas listas!")

# Some os números pares da primeira lista com os números pares da segunda lista

lista1 = [10,16,24,39,47]
lista2 = [32,89,47,76,12]
soma = 0

# Loop externo
for lista in [lista1, lista2]:
    
    # Loop interno
    for num in lista:
        
        # Condicional
        if num % 2 == 0:
            soma += num
            
print("O soma dos números pares das duas listas é igual a", soma)

# Listas podem ser concatenadas em Python
lista1 + lista2

# Some os números pares da primeira lista com os números pares da segunda lista

lista1 = [10,16,24,39,47]
lista2 = [32,89,47,76,12]
soma = 0

for num in lista1 + lista2:
    if num % 2 == 0:
        soma += num

print("Soma dos valores pares:", soma)

# Loop em lista de listas (matrizes) para encontrar o maior número

matriz = [[42,23,34] , [100,215,114] , [10.1,98.7,12.3]]
maior_numero = 0

#loop externo para percorrer cada matriz
for linha in matriz:

    #loop interno para percorrer cada linha
    for num in linha:
        
        #condicional
        if num > maior_numero: 
            maior_numero = num
            
print("Maior número:", maior_numero)

# Listando as chaves de um dicionário
dict = {'k1':'Python','k2':'R','k3':'Scala'}
for item in dict: #por padrão ele vai imprimir apenas as chaves 
    print(item)

#imprimindo chave e valor do dicionario. usando o metodo items()
#para retornar os itens de um dicionario

for k,v in dict.items():
    print(k,v)











