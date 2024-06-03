'''
local e global
'''

#variavel global
var_global = 10

#função

def multiplica_numeros(num1,num2):
    var_local = num1 * num2 #esta é uma variavel local
    print(var_local)

multiplica_numeros(2,9)

print(var_global)