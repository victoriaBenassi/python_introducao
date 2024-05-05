'''
While e For Juntos

Vamos encontrar números primos em uma coleção de números usando loop While e For juntos.

Um número primo é um número natural maior do que 1 que é divisível apenas por 1 e por ele mesmo. Isso significa que não há nenhum outro número inteiro que possa dividir o número primo sem deixar resto. Por exemplo, o número 2 é primo, pois é divisível apenas por 1 e 2. O número 4 não é primo, pois é divisível por 2.

Aqui está o pseudocódigo:

    Inicialize uma lista vazia para armazenar os números primos
    Para cada número N entre 2 e 30:
    Inicialize uma variável eh_primo como verdadeira
    Para cada número i entre 2 e N/2:
        Se N é divisível por i, então:
        Altere a variável eh_primo para falso
        Pare de verificar os outros números
    Se a variável eh_primo ainda é verdadeira, adicione N à lista de números primos
    Imprima a lista de números primos
'''

# Encontrando números primos entre 2 e 30 usando loop for e while

# Variável para armazenar números primos
primos = []

# Loop for para percorrer números de 2 a 30
for num in range(2, 31):
    
    # Variável de controle
    eh_primo = True
    
    # Loop while para verificar se o número é primo
    i = 2
    while i <= num // 2:
        if num % i == 0:
            eh_primo = False
            break
        i += 1
    
    # Adicionando o número primo na lista
    if eh_primo:
        primos.append(num)

# Imprimindo a lista de números primos
print(primos)

# Encontrando números primos entre 2 e 30 usando loop for e while (outro exemplo)

# Loop for para percorrer números de 2 a 30
for i in range(2,31):
    
    # Variável de controle
    j = 2
    
    # Contador
    valor = 0
    
    # Loop while para verificar se o número é primo
    while j < i:
        if i % j == 0:
            valor = 1
            j = j + 1
        else:
            j = j + 1
    
    if valor == 0:
        print(str(i) + " é um número primo")
        valor = 0
    else:
        valor = 0