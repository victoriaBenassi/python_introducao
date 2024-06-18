'''
Erros e Exceções

Sempre leia as mensagens de erro. Erros fazem parte do processo de 
aprendizagem e vão acompanhar você na sua jornada em programação, 
em qualquer linguagem.
'''

# Erro (leia a mensagem de erro)
#print('Hello)

# Erro (leia a mensagem de erro)
#8 + 's'

# Criando uma função
def divisao (num1, num2):
    resultado = num1 / num2
    print(resultado)

# Execução não gera erro


# Execução gerando erro (leia a mensagem de erro)
#divisao(4,0)
#não tem como dividir por 0 

'''         Try, Except, Finally        '''

#usando try, except

try:
    8+'s'
except TypeError:
    print('Operação não permitida')

#usando try, except e else 
try:
    arquivo = open('arquivos/testandoErros.txt','w')
    arquivo.write('Gravando no arquivo')
except IOError:
    print('Erro: o arquivo não encontrado ou não pode ser salvo')
else:
    print('Conteudo gravado com sucesso!')
    arquivo.close()

#usando try, except, else e finally
try:
    arquivo = open('arquivos/testandoErros','r')
    arquivo.write('Gravando no arquivo')
except IOError:
    print('Erro: o arquivo não encontrado ou não pode ser salvo')
else:
    print('Conteudo gravado com sucesso!')
    arquivo.close()
finally:
    print('comandos no bloco finally são sempre executados')