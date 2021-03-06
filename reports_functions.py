#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd

#gera CSV de quantidade de alunos por semestre
def generate_amount_csv(itens):
    df = pd.DataFrame(itens, columns=['Semestre', 'Quantidade de alunos', 'Homens', 'Mulheres'])
    df.to_csv("data/reports/quantidade_de_alunos.csv")

def generate_cotistas_csv(itens):
    df = pd.DataFrame(itens, columns=['Semestre', 'Homens cotistas', 'Mulheres cotistas'])
    df.to_csv("data/reports/alunos_cotistas.csv")

def generate_mulheres_cotistas_csv(itens):
    df = pd.DataFrame(itens, columns=['cotista', 'Total'])
    df.to_csv("data/reports/mulheres_cotistas_e_nao_cotistas.csv")

def generate_bairro_mulheres(dataframe, semestre):
    grouped = dataframe.groupby(['bairro'])['sexo'].count()
    df = pd.DataFrame(grouped)
    df.to_csv("data/reports/bairros/alunas_bairros"+semestre+".csv")

def generate_zonas_mulheres(dataframe, semestre):
    grouped = dataframe.groupby(['zona'])['sexo'].count()
    df = pd.DataFrame(grouped)
    df.to_csv("data/reports/zonas/alunas_zonas"+semestre+".csv")

def generate_total_zonas_mulheres(dataframe):
    df = pd.DataFrame(dataframe)
    df.to_csv("data/reports/zonas/alunas_total_zonas.csv")

def generate_total_racas_mulheres(dataframe):
    df = pd.DataFrame(dataframe)
    df.to_csv("data/reports/racas/alunas_total_racas.csv")

#gera lista de dataframes de acordo com coluna desejada
def generate_list_of_dataframes(dataframes, column):
    data_grouped = []
    for dataframe in dataframes:
        dataframe = dataframe[dataframe.sexo == 'F']

        data_grouped.append(pd.DataFrame({'quantidade' : dataframe.groupby( [ column] ).size()}).reset_index())

    return data_grouped

def generate_total_dataframe(data_grouped, column):
    data_total = pd.concat(data_grouped)
    data_total['Total'] = data_total.groupby([column])['quantidade'].transform('sum')
    data_total.drop_duplicates(subset=column, keep='first', inplace=True)
    data_total.drop(['quantidade'], axis=1, inplace=True)
    return data_total

def zonas_natal(row):
    leste = ['SANTOS_REIS', 'ROCAS', 'RIBEIRA', 'PRAIA_DO_MEIO', 'CIDADE_ALTA', 'PETROPOLIS', 'AREIA_PRETA', 'MAE_LUÍZA', 'ALECRIM', 'BARRO_VERMELHO', 'TIROL', 'LAGOA_SECA']
    norte = ['LAGOA_AZUL', 'PAJUCARA', 'POTENGI', 'REDINHA', 'NOSSA_SENHORA_DA_APRESENTACAO', 'IGAPO', 'SALINAS']
    oeste = ['FELIPE_CAMARAO', 'CIDADE_DA_ESPERANCA', 'PLANALTO', 'CIDADE_NOVA', 'GUARAPES', 'QUINTAS', 'NORDESTE', 'DIX_SEPT_ROSADO', 'BOM_PASTOR' , 'NOSSA_SENHORA_DE_NAZARE']
    sul = ['NEOPOLIS', 'PONTA_NEGRA', 'NOVA_DESCOBERTA', 'LAGOA_NOVA','CANDELARIA', 'CAPIM_MACIO', 'PITIMBU']

    if row['bairro'] in leste:
        return 'ZONA_LESTE'
    elif row['bairro'] in norte:
        return 'ZONA_NORTE'
    elif row['bairro'] in oeste:
        return 'ZONA_OESTE'
    elif row['bairro'] in sul:
        return 'ZONA_SUL'
