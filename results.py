import matplotlib.pyplot as plt
import pandas as pd 
import argparse


parser = argparse.ArgumentParser(description='Script para gerar gráficos')
parser.add_argument('-s','--semestre', help='Semestre referência', required=False)

args = parser.parse_args()

#gera CSV de quantidade de alunos por semestre
def generate_amount_csv(itens):
	df = pd.DataFrame(itens, columns=['Semestre', 'Quantidade de alunos', 'Homens', 'Mulheres'])
	plt.figure()
	df.plot.bar(x='Semestre')
	plt.show()
	#df.to_csv("data/resultados/quantidade_pessoas_ativas.csv", sep=';', index=False)

def generate_bairro_mulheres(dataframe, semestre):
	dataframe = dataframe[dataframe.sexo == 'F']
	grouped = dataframe.groupby(['bairro'])['sexo'].count()
	#plt.figure()
	#grouped.plot.bar(title=semestre +" - Quantidade de mulheres x bairros")
	#plt.show()
	df = pd.DataFrame(grouped, columns=['sexo', 'bairro'])
	#grouped.to_csv("data/resultados/mulheres_bairro"+semestre+".csv", sep=';', index=False)

def generate_cidade_mulheres(dataframe, semestre):
	dataframe = dataframe[dataframe.sexo == 'F']
	grouped = dataframe.groupby(['cidade_origem'])['sexo'].count()
	#plt.figure()
	#grouped.plot.bar(title=semestre +" - Quantidade de mulheres x cidade de origem")
#	plt.show()


semestres = args.semestre
semestres = semestres.split(',')

dataframes = []
periodo = []
quantidade = []
homens = []
mulheres = []
bairros = []

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

	generate_bairro_mulheres(dataframe, semestres[i])
	generate_cidade_mulheres(dataframe, semestres[i])


raw_data = {'Semestre' : periodo, 'Quantidade de alunos' : quantidade, 'Homens' : homens, 'Mulheres' : mulheres}
generate_amount_csv(raw_data)
