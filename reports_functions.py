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

def generate_bairros_csv(itens):
    df = pd.DataFrame(itens, columns=['Bairro', 'Quantidade de mulheres'])
    df.to_csv("data/reports/alunas_bairros.csv")

def generate_bairro_mulheres(dataframe, semestre):
    grouped = dataframe.groupby(['bairro'])['sexo'].count()
    df = pd.DataFrame(grouped)
    df.to_csv("data/reports/bairros/alunas_bairros"+semestre+".csv")

def generate_cotistas_bairros_por_ano_csv(itens, ano):
    df = pd.DataFrame(itens, columns=['Bairro', 'Quantidade de mulheres cotistas'])
    df.to_csv("data/reports/"+ano+"_alunas_cotistas_por_bairros.csv")

def generate_racas_csv(itens):
    df = pd.DataFrame(itens, columns=['Raças', 'Quantidade de Mulheres'])
    df.to_csv("data/reports/racas_alunas.csv")