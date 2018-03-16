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

#deleta colunas selecionadas
def drop_columns(dataframe, *columns):
    dataframe.drop([*columns], axis=1, inplace=True)

#preenche campos vazios
def fill_empty_fields(dataframe):
    values = {'estado_origem' : 'NAO INFORMADO', 'cidade_origem' : 'NAO INFORMADO',
    'estado' : 'NAO INFORMADO', 'municipio' : 'NAO INFORMADO', 'bairro' : 'NAO INFORMADO'}
    dataframe.fillna(value=values, inplace=True)

    return dataframe

#padroniza nomes de bairros
def replace_to_standardize(dataframe):
    #converte dados do dataframe em strings
    dataframe = dataframe.astype(str)

    for i in range(2, len(dataframe.columns)):
    
        #Seleção de dados onde registro em column_selected é igual a 'name'
        dataframe[dataframe.columns[i]] = dataframe[dataframe.columns[i]].str.upper()
        
        strings_to_repl = {',' : '', 'NOSSA SRA DA APRESENTAÇÃO' : 'NOSSA_SENHORA_DA_APRESENTACAO', 'S.G. AMARANTE' : 'SAO_GONCALO_DO_AMARANTE', 'CEARÁ - MIRIM' : 'CEARA_MIRIM', 'CEARA - MIRIM' : 'CEARA_MIRIM', 'Á' : 'A', 'Ã' : 'A', 'Â' : 'A', 'É' : 'E', 'Ẽ' : 'E', 'Ê' : 'E', 'Í' : 'I', 'Ĩ' : 'I', 'Î' : 'I', 'Ó': 'O', 'Õ' : 'O', 'Ô' : 'O', 'Ú' : 'U', 'Ũ' : 'U', 'Û' : 'U', 'Ç' : 'C', '-' : '_', ' ' : '_', '__' : '_', 'NSA._SENHORA_DA_APRESENTACAO' : 'NOSSA_SENHORA_DA_APRESENTACAO', '\'' : ''}

        dataframe = dataframe.replace({dataframe.columns[i] : strings_to_repl}, regex=True)

    return dataframe
