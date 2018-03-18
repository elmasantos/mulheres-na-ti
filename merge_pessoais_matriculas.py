#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import argparse
import data_handler

#parametros para script
parser = argparse.ArgumentParser(description='Script para cruzar tabelas')
parser.add_argument('-m','--matricula', help='Arquivo de matriculas', required=True)
parser.add_argument('-s','--semestre', help='Semestre referencia', required=False)

args = parser.parse_args()

#coleta semestre e arquivo passados como parametros
semestre = args.semestre[:4]
periodo = args.semestre[-1]
matriculas_file = args.matricula

#dados-pessoais-discentes dataframe
dados_pessoais_df = pd.read_csv('data/dados-pessoais-discentes.csv', sep=';', encoding="utf-8")
#matricula dataframe
matriculas_df = pd.read_csv(matriculas_file, sep=';', encoding="utf-8")
id_curso_ti = 92127264

#seleciona apenas discentes do curso BTI
matriculas_no_missing = data_handler.select_data(matriculas_df, 'discente', 'id_curso', id_curso_ti)

#merge entre dataframes dados-pessoais-discentes e matricula
merge = pd.merge(dados_pessoais_df, matriculas_no_missing, how='inner', left_on='id_discente', right_on='discente')

#deleta colunas desnecessarias
data_handler.drop_columns(merge, 'discente', 'id_turma', 'unidade', 'nota', 'reposicao', 'media_final', 'faltas_unidade', 'numero_total_faltas', 'descricao')

#deleta registros com o mesmo 'id_discente', exceto a primeira ocorrência
merge.drop_duplicates(subset='id_discente', keep='first', inplace=True)

#seleciona registros do ano de ingresso escolhido
merge = merge[merge['ano_ingresso'] == int(semestre)]

#seleciona registros do periodo de ingresso escolhido
merge = merge[merge['periodo_ingresso'] == int(periodo)]

#preenche campos vazios
merge = data_handler.fill_empty_fields(merge)

#padroniza nomes de bairros
merge = data_handler.replace_to_standardize(merge)

#apenas para chegar quantidade de registros nulos em cada coluna
print(merge['periodo_ingresso'].value_counts())
print(merge.isnull().sum())

#dataframe com o merge final
merge.to_csv("data/merge/alunos" + args.semestre + ".csv")

