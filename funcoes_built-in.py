'''
 Funções built-in em Python são funções que estão 
 integradas diretamente na linguagem e estão sempre 
 disponíveis para uso, não exigindo a importação de 
 módulos adicionais. Elas são parte fundamental da 
 linguagem e oferecem funcionalidades básicas que podem
 ser usadas em qualquer programa Python.
'''
#funções Built-in

print(abs(-56))#retorna valor absoluto
print(abs(23))#retorna valor absoluto 
print(bool(1))#retorna valor booleano
print(bool(0))#retorna valor booleano
print(int(4.3))#retorna valor inteiro
print(str(13))#retorna valor em string
print(float(5))#retorna valor float

#usando a funcao int para converter o valor digitado
idade = int(input('Digite sua idade: '))
if idade > 13:
    print('Voce tem mais de 13 anos')
else:
    print('Menos de 14 anos')

print(int('10'))#converte string para inteiro
print(float('1034.4435'))#converte string para float
print(str(10))#converte inteiro para string
print(len([23,24,25,28]))#para capturar o comprimento de uma lista
array = [1,2,3] 
print(max(array))#buscando o valor maximo de um array
print(min(array))#buscando o valor minimo de um array
list1=[13,45,67,89]
print(sum(list1))#somando uma lista de numeros
