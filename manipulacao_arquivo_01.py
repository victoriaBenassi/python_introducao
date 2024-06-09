'''
    manipulação de arquivos
        lendo arquivos
'''

#abrindo o arquivo para leitura
arquivo_1 = open('arquivos/arquivo1.txt', 'r')
#'(pasta/arquivo)' , 'r' = read(ler)

#verificando o tipo
print(type(arquivo_1))

#lendo o arquivo
print(arquivo_1.read())

#contar o numero de caracteres
print(arquivo_1.tell())

#retornar para o inicio do arquivo e indica as cordenadas
print(arquivo_1.seek(0,0))

#lendo os primeiros 23 caracteres
print(arquivo_1.read(23))

#termina a leitura de onde parou
print(arquivo_1.read())

