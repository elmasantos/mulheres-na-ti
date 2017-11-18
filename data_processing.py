#!/usr/bin/python                                                                        
# -*- coding: utf-8 -*-

import pandas as pd 

#id do curso tecnologia da informação
id_curso_ti = 92127264
#leitura de arquivo
discentes_df = pd.read_csv('data/discentes2.csv', sep=';')
matriculas20172_df = pd.read_csv('data/matricula-componente-20172.csv', sep=';')


#seleção de dados do dataset
def select_data(dataframe, column_notnull, column_selected, name):
	#Seleção de dados onde registros na coluna id_discente não são nulos
	df_no_missing = dataframe[pd.notnull(dataframe[column_notnull])]

	#Seleção de dados onde registro em column_selected é igual a 'name'
	df_no_missing = df_no_missing[df_no_missing[column_selected] == name]

	return df_no_missing

#preenchimento de campos vazios
def fill_nandata(dataframe, column, data):
	values = {column : data}
	dataframe.fillna(value=values, inplace=True)

	return dataframe

#discentes dataset
df_no_missing = select_data(discentes_df, 'id_discente', 'nivel_ensino', 'GRADUAÇÃO')
df_no_missing = fill_nandata(df_no_missing, 'cep', '59000-000')
df_no_missing = fill_nandata(df_no_missing, 'forma_ingresso', 'forma de ingresso')

#preenchimento de campos de CEP com valor 59
df_no_missing.replace('59', '59000-000', inplace=True)

#retirando máscara de CEP, pontos e espaços
df_no_missing['cep'] = df_no_missing['cep'].str.replace('-', '')
df_no_missing['cep'] = df_no_missing['cep'].str.replace('.', '')
df_no_missing['cep'] = df_no_missing['cep'].str.replace(' ', '')

#matriculas dataset
print(len(matriculas20172_df))

mat_no_missing = select_data(matriculas20172_df, 'discente', 'id_curso', id_curso_ti)
#excluindo coluna desnecessária
mat_no_missing.drop('faltas_unidade', axis=1, inplace=True)
print(mat_no_missing.head(10))




#novo arquivo csv sem missing values, sem outliers e apenas graduação
#df_no_missing.to_csv("data/discentes_processed2.csv")


'''
#preenchimento de campos de CEP vazios
value = {'cep': '59000-000', 'forma_ingresso' : 'forma de ingresso'}
df_no_missing.fillna(value=value, inplace=True)


#preenchimento de campos de CEP com valor 59
df_no_missing.replace('59', '59000-000', inplace=True)

#retirando máscara de CEP, pontos e espaços
df_no_missing['cep'] = df_no_missing['cep'].str.replace('-', '')
df_no_missing['cep'] = df_no_missing['cep'].str.replace('.', '')
df_no_missing['cep'] = df_no_missing['cep'].str.replace(' ', '')

#novo arquivo csv sem missing values, sem outliers e apenas graduação
#df_no_missing.to_csv("data/discentes_processed2.csv")'''
'''print(matriculas20172_df.dtypes)

df_matriculas_no_missing = matriculas20172_df[pd.notnull(matriculas20172_df['discente'])]
print(len(df_matriculas_no_missing))

df_matriculas_no_missing = df_matriculas_no_missing[df_matriculas_no_missing.id_curso == id_curso_ti]

print(len(df_matriculas_no_missing))'''


