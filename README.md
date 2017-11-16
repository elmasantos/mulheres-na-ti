# mulheres-na-ti

Em razão do baixo número de mulheres na área de tecnologia da informação, decidimos levantar dados a fim de compreender essa realidade. O nosso objetivo é analisar os fatores que levam à evasão de mulheres que ingressam no BTI-UFRN. Para isso, vamos relacionar dados acadêmicos e socioeconômicos.
O projeto está sendo desenvolvido para a disciplina Tópicos Especiais em Informática Educacional "C".


#### Seleção dos dados

O conjunto de dados escolhido contém informações sobre discentes de cursos da UFRN:
- data/discentes.csv


#### Pré processamento dos dados

- Substituição dos separadores de colunas de “;” para “,” no arquivo discentes.CSV.
- Exclusão de registros onde dados da coluna id_discente são nulos.
- Exclusão de registros onde nível de ensino não for graduação.
- Preenchimento de campos de CEP vazios (preenchidos com 59000000).
- Preenchimento de campos de CEP incompletos (de 59 para 59000000)
- Exclusão de traços, pontos e espaços nos campos de CEP.

Após o préprocessamento, é gerado o arquivo final:
- data/discentes_processed.csv



#### Autores

* [Elma](https://github.com/elmasantos/)
* Joicy
* Julliana
* Gabriel
* [Thayrone](https://github.com/thaydds)


