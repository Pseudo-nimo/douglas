O robô Charlie é o robô responsável por explorar uma região desconhecida, entre dois pontos inicial (Pi) e final (Pf), do planeta Marte. Durante uma missão de exploração, ele deverá mapear as rotas navegáveis, catalogar itens de exploração e monitorar e preservar o estado de sua bateria. O Robô charlie sempre inicia sua navegação com uma bateria com capacidade máxima, com quatro unidades de deslocamento. Ele é dotato de um sistema de recarregamento baseado em energia solar, que damanda 4 segundos para recarregar as quatro unidades. O carregamento só ocorre com o robô parado e ele sempre deve recarregar quando o nível da bateria atingir 25% da capacidade ou quando a próxima unidade de deslocamento for uma região com impossibilidade de carregamento e a bateria estiver em 50% da capacidade. A bateria do robô deve ser representada por uma estrutura de dados pilha. O mapa de navegação da região desconhecida é dado por uma matriz bidimensional. Um exemplo simplificado é dado abaixo:



Neste mapa, o ponto de partida sempre será o canto esquerdo inferior, ou seja, o ponto (0,0), marcado em azul. O ponto de chegada é marcado na cor verde e, no caso do mapa exemplo, tem coordenadas (7, 6). O robô terá a liberdade de se deslocar em qualquer direção, um quadrado por deslocamento. Cada deslocamento deverá ter a duração de 2 segundos. De forma a simplificar a análise, o robô sempre deverá, se possível, se deslocar na diagonal até se alinhar verticalmente ou horizontalmente ao ponto de chegada. Ao se alinhar verticalmente ou horizontalmente, o robô deverá andar apenas nas direções vertical ou horizontal. Essa técnica visa fazer o robô andar o mais próximo possível em uma linha "reta" entre os pontos de partida e chegada.

É importante mencionar que o robô não possui, em sua base de dados, informações acerca dos itens presentes em cada unidade de deslocamento, do mapa da região a ser explorada. Ao longo da navegação, cada unidade de deslocamento irá conter valores inteiros que representam obstáculos (valor 0 - preto), áreas navegáveis (valor 255 - branco), mineral ouro (valor 191 - dourado), mineral prata (valor 127 - cinza), mineral bronze (valor 63 - marrom) e região com impossibilidade de carregamento de bateria (valor -1 - roxo), devido a ausência de luz solar. O robô tem conhecimento se o conteúdo das unidades de deslocamento vizinhas é um obstáculo ou uma área com impossibilidade de carregamento de bateria. Por ter que analisar o solo, o robô só identifica um mineral estando na unidade de deslocamento que possui o mineral em questão.

Sempre que encontrar um obstáculo, o robô deverá tentar contorná-lo se deslocando para o lado que apresentar o menor cateto, considerando que a posição do robô e o ponto de chegada formam uma hipotenusa. Caso os dois lados apresentem catetos de mesmo comprimento, o robô deverá se deslocar para a direita. Caso o robô esteja alinhado verticalmente ou horizontalmente com o ponto de chegada, ele deverá se deslocar para a direita e contornar o obstáculo. 

O robô deve contornar o obstáculo até ser possível traçar novamente um caminho diagonal para se dirigir até o ponto de chegada. Caso, após contornar o obstáculo, o robô esteja alinhado verticalmente ou horizontalmente com o ponto de chegada, ele deverá seguir em linha reta. 
Caso não encontre um caminho livre, por chegar ao final de uma borda do mapa, o robô deverá retornar ao ponto onde identificou o obstáculo e tentar a outra direção. Caso não encontre uma possibilidade de chegar até o ponto de chegada, esse será um caso de falha na navegação. Observe que, em cada unidade de deslocamento, você deverá ter um módulo para recalcular ou não a rota face ao estado da próxima unidade de deslocamento a ser visitada. É importante ressaltar que a técnica de desvio de obstáculos sugerida é bastante rudimentar e pode levar a estagnação em mínimos locais, não encontrando caminhos alternativos. O desenvolvedor não deve se preocupar com isso neste projeto.

Ao longo de seu deslocamento, o robô deverá armazenar, em uma única lista, a coordenada x e y dos pontos por onde passou e o nome do elemento correspondente a essa coordenada. Ou seja, se for uma unidade de deslocamento com área navegável, o nome a ser armazenado será "free_2_go", se for uma unidade de deslocamento com o mineral ouro, o nome a ser armazenado será "gold", se for uma unidade de deslocamento com o mineral prata, o nome a ser armazenado será "silver", se for uma unidade de deslocamento com o mineral bronze. o nome a ser armazenado será "bronze" ou se for uma unidade de deslocamento com impossibilidade de carregamento de bateria, o nome a ser armazenado será "charging_impossible". Além disso, em outra lista, o robô deverá armazenar as coordenadas identificadas como obstáculos no mapa. Ao final de seu deslocamento, o robô deverá apresentar, em arquivos, alguns registros (logs) de navegação. Ele deverá apresentar:

1) Um arquivo contendo todas as coordenadas por onde passou, onde cada coordenada irá ocupar uma linha. O arquivo deve se chamar path.txt;

Exemplo para o mapa acima:

0,0
1,1
2,1
3,1
4,2
5,2
6,3
7,4
7,5
7,6

2) Um arquivo contendo as coordenadas por onde passou, que formam o menor caminho, onde cada coordenada irá ocupar uma linha. O arquivo deve se chamar fastest_path.txt;

Exemplo para o mapa acima:

0,0
1,1
2,1
3,1
4,2
5,2
6,3
7,4
7,5
7,6

OBS: Neste caso, como o robô não teve que retornar para tentar outro caminho face a um obstáculo, o caminho executado é o caminho mais rápido conhecido.

3) Um arquivo com as coordenadas onde ocorreram os carregamentos, onde cada coordenada irá ocupar uma linha. O arquivo deve se chamar charge_impossible.txt;

Exemplo para o mapa acima:

6,3
8,4

4) Um arquivo com as coordenadas onde se encontrou ouro, onde cada coordenada irá ocupar uma linha. O arquivo deve se chamar gold.txt;

Exemplo para o mapa acima:

1,1

5) Um arquivo com as coordenadas onde se encontrou prata, onde cada coordenada irá ocupar uma linha. O arquivo deve se chamar silver.txt;

Exemplo para o mapa acima:

3,1
7,4

6) Um arquivo com as coordenadas onde se encontrou bronze, onde cada coordenada irá ocupar uma linha. O arquivo deve se chamar bronze.txt;

Exemplo para o mapa acima:

4,2
7,5

7) Um arquivo com as coordenadas dos pontos de parada para recarga da bateria, onde cada coordenada irá ocupar uma linha. O arquivo deve se chamar charging.txt.

Exemplo para o mapa acima:

5,2

8) Um arquivo com as coordenadas dos obstáculos, onde cada coordenada irá ocupar uma linha. O arquivo deve se chamar obstacles.txt.

Exemplo para o mapa acima:

2,2
3,2
5,1
5,3

Além disso, ao longo da navegação, toda vez que encontrar um obstáculo, o robô deverá detectar essa "excessão" e imprimir no prompt de comando a mensagem "obstacle_found" e a coordenada na qual ocorre. Por fim, o robô deverá exibir no prompt de comando, ao final de sua navegação, qual a quantidade de unidades de deslocamento com ouro, prata e bronze encontradas, o tempo total de naveação em segundos e se ele alcançou o ponto de chegada ("success") ou se não alcançou o ponto de chegada ("failure"). Essas impressões devem sempre ser feitas em uma nova linha.

Exemplo para o mapa acima:

obstacle_found 1,1
obstacle_found 2,1
obstacle_found 4,2
1
2
2
30
success

OBS: Nas unidades de deslocamento em que houver recarga, o tempo total gasto será o do deslocamento somado ao do abastecimento. Já na coordenada 0,0 gasta-se 2 segundos, devido ao deslocamento a ser realizado para a unidade de deslocamento 1,1. Na última unidade de deslocamento não se gasta tempo algum, tendo em vista que o robô irá entrar em estado estacionário.

É importante ressaltar que, além de terem que executar e apresentar resultados corretos, os códigos-fonte produzidos devem respeitar as boas práticas de formatação e seguir os princípios que levam a uma boa legibilidade, modularização e economia de recursos computacionais. Por exemplo, deve-se evitar o vazamento de memória. A solução para o problema acima deve ser apresentada nas linguagens C, C++, Python e Matlab. Os códigos que não compilarem ou executarem receberam nota zero. Casos de plágio levarão a penalização tanto do autor quanto do plagiador. Serão enviadas, posteriormente, instruções detalhadas para envio do trabalho.

Itens obrigatórios de serem utilizados além dos conceitos de matrizes, pilhas e listas:

C:
 - Funções;
 - Passagem de parâmetros por ponteiros;
 - Simulação de tipos abstratos de dados para as listas e pilhas.

C++:
 - Passagem de parâmetro por referência;
 - Classes;
 - Herança.

Python:
 - Classes;
 - Herança.

Matlab:
 - Sem restrições, a escolha do desenvolvedor.