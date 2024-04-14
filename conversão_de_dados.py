'''
funções de conversão

int(<dado>) para obter numeros inteiros
str(<dado>) para obter dados em seu formato texto
float(<dado>) para obter numeros reais
bool(<dado>) para obter dados booleanos
'''

idade = 0
altura = 0.0
nome = ""

idade=int(input("Digite a idade: "))
altura=float(input("Digite a altura: "))
nome=input("Digite o nome: ")

print(f"\tnome: {nome}\t \n \tidade: {idade} \n \taltura: {altura:.2f}")