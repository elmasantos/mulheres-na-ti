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


#limpando dataframe
def mat_fill_and_drop_data(dataframe, column):
	#excluindo coluna desnecessária	
	dataframe.drop(column, axis=1, inplace=True)
	#excluindo registros com descrição 'EXCLUIDA' ou 'CANCELADO'
	dataframe = dataframe[dataframe.descricao != 'EXCLUIDA']
	dataframe = dataframe[dataframe.descricao != 'CANCELADO']
	dataframe = dataframe[dataframe.descricao != 'INDEFERIDO']
	#preenchendo campos vazios
	values = {'unidade' : '0', 'nota' : '0', 'reposicao' : '0', 'media_final' : '0', 
	'numero_total_faltas' : '0'}
	dataframe.fillna(value=values, inplace=True)
	
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
#preenchimento de campos vazios
values = {'cep' : '59000000', 'forma_ingresso' : 'forma de ingresso'}
df_no_missing.fillna(value=values, inplace=True)
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


mat20141_no_missing = mat_fill_and_drop_data(mat20141_no_missing, 'faltas_unidade')
mat20142_no_missing = mat_fill_and_drop_data(mat20142_no_missing, 'faltas_unidade')
mat20151_no_missing = mat_fill_and_drop_data(mat20151_no_missing, ['faltas_unidade', 'Unnamed: 10'])
mat20152_no_missing = mat_fill_and_drop_data(mat20152_no_missing, ['faltas_unidade', 'Unnamed: 10'])
mat20161_no_missing = mat_fill_and_drop_data(mat20161_no_missing, ['faltas_unidade', 'Unnamed: 10'])
mat20162_no_missing = mat_fill_and_drop_data(mat20162_no_missing, ['faltas_unidade', 'Unnamed: 10'])

#convertendo notas para float
mat20141_no_missing['nota'] = mat20141_no_missing['nota'].astype(float)
mat20142_no_missing['nota'] = mat20142_no_missing['nota'].astype(float)
mat20151_no_missing['nota'] = mat20151_no_missing['nota'].astype(float)
mat20152_no_missing['nota'] = mat20152_no_missing['nota'].astype(float)
mat20161_no_missing['nota'] = mat20161_no_missing['nota'].astype(float)
mat20162_no_missing['nota'] = mat20162_no_missing['nota'].astype(float)

#alterando notas para 2 casas decimais
mat20141_no_missing = mat20141_no_missing.round({'nota' : 2})
mat20142_no_missing = mat20142_no_missing.round({'nota' : 2})
mat20151_no_missing = mat20151_no_missing.round({'nota' : 2})
mat20152_no_missing = mat20152_no_missing.round({'nota' : 2})
mat20161_no_missing = mat20161_no_missing.round({'nota' : 2})
mat20162_no_missing = mat20162_no_missing.round({'nota' : 2})

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