'''
 criando funções usando outras funções
'''

import math

#verificando se um numero é primo
def numeroPrimo(num):
    if(num % 2) == 0 and num >2:
        return print('Este numero não é primo')
    
    for i in range(3,int(math.sqrt(num))+1,2):
        if (num % i) == 0:
            return print('Este numero não é primo')
    return print('Este número é primo')

numeroPrimo(541)

numeroPrimo(2)

caixa_baixa = 'Hello World'

def lowerCase(text):
    return text.lower()

lowercased_string = lowerCase(caixa_baixa)
print(lowercased_string)