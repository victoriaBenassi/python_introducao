'''
fazendo split dos dados
'''

#fazendo split dos dados
def split_string_palavras(text):
    return text.split(" ")
    #toda vez que encontrar um espaço a palavra vai ser dividida

texto = 'esta função sera bastante util para separa grandes volumes de dados'

#isso divide a string em uma lista de palavras
print(split_string_palavras(texto))

#podemos atribuir o output de uma função para uma variavel 
token = split_string_palavras(texto)
print(token)

#fazendo split dos dados
def split_string_letras(text):
    texto = text.upper()
    for letra in texto:
        print(letra)

print(split_string_letras(texto))