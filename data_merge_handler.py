import pandas as pd
import argparse

'''
script temporário para tratar dados
'''

#seleção de dados do dataset
def select_data(dataframe):
	for i in range(2, len(dataframe.columns)):
	
		#Seleção de dados onde registro em column_selected é igual a 'name'
		dataframe[dataframe.columns[i]] = dataframe[dataframe.columns[i]].str.upper()
		#dataframe[column2] = dataframe[column2].str.upper()
		#dataframe[column3] = dataframe[column3].str.upper()

		strings_to_repl = {',' : '', 'NOSSA SRA DA APRESENTAÇÃO' : 'NOSSA_SENHORA_DA_APRESENTACAO', 'S.G. AMARANTE' : 'SAO_GONCALO_DO_AMARANTE', 'CEARÁ - MIRIM' : 'CEARA_MIRIM', 'CEARA - MIRIM' : 'CEARA_MIRIM', 'Á' : 'A', 'Ã' : 'A', 'Â' : 'A', 'É' : 'E', 'Ẽ' : 'E', 'Ê' : 'E', 'Í' : 'I', 'Ĩ' : 'I', 'Î' : 'I', 'Ó': 'O', 'Õ' : 'O', 'Ô' : 'O', 'Ú' : 'U', 'Ũ' : 'U', 'Û' : 'U', 'Ç' : 'C', '-' : '_', ' ' : '_', '__' : '_', 'NSA._SENHORA_DA_APRESENTACAO' : 'NOSSA_SENHORA_DA_APRESENTACAO', '\'' : ''}

		dataframe = dataframe.replace({dataframe.columns[i] : strings_to_repl}, regex=True)

		#dataframe = dataframe.replace({column2 : strings_to_repl}, regex=True)

		#dataframe = dataframe.replace({column3 : strings_to_repl}, regex=True)

	return dataframe


parser = argparse.ArgumentParser(description='Script para tratar tabelas')
parser.add_argument('-f','--file', help='Tabela a ser tratada', required=True)
parser.add_argument('-s','--semestre', help='Semestre referência', required=False)

args = parser.parse_args()

semestre = args.semestre
discentes = args.file

discentes_df = pd.read_csv(discentes, sep=',')
discentes_df = discentes_df.astype(str)

discentes_df.drop('Unnamed: 0', axis=1, inplace=True)


discentes_df = select_data(discentes_df)


discentes_df.to_csv("data/temp/merge"+semestre+".csv", sep=';', index=False)
