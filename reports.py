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
bairros_grouped = []
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

    mulheres_df['zona'] = mulheres_df.apply(lambda row: reports_functions.zonas_natal(row), axis=1)
    reports_functions.generate_zonas_mulheres(mulheres_df, semestres[i][:4]+"."+semestres[i][4])


#relatorio cotistas
raw_data = {'Semestre' : periodo, 'Homens cotistas' : cotistas_homens, 'Mulheres cotistas' : cotistas_mulheres}

#reports_functions.generate_cotistas_csv(raw_data)

#relatorio quantidades
raw_data = {'Semestre' : periodo, 'Quantidade de alunos' : quantidade, 'Homens' : homens, 'Mulheres' : mulheres}

#reports_functions.generate_amount_csv(raw_data)

#relatorio bairros

#raw_data = {'Bairro' : bairros, 'Quantidade de mulheres' : mulheres}

#reports_functions.generate_bairros_csv(raw_data)