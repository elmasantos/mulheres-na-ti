#!/usr/bin/python                                                                        
# -*- coding: utf-8 -*-

import pandas as pd 
import MySQLdb


#leitura de arquivo
discentes_df = pd.read_csv('../data/processed/matriculas_20161_processed.csv')


id_discente = discentes_df.discente.tolist()
id_turma = discentes_df.id_turma.tolist()
id_curso = discentes_df.id_curso.tolist()
unidade = discentes_df.unidade.tolist()
nota = discentes_df.nota.tolist()
reposicao = discentes_df.reposicao.tolist()
media = discentes_df.media_final.tolist()
faltas = discentes_df.numero_total_faltas.tolist()
descricao = discentes_df.descricao.tolist()

# Open database connection
db = MySQLdb.connect("localhost","root","123","mulheres_na_ti" )

# prepare a cursor object using cursor() method and insert data
cursor = db.cursor()

query = "INSERT INTO matricula2016_1 (id_turma, discente, id_curso, unidade, nota, reposicao,media_final, numero_total_faltas, descricao ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

cursor.executemany(query, [(id_turma[i], id_discente[i], id_curso[i], unidade[i], nota[i], reposicao[i], media[i], faltas[i], descricao[i]) for i in range(0,len(discentes_df))])

#save mudanças
db.commit()

# disconnect from server    
db.close()
