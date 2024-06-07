dict_alunos = {'Bob': 68,'Michael': 84,'Ana': 93, 'Zico': 57}


#criamos um novo dicionario com o status : nota maior que 70, aprovado, senão, reprovado
dict_alunos_status = {k: ('aprovado' if v > 70 else 'reprovado') for (k, v) in dict_alunos.items()}
print(dict_alunos_status)