#!/usr/bin/python                                                                        
# -*- coding: utf-8 -*-

import pandas as pd 
import MySQLdb


#leitura de arquivo
discentes_df = pd.read_csv('../data/processed/matriculas_20161_processed.csv')
discentes_df1 = pd.read_csv('../data/processed/matriculas_20162_processed.csv')
discentes_df2 = pd.read_csv('../data/processed/matriculas_20151_processed.csv')
discentes_df3 = pd.read_csv('../data/processed/matriculas_20152_processed.csv')
discentes_df4 = pd.read_csv('../data/processed/matriculas_20141_processed.csv')
discentes_df5 = pd.read_csv('../data/processed/matriculas_20142_processed.csv')

#dividindo as colulas dos datasets em arrays
id_discente = discentes_df.discente.tolist()
id_turma = discentes_df.id_turma.tolist()
id_curso = discentes_df.id_curso.tolist()
unidade = discentes_df.unidade.tolist()
nota = discentes_df.nota.tolist()
reposicao = discentes_df.reposicao.tolist()
media = discentes_df.media_final.tolist()
faltas = discentes_df.numero_total_faltas.tolist()
descricao = discentes_df.descricao.tolist()

print(len(id_turma))

id_discente1 = discentes_df1.discente.tolist()
id_turma1 = discentes_df1.id_turma.tolist()
id_curso1 = discentes_df1.id_curso.tolist()
unidade1 = discentes_df1.unidade.tolist()
nota1 = discentes_df1.nota.tolist()
reposicao1 = discentes_df1.reposicao.tolist()
media1 = discentes_df1.media_final.tolist()
faltas1 = discentes_df1.numero_total_faltas.tolist()
descricao1 = discentes_df1.descricao.tolist()

print(len(id_turma1))

id_discente2 = discentes_df2.discente.tolist()
id_turma2 = discentes_df2.id_turma.tolist()
id_curso2 = discentes_df2.id_curso.tolist()
unidade2 = discentes_df2.unidade.tolist()
nota2 = discentes_df2.nota.tolist()
reposicao2 = discentes_df2.reposicao.tolist()
media2 = discentes_df2.media_final.tolist()
faltas2 = discentes_df2.numero_total_faltas.tolist()
descricao2 = discentes_df2.descricao.tolist()

print(len(id_turma2))

id_discente3 = discentes_df3.discente.tolist()
id_turma3 = discentes_df3.id_turma.tolist()
id_curso3 = discentes_df3.id_curso.tolist()
unidade3 = discentes_df3.unidade.tolist()
nota3 = discentes_df3.nota.tolist()
reposicao3 = discentes_df3.reposicao.tolist()
media3 = discentes_df3.media_final.tolist()
faltas3 = discentes_df3.numero_total_faltas.tolist()
descricao3 = discentes_df3.descricao.tolist()

print(len(id_turma3))

id_discente4 = discentes_df4.discente.tolist()
id_turma4 = discentes_df4.id_turma.tolist()
id_curso4 = discentes_df4.id_curso.tolist()
unidade4 = discentes_df4.unidade.tolist()
nota4 = discentes_df4.nota.tolist()
reposicao4 = discentes_df4.reposicao.tolist()
media4 = discentes_df4.media_final.tolist()
faltas4 = discentes_df4.numero_total_faltas.tolist()
descricao4 = discentes_df4.descricao.tolist()

print(len(id_turma4))

id_discente5 = discentes_df5.discente.tolist()
id_turma5 = discentes_df5.id_turma.tolist()
id_curso5 = discentes_df5.id_curso.tolist()
unidade5 = discentes_df5.unidade.tolist()
nota5 = discentes_df5.nota.tolist()
reposicao5 = discentes_df5.reposicao.tolist()
media5 = discentes_df5.media_final.tolist()
faltas5 = discentes_df5.numero_total_faltas.tolist()
descricao5 = discentes_df5.descricao.tolist()

print(len(id_turma5))

# Open database connection
db = MySQLdb.connect("localhost","root","123","mulheres_na_ti" )

# prepare a cursor object using cursor() method and insert data
cursor = db.cursor()

#query para inserir os arrays obtidos nas tabelas
query = "INSERT INTO matricula2016_1 (id_turma, discente, id_curso, unidade, nota, reposicao,media_final, numero_total_faltas, descricao ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
query1 = "INSERT INTO matricula2016_2 (id_turma, discente, id_curso, unidade, nota, reposicao,media_final, numero_total_faltas, descricao ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
query2 = "INSERT INTO matricula2015_1 (id_turma, discente, id_curso, unidade, nota, reposicao,media_final, numero_total_faltas, descricao ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
query3 = "INSERT INTO matricula2015_2 (id_turma, discente, id_curso, unidade, nota, reposicao,media_final, numero_total_faltas, descricao ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
query4 = "INSERT INTO matricula2014_1 (id_turma, discente, id_curso, unidade, nota, reposicao,media_final, numero_total_faltas, descricao ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
query5 = "INSERT INTO matricula2014_2 (id_turma, discente, id_curso, unidade, nota, reposicao,media_final, numero_total_faltas, descricao ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

#funcao para inserir a tabela no banco
cursor.executemany(query, [(id_turma[i], id_discente[i], id_curso[i], unidade[i], nota[i], reposicao[i], media[i], faltas[i], descricao[i]) for i in range(0,len(discentes_df))])
cursor.executemany(query1, [(id_turma1[i], id_discente1[i], id_curso1[i], unidade1[i], nota1[i], reposicao1[i], media1[i], faltas1[i], descricao1[i]) for i in range(0,len(discentes_df1))])
cursor.executemany(query2, [(id_turma2[i], id_discente2[i], id_curso2[i], unidade2[i], nota2[i], reposicao2[i], media2[i], faltas2[i], descricao2[i]) for i in range(0,len(discentes_df2))])
cursor.executemany(query3, [(id_turma3[i], id_discente3[i], id_curso3[i], unidade3[i], nota3[i], reposicao3[i], media3[i], faltas3[i], descricao3[i]) for i in range(0,len(discentes_df3))])
cursor.executemany(query4, [(id_turma4[i], id_discente4[i], id_curso4[i], unidade4[i], nota4[i], reposicao4[i], media4[i], faltas4[i], descricao4[i]) for i in range(0,len(discentes_df4))])
cursor.executemany(query5, [(id_turma5[i], id_discente5[i], id_curso5[i], unidade5[i], nota5[i], reposicao5[i], media5[i], faltas5[i], descricao5[i]) for i in range(0,len(discentes_df5))])

#save mudanças
db.commit()

# disconnect from server    
db.close()
