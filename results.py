import matplotlib.pyplot as plt 
import pandas as pd 
import argparse


parser = argparse.ArgumentParser(description='Script para gerar gráficos')
parser.add_argument('-s','--semestre', help='Semestre referência', required=False)

args = parser.parse_args()

#gera CSV de quantidade de alunos por semestre
def generate_amount_csv(itens):
	df = pd.DataFrame(itens, columns=['Semestre', 'Quantidade de alunos', 'Homens', 'Mulheres'])
	df.to_csv("data/resultados/quantidade_pessoas_ativas.csv", sep=';', index=False)

def statistic():
	pass

semestres = args.semestre
semestres = semestres.split(',')

dataframes = []
periodo = []
quantidade = []
homens = []
mulheres = []
bairro = []

#lendo dataframes
for sem in semestres:
	dataframe = pd.read_csv("data/merge/merge"+sem+"_sem_rep.csv", sep=';')
	dataframes.append(dataframe)

#coletando dados
for i, dataframe in enumerate(dataframes):
	periodo.append(semestres[i][:4]+"."+semestres[i][4])
	quantidade.append(len(dataframe))
	homens.append(len(dataframe[dataframe.sexo == 'M']))
	mulheres.append(len(dataframe[dataframe.sexo == 'F']))

raw_data = {'Semestre' : periodo, 'Quantidade de alunos' : quantidade, 'Homens' : homens, 'Mulheres' : mulheres}
generate_amount_csv(raw_data)

