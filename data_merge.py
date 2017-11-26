import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Script para cruzar tabelas')
parser.add_argument('-f','--file', help='Tabela de matrículas processada', required=True)
parser.add_argument('-s','--semestre', help='Semestre das matrículas', required=False)

args = parser.parse_args()

semestre_matriculas = args.semestre
matriculas_file = args.file

discentes_df = pd.read_csv('data/processed/dados_discentes_processed.csv', sep=',')
matriculas_df = pd.read_csv(matriculas_file, sep=',')

print(discentes_df.columns.tolist)
print(matriculas_df.columns.tolist)
merge = pd.merge(discentes_df, matriculas_df, how='inner', left_on='id_discente', right_on='discente')

#deletando colunas 'Unnamed: 0_x' e 'Unnamed: 0_y'
merge.drop(['Unnamed: 0_x', 'Unnamed: 0_y'], axis=1, inplace=True)

#preenchendo campos vazios
values = {'estado_origem' : 'NAO INFORMADO', 'cidade_origem' : 'NAO INFORMADO',
'estado' : 'NAO INFORMADO', 'municipio' : 'NAO INFORMADO', 'bairro' : 'NAO INFORMADO'}
merge.fillna(value=values, inplace=True)

print(merge.isnull().sum())

merge.to_csv("data/merge/merge"+semestre_matriculas+".csv")

