'''
função lambda - tipo especial de função usada 
em analise de dados e ciencia de dado.
 Uma função lambda em Python é uma função anônima e pequena 
 que pode ter qualquer número de argumentos, mas apenas uma 
 expressão. Ela é definida usando a palavra-chave lambda, seguida
 pela lista de parâmetros, dois pontos : e a expressão a ser retornada.
    lambda arguments: expression
'''

# Definindo uma função - 3 linhas de código
def potencia(num):
    resultado = num ** 2
    return resultado

print(potencia(5))

# Definindo uma função - 2 linhas de código
def potencia(num):
    return num ** 2

print(potencia(5))

# Definindo uma função - 1 linha de código
def potencia(num): return num ** 2

print(potencia(5))

# Definindo uma expressão lambda (função anônima)
potencia = lambda num: num ** 2
print(potencia(5))

# Lembre: operadores de comparação retornam boolean: true or false

par = lambda num: num % 2 == 0
print(par(3))
print(par(4))

#retorna a letra no indice 0
primeiro = lambda letra: letra[0]
print(primeiro('Python'))

#inverte a string
reverso = lambda s: s[::-1]
print(reverso('Python'))

#somar numeros
soma = lambda num1,num2 : num1 + num2
print(soma(99,1))