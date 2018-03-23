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

    #coletando quantidade de cotistas por sexo
    cotistas_mulheres.append(len(mulheres_df[mulheres_df['cotista'] == 'T']))
    cotistas_homens.append(len(homens_df[homens_df['cotista'] == 'T']))

    #gera relatorio de bairros das mulheres ingressantes por semestre
    reports_functions.generate_bairro_mulheres(mulheres_df, semestres[i][:4]+"."+semestres[i][4])

    #adiciona coluna de zonas
    dataframe['zona'] = dataframe.apply(lambda row: reports_functions.zonas_natal(row), axis=1)

    #gera relatorios de zonas das mulheres ingressantes por semestre
    reports_functions.generate_zonas_mulheres(dataframe[dataframe.sexo == 'F'], semestres[i][:4]+"."+semestres[i][4])

#gera lista de dataframes desejados
zonas_grouped = reports_functions.generate_list_of_dataframes(dataframes, 'zona')
racas_grouped = reports_functions.generate_list_of_dataframes(dataframes, 'raca')
cotistas_grouped = reports_functions.generate_list_of_dataframes(dataframes, 'cotista')


#gera dataframe com total de zonas
racas = reports_functions.generate_total_dataframe(racas_grouped, 'raca')
#relatorio de total de raças
reports_functions.generate_total_racas_mulheres(racas)

#gera dataframe com total de cotistas
cotistas = reports_functions.generate_total_dataframe(cotistas_grouped, 'cotista')
#relatorio de total de cotistas
reports_functions.generate_mulheres_cotistas_csv(cotistas)

#gera dataframe com total de zonas
zonas = reports_functions.generate_total_dataframe(zonas_grouped, 'zona')
#relatorio de total de zonas
reports_functions.generate_total_zonas_mulheres(zonas)

#relatorio cotistas
raw_data = {'Semestre' : periodo, 'Homens cotistas' : cotistas_homens, 'Mulheres cotistas' : cotistas_mulheres}

reports_functions.generate_cotistas_csv(raw_data)

#relatorio quantidades
raw_data = {'Semestre' : periodo, 'Quantidade de alunos' : quantidade, 'Homens' : homens, 'Mulheres' : mulheres}

reports_functions.generate_amount_csv(raw_data)
