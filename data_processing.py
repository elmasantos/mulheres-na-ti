#!/usr/bin/python                                                                        
# -*- coding: utf-8 -*-

import pandas as pd 

#leitura de arquivo
discentes_df = pd.read_csv('data/discentes.csv')

#Seleção de dados onde registros na coluna id_discente não são nulos
df_no_missing = discentes_df[pd.notnull(discentes_df['id_discente'])]

#Seleção de dados onde o nível de ensino é graduação
df_no_missing = df_no_missing[df_no_missing.nivel_ensino == 'GRADUAÇÃO']

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
df_no_missing.to_csv("data/discentes_processed.csv")
