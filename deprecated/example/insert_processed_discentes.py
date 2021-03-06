#!/usr/bin/python                                                                        
# -*- coding: utf-8 -*-

import pandas as pd 
import MySQLdb


#leitura de arquivo,
discentes_df = pd.read_csv('merge20141_sem_rep.csv', sep = ";")
discentes_df2 = pd.read_csv('merge20142_sem_rep.csv', sep = ";")
discentes_df3 = pd.read_csv('merge20151_sem_rep.csv', sep = ";")
discentes_df4 = pd.read_csv('merge20152_sem_rep.csv', sep = ";")
discentes_df5 = pd.read_csv('merge20161_sem_rep.csv', sep = ";")
discentes_df6 = pd.read_csv('merge20162_sem_rep.csv', sep = ";")

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
id_turma = discentes_df.id_turma.tolist()
id_curso = discentes_df.id_curso.tolist()
unidade = discentes_df.unidade.tolist()
nota = discentes_df.unidade.tolist()
reposicao = discentes_df.unidade.tolist()
media_final = discentes_df.media_final.tolist()
numero_total_de_faltas = discentes_df.numero_total_faltas.tolist()
descricao = discentes_df.descricao.tolist()
ano = discentes_df.ano.tolist()
periodo = discentes_df.ano.tolist()
escola_ens_medio = discentes_df.escola_ens_medio.tolist()
possui_auxilio_alimentacao = discentes_df.possui_auxilio_alimentacao.tolist()
possui_bolsa_pesquisa = discentes_df.possui_bolsa_pesquisa.tolist()
possui_auxilio_transporte = discentes_df.possui_auxilio_transporte.tolist()
possui_auxilio_residencia_moradia = discentes_df.possui_auxilio_residencia_moradia.tolist()


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
id_turma2 = discentes_df2.id_turma.tolist()
id_curso2 = discentes_df2.id_curso.tolist()
unidade2 = discentes_df2.unidade.tolist()
nota2 = discentes_df2.unidade.tolist()
reposicao2 = discentes_df2.unidade.tolist()
media_final2 = discentes_df2.media_final.tolist()
numero_total_de_faltas2 = discentes_df2.numero_total_faltas.tolist()
descricao2 = discentes_df2.descricao.tolist()
ano2 = discentes_df2.ano.tolist()
periodo2 = discentes_df2.ano.tolist()
escola_ens_medio2 = discentes_df2.escola_ens_medio.tolist()
possui_auxilio_alimentacao2 = discentes_df2.possui_auxilio_alimentacao.tolist()
possui_bolsa_pesquisa2 = discentes_df2.possui_bolsa_pesquisa.tolist()
possui_auxilio_transporte2 = discentes_df2.possui_auxilio_transporte.tolist()
possui_auxilio_residencia_moradia2 = discentes_df2.possui_auxilio_residencia_moradia.tolist()

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
id_turma3 = discentes_df3.id_turma.tolist()
id_curso3 = discentes_df3.id_curso.tolist()
unidade3 = discentes_df3.unidade.tolist()
nota3 = discentes_df3.unidade.tolist()
reposicao3 = discentes_df3.unidade.tolist()
media_final3 = discentes_df3.media_final.tolist()
numero_total_de_faltas3 = discentes_df3.numero_total_faltas.tolist()
descricao3 = discentes_df3.descricao.tolist()
ano3 = discentes_df3.ano.tolist()
periodo3 = discentes_df3.ano.tolist()
escola_ens_medio3 = discentes_df3.escola_ens_medio.tolist()
possui_auxilio_alimentacao3 = discentes_df3.possui_auxilio_alimentacao.tolist()
possui_bolsa_pesquisa3 = discentes_df3.possui_bolsa_pesquisa.tolist()
possui_auxilio_transporte3 = discentes_df3.possui_auxilio_transporte.tolist()
possui_auxilio_residencia_moradia3 = discentes_df3.possui_auxilio_residencia_moradia.tolist()

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
id_turma4 = discentes_df4.id_turma.tolist()
id_curso4 = discentes_df4.id_curso.tolist()
unidade4 = discentes_df4.unidade.tolist()
nota4 = discentes_df4.unidade.tolist()
reposicao4 = discentes_df4.unidade.tolist()
media_final4 = discentes_df4.media_final.tolist()
numero_total_de_faltas4 = discentes_df4.numero_total_faltas.tolist()
descricao4 = discentes_df4.descricao.tolist()
ano4 = discentes_df4.ano.tolist()
periodo4 = discentes_df4.ano.tolist()
escola_ens_medio4 = discentes_df4.escola_ens_medio.tolist()
possui_auxilio_alimentacao4 = discentes_df4.possui_auxilio_alimentacao.tolist()
possui_bolsa_pesquisa4 = discentes_df4.possui_bolsa_pesquisa.tolist()
possui_auxilio_transporte4 = discentes_df4.possui_auxilio_transporte.tolist()
possui_auxilio_residencia_moradia4 = discentes_df4.possui_auxilio_residencia_moradia.tolist()

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
id_turma5 = discentes_df5.id_turma.tolist()
id_curso5 = discentes_df5.id_curso.tolist()
unidade5 = discentes_df5.unidade.tolist()
nota5 = discentes_df5.unidade.tolist()
reposicao5 = discentes_df5.unidade.tolist()
media_final5 = discentes_df5.media_final.tolist()
numero_total_de_faltas5 = discentes_df5.numero_total_faltas.tolist()
descricao5 = discentes_df5.descricao.tolist()
ano5 = discentes_df5.ano.tolist()
periodo5 = discentes_df5.ano.tolist()
escola_ens_medio5 = discentes_df5.escola_ens_medio.tolist()
possui_auxilio_alimentacao5 = discentes_df5.possui_auxilio_alimentacao.tolist()
possui_bolsa_pesquisa5 = discentes_df5.possui_bolsa_pesquisa.tolist()
possui_auxilio_transporte5 = discentes_df5.possui_auxilio_transporte.tolist()
possui_auxilio_residencia_moradia5 = discentes_df5.possui_auxilio_residencia_moradia.tolist()

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
id_turma6 = discentes_df6.id_turma.tolist()
id_curso6 = discentes_df6.id_curso.tolist()
unidade6 = discentes_df6.unidade.tolist()
nota6 = discentes_df6.unidade.tolist()
reposicao6 = discentes_df6.unidade.tolist()
media_final6 = discentes_df6.media_final.tolist()
numero_total_de_faltas6 = discentes_df6.numero_total_faltas.tolist()
descricao6 = discentes_df6.descricao.tolist()
ano6 = discentes_df6.ano.tolist()
periodo6 = discentes_df6.ano.tolist()
escola_ens_medio6 = discentes_df6.escola_ens_medio.tolist()
possui_auxilio_alimentacao6 = discentes_df6.possui_auxilio_alimentacao.tolist()
possui_bolsa_pesquisa6 = discentes_df6.possui_bolsa_pesquisa.tolist()
possui_auxilio_transporte6 = discentes_df6.possui_auxilio_transporte.tolist()
possui_auxilio_residencia_moradia6 = discentes_df6.possui_auxilio_residencia_moradia.tolist()

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
query = "INSERT INTO alunos_bti_2014_1_sem_rep (id_discente, sexo, data_nascimento, raca, estado_origem, cidade_origem, estado, municipio, bairro, nivel_ensino, forma_ingresso, ano_ingresso, periodo_ingresso, cotista, id_turma, id_curso, unidade, nota, reposicao, media_final, numero_total_de_faltas, descricao, ano, periodo, escola_ens_medio, possui_auxilio_alimentacao, possui_bolsa_pesquisa, possui_auxilio_transporte, possui_auxilio_residencia_moradia ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
query2 = "INSERT INTO alunos_bti_2014_2_sem_rep (id_discente, sexo, data_nascimento, raca, estado_origem, cidade_origem, estado, municipio, bairro, nivel_ensino, forma_ingresso, ano_ingresso, periodo_ingresso, cotista, id_turma, id_curso, unidade, nota, reposicao, media_final, numero_total_de_faltas, descricao, ano, periodo, escola_ens_medio, possui_auxilio_alimentacao, possui_bolsa_pesquisa, possui_auxilio_transporte, possui_auxilio_residencia_moradia ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
query3 = "INSERT INTO alunos_bti_2015_1_sem_rep (id_discente, sexo, data_nascimento, raca, estado_origem, cidade_origem, estado, municipio, bairro, nivel_ensino, forma_ingresso, ano_ingresso, periodo_ingresso, cotista, id_turma, id_curso, unidade, nota, reposicao, media_final, numero_total_de_faltas, descricao, ano, periodo, escola_ens_medio, possui_auxilio_alimentacao, possui_bolsa_pesquisa, possui_auxilio_transporte, possui_auxilio_residencia_moradia ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
query4 = "INSERT INTO alunos_bti_2015_2_sem_rep (id_discente, sexo, data_nascimento, raca, estado_origem, cidade_origem, estado, municipio, bairro, nivel_ensino, forma_ingresso, ano_ingresso, periodo_ingresso, cotista, id_turma, id_curso, unidade, nota, reposicao, media_final, numero_total_de_faltas, descricao, ano, periodo, escola_ens_medio, possui_auxilio_alimentacao, possui_bolsa_pesquisa, possui_auxilio_transporte, possui_auxilio_residencia_moradia ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
query5 = "INSERT INTO alunos_bti_2016_1_sem_rep (id_discente, sexo, data_nascimento, raca, estado_origem, cidade_origem, estado, municipio, bairro, nivel_ensino, forma_ingresso, ano_ingresso, periodo_ingresso, cotista, id_turma, id_curso, unidade, nota, reposicao, media_final, numero_total_de_faltas, descricao, ano, periodo, escola_ens_medio, possui_auxilio_alimentacao, possui_bolsa_pesquisa, possui_auxilio_transporte, possui_auxilio_residencia_moradia ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
query6 = "INSERT INTO alunos_bti_2016_2_sem_rep (id_discente, sexo, data_nascimento, raca, estado_origem, cidade_origem, estado, municipio, bairro, nivel_ensino, forma_ingresso, ano_ingresso, periodo_ingresso, cotista, id_turma, id_curso, unidade, nota, reposicao, media_final, numero_total_de_faltas, descricao, ano, periodo, escola_ens_medio, possui_auxilio_alimentacao, possui_bolsa_pesquisa, possui_auxilio_transporte, possui_auxilio_residencia_moradia ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

#funcao para inserir a tabela no banco
cursor.executemany(query, [(id_discente[i], sexo[i], data_nascimento[i], raca[i], estado_origem[i], cidade_origem[i], estado[i], municipio[i], bairro[i], nivel_ensino[i], forma_ingresso[i], ano_ingresso[i], periodo_ingresso[i], cotista[i], id_turma[i], id_curso[i], unidade[i], nota[i], reposicao[i], media_final[i], numero_total_de_faltas[i], descricao[i], ano[i], periodo[i], escola_ens_medio[i], possui_auxilio_alimentacao[i], possui_auxilio_transporte[i], possui_bolsa_pesquisa[i], possui_auxilio_residencia_moradia[i]) for i in range(0,len(discentes_df))])
cursor.executemany(query2, [(id_discente2[i], sexo2[i], data_nascimento2[i], raca2[i], estado_origem2[i], cidade_origem2[i], estado2[i], municipio2[i], bairro2[i], nivel_ensino2[i], forma_ingresso2[i], ano_ingresso2[i], periodo_ingresso2[i], cotista2[i], id_turma2[i], id_curso2[i], unidade2[i], nota2[i], reposicao2[i], media_final2[i], numero_total_de_faltas2[i], descricao2[i], ano2[i], periodo2[i], escola_ens_medio2[i], possui_auxilio_alimentacao2[i], possui_auxilio_transporte2[i], possui_bolsa_pesquisa2[i], possui_auxilio_residencia_moradia2[i]) for i in range(0,len(discentes_df2))])
cursor.executemany(query3, [(id_discente3[i], sexo3[i], data_nascimento3[i], raca3[i], estado_origem3[i], cidade_origem3[i], estado3[i], municipio3[i], bairro3[i], nivel_ensino3[i], forma_ingresso3[i], ano_ingresso3[i], periodo_ingresso3[i], cotista3[i], id_turma3[i], id_curso3[i], unidade3[i], nota3[i], reposicao3[i], media_final3[i], numero_total_de_faltas3[i], descricao3[i], ano3[i], periodo3[i], escola_ens_medio3[i], possui_auxilio_alimentacao3[i], possui_auxilio_transporte3[i], possui_bolsa_pesquisa3[i], possui_auxilio_residencia_moradia3[i]) for i in range(0,len(discentes_df3))])
cursor.executemany(query4, [(id_discente4[i], sexo4[i], data_nascimento4[i], raca4[i], estado_origem4[i], cidade_origem4[i], estado4[i], municipio4[i], bairro4[i], nivel_ensino4[i], forma_ingresso4[i], ano_ingresso4[i], periodo_ingresso4[i], cotista4[i], id_turma4[i], id_curso4[i], unidade4[i], nota4[i], reposicao4[i], media_final4[i], numero_total_de_faltas4[i], descricao4[i], ano4[i], periodo4[i], escola_ens_medio4[i], possui_auxilio_alimentacao4[i], possui_auxilio_transporte4[i], possui_bolsa_pesquisa4[i], possui_auxilio_residencia_moradia4[i]) for i in range(0,len(discentes_df4))])
cursor.executemany(query5, [(id_discente5[i], sexo5[i], data_nascimento5[i], raca5[i], estado_origem5[i], cidade_origem5[i], estado5[i], municipio5[i], bairro5[i], nivel_ensino5[i], forma_ingresso5[i], ano_ingresso5[i], periodo_ingresso5[i], cotista5[i], id_turma5[i], id_curso5[i], unidade5[i], nota5[i], reposicao5[i], media_final5[i], numero_total_de_faltas5[i], descricao5[i], ano5[i], periodo5[i], escola_ens_medio5[i], possui_auxilio_alimentacao5[i], possui_auxilio_transporte5[i], possui_bolsa_pesquisa5[i], possui_auxilio_residencia_moradia5[i]) for i in range(0,len(discentes_df5))])
cursor.executemany(query6, [(id_discente6[i], sexo6[i], data_nascimento6[i], raca6[i], estado_origem6[i], cidade_origem6[i], estado6[i], municipio6[i], bairro6[i], nivel_ensino6[i], forma_ingresso6[i], ano_ingresso6[i], periodo_ingresso6[i], cotista6[i], id_turma6[i], id_curso6[i], unidade6[i], nota6[i], reposicao6[i], media_final6[i], numero_total_de_faltas6[i], descricao6[i], ano6[i], periodo6[i], escola_ens_medio6[i], possui_auxilio_alimentacao6[i], possui_auxilio_transporte6[i], possui_bolsa_pesquisa6[i], possui_auxilio_residencia_moradia6[i]) for i in range(0,len(discentes_df6))])

#save mudanças
db.commit()

# disconnect from server    
db.close()

