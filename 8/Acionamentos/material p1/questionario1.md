Questionário Acionamentos 
===

Teoria Partida de motores
---



__1) Defina escorregamento nos motores assíncronos.__

É a diferença entre a velocidade síncrona e a velocidade nominal do motor, medida em pu(ou porcentagem)

__2) Represente o modelo do Motor Trifásico de Indução (MIT).__


__3) As curvas abaixo representam a variação da velocidade do rotação do rotor de um MIT de 5hp submetido a uma partida direta. Com base nas curvas, responda as questões a ,b e c justificando a resposta.__

__a) Em quais curvas o motor parte com carga e em quais a vazio?__

B, e D : Carga
A  C      : Vazio

__b) Em quais curvas a inércia do conjunto girante foi alterada?__

C e D

__c) Qual o tempo de partida de cada curva?__

| Curva | Tempo partida(s) |
|-------|------------------|
| A     | 0.25             |
| B     | 0.3              |
| C     | 0.35             |
| D     | 0.45             |


__5) Qual a influência que a inércia causa na partida de um MIT?__

Inércia é toda oposição a movimentos, na partida de motores, essa oposição faz com que o motor demore para atingir sua velocidade de regime permanente.

__6) Qual a influência que o conjugado resistente causa na partida do MIT?__

O conjugado resistente influencia diretamente no tempo de partida do motor. Maiores conjugados resistentes(também chamados de torque de carga) tornam a partida do MIT mais demorada

__7) Porque os parâmetros mecânicos (inercia e conjugado da carga) não alteram o valor da corrente de partida?__

Pois a corrente de partida é definida pelo circuito. Como em toda partida o escorregamento é 1 (velocidade do motor é zero), a resistência variável é $r_2$(constante), e isso faz com que a corrente sempre seja a mesma.

__8) As curvas abaixo representam a variação da corrente de partida de um MIT de 5hp partindo sem carga. Com base nas curvas, responda as questões a, b, c e d justificando a resposta.__

__a) Qual curva é resultado de uma partida direta?__

Curva C

__b) A partida, que resultou nas curvas A e B, foi realizada com a mesma tensão de partida? Qual percentual aproximado em relação a nominal?__

Sim, a corrente é proporcional à tensão. O percentual é de 60% aproximadamente.

__c) A partida, que resultou na curva B, foi corretamente executada?__

Não, a corrente não tem quase nenhuma redução

__d) Se a inércia do conjunto girante fosse aumentada (ex. em 50%), qual ação deveria ser tomada para que seja mantido o desempenho da partida representado pela curva A.__

O tempo de espera para a aplicação da tensão nominal precisa ser maior, com aumento de inercia aumenta o tempo de partida

__9) A partir do catálogo da WEG, motores da família W22 – IR 2, determine a tensão reduzida mínima (partida indireta) que deve ser aplicada no motor de 50HP – 4 pólos , para que o mesmo parta com 85% da sua carga nominal.__

__10) Qual a influência que a corrente de partida do MIT causa na rede de energia elétrica interna da planta?__

Afundamento de tensão: a tensão da rede interna assume valores críticos
O motor precisa de muita corrente para partir, Isso faz com que a corrente da rede seja redirecionada ao motor, o que faz com que a rede sofra um pouco.

__11) Determine (por cálculo ou por simulação) o percentual de queda de tensão nos pontos A, B e C do circuito abaixo quando é dada uma partida direta no motor: Os dados de corrente de partida do motor devem ser obtidos no catálogo.__

Considerar:
Rtr=0.05Ω Xltr=0.3Ω
Rcabo1=0.01 Xlcabo1=0.03
Rcabo2=0.01 Xlcabo2=0.03
Motor de 100CV
Desconsiderar a impedância da rede.

__12) Considerando os dados (parâmetros da instalação) da questão anterior, quais seriam os percentuais de queda, caso a tensão no secundário do transformador fosse alterada para 440/254V?__

__13) Represente a ligação de um MIT de 12 terminais para que este opere na tensão de 380V__
