#!/usr/bin/python                                                                        
# -*- coding: utf-8 -*-

import pandas as pd 
import MySQLdb

colnames =["discente", "sexo", "nota_final", "cotista", "cep", "descricao"]
discentes_dataset = pd.read_csv('data/discente_no_missing.csv', names = colnames)

id_aluno = discentes_dataset.discente.tolist()
sexo = discentes_dataset.sexo.tolist()
nota_final = discentes_dataset.nota_final.tolist()
cotista = discentes_dataset.cotista.tolist()
cep = discentes_dataset.cep.tolist()
descricao = discentes_dataset.descricao.tolist()

# Open database connection
db = MySQLdb.connect("localhost","root","123","mulheres_na_ti" )

# prepare a cursor object using cursor() method and insert data
cursor = db.cursor()

query = "INSERT INTO cotistas (discente, sexo, nota_final, cotista, cep, descricao) VALUES (%s, %s, %s, %s, %s, %s)"

cursor.executemany(query, [(id_aluno[i], sexo[i], nota_final[i], cotista[i], cep[i], descricao[i]) for i in range(2,27184)])

#save mudanças
db.commit()

# disconnect from server    
db.close()

print(sexo[3])