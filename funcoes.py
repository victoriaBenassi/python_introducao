'''
 Funções são blocos de codigos que podem ser 
 executados todas vezes que são chamados, quando
 a função faz parte de uma classe, ela é chamada de metodo
'''

#o print() é uma função built-in(interna do python)
print('bem-vindo(a)')

#definindo uma função
def primeiraFuncao():
    print('hello world')

#chamando a função
primeiraFuncao()

#definindo uma função
def primeiraFuncao():
    nome = input("Insira seu nome ")
    print('Hello %s' %(nome))

#chamando a função
primeiraFuncao()

#definindo uma função com parametro
def segundaFuncao(nome):
    print('Hello %s'%(nome))

segundaFuncao('Aluna')

#função para imprimir numeros
def imprimeNumeros():
    #loop
    for i in range(0,5):
        print('Numero '+ str(i))

imprimeNumeros()

#função para somar numeros
def addNum(firstnum, secondnum):
    print('Primeiro numero: ' + str(firstnum))
    print('Segundo numero: ' + str(secondnum))
    print('Soma: ', firstnum + secondnum)

#chamando a função e passando parametros
addNum(4,7)
#chamando a função e passando parametros
addNum(45,3)

#funções com numeros variavel de argumentos
def printVarInfo( arg1, *vartuple ):
    #imprimindo o valor do primeiro argumento
    print('o argumento passado foi: ', arg1)

    #imprimindo o valor do segundo argumento
    for item in vartuple:
        print('o argumento passado foi: ', item)
    return;

#fazendo a chamada á função usando apenas 1 argumeto
printVarInfo(10)

printVarInfo('chocolate','morango')

printVarInfo('chocolate','morango','pessego')