'''
operadores logicos - validar mais de uma condição ou 
concatenar as condições das estruturas condicionais por exemplo
Os operadores lógicos funcionam assim:

- Operador and - Retorna True se ambas as declarações forem verdadeiras.
- Operador or - Retorna True se uma das declarações for verdadeira.
- Operador not - Inverte o resultado, retorna False se o resultado for True.
'''

# se as duas forem verdadeiras, toda condição será verdadeira
idade = 18
nome = 'Bob'
if idade > 17 and nome == "Bob":
    print("Autorizado!")

# Operador and

numero = 4

if (numero > 2) and (numero % 2 == 0):
    print("Isso está sendo impresso porque as duas condições são verdadeiras!")

# Operador and

numero = 4

if (numero > 5) and (numero % 2 == 0):
    print("Isso está sendo impresso porque as duas condições são verdadeiras!")
else:
    print("Isso está sendo impresso porque uma das duas condições é falsa!")

# Operador or

numero = 4

if (numero > 5) or (numero % 2 == 0):
    print("Isso está sendo impresso porque uma duas condições é verdadeira!")

# Operador not

numero = 4

if not(numero > 5) and (numero % 2 == 0):
    print("Isso está sendo impresso porque as duas condições são verdadeiras!")
else:
    print("Isso está sendo impresso porque uma das duas condições é falsa!")

# Operador and, or e not

numero = 4

if (not(numero > 5) and (numero % 2 == 0)) or (numero == 4):
    print("Isso está sendo impresso porque as duas primeiras condições são verdadeiras ou a terceira é verdadeira!")

# Exemplo com o uso de variáveis

disciplina = 'Data Science'
nota_final = 70

if disciplina == 'Data Science' and nota_final >= 70:
    print('Você foi aprovado!')
else:
    print('Lamento, acho que você precisa estudar mais!')

# Usando mais de uma condição na cláusula if 

disciplina = 'Data Science'
nota_final = 60

if disciplina == 'Data Science' and nota_final >= 70:
    print('Você foi aprovado!')
else:
    print('Lamento, acho que você precisa estudar mais!')

# Usando mais de uma condição na cláusula if e introduzindo Placeholders
#placeholders - guardador de lugar
#%s - string  %r - numero
disciplina = 'Data Science'
nota_final = 90
semestre = 2

if disciplina == 'Data Science' and nota_final >= 80 and semestre != 1:
    print('Você foi aprovado em %s com média final %r!' %(disciplina, nota_final))
else:
    print('Lamento, acho que você precisa estudar mais!')