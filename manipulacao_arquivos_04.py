'''
    Contando as linhas de um arquivo
'''

f = open('arquivos/salarios.csv','r')
data = f.read()
rows = data.split('\n')
full_data = []

for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)

print(full_data)

#loop para contar quantas linhas tem no arquivo

contador = 0
for row in rows:
    contador+=1 #equivalente a : contador = contador + 1

print(contador)

'''
    Contando o numero de colunas de um arquivo
'''

f = open('arquivos/salarios.csv','r')
data = f.read()
rows = data.split('\n')
full_data = []

for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)
    first_row = full_data[0]

contador = 0
for coluna in first_row:
    contador=contador+1

print(contador)

#abrindo arquivo para leitura
arquivo_3 = open('arquivos/arquivo3.txt','r')
print(arquivo_3.read())

#estamos no final do arquivo e não há mais nada para ler
print(arquivo_3.read)

#retornando ao inicio do arquivo
print(arquivo_3.seek(0))

print(arquivo_3.seek(0))
print(arquivo_3.readlines())#ler linha a linha

#podemos usar um loop for para ler o arquivo
for line in open('arquivos/arquivo3.txt'):
    print(line)