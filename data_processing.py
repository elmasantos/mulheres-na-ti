#!/usr/bin/python                                                                        
# -*- coding: utf-8 -*-

import pandas as pd 


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

#limpando dataframe
def matricula_drop_data(dataframe, column):
	#excluindo coluna desnecessária	
	dataframe.drop(column, axis=1, inplace=True)
	#excluindo registros com descrição 'EXCLUIDA' ou 'CANCELADO'
	dataframe = dataframe[dataframe.descricao != 'EXCLUIDA']
	dataframe = dataframe[dataframe.descricao != 'CANCELADO']
	dataframe = dataframe[dataframe.descricao != 'INDEFERIDO']
	
	return dataframe


#id do curso tecnologia da informação
id_curso_ti = 92127264

#leitura de arquivos
discentes_df = pd.read_csv('data/discentes.csv', sep=';')
matriculas20141_df = pd.read_csv('data/matricula-componente-20141.csv', sep=';')
matriculas20142_df = pd.read_csv('data/matricula-componente-20142.csv', sep=';')
matriculas20151_df = pd.read_csv('data/matriculas-de-2015.1.csv', sep=';')
matriculas20152_df = pd.read_csv('data/matriculas-de-2015.2.csv', sep=';')
matriculas20161_df = pd.read_csv('data/matriculas-de-2016.1.csv', sep=';')
matriculas20162_df = pd.read_csv('data/matriculas-de-2016.2.csv', sep=';')

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
mat20141_no_missing = select_data(matriculas20141_df, 'discente', 'id_curso', id_curso_ti)
mat20142_no_missing = select_data(matriculas20142_df, 'discente', 'id_curso', id_curso_ti)
mat20151_no_missing = select_data(matriculas20151_df, 'discente', 'id_curso', id_curso_ti)
mat20152_no_missing = select_data(matriculas20152_df, 'discente', 'id_curso', id_curso_ti)
mat20161_no_missing = select_data(matriculas20161_df, 'discente', 'id_curso', id_curso_ti)
mat20162_no_missing = select_data(matriculas20162_df, 'discente', 'id_curso', id_curso_ti)


mat20141_no_missing = matricula_drop_data(mat20141_no_missing, 'faltas_unidade')
mat20142_no_missing = matricula_drop_data(mat20142_no_missing, 'faltas_unidade')
mat20151_no_missing = matricula_drop_data(mat20151_no_missing, ['faltas_unidade', 'Unnamed: 10'])
mat20152_no_missing = matricula_drop_data(mat20152_no_missing, ['faltas_unidade', 'Unnamed: 10'])
mat20161_no_missing = matricula_drop_data(mat20161_no_missing, ['faltas_unidade', 'Unnamed: 10'])
mat20162_no_missing = matricula_drop_data(mat20162_no_missing, ['faltas_unidade', 'Unnamed: 10'])


#convertendo dados em string
mat20141_no_missing = mat20141_no_missing.astype(str)
mat20142_no_missing = mat20142_no_missing.astype(str)
mat20151_no_missing = mat20151_no_missing.astype(str)
mat20152_no_missing = mat20152_no_missing.astype(str)
mat20161_no_missing = mat20161_no_missing.astype(str)
mat20162_no_missing = mat20162_no_missing.astype(str)




df_no_missing.to_csv("data/processed/discentes_processed.csv")
mat20141_no_missing.to_csv("data/processed/matriculas_20141_processed.csv")
mat20142_no_missing.to_csv("data/processed/matriculas_20142_processed.csv")
mat20151_no_missing.to_csv("data/processed/matriculas_20151_processed.csv")
mat20152_no_missing.to_csv("data/processed/matriculas_20152_processed.csv")
mat20161_no_missing.to_csv("data/processed/matriculas_20161_processed.csv")
mat20162_no_missing.to_csv("data/processed/matriculas_20162_processed.csv")
