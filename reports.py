#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import argparse
import numpy as np
import reports_functions

#variaveis
semestres = ['20131', '20132', '20141', '20142', '20151', '20152', '20161', '20162', '20171']
dataframes = []
periodo = []
homens = []
quantidade = []
mulheres = []
cotistas_mulheres = []
cotistas_homens = []
zonas_grouped = []
racas_grouped = []
cotistas_grouped = []

#lendo dataframes
for sem in semestres:
    dataframe = pd.read_csv("data/merge/alunos"+sem+".csv", sep=',')
    dataframes.append(dataframe)

#coletando dados
for i, dataframe in enumerate(dataframes):
    periodo.append(semestres[i][:4]+"."+semestres[i][4])
    quantidade.append(len(dataframe['id_discente']))
    homens.append(len(dataframe[dataframe.sexo == 'M']))
    mulheres.append(len(dataframe[dataframe.sexo == 'F']))

    #separando dataframes por sexo
    mulheres_df = dataframe[dataframe.sexo == 'F']
    homens_df = dataframe[dataframe.sexo == 'M']

    cotistas_mulheres.append(len(mulheres_df[mulheres_df['cotista'] == 'T']))
    cotistas_homens.append(len(homens_df[homens_df['cotista'] == 'T']))

    reports_functions.generate_bairro_mulheres(mulheres_df, semestres[i][:4]+"."+semestres[i][4])

    #adiciona coluna de zonas
    dataframe['zona'] = dataframe.apply(lambda row: reports_functions.zonas_natal(row), axis=1)
    #gera relatorios de zonas por semestre
    reports_functions.generate_zonas_mulheres(dataframe[dataframe.sexo == 'F'], semestres[i][:4]+"."+semestres[i][4])

#gera lista de dataframes de zonas
for dataframe in dataframes:
    dataframe = dataframe[dataframe.sexo == 'F']
    #zonas_grouped.append(dataframe.groupby(['zona', 'sexo']).count())
    zonas_grouped.append(pd.DataFrame({'quantidade' : dataframe.groupby( [ "zona"] ).size()}).reset_index())
    racas_grouped.append(pd.DataFrame({'quantidade' : dataframe.groupby( [ "raca"] ).size()}).reset_index())
    cotistas_grouped.append(pd.DataFrame({'quantidade' : dataframe.groupby( [ "cotista"] ).size()}).reset_index())

#gera dataframe com total de zonas
racas = pd.concat(racas_grouped)
racas['Total'] = racas.groupby(['raca'])['quantidade'].transform('sum')
racas.drop_duplicates(subset='raca', keep='first', inplace=True)
racas.drop(['quantidade'], axis=1, inplace=True)

#relatorio de total de raças
reports_functions.generate_total_racas_mulheres(racas)

#gera dataframe com total de cotistas
cotistas = pd.concat(cotistas_grouped)
cotistas['Total'] = cotistas.groupby(['cotista'])['quantidade'].transform('sum')
cotistas.drop_duplicates(subset='cotista', keep='first', inplace=True)
cotistas.drop(['quantidade'], axis=1, inplace=True)

#relatorio de total de cotistas
reports_functions.generate_mulheres_cotistas_csv(cotistas)

#gera dataframe com total de zonas
zonas = pd.concat(zonas_grouped)
zonas['Total'] = zonas.groupby(['zona'])['quantidade'].transform('sum')
zonas.drop_duplicates(subset='zona', keep='first', inplace=True)
zonas.drop(['quantidade'], axis=1, inplace=True)


#relatorio de total de zonas
reports_functions.generate_total_zonas_mulheres(zonas)

#relatorio cotistas
raw_data = {'Semestre' : periodo, 'Homens cotistas' : cotistas_homens, 'Mulheres cotistas' : cotistas_mulheres}

reports_functions.generate_cotistas_csv(raw_data)

#relatorio quantidades
raw_data = {'Semestre' : periodo, 'Quantidade de alunos' : quantidade, 'Homens' : homens, 'Mulheres' : mulheres}

reports_functions.generate_amount_csv(raw_data)
