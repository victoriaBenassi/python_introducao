'''
Calculadora simples
'''

    #função para somar
def soma(): 
    numero_1=float(input("Digite o primeiro número: "))
    numero_2=float(input("Digite o segundo número: "))

    resultado = numero_1+numero_2
    print(f"O resultado da soma é {resultado}.")

    #função para subtrair
def subtracao():
    numero_1=float(input("Digite o primeiro número: "))
    numero_2=float(input("Digite o segundo número: "))

    resultado = numero_1-numero_2
    print(f"O resultado da subtração é {resultado}.")
    
    #função para dividir
def divisao():
    numero_1=float(input("Digite o primeiro número: "))
    numero_2=float(input("Digite o segundo número: "))

    resultado = numero_1/numero_2
    print(f"O resultado da divisão é {resultado}.")

    #função para multiplicar
def multiplicacao():
    numero_1=float(input("Digite o primeiro número: "))
    numero_2=float(input("Digite o segundo número: "))

    resultado = numero_1*numero_2
    print(f"O resultado da multiplicação é {resultado}.")

print("\tBem-vindo(a) à Calculadora")
print("\tQual operação deseja realizar?")
opcao=int(input("\n\t1-Soma  2-Subtração  3-Divisão  4-Multiplicação \n"))

'''
 O usuario escolhe a operação que deseja realizar
 e temos uma estrutura de decisão que realiza o calculo 
 escolhido pelo usuario chamando as funções criadas acima.
'''

if opcao == 1:
    soma()
elif opcao == 2:
    subtracao()
elif opcao == 3:
    divisao()
elif opcao == 4:
    multiplicacao()
else:
    print("Opção inválida.")

