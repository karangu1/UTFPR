# Coisas para fazer 

## Escrever o pq das localizacoes das subestações e ponto de entrega

Para encontrar um ponto ideal para as subestações, foi utilizado o método da média de posições. Encontrar um lugar que contenha a média de todas as cargas de uma determinada localização implica no lugar com os menores custos de materiais. Infelizmente, este método sempre resulta em subestações que ficam na parte interna do ambiente fabril, sendo necessário realizar alterações para o projeto real.

### SE1

O ponto de referencia para a região da fábrica 1 foi o canto inferior direito do local, usando as posições relativas de 'x' e de 'y':

$$ Pos_x = \frac{\sum{Dem_i.X_i}}{\sum{Dem}} $$
$$ Pos_x = \frac{29440.33,57+29440.31,90+29440.31,90+316480.190,38}{404800} $$
$$ Pos_x = 155.92 $$
$$ Pos_y = \frac{\sum{Dem_i.y_i}}{\sum{Dem}} $$
$$ Pos_y = \frac{29440.4,77+29440.49,44+29440.95,79+316480.34,61}{404800} $$
$$ Pos_y = 37,92 $$

## SE2

O ponto de referencia para a região do centro de convivência foi o canto inferior do local, usando as posições relativas de 'x' e de 'y':

$$ Pos_x = \frac{\sum{Dem_i.X_i}}{\sum{Dem}} $$
$$ Pos_x = \frac{20000.(-25,01)+110000.37,17}{130000}$$
$$ Pos_x = 27,60 $$
$$ Pos_y = \frac{\sum{Dem_i.y_i}}{\sum{Dem}} $$
$$ Pos_y = \frac{20000.(40,30)+110000.92,41}{130000}$$
$$ Pos_y = 83,39 $$

## SE3

O ponto de referencia para a região da fábrica 2 foi o canto inferior direito do local, usando as posições relativas de 'x' e de 'y':

$$ Pos_x = \frac{\sum{Dem_i.X_i}}{\sum{Dem}} $$
$$ Pos_x = \frac{129213,48.29,24+73600.2,02+124800.51,18}{327613}$$
$$ Pos_x = 31,48 $$
$$ Pos_y = \frac{\sum{Dem_i.y_i}}{\sum{Dem}} $$
$$ Pos_y = \frac{129213,48.97,59+73600.45,09+124800.2.03}{327613}$$
$$ Pos_y = 49,39 $$

## SE4

Para os depósitos, foi considerado que as cargas de iluminação e de TUGs estão distribuídas uniformemente, então, optou-se por colocar a subestação centralizada e à direita dos depósitos a fim de dar continuidade ao sistema de distribuição.

## SE5

O ponto de referencia para a região da oficina foi o canto inferior direito do local, usando as posições relativas de 'x' e de 'y':

$$ Pos_x = \frac{\sum{Dem_i.X_i}}{\sum{Dem}} $$
$$ Pos_x = \frac{7360.22,7+47368,42.70,31+63157,89.9,24+22080.0}{139966} $$
$$ Pos_x = 29,16 $$
$$ Pos_y = \frac{\sum{Dem_i.y_i}}{\sum{Dem}} $$
$$ Pos_y = \frac{7360.0+47368,42.0+63157,89.52.83+22080.98.52}{139966} $$
$$ Pos_y = 39,38 $$

## SE6

O ponto de referencia para a região do laboratório foi o canto superior direito do local, usando as posições relativas de 'x' e de 'y':

$$ Pos_x = \frac{\sum{Dem_i.X_i}}{\sum{Dem}} $$
$$ Pos_x = \frac{66240.14,72+40000.4,9}{106240}$$
$$ Pos_x = 11,02 $$
$$ Pos_y = \frac{\sum{Dem_i.y_i}}{\sum{Dem}} $$
$$ Pos_x = \frac{66240.0.90+40000.42.48}{106240}$$
$$ Pos_y = 16,56 $$

## SE7

Para o bloco administrativo, foi considerado que as cargas de iluminação e de TUGs estão distribuídas uniformemente. Então, optou-se por colocar a subestação o mais próximo possível do sistema de ar condicionado, a fim de dar continuidade ao sistema de distribuição e reduzir o uso de materiais.

## Distribuição das SEs e Ponto de entrega

Com todas as regiões calculadas, basta estipular os melhores valores possíveis para cada subestação, e com esses valores, encontrar a melhor localização do ponto de entrega. A tabela a seguir apresenta os valores calculados (posições relativas já citadas) e os valores optados(posição total, com a origem no canto inferior direito da planta baixa).

| Local                 | SE | x calc | y calc | x real | y real |
|-----------------------|----|--------|--------|--------|--------|
| Fabrica 1             | 1  | 155,92 | 37,96  | 665    | 191,5  |
| Centro de convivência | 2  | 27,60  | 84,39  | 1087,8 | 690,7  |
| Fábrica 2             | 3  | 31,48  | 49,39  | 135,22 | 436,36 |
| Depósitos 1 e 2       | 4  | 125,51 | 307,76 | 125    | 308    |
| Oficina               | 5  | 29,16  | 39,38  | 1087,8 | 690,7  |
| Laboratório           | 6  | 11,02  | 16,56  | 8      | 170    |
| Administrativo        | 7  | 322,11 | 109.89 | 322,11 | 109.89 |
| Ponto de Entrega      |    | 398,8  | 337,33 | 374.56 | 10     |





## Unifilar

Os quesitos para a conclusão do unifilar(se quiserem conferir e mandar alguma observação fiquem à vontade):

- [x] Apresentação folha padrão ABNT com margem e legenda
- [x] Indicação e identificação das SE's
- [ ] Indicação e identificação dos trafos (potência e tensões pelo menos)
- [x] Indicação do esquema de aterramento adotado em cada trafo
- [x] Indicação e identificação dos quadros gerais de distribuição
- [x] Indicação e identificação dos quadros terminais de cargas
- [x] Indicação, identificação e especificação do grupo motor gerador
- [x] Indicação, identificação e ligações do QTA
- [x] Indicação dos alimentadores de M.T
- [x] Indicação dos alimentadores de B.T
- [x] Indicação, identificação e especificação dos bancos de capacitores
- [x] Indicação, identificação e especificação da usina fotovoltaica (até inversores)
- [x] identifição do nobreak

Gerações de energia no estabelecimento

| Lugar         | subestacao   | Usina                    | ok    |
| :-----------: | ------------ | ------------------------ | ----- |
| fabrica 1     | SE1          | 500 paineis 325W         | [x]   |
| centro conv   | SE2          | nada                     | [x]   |
| f_02          | SE3          | 150 paineis de 325W      | [x]   |
| dep1 e 2      | SE4          | nada                     | [x]   |
| oficina       | SE5          | 150 Fotovoltaicos 325W   | [x]   |
| lab           | SE6          | geracao diesel (40kVA)   | [x]   |
| adm           | SE7          | geracao propria rampa    | [x]   |




## Referências

[Como representei a geraçao fotovoltaica e o inversor](https://maisengenharia.altoqi.com.br/wp-content/uploads/2016/05/energia-fotovoltaica-4.jpg)

[Como representei a geraçao fotovoltaica e o inversor](http://www.cemig.com.br/pt-br/atendimento/corporativo/PublishingImages/0DUB_Diagrama_Unifilar_Basico.PNG)

[QTA](http://www.naganoprodutos.com.br/novosite/upload/download/1483.pdf)

[Representação ccm](https://www.estudegratis.com.br/images/questoes/1d179d876db8dcc35264.gif)

nao encontrei representação do nobreak, fiz só um retangulo




