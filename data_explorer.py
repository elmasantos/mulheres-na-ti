import pandas as pd
import argparse

'''
script temporário para tratar dados
'''

#seleção de dados do dataset
def select_data(dataframe, column1, column2, column3):
	#Seleção de dados onde registro em column_selected é igual a 'name'
	dataframe[column1] = dataframe[column1].str.upper()
	dataframe[column2] = dataframe[column2].str.upper()
	dataframe[column3] = dataframe[column3].str.upper()

	strings_to_repl = {'NOSSA SRA DA APRESENTAÇÃO' : 'NOSSA_SENHORA_DA_APRESENTACAO', 'S.G. AMARANTE' : 'SAO_GONCALO_DO_AMARANTE', 'CEARÁ - MIRIM' : 'CEARA_MIRIM', 'CEARA - MIRIM' : 'CEARA_MIRIM', 'Á' : 'A', 'Ã' : 'A', 'Â' : 'A', 'É' : 'E', 'Ẽ' : 'E', 'Ê' : 'E', 'Í' : 'I', 'Ĩ' : 'I', 'Î' : 'I', 'Ó': 'O', 'Õ' : 'O', 'Ô' : 'O', 'Ú' : 'U', 'Ũ' : 'U', 'Û' : 'U', 'Ç' : 'C', '-' : '_', ' ' : '_', '__' : '_', 'NSA._SENHORA_DA_APRESENTACAO' : 'NOSSA_SENHORA_DA_APRESENTACAO', '\'' : ''}

	dataframe = dataframe.replace({column1 : strings_to_repl}, regex=True)

	dataframe = dataframe.replace({column2 : strings_to_repl}, regex=True)

	dataframe = dataframe.replace({column3 : strings_to_repl}, regex=True)
	
	dataframe = dataframe[['id_discente', column1, column2, column3]]

	return dataframe


parser = argparse.ArgumentParser(description='Script para tratar tabelas')
parser.add_argument('-f','--file', help='Tabela a ser tratada', required=True)
parser.add_argument('-s','--semestre', help='Semestre referência', required=False)

args = parser.parse_args()

semestre = args.semestre
discentes = args.file

discentes_df = pd.read_csv(discentes, sep=',')

result1_df = select_data(discentes_df, 'sexo', 'municipio', 'descricao')
result2_df = select_data(discentes_df, 'raca', 'bairro', 'descricao')
result3_df = select_data(discentes_df, 'municipio', 'cotista', 'descricao')

result1_df.to_csv("data/temp/sexo_mun_desc"+semestre+".csv", sep=';', index=False)
result2_df.to_csv("data/temp/raca_bairro_desc"+semestre+".csv", sep=';', index=False)
result3_df.to_csv("data/temp/mun_cot_desc"+semestre+".csv", sep=';', index=False)