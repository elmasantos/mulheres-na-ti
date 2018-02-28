# Mulheres na TI

Em razão do baixo número de mulheres na área de tecnologia da informação, decidimos levantar dados a fim de compreender essa realidade. O nosso objetivo é analisar os fatores que levam à evasão de mulheres que ingressam no curso do BTI-UFRN. 
O projeto está sendo desenvolvido para a disciplina Tópicos Especiais em Informática Educacional "C".


#### Seleção dos dados

O conjunto de dados escolhido contém informações sobre discentes de cursos de graduação da UFRN, provenientes do [Portal de Dados Abertos da Universidade Federal do Rio Grande do Norte](http://dados.ufrn.br/).

Bases utilizadas:
- DISCENTES DA INSTITUIÇÃO
- MATRÍCULAS EM COMPONENTES de 2014 a 2016 (semestralmente)


#### Pré-processamento e limpeza dos dados

data/dados-pessoais-discentes.csv
- Exclusão de registros onde dados da coluna 'id_discente' são nulos.
- Exclusão de registros onde dados na coluna 'nível_ensino' não é 'GRADUAÇÃO'.
- Substituição de texto 'CANDEL&#65533;RIA' por 'CANDELARIA' na coluna ‘bairro’.

data/matricula*.csv
- Exclusão de registros onde dados da coluna 'discente' são nulos.
- Exclusão de registros onde dados da coluna 'id_curso' não é id do BTI.
- Exclusão de colunas 'faltas_unidade' e 'Unnamed: 10'.
- Exclusão de registros onde 'descricao' for 'EXCLUIDA', 'CANCELADO' ou 'INDEFERIDO'.
- Alteração de coluna 'nota' para números com 1 casa decimal após a vírgula;
- Preenchimento de campos vazios por '0' nas colunas 'unidade', 'nota', 'reposicao', 'media_final' e 'numero_total_faltas'.
- Conversão de dados para string.

Após o pré-processamento, são gerados os arquivos finais:
- data/processed/dados_discentes_processed.csv
- data/processed/matricula*.csv

##### Cruzamento

Merge entre a base “discentes da instituição” e as demais bases “matrículas em componentes”, utilizando como chave o identificador do discente. 
- data/merge/merge*.csv
  - Remoção de colunas 'Unnamed: 0_x' e 'Unnamed: 0_y';
  - Preenchimento de campos vazios por texto 'NAO INFORMADO' nas colunas 'cidade_origem', 'estado', 'municipio' e 'bairro'.


#### Autores

* [Elma](https://github.com/elmasantos/)
* Joicy
* [Julliana](https://github.com/JuhCrln)
* Gabriel
* [Thayrone](https://github.com/thaydds)


