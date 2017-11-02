#!/usr/bin/python                                                                        
# -*- coding: utf-8 -*-

import pandas as pd 

colnames =["discente", "sexo", "nota_final", "cotista", "cep", "descricao"]
discentes_dataset = pd.read_csv('data/discente.csv', names = colnames)

#novo dataframe sem missing data
dataset_no_missing = discentes_dataset.dropna()
#criando novo arquivo csv sem missing data
dataset_no_missing.to_csv("data/discente_no_missing.csv")

id_aluno = dataset_no_missing.discente.tolist()
sexo = dataset_no_missing.sexo.tolist()
nota_final = dataset_no_missing.nota_final.tolist()
cotista = dataset_no_missing.cotista.tolist()
cep = dataset_no_missing.cep.tolist()
descricao = dataset_no_missing.descricao.tolist()

tamanho = len(id_aluno)
print(tamanho)