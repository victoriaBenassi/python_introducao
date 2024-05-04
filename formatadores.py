'''
strings 

{<dado>:<tam>}
{<dado>:>tam>}
{<dado>:^tam>}
'''
'''
inteiros

{<dado>: d} decimal
{<dado>: x} hexadecimal
{<dado>: o} octal
{<dado>: b} binario
'''
'''
float

{<dado>: .<tam>f} formata com um número específico de casas decimais
{<dado>: e} formata usando a notação científica
{<dado>: .<tam>e} formata em notação científica, especificando o número de casas decimais 
'''
'''
data e tempo

{<dado>: %Y-%m-%d} ano, mes e dia
{<dado>: %H-%M-%S} hora, minuto e segundo
{<dado>: %Y-%m-%d %H:M} ano, mes, dia e hora e minuto 
'''

#string

nome = "victoria"

print(f'nome é {nome:^30}') 
print(f'nome é {nome:<30}')
print(f'nome é {nome:>30}')