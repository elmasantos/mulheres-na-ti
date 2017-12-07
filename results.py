import matplotlib.pyplot as plt
import pandas as pd 
import argparse
import numpy as np

parser = argparse.ArgumentParser(description='Script para gerar gráficos')
parser.add_argument('-s','--semestre', help='Semestre referência', required=False)

args = parser.parse_args()

semestres = args.semestre
semestres = semestres.split(',')

#gera CSV de quantidade de alunos por semestre
def generate_amount_csv(itens):
	df = pd.DataFrame(itens, columns=['Semestre', 'Quantidade de alunos', 'Homens', 'Mulheres'])
	plt.figure()
	df.plot.bar(x='Semestre')
	plt.tight_layout() 
	plt.savefig("data/resultados/plots/quantidade.png")
	plt.close()

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

def box_plot(df1, df2, column, semestre):
	fig = plt.figure()
	# Create an axes instance
	ax = fig.add_subplot(111)

	box1 = plt.boxplot([df1[column], df2[column]], notch=False, patch_artist=True)

	ax.set_xticklabels(['Mulheres', 'Homens'])

	plt.title(semestre[:4]+'.'+semestre[4])
	plt.legend()

	plt.tight_layout()
	plt.savefig("data/resultados/plots/boxplot_"+column+semestre+".png")  
	plt.close()


def bar_plot(itens, semestre):
	df = pd.DataFrame(itens, columns=['Descricao', 'Mulheres', 'Homens'])
	plt.figure()
	plt.xlabel('Status acadêmico')
	plt.ylabel('Quantidade')
	df.plot.bar(x='Descricao')
	plt.tight_layout() 
	plt.savefig("data/resultados/plots/status"+semestre+".png")
	plt.close()

dataframes = []
dataframes_completos = []
periodo = []
quantidade = []
homens = []
mulheres = []
bairros = []

##########################################################
#lendo dataframes sem repetição
for sem in semestres:
	dataframe = pd.read_csv("data/mining/tabela"+sem+".csv", sep=',')
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

###########################################################
#lendo dataframe completo com rep
for sem in semestres:
	dataframe = pd.read_csv("data/merge/merge"+sem+".csv", sep=';')
	dataframes_completos.append(dataframe)

for i, dataframe in enumerate(dataframes_completos):
	# selecionar so os dados por sexo
	mulheres_df = dataframe[dataframe.sexo == 'F']
	homens_df = dataframe[dataframe.sexo == 'M']
	#excluindo trancamento e desistencia para nao contar com 0 na media
	mulheres_df = mulheres_df[mulheres_df.descricao != 'DESISTENCIA']
	mulheres_df = mulheres_df[mulheres_df.descricao != 'TRANCADO']
	homens_df = homens_df[homens_df.descricao != 'DESISTENCIA']
	homens_df = homens_df[homens_df.descricao != 'TRANCADO']

	box_plot(mulheres_df, homens_df, 'media_final', semestres[i])
	box_plot(mulheres_df, homens_df, 'numero_total_faltas', semestres[i])


for i, dataframe in enumerate(dataframes_completos):
	# selecionar so os dados por sexo
	mulheres_df = dataframe[dataframe.sexo == 'F']
	homens_df = dataframe[dataframe.sexo == 'M']

	status_mulheres = mulheres_df.groupby(["descricao"])['sexo'].count()
	status_homens = homens_df.groupby(["descricao"])['sexo'].count()

	lista_descricao = dataframe['descricao'].unique()
	raw_data = {'Descricao' : lista_descricao, 'Mulheres' : status_mulheres, 'Homens' : status_homens}

	bar_plot(raw_data, semestres[i])
