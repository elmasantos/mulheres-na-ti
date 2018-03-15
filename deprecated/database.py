#!/usr/bin/python                                                                        
# -*- coding: utf-8 -*-

import pandas as pd 
import MySQLdb


#leitura de arquivo
#colnames =["id_discente", "sexo", "cep", "cotista", "forma_ingresso", "nivel_ensino"]
discentes_df = pd.read_csv('data/processed/discentes_processed.csv')

id_discente = discentes_df.id_discente.tolist()
sexo = discentes_df.sexo.tolist()
cep = discentes_df.cep.tolist()
cotista = discentes_df.cotista.tolist()
forma_ingresso = discentes_df.forma_ingresso.tolist()
nivel_ensino = discentes_df.nivel_ensino.tolist()

# Open database connection
db = MySQLdb.connect("localhost","root","123","mulheres_na_ti" )

# prepare a cursor object using cursor() method and insert data
cursor = db.cursor()

query = "INSERT INTO cotistas (discente, sexo, cep, cotista, forma_ingresso, nivel_ensino) VALUES (%s, %s, %s, %s, %s, %s)"

cursor.executemany(query, [(id_discente[i], sexo[i], cep[i], cotista[i], forma_ingresso[i], nivel_ensino[i]) for i in range(0,len(discentes_df))])

#save mudanças
db.commit()

# disconnect from server    
db.close()
