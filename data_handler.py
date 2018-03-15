#!/usr/bin/python                                                                        
# -*- coding: utf-8 -*-
import pandas as pd

#Funções para facilitar manipulação de dados


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
