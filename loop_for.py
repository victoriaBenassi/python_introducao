'''
 loop for - Um loop em Python é uma estrutura de controle 
 que permite executar um bloco de código repetidamente.

'''

#criando uma tupla e imprimindo cada um dos valores
# i é o nome de uma variavel, que é criada em tempo de execução e representa cada elemento da lista
tupla=(2,3,4)
for i in tupla: # para cada valor dentro da tupla
    print(i)    # imprima o valor

#criando uma lista e imprimindo cadaa um dos valores
lista_de_strings = ['macarrão', 'manteiga', 'bacon']
for i in lista_de_strings:
    print(i)

#imprimindo os valores no intervalo entre 0 e 5(exclusive)
for contador in range(0,5):
    print(contador)

#imprimindo os numeros pares da lista de numeros
lista = [1,2,3,4,5,6,7,8,9,10]
for numero in lista:
    if numero % 2 == 0:
        print(numero)  

#listando numeros no intervalo de 0 e 101, com incremento em 2
for i in range(0,101,2): #função range permite definir o salto, pulando de 2 em 2
    print(i)     

# Strings também são sequências
for caracter in ' hello world':
    print(caracter)



