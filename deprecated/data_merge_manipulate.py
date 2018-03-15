import pandas as pd 
import argparse 
import datetime as DT

def faixa_salarial(row):
	if row['renda'] <= 1000:
		return 'ATE_1000_REAIS'
	elif row['renda'] > 1000 and row['renda'] <= 2000:
		return 'MAIOR_QUE_1000_ATE_2000'
	elif row['renda'] > 2000 and row['renda'] <= 3000:
		return 'MAIOR_QUE_2000_ATE_3000'
	elif row['renda'] > 3000 and row['renda'] <= 4000:
		return 'MAIOR_QUE_3000_ATE_4000'
	else:
		return 'MAIOR_QUE_4000'

def idade(row):
	return (pd.to_datetime('today').year-pd.to_datetime(row['data_nascimento']).year)

def faixa_etaria(row):
	if row['idade'] <= 20:
		return 'ATE_20_ANOS'
	elif row['idade'] > 20 and row['idade'] <= 25:
		return 'MAIOR_QUE_20_ATE_25'
	elif row['idade'] > 25 and row['idade'] <= 35:
		return 'MAIOR_QUE_25_ATE_35'
	elif row['idade'] > 35 and row['idade'] <= 45:
		return 'MAIOR_QUE_35_ATE_45'
	else:
		return 'MAIOR_QUE_45'

parser = argparse.ArgumentParser(description='Script para manipular tabelas de merge')
parser.add_argument('-f','--file', help='Tabela a ser tratada', required=True)
parser.add_argument('-s','--semestre', help='Semestre referência', required=False)

args = parser.parse_args()

semestre = args.semestre
discentes = args.file

discentes_df = pd.read_csv(discentes, sep=';')

discentes_df['faixa_salarial'] = discentes_df.apply(lambda row: faixa_salarial(row), axis=1)

discentes_df['data_nascimento'] = discentes_df['data_nascimento'].str.replace('_', '/')

discentes_df['data_nascimento'] = pd.to_datetime(discentes_df['data_nascimento'])

discentes_df['idade'] = discentes_df.apply(lambda row: idade(row), axis=1)

discentes_df['faixa_etaria'] = discentes_df.apply(lambda row: faixa_etaria(row), axis=1)

discentes_df.to_csv("data/mining/tabela"+semestre+".csv", sep=',', index=False)