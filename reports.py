#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import argparse
import numpy as np

#gera CSV de quantidade de alunos por semestre
def generate_amount_csv(itens):
    df = pd.DataFrame(itens, columns=['Semestre', 'Quantidade de alunos', 'Homens', 'Mulheres'])
    df.to_csv("data/reports/quantidade_de_alunos.csv")


semestres = ['20131', '20132', '20141', '20142', '20151', '20152', '20161', '20162', '20171']
dataframes = []
periodo = []
homens = []
quantidade = []
mulheres = []
bairros = []

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


raw_data = {'Semestre' : periodo, 'Quantidade de alunos' : quantidade, 'Homens' : homens, 'Mulheres' : mulheres}

generate_amount_csv(raw_data)
