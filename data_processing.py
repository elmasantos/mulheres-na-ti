#!/usr/bin/python                                                                        
# -*- coding: utf-8 -*-

import sys
import pandas as pd 
import argparse

parser = argparse.ArgumentParser(description='Script para tratar arquivos csv')
parser.add_argument('-f','--file', help='Arquivo CSV de matrículas', required=False)
parser.add_argument('-s','--semestre', help='Semestre das matrículas', required=False)

args = parser.parse_args()


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

if args.file is not None:
	#guardando nome do arquivo e semestre
	matriculas_file = args.file
	semestre_matriculas = args.semestre

	#leitura de arquivo
	matriculas_df = pd.read_csv(matriculas_file, sep=';')
	#matriculas dataset
	matriculas_no_missing = select_data(matriculas_df, 'discente', 'id_curso', id_curso_ti)
	#limpeza
	if args.semestre == '20141' or args.semestre == '20142':
		matriculas_no_missing = mat_fill_and_drop_data(matriculas_no_missing, ['faltas_unidade'])
	else:
		matriculas_no_missing = mat_fill_and_drop_data(matriculas_no_missing, ['faltas_unidade', 'Unnamed: 10'])

	#convertendo notas para float
	matriculas_no_missing['nota'] = matriculas_no_missing['nota'].astype(float)

	#alterando notas para 2 casas decimais
	matriculas_no_missing = matriculas_no_missing.round({'nota' : 2})

	#convertendo dados para string
	matriculas_no_missing = matriculas_no_missing.astype(str)

	matriculas_no_missing.to_csv("data/processed/matriculas_"+args.semestre+"_processed.csv")

else:
	#leitura de arquivos
	discentes_df = pd.read_csv('data/dados-pessoais-discentes.csv', sep=';')

	#discentes dataset
	df_no_missing = select_data(discentes_df, 'id_discente', 'nivel_ensino', 'GRADUAÇÃO')
	df_no_missing['bairro'] = df_no_missing['bairro'].str.replace('CANDEL&#65533;RIA', 'CANDELARIA')
	#preenchimento de campos vazios
	#values = {'forma_ingresso' : 'forma de ingresso'}
	#df_no_missing.fillna(value=values, inplace=True)

	#preenchimento de campos de CEP com valor 59
	'''df_no_missing.replace('59', '59000-000', inplace=True)
	#retirando máscara de CEP, pontos e espaços
	df_no_missing['cep'] = df_no_missing['cep'].str.replace('-', '')
	df_no_missing['cep'] = df_no_missing['cep'].str.replace('.', '')
	df_no_missing['cep'] = df_no_missing['cep'].str.replace(' ', '')'''

	
	df_no_missing.to_csv("data/processed/dados_discentes_processed.csv")