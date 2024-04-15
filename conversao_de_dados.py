'''
funções de conversão

int(<dado>) para obter numeros inteiros

str(<dado>) para obter dados em seu formato texto

float(<dado>) para obter numeros reais

bool(<dado>) para obter dados booleanos

hex(<dado>) para obter dados hexadecimal

bin(<dado>) para obter dados binario


abs(<dado>) retorna o valor absoluto

round(<dado>, <casas_decimais>) aredonda o dado para 
a quantidade de casas decimais informada 

pow(<base>,<potencia>) potencia
'''
print(bin(10))

idade = 0
altura = 0.0
nome = ""

idade=int(input("\tDigite a idade: "))
altura=float(input("\tDigite a altura: "))
nome=input("\tDigite o nome: ")

print(f"\n\tnome: {nome}\t \n \tidade: {idade} \n \taltura: {altura:.2f}")

print(int(9.1))
print(float(10))