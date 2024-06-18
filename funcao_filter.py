'''
Função Filter

A função filter() em Python é uma função que filtra elementos de uma estrutura 
de dados iterável (como uma lista, tupla ou outro objeto iterável) com base em 
uma determinada condição. A função filter() retorna um objeto filtro, que pode 
ser convertido em outra estrutura de dados, como uma lista, se necessário.
'''

#criando uma função 

def verificaPar(num):
    if num % 2 == 0 :
        return True
    else:
        return False
    
#chamando a função e passando um numero como parametro, retornara 
#falso se for impar e true se for par

print(verificaPar(2))

lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

#a função filter() retorna um iterator
filter(verificaPar,lista)

print(list(filter(verificaPar,lista)))

#usando a expressão lambda

print(list(filter(lambda num : num % 2 == 0 , lista)))

#verificar numeros acima de 8

print(list(filter(lambda num: num > 8 , lista)))

