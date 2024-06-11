'''
    Manipulando Arquivos TXT

    TXT é a extensão de arquivo para arquivos de texto puro. Um 
    arquivo TXT é um arquivo de texto simples sem formatação, 
    como negrito, itálico ou fontes diferentes. Ele pode ser 
    aberto e editado com muitos aplicativos diferentes, incluindo 
    editores de texto, processadores de texto e IDEs. Arquivos TXT 
    são amplamente utilizados para armazenar dados de texto simples,
    como listas, notas e documentos de texto. Eles são universais
    e podem ser lidos em praticamente qualquer dispositivo ou 
    sistema operacional.
'''

#gerando variavel 
texto = 'Ciencia de dados pode seu uma excelente alternativa de carreira.\n'
texto = texto + 'Esses profissionais precisam saberr como programar em python.\n'
texto+= 'E, claro, devem ser profissionais em Data Science'

print(texto)

#importando os modulos os, permite interagir com o sistema operacional 
#de forma mais simples rapida e com securança
import os

#criando um arquivo
#chamando as funções path que é caminho e join para juntar do pacote os
#abrindo arquivo para gravação a partir da função join do os
arquivo = open(os.path.join('arquivos/cientista.txt'),'w')#pacote superir para quando quiser manipular arquivo no SO

#gravando os dados no arquivo
for palavra in texto.split():
    arquivo.write(palavra + ' ')

#fechando o arquivo
arquivo.close()

#lendo o arquivo
arquivo = open('arquivos/cientista.txt', 'r')
conteudo = arquivo.read()
arquivo.close()
print(conteudo)

