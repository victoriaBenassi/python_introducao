'''
    Usando a Expressão with 
    quando usamos with método close() é executado automaticamente.
'''
texto = 'Ciencia de dados pode seu uma excelente alternativa de carreira.\n'
texto = texto + 'Esses profissionais precisam saberr como programar em python.\n'
texto+= 'E, claro, devem ser profissionais em Data Science'

#com arquivo aberto no modo leitura chame de arquivo
with open('arquivos/cientista.txt','r') as arquivo:
    conteudo = arquivo.read()
    #a expressão with vai finalizar e fechar a conexão com o arquivo

print(len(conteudo))#comprimento do conteudo

print(conteudo)


#com arquivo aberto no modo escrita chame de arquivo
with open('arquivos/cientista.txt','w') as arquivo:
    arquivo.write(texto[:19])
    arquivo.write('\n')
    arquivo.write(texto[28:66])
#a expressão with após fazer a gravação vai finalizar e fechar a conexão com o arquivo

#lendo o arquivo
arquivo = open('arquivos/cientista.txt','r')
conteudo = arquivo.read()
arquivo.close()
print(conteudo)
