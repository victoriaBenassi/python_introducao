'''
 Condicionais aninhados
 colocar uma instrução condicional dentro de outra.
 Isso permite que você faça verificações mais específicas ou complexas
'''

idade = 18
if idade > 17:
    print("Você pode dirigir!")

#condicional aninhado
Nome = "Bob"
if idade > 13:
    if Nome == "Bob":
        print("Ok Bob, você está autorizado a entrar!")
    else:
        print("Desculpe, mas você não pode entrar!")

#usando operadores logicos
idade = 13
Nome = "Bob"
if idade >= 13 and Nome == "Bob":
    print("Ok Bob, você está autorizado a entrar!")

idade = 12
Nome = "Bob"
if (idade >= 13) or (Nome == "Bob"):
    print("Ok Bob, você está autorizado a entrar!")