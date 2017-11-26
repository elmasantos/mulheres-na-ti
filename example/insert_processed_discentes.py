#!/usr/bin/python                                                                        
# -*- coding: utf-8 -*-

import pandas as pd 
import MySQLdb


#leitura de arquivo
discentes_df = pd.read_csv('../data/merge/merge20141.csv')
discentes_df2 = pd.read_csv('../data/merge/merge20142.csv')
discentes_df3 = pd.read_csv('../data/merge/merge20151.csv')
discentes_df4 = pd.read_csv('../data/merge/merge20152.csv')
discentes_df5 = pd.read_csv('../data/merge/merge20161.csv')
discentes_df6 = pd.read_csv('../data/merge/merge20162.csv')

#dividindo as colulas dos datasets em arrays
id_discente = discentes_df.id_discente.tolist()
sexo = discentes_df.sexo.tolist()
data_nascimento = discentes_df.data_nascimento.tolist()
raca = discentes_df.raca.tolist()
estado_origem = discentes_df.estado_origem.tolist()
cidade_origem = discentes_df.cidade_origem.tolist()
estado = discentes_df.estado.tolist()
municipio = discentes_df.municipio.tolist()
bairro = discentes_df.bairro.tolist()
nivel_ensino = discentes_df.nivel_ensino.tolist()
forma_ingresso = discentes_df.forma_ingresso.tolist()
ano_ingresso = discentes_df.ano_ingresso.tolist()
periodo_ingresso = discentes_df.periodo_ingresso.tolist()
cotista = discentes_df.cotista.tolist()

id_discente2 = discentes_df2.id_discente.tolist()
sexo2 = discentes_df2.sexo.tolist()
data_nascimento2 = discentes_df2.data_nascimento.tolist()
raca2 = discentes_df2.raca.tolist()
estado_origem2 = discentes_df2.estado_origem.tolist()
cidade_origem2 = discentes_df2.cidade_origem.tolist()
estado2 = discentes_df2.estado.tolist()
municipio2 = discentes_df2.municipio.tolist()
bairro2 = discentes_df2.bairro.tolist()
nivel_ensino2 = discentes_df2.nivel_ensino.tolist()
forma_ingresso2 = discentes_df2.forma_ingresso.tolist()
ano_ingresso2 = discentes_df2.ano_ingresso.tolist()
periodo_ingresso2 = discentes_df2.periodo_ingresso.tolist()
cotista2 = discentes_df2.cotista.tolist()

id_discente3 = discentes_df3.id_discente.tolist()
sexo3 = discentes_df3.sexo.tolist()
data_nascimento3 = discentes_df3.data_nascimento.tolist()
raca3 = discentes_df3.raca.tolist()
estado_origem3 = discentes_df3.estado_origem.tolist()
cidade_origem3 = discentes_df3.cidade_origem.tolist()
estado3 = discentes_df3.estado.tolist()
municipio3 = discentes_df3.municipio.tolist()
bairro3 = discentes_df3.bairro.tolist()
nivel_ensino3 = discentes_df3.nivel_ensino.tolist()
forma_ingresso3 = discentes_df3.forma_ingresso.tolist()
ano_ingresso3 = discentes_df3.ano_ingresso.tolist()
periodo_ingresso3 = discentes_df3.periodo_ingresso.tolist()
cotista3 = discentes_df3.cotista.tolist()

id_discente4 = discentes_df4.id_discente.tolist()
sexo4 = discentes_df4.sexo.tolist()
data_nascimento4 = discentes_df4.data_nascimento.tolist()
raca4 = discentes_df4.raca.tolist()
estado_origem4 = discentes_df4.estado_origem.tolist()
cidade_origem4 = discentes_df4.cidade_origem.tolist()
estado4 = discentes_df4.estado.tolist()
municipio4 = discentes_df4.municipio.tolist()
bairro4 = discentes_df4.bairro.tolist()
nivel_ensino4 = discentes_df4.nivel_ensino.tolist()
forma_ingresso4 = discentes_df4.forma_ingresso.tolist()
ano_ingresso4 = discentes_df4.ano_ingresso.tolist()
periodo_ingresso4 = discentes_df4.periodo_ingresso.tolist()
cotista4 = discentes_df4.cotista.tolist()

id_discente5 = discentes_df5.id_discente.tolist()
sexo5 = discentes_df5.sexo.tolist()
data_nascimento5 = discentes_df5.data_nascimento.tolist()
raca5 = discentes_df5.raca.tolist()
estado_origem5 = discentes_df5.estado_origem.tolist()
cidade_origem5 = discentes_df5.cidade_origem.tolist()
estado5 = discentes_df5.estado.tolist()
municipio5 = discentes_df5.municipio.tolist()
bairro5 = discentes_df5.bairro.tolist()
nivel_ensino5 = discentes_df5.nivel_ensino.tolist()
forma_ingresso5 = discentes_df5.forma_ingresso.tolist()
ano_ingresso5 = discentes_df5.ano_ingresso.tolist()
periodo_ingresso5 = discentes_df5.periodo_ingresso.tolist()
cotista5 = discentes_df5.cotista.tolist()

id_discente6 = discentes_df6.id_discente.tolist()
sexo6 = discentes_df6.sexo.tolist()
data_nascimento6 = discentes_df6.data_nascimento.tolist()
raca6 = discentes_df6.raca.tolist()
estado_origem6 = discentes_df6.estado_origem.tolist()
cidade_origem6 = discentes_df6.cidade_origem.tolist()
estado6 = discentes_df6.estado.tolist()
municipio6 = discentes_df6.municipio.tolist()
bairro6 = discentes_df6.bairro.tolist()
nivel_ensino6 = discentes_df6.nivel_ensino.tolist()
forma_ingresso6 = discentes_df6.forma_ingresso.tolist()
ano_ingresso6 = discentes_df6.ano_ingresso.tolist()
periodo_ingresso6 = discentes_df6.periodo_ingresso.tolist()
cotista6 = discentes_df6.cotista.tolist()

print(len(id_discente))
print(len(sexo2))
print(len(data_nascimento3))
print(len(raca4))
print(len(estado_origem5))
print(len(cidade_origem6))


# Open database connection
db = MySQLdb.connect("localhost","root","123","mulheres_na_ti" )

# prepare a cursor object using cursor() method and insert data
cursor = db.cursor()

#query para inserir os arrays obtidos nas tabelas
query = "INSERT INTO alunos_bti_2014_1 (id_discente, sexo, data_nascimento, raca, estado_origem, cidade_origem, estado, municipio, bairro, nivel_ensino, forma_ingresso, ano_ingresso, periodo_ingresso, cotista ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
query2 = "INSERT INTO alunos_bti_2014_2 (id_discente, sexo, data_nascimento, raca, estado_origem, cidade_origem, estado, municipio, bairro, nivel_ensino, forma_ingresso, ano_ingresso, periodo_ingresso, cotista ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
query3 = "INSERT INTO alunos_bti_2015_1 (id_discente, sexo, data_nascimento, raca, estado_origem, cidade_origem, estado, municipio, bairro, nivel_ensino, forma_ingresso, ano_ingresso, periodo_ingresso, cotista ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
query4 = "INSERT INTO alunos_bti_2015_2 (id_discente, sexo, data_nascimento, raca, estado_origem, cidade_origem, estado, municipio, bairro, nivel_ensino, forma_ingresso, ano_ingresso, periodo_ingresso, cotista ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
query5 = "INSERT INTO alunos_bti_2016_1 (id_discente, sexo, data_nascimento, raca, estado_origem, cidade_origem, estado, municipio, bairro, nivel_ensino, forma_ingresso, ano_ingresso, periodo_ingresso, cotista ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
query6 = "INSERT INTO alunos_bti_2016_2 (id_discente, sexo, data_nascimento, raca, estado_origem, cidade_origem, estado, municipio, bairro, nivel_ensino, forma_ingresso, ano_ingresso, periodo_ingresso, cotista ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

#funcao para inserir a tabela no banco
cursor.executemany(query, [(id_discente[i], sexo[i], data_nascimento[i], raca[i], estado_origem[i], cidade_origem[i], estado[i], municipio[i], bairro[i], nivel_ensino[i], forma_ingresso[i], ano_ingresso[i], periodo_ingresso[i], cotista[i]) for i in range(0,len(discentes_df))])
cursor.executemany(query2, [(id_discente2[i], sexo2[i], data_nascimento2[i], raca2[i], estado_origem2[i], cidade_origem2[i], estado2[i], municipio2[i], bairro2[i], nivel_ensino2[i], forma_ingresso2[i], ano_ingresso2[i], periodo_ingresso2[i], cotista2[i]) for i in range(0,len(discentes_df2))])
cursor.executemany(query3, [(id_discente3[i], sexo3[i], data_nascimento3[i], raca3[i], estado_origem3[i], cidade_origem3[i], estado3[i], municipio3[i], bairro3[i], nivel_ensino3[i], forma_ingresso3[i], ano_ingresso3[i], periodo_ingresso3[i], cotista3[i]) for i in range(0,len(discentes_df3))])
cursor.executemany(query4, [(id_discente4[i], sexo4[i], data_nascimento4[i], raca4[i], estado_origem4[i], cidade_origem4[i], estado4[i], municipio4[i], bairro4[i], nivel_ensino4[i], forma_ingresso4[i], ano_ingresso4[i], periodo_ingresso4[i], cotista4[i]) for i in range(0,len(discentes_df4))])
cursor.executemany(query5, [(id_discente5[i], sexo5[i], data_nascimento5[i], raca5[i], estado_origem5[i], cidade_origem5[i], estado5[i], municipio5[i], bairro5[i], nivel_ensino5[i], forma_ingresso5[i], ano_ingresso5[i], periodo_ingresso5[i], cotista5[i]) for i in range(0,len(discentes_df5))])
cursor.executemany(query6, [(id_discente6[i], sexo6[i], data_nascimento6[i], raca6[i], estado_origem6[i], cidade_origem6[i], estado6[i], municipio6[i], bairro6[i], nivel_ensino6[i], forma_ingresso6[i], ano_ingresso6[i], periodo_ingresso6[i], cotista6[i]) for i in range(0,len(discentes_df6))])

#save mudanças
db.commit()

# disconnect from server    
db.close()
