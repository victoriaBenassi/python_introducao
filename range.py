'''
intervalo de valores usando a função Range

a função range() é usada para gerar uma sequência de números. 
Pode ser usada de várias maneiras diferentes, mas as formas mais comuns 
de uso são:

 range(stop): Gera uma sequência de números que começam em 0 e vão até 
 (mas não incluindo) o número especificado em "stop".

 range(start, stop): Gera uma sequência de números que começam em "start" 
 e vão até (mas não incluindo) o número especificado em "stop".

 range(start, stop, step): Gera uma sequência de números que começam em "start" 
 e vão até (mas não incluindo) o número especificado em "stop", incrementando 
 o valor por "step".

A função range() é comumente usada em loops for para iterar sobre uma sequência 
de números. Ela é muito eficiente em termos de memória, pois gera os números 
conforme necessário, sem armazenar todos os números em memória de uma vez.
'''

#range(stop)
for i in range(5):
    print(i)

#range(start, stop)
for i in range(2, 5):
    print(i)

#range(start, stop, step)
for i in range(0, 10, 2):
    print(i)


#imprimindo numeros de 1 a 10
for i in range(1,11):#o segundo numero é exclusivo, ele não é incluido
    print(i)

#imprimindo numeros pares entre 50 e 101
for i in range(50,101,2):
    print(i)

#imprimindo numeros pares negativos entre 0 e -20
for i in range(0,-21,-2):
    print(i)

#usando o tamanho de uma lista de função range()
lista = ['abacaxi','banana','morango','uva']
lista_tamanho = len(lista)

for i in range(0,lista_tamanho):
    print(lista[i])