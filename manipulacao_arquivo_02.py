'''
    gravando arquivos - sobescreve o arquivo
'''

#abrindo o arquivo para gravação
arquivo_2 = open('arquivos/arquivo2.txt','w') #w = write(escrever)
#se o arquivo não existe ele vai criar, se existir ele sobescreve

#como usamos o arquivo apenas para gravacao, não podemos usar comandos de leitura
#print(arquivo_2.read())

#gravando arquivo
arquivo_2.write("Aprendendo a programar em python ")

#lendo arquivo gravado
arquivo_2 = open('arquivos/arquivo2.txt' , 'r')

print(arquivo_2.read())

#acrescentando conteudo
arquivo_2 = open('arquivos/arquivo2.txt','a') # a = append(acrescentar)

arquivo_2.write('e a metodologia de ensino da dsa facilita o aprendizado')

#fechar o arquivo
arquivo_2.close()
  
#abrindo para leitura
arquivo_2 = open('arquivos/arquivo2.txt','r')
print(arquivo_2.read())

#retornando ao inicio do arquivo para leiturA
arquivo_2.seek(0,0)

print(arquivo_2.read())

#fazendo a gravação vai rescrever o que está escrito
arquivo_2 = open('arquivos/arquivo2.txt','w')

arquivo_2.write('rescrevendo')

