#!/usr/bin/python                                                                        
# -*- coding: utf-8 -*-

import pandas as pd 

colnames =["discente", "sexo", "nota_final", "cotista", "cep", "descricao"]
discentes_dataset = pd.read_csv('data/discente.csv', names = colnames)

id_aluno = discentes_dataset.discente.tolist()
sexo = discentes_dataset.sexo.tolist()
nota_final = discentes_dataset.nota_final.tolist()
cotista = discentes_dataset.cotista.tolist()
cep = discentes_dataset.cep.tolist()
descricao = discentes_dataset.descricao.tolist()

tamanho = len(id_aluno)