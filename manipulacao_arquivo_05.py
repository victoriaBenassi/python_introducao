'''
importando um Dataset com pandas
poderá instalá-lo executando o seguinte comando 
em um terminal ativado: python -m pip install {package_name}
'''

import pandas as pd

#verificando a versão
print(pd.__version__)

#criando uma variavel com o nome do arquivo
arquivo = 'arquivos/salarios.csv'

#carregando o arquivo
#chamando o metodo read e gravando o arquivo na variavel df
df = pd.read_csv(arquivo)

#arquivo carregado no formato de tabela
#cabeca do dataframe (primeiras linhas)
print(df.head())

#filtrando o dataframe por uma das colunas e contando quantos registros
#tem para cada categoria dessa coluna 
print(df['Position Title'].value_counts())