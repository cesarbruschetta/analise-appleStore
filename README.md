# Analise de dados do Apple Store



Uma empresa que fornece aplicativos de música e livros, precisa acompanhar 
regularmente a evolução das métricas de aplicativos de música disponíveis na Apple Store. 
Hoje, para que esse acompanhamento seja feito, um profissional precisa
diariamente realizar a coleta desses dados atualizados, realizar a transformação
desses dados. 
Atualmente a empresa não dispõe de nenhuma ferramenta que faça
esse trabalho de forma automatizada. Além disso, esse profissional está envolvido em
diversas outras atividades, fazendo com que, muitas vezes, esses relatórios deixem de
ser enviados.

Utilizando a linguagem Python, acesse o arquivo AppleStore.csv que terá os seguintes
dados disponíveis:

## Dados disponíveis 

 * id = Identificação do App 
 * track_name = Nome 
 * size_bytes = Tamanho em Bytes 
 * currency = Moeda 
 * price = Valor na Apple Store
 * rating_count_tot = Qtde de Avaliações
 * rating_count_ver = Qtde de Avaliações última versão 
 * user_rating = Avaliação Média 
 * user_rating_ver = Avaliação Média da última versão 
 * ver = Última Versão 
 * cont_rating = Classificação Indicativa
 * prime_genre = Gênero do App

Para isso, é preciso extrair os dados relativos a Aplicações “Apps”, do gênero News. 
Já para a Aplicação da categoria News, que tiver a maior quantidade de
avaliações, utilizar a API dessa Aplicação para identificar quais são as 10 Aplicações
do gênero Music e Book que possuem o maior número de citações.

Em seguida, será necessário armazenar esses dados em um arquivo CSV, com os
campos: 

* id
* track_name
* n_citacoes
* size_bytes
* price
* prime_genre

Para isso, precisa armazenar os dados do arquivo criado no passo anterior numa base de dados com as respectivas colunas. 
Por último, deverá acessar os dados e retornar um JSON com todas as informações contidas.

## Arquivo de dados:

Os dados relativos as Aplicações estão disponíveis no arquivo abaixo.
* AppleStore.csv