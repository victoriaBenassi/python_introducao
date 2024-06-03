'''
Métodos

Tudo em Python é objeto(porque python é uma linguagem orientada a objeto). 
E cada objeto tem métodos e atributos.

- Atributos são propriedades, características do objeto.
- Métodos são funções com ações que podem ser executadas nos objetos.
'''

#criando uma lista 
lista=[100,-2,12,65,0]
type(lista)
  
#verificar métodos e atributos .
#lista.

#usando um metodo do objeto lista
lista.append(100)#incluir o numero 100 á lista

print(lista)

#metodo para contar quantas vezes o numero aparece na lista
print(lista.count(100))

#a função help() explica como utilizar cada metodo de um objeto
help(lista.count)

#a função dir() mostra todos os metodos e atributos de um objeto
print(dir(lista))

frase = 'isso e uma string'

type(frase)

#verificando os metodos e atributos frase.

#o metodo de um objeto pode ser chamado dentro de uma função, como print()
print(frase.split())#dividir a frase em pedaços menores
                    #split faz a divisão por espaços
