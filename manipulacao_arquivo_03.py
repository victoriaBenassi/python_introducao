'''
    Abrindo dataset em linha unica
'''

#abrindo arquivo
f = open('arquivos/salarios.csv','r')

#gravando a leitura em uma variavel
data = f.read()

#dividindo quando encontrar um \n para o meu arquivo e gravando em uma variavel 

rows = data.split('\n')

print(rows)

'''
    Dividindo um arquivo em colunas
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