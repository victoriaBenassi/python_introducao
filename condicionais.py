# Condicional If (Se)
if 5 > 2:
    print("A sentença é verdadeira!")

# Condicional If...Else
if 5 < 2:
    print("A sentença é verdadeira!")
else:
    print("A sentença é falsa!")

# Condicional If...Else com variável
dia = "Terça"
if dia == "Segunda":
    print("Hoje fará sol!")
else:
    print("Hoje vai chover!")

''' 
 Podemos usar o operador elif para validar mais de uma condição
 Em Python, não existe a palavra-chave else if, mas sim elif,
 que é uma combinação de else e if, permitindo criar várias 
 condições intermediárias entre o if inicial e o else final
'''
if dia == "Segunda":
    print("Hoje fará sol!")
elif dia == "Terça":
    print("Hoje vai chover!")
else:
    print("Sem previsão do tempo para o dia selecionado")