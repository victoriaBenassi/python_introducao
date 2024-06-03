'''
 range() é uma função que cria um objeto de 
 sequência que representa uma série de números. 
 Ele é comumente usado em loops para iterar sobre
 uma sequência de números especificada.
'''

#imprimir de 1 até 10
for i in range(1,11):#o segundo numero é exclusivo
    print(i)

#imprimindo de 0 ate 100 saltando de 2 em 2
for i in range(0,101,2):
    print(i)

#imprmindo numeros pares negativos entre 0 e -20
for i in range(0,-21,-2):
    print(i)

#usando o tamanho de uma lista na função range()
brinquedos=['boneca','bola','urso']
brinquedos_tamanho = len(brinquedos)
for i in range(0,brinquedos_tamanho):
    print(brinquedos[i])

