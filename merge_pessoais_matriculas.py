import pandas as pd
import argparse


dados_pessoais_df = pd.read_csv('data/dados-pessoais-discentes.csv', sep=';', encoding="utf-8")
matriculas_df = pd.read_csv('data/matriculas-de-2016.2.csv', sep=';', encoding="utf-8")
id_curso_ti = 92127264

#seleção de dados do dataset
def select_data(dataframe, column_notnull, column_selected, name):
    #Seleção de dados onde registros na coluna id_discente não são nulos
    df_no_missing = dataframe[pd.notnull(dataframe[column_notnull])]

    #Seleção de dados onde registro em column_selected é igual a 'name'
    df_no_missing = df_no_missing[df_no_missing[column_selected] == name]

    return df_no_missing

matriculas_no_missing = select_data(matriculas_df, 'discente', 'id_curso', id_curso_ti)

merge = pd.merge(dados_pessoais_df, matriculas_no_missing, how='inner', left_on='id_discente', right_on='discente')

#deletando colunas 'Unnamed: 0_x' e 'Unnamed: 0_y'
#merge.drop(['Unnamed: 0_x', 'Unnamed: 0_y', 'discente'], axis=1, inplace=True)
merge.drop(['discente'], axis=1, inplace=True)

merge2 = merge
merge2.drop_duplicates(subset='id_discente', keep='first', inplace=True)
merge2 = merge2[merge2['ano_ingresso'] == 2016]
merge2 = merge2[merge2['periodo_ingresso'] == 2]

print(merge2.isnull().sum())
merge2.to_csv("data/merge/alunos20162.csv")

