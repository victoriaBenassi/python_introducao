'''
Expressões Regulares

Expressões regulares são padrões usados para combinar ou encontrar 
ocorrências de sequências de caracteres em uma string. Em Python, 
expressões regulares são geralmente usadas para manipular strings e 
realizar tarefas como validação de entrada de dados, extração de 
informações de strings e substituição de texto.
'''

#importando pacote re (regular expression)
import re

#criando uma string
texto = "Meu e-mail é exemplo@gmail.com e você pode me contatar em outro_email@yahoo.com."

# Expressão regular para contar quantas vezes o caracter arroba aparece no texto
resultado = len(re.findall('@',texto))#findall = encontre tudo
print("O caractere '@' apareceu ", resultado, ' vezes no texto')

# Expressão regular para extrair a palavra que aparece após a palavra "você" em um texto
resultado = re.findall(r'você (\w+)',texto) # você - ponto de partida espaço e buscando qualquer palavra depois
#com o codigo \w, r - permite que considere o \w como padrão e não com string

print(resultado[0])

'''
Nota: O r antes da string que representa a expressão regular em Python 
é usado para indicar que a string é uma string literal raw. Isso significa 
que as barras invertidas (\) não são interpretadas como caracteres de escape, 
mas são incluídas na expressão regular como parte do padrão.
'''