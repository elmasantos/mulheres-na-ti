# mulheres-na-ti

Em razão do baixo número de mulheres na área de tecnologia da informação, decidimos levantar dados a fim de compreender essa realidade. O nosso objetivo é analisar os fatores que levam à evasão de mulheres que ingressam no BTI-UFRN. Para isso, vamos relacionar dados acadêmicos e socioeconômicos.
O projeto está sendo desenvolvido para a disciplina Tópicos Especiais em Informática Educacional "C".


#### Seleção dos dados

O conjunto de dados escolhido contém informações sobre discentes de cursos de graduação da UFRN:
- data/discentes.csv
- data/matricula-componente-20141.csv
- data/matricula-componente-20142.csv
- data/matriculas-de-2015.1.csv
- data/matriculas-de-2015.2.csv
- data/matriculas-de-2016.1.csv
- data/matriculas-de-2016.2.csv


#### Pré-processamento e limpeza dos dados

data/discentes.csv
- Exclusão de registros onde dados da coluna 'id_discente' são nulos.
- Exclusão de registros onde dados na coluna 'nível_ensino' não for 'GRADUAÇÃO'.
- Preenchimento de campos vazios na coluna 'cep' (preenchidos com 59000000).
- Preenchimentos de campos vazios na coluna 'forma_ingresso'.
- Preenchimento de campos de 'cep' incompletos (de 59 para 59000000)
- Exclusão de traços, pontos e espaços nos campos de 'cep'.

data/matricula*.csv
- Exclusão de registros onde dados da coluna 'discente' são nulos.
- Exclusão de registros onde dados da coluna 'id_curso' não for id do BTI.
- Exclusão de colunas 'faltas_unidade' e 'Unnamed: 10'.
- Exclusão de registros onde 'descricao' for 'EXCLUIDA', 'CANCELADO' ou 'INDEFERIDO'.
- Conversão de dados para string.


Após o pré-processamento, são gerados os arquivos finais:
- data/processed/discentes_processed.csv
- data/processed/matricula*.csv


#### Autores

* [Elma](https://github.com/elmasantos/)
* Joicy
* [Julliana](https://github.com/JuhCrln)
* Gabriel
* [Thayrone](https://github.com/thaydds)


