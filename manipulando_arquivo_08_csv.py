'''
Manipulando Arquivos CSV 

CSV (Comma-Separated Values) é um formato de arquivo que armazena dados tabulares 
em formato de texto plano. Cada linha do arquivo CSV representa uma linha da tabela 
e as colunas são separadas por vírgulas. É amplamente utilizado para exportar e importar 
dados em diferentes aplicações, como planilhas e banco de dados. CSV é uma opção simples 
e universal para compartilhar dados, pois pode ser aberto e editado com muitos aplicativos 
diferentes, incluindo programas de planilha e editores de texto.
'''

#importando o modulo csv
import csv

with open('arquivos/numeros.csv','w') as arquivo:
    #cria o objeto de gravação
    #chama o pacote csv, chama o metodo writer e coloco o arquivo como argumento
    #cria o objeto chamado writer
    writer = csv.writer(arquivo)

    #grava no arquivo linha a linha
    #para esse objeto eu chamo o metodo writerow(escrever linha)
    writer.writerow(('nota1','nota2','nota3'))
    writer.writerow((63,87,92))
    writer.writerow((61,79,76))
    writer.writerow((72,64,91))

#leitura de arquivo csv
# encoding= codificação do arquivo, formato de caracteres 
# newline= indicando que quero o caracter \r e \n
with open('arquivos/numeros.csv','r',encoding='utf8',newline='\r\n') as arquivo:
    #cria o objeto de leitura
    leitor = csv.reader(arquivo)#metodo reader do pacote csv com o argumento arquivo
    
    #loop para percorrer o objeto leitor e imprimir cada letra
    for x in leitor:
        print(x)

#gerando uma lista com dados do arquivo csv
with open('arquivos/numeros.csv','r',encoding='utf8',newline='\r\n') as arquivo:
    #cria o objeto de leitura
    leitor = csv.reader(arquivo)#metodo reader do pacote csv com o argumento arquivo
    dados = list(leitor)
print(dados)

#imprimindo a partir da segunda linha
for linha in dados[1:]:
    print(linha)
