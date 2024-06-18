'''     Cada possibilidade de erro deve ser tratada no seu programa.        '''

#tratando qualquer erro
def numeroInt():
    try:
        valor = int(input('Digite um numero: '))  
    except:
        print('Voçê não digitou um numero! ')
    finally:
        print('Obrigado(a)!')
numeroInt()

#Dando uma chance de digitar novamente
def numeroInt():
    try:
        valor = int(input('Digite um numero: '))  
    except:
        print('Voçê não digitou um numero! ')
        valor = int(input('Tente novamente. Digite um número: '))
    finally:
        print('Obrigado(a)!')
    print(valor)

numeroInt()

#usando um loop para tratar erro
def numeroInt():
    while True:
        try:
            valor = int(input('Digite um numero: '))  
        except:
            print('Voçê não digitou um numero! ')
            continue
        else:
            print("Obrigado por digitar um número!")
            break
        finally:
            print('fim da execução!')
        print(valor)

numeroInt()