'''
podemos usar aspas duplas ou simples para strings em Python
ou usar as duas juntas

'''

print("Hello world")
print('Hello world')
print("'Hello world'")

nome= 'Victoria Benassi'

#indexação em python

print(nome[0])#posição que esta a letra
#notação de fatiamento ou silicing
print(nome[:])#executa um silicing que faz a leitura de tudo até o ponto designado
print(nome[1:])#retorna todos elementos da string, começando pelo indice 1
print(nome[:3])#retorna tudo até o indice 3
print(nome[-1])#indexação negativa, le de tras pra frente
print(nome[:-1])#retorna tudo, exceto a ultima leta


'''
podemos usar dois pontos duas vezes em uma linha e, em seguida, um numero
que especifica a frequência para retornar elementos
'''

print(nome[::1])#le de uma em uma
print(nome[::2])#le de duas em duas posições
print(nome[::-1])#inverte os caracteres de tras pra frente

'''
propriedades de strings
'''

print(nome)#imprime a string
#print(nome[0] = 'x') não é possivel alterar um elemento da string
print("nome: "+ nome) #concatenando a string
nome = ' nome: ' + nome #concatenando na variavel
print(nome) 

#podemos usar o simbolo de multiplicaçao para criar repetição
print('w' * 3)
'''
Funções built-in de strings
'''

print(nome.upper()) #todos caracteres maiusculos
print(nome.lower()) #todos caracteres minisculos
print(nome.split()) #divisão da string por espaços em branco(padrão)
print(nome.split(':')) #dividir uma string por um elemento especifico

'''
Funções string
'''

mensagem='Seja bem vindo(a) a linguagem python!'

print(mensagem.capitalize())#converte a primeira letra para maiusculo
print(mensagem.count('a'))#conta quantas vezes aparece o caractere na string
print(mensagem.isalnum())#verifica se a string toda é de numeros e retorna um valor bool
print(mensagem.islower())#verifica se todos elementos são minusculos
print(mensagem.isspace())#verifica essa string é toda espaço
print(mensagem.islower())#verifica se todos elementos são minusculos
print(mensagem.endswith('o'))#verifica se a string termina com a letra o
numero = '1000' #numero 1000 representado como string
print(numero.isalnum())#verifica se todos elementos da string são numeros

'''
comparando strings
'''

print('Python' == 'R')#compara se as strings são iguais
print('Python' == 'Python')

