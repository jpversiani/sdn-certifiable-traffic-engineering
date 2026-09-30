UNIVERSIDADE ESTADUAL DE MONTES CLAROS

Centro de Ciências Exatas e Tecnológicas

Programa de Pós Graduação em Modelagem Computacional e Sistemas

João Paulo Versiani Ladeia

# OTIMIZAÇÃO APLICADA AO PROBLEMA DE ENGENHARIA DE TRÁFEGO EM REDES DEFINIDAS POR SOFTWARE {#otimização-aplicada-ao-problema-de-engenharia-de-tráfego-em-redes-definidas-por-software .TOC-Heading}

Montes Claros - MG

Outubro de 2018

João Paulo Versiani Ladeia

**OTIMIZAÇÃO APLICADA AO PROBLEMA DE ENGENHARIA DE TRÁFEGO EM REDES
DEFINIDAS POR SOFTWARE**

> Dissertação apresentada no Programa de Pós Graduação em Modelagem
> Computacional e Sistemas, da Universidade Estadual de Montes Claros
> como exigência para obtenção do grau de Mestre em Modelagem
> Computacional e Sistemas.
>
> Orientador: Prof^º^. Dr. Nilton Alves Maia

Montes Claros - MG

Outubro de 2018

João Paulo Versiani Ladeia

**OTIMIZAÇÃO APLICADA AO PROBLEMA DE ENGENHARIA DE TRÁFEGO EM REDES
DEFINIDAS POR SOFTWARE**

> Dissertação apresentada no Programa de Pós Graduação em Modelagem
> Computacional e Sistemas, da Universidade Estadual de Montes Claros
> como exigência para obtenção do grau de Mestre em Modelagem
> Computacional e Sistemas.
>
> Montes Claros, 06 de Novembro de 2018.

Orientador:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Prof^º^. Dr. Nilton Alves Maia

Universidade Estadual de Montes Claros

Membros:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Prof^º^. Dr. João Batista Mendes

Universidade Estadual de Montes Claros

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Prof^º^. Dr. Marcos Flávio Silveira Vasconcelos D\'Angelo

Universidade Estadual de Montes Claros

Montes Claros - MG

Outubro de 2018

Catalogação Biblioteca Central Professor Antônio Jorge

***"O que sabemos é uma gota; o que ignoramos é um oceano."***

***Isaac Newton***

***"O estudo, a busca da verdade e da beleza são domínios***

***em que nos é consentido sermos crianças por toda a vida."***

***Albert Einstein***

***''A vida é demasiado curta para nos permitir interessar-nos por todas
as coisas, mas é bom que nos interessemos por tantas quantas forem
necessárias para preencher os nossos dias.''***

***Bertrand Russell***

***\"A persistência é o caminho do êxito.\"***

***Chaplin, Charlie***

AGRADECIMENTOS

A Deus por tudo e todos sempre!

A Unimontes e ao PPGMCS pela oportunidade de realizar o mestrado.

Ao Professor Nilton pelos ensinamentos, orientação, disponibilidade,
dedicação e amizade.

Aos Professores José Higino, João Batista, Marcos Flávio, Narciso
Ferreira, Renê e Rômulo pelos conhecimentos adquiridos muito importantes
para o desenvolvimento desta pesquisa.

Aos demais professores e funcionários do PPGMCS.

Aos meus queridos Pais Veraldino e Socorro pelo que sou, pelo amor,
apoio e compreensão sempre presentes.

Aos meus Irmãos Igor, Emelline e Júnior.

Ao Léo, Luna e Luciana.

Aos meus sobrinhos Maria Vitória, João Artur, Luiz Benício, Maria Alice
e Heitor.

A minha querida namorada Francelli pelo amor, carinho, apoio,
compreensão, paciência e incentivo durante todo esse meu percurso. Ao
Fred pelo amor, carinho, compreensão e motivação.

Aos colegas Glayson, Oberdan, Henrique, Abel, Fernando, Pedro, Salmo,
Danila, Raphael e demais colegas do PPGMCS, pela amizade e troca nesses
dois anos de estudo.

A todos meus parentes e amigos.

Demais pessoas que contribuíram para a realização do mestrado e do
presente trabalho.

Meu muito obrigado a todos!

RESUMO

OTIMIZAÇÃO APLICADA AO PROBLEMA DE ENGENHARIA DE TRÁFEGO EM REDES
DEFINIDAS POR SOFTWARE.

Resumo: Em função do crescimento da internet, aumento no número de
usuários/dispositivos e mudança no padrão do tráfego tornou-se,
atualmente importante o uso da engenharia de tráfego e da otimização
como forma de melhorar o desempenho das redes de computadores. Esta
abordagem é uma alternativa ao crescente investimento em infraestrutura
das redes. No presente trabalho é proposto a otimização do uso dos
recursos de uma rede SDN utilizando Engenharia de Tráfego (TE)
considerando os requisitos de Qualidade de Serviço (QoS). A otimização é
realizada utilizando duas heurísticas híbridas (ACO+AG e ACO+DE) e as
melhores rotas encontradas foram implementadas numa rede SDN. Os
resultados do desempenho da rede SDN foram obtidos por meio da
comparação de duas redes, uma otimizada utilizando uma das heurísticas
híbridas e outra rede utilizando rotas calculadas pelo algoritmo de
Dijkstra. A rede otimizada obteve os seguintes resultados em relação a
rede usando Dijkstra: vazão média 34% superior, atraso fim-a-fim médio
51 vezes inferior, jitter médio 7,5 vezes inferior e perda de pacotes
média 510 vezes inferior. Dessa forma, os resultados sugerem que os
algoritmos propostos produziram resultados satisfatórios e cumpriram
adequadamente a tarefa de roteamento, resultando em um uso efetivo da TE
atendendo aos critérios de QoS da rede SDN.

*Palavras-Chave: ACO, AG, DE, QoS, SDN, TE.*

ABSTRACT

OPTIMIZATION APPLIED TO THE PROBLEM OF TRAFFIC ENGINEERING IN SOFTWARE
DEFINED NETWORKS.

Abstract: Due to the growth of the Internet, increase in the number of
users/devices and changes in the traffic pattern, it is now important to
use traffic engineering and optimization as a way to improve the
performance of computer networks. This approach is an alternative to
increasing investment in network infrastructure. In the present work it
is proposed the optimization of the use of the resources of an SDN
network using Traffic Engineering (TE) considering the Quality of
Service (QoS) requirements. The optimization is performed using two
hybrid heuristics (ACO+AG and ACO+DE) and the best routes found were
implemented in an SDN network. The results of the SDN network
performance were obtained through the comparison of two networks, one
optimized using one of the hybrid heuristics and another network using
routes calculated by the Dijkstra algorithm. The optimized network
obtained the following results in relation to the network using
Dijkstra: average flow 34% higher, average end-to-end delay 51 times
lower, average jitter 7.5 times lower and packet loss average 510 times
lower. Thus, the results suggest that the proposed algorithms have
produced satisfactory results and adequately fulfilled the routing task,
resulting in an effective use of the TE meeting the QoS criteria of the
SDN network.

Keywords: *ACO, GA, DE, QoS, SDN, TE.*

LISTA DE FIGURAS

Figura 1 -- Camadas da arquitetura SDN.

Figura 2 -- Desacoplamento do plano de controle e plano de dados.

Figura 3 - Visão Geral da arquitetura SDN.

Figura 4 -- Diferentes rotas definidas pela Engenharia de Tráfego (TE).

Figura 5 -- Engenharia de Tráfego (TE) do passado para o futuro.

Figura 6 -- Tela da interface GUI do Floodlight.

Figura 7 -- Comandos POST no formato JSON.

Figura 8 -- Processo da seleção do menor caminho.

Figura 9 - Pseudo-Algoritmo de Dijkstra

Figura 10 - Operações do algoritmo - DE

Figura 11 -- Operação de Mutação - DE

Figura 12 -- Operação de Cruzamento - DE

Figura 13 -- Estrutura básica de um Algoritmo Genético

Figura 14 -- Modelo Geral de Engenharia de tráfego em SDN

Figura 15 -- Modelo de otimização utilizando as heurísticas ACO e DE.

Figura 16 - Pseudo-Algoritmo ACO

Figura 17 - Pseudo-Algoritmo DE

Figura 18 -- Modelo de otimização utilizando as heurísticas ACO e AG.

Figura 19 - Pseudo-Algoritmo DE

Figura 20 -- Topologia adotada - Adaptado de Maia (2006).

Figura 21 -- Gráfico de desempenho do modelo ACO+AG variando os
parâmetros do Algoritmo ACO: Número de Formigas e Iterações.

Figura 22 -- Gráfico de desempenho do modelo ACO+DE variando os
parâmetros do Algoritmo ACO: Número de Formigas e Iterações.

Figura 23 -- Gráfico de desempenho dos algoritmos AC+AG variando os
parâmetros de probabilidade de mutação (Pm) e probabilidade de
cruzamento (Pc) do algoritmo AG.

Figura 24 -- Gráfico de desempenho dos algoritmos ACO+DE variando o
parâmetro de probabilidade de cruzamento (Pcr) do algoritmo DE.

Figura 25 -- Topologia considerando as portas dos dispositivos ligando
os enlaces

Figura 26 -- Tela do Floodlight mostrando as tabelas do Switch 17.

Figura 27 -- Tela do Mininet mostrando hostes executando os comandos de
fluxo do D-ITG

Figura 28 -- Tela do sFlow-RT (Flow Trend) mostrando vários fluxos
injetados na rede

Figura 29 -- Tela do sFlow-RT (Top Flows) mostrando vários fluxos
injetados na rede.

Figura 30 -- Comparativo de Desempenho entre ACO+AG, ACO+DE e Dijkstra
com 100 execuções com 200 iterações.

Figura 31 - Comparativo de Desempenho entre ACO+AG, ACO+DE e Dijkstra
com 100 execuções.

Figura 32 -- Resultado médio dos 5 testes realizados entre a Rede
Otimizada (ACO+AG) e a Rede usando Dijkstra.

Figura 33 -- Resultados da Aplicação 1 do IP:10.0.1.52 para o
IP:10.0.1.49

Figura 34 -- Resultados da Aplicação 2 do IP:10.0.1.1 para o
IP:10.0.1.33

Figura 35 -- Resultados da Aplicação 3 do IP:10.0.1.2 para o
IP:10.0.1.51

Figura 36 -- Resultados da Aplicação 4 do IP:10.0.1.3 para o
IP:10.0.1.50

Figura 37 -- Resultados da Aplicação 5 do IP:10.0.1.4 para o
IP:10.0.1.37

Figura 38 -- Resultados da Aplicação 6 do IP:10.0.1.31 para o
IP:10.0.1.36

Figura 39 -- Resultados da Aplicação 7 do IP:10.0.1.32 para o
IP:10.0.1.46

Figura 40 -- Resultados da Aplicação 8 do IP:10.0.1.5 para o
IP:10.0.1.48

Figura 41 -- Resultados da Aplicação 9 do IP:10.0.1.6 para o
IP:10.0.1.47

Figura 42 -- Resultados da Aplicação 10 do IP:10.0.1.7 para o
IP:10.0.1.34

Figura 43 -- Resultados da Aplicação 11 do IP:10.0.1.8 para o
IP:10.0.1.44

Figura 44 -- Resultados da Aplicação 12 do IP:10.0.1.9 para o
IP:10.0.1.43

Figura 45 -- Resultados da Aplicação 13 do IP:10.0.1.11 para o
IP:10.0.1.41

Figura 46 -- Resultados da Aplicação 14 do IP:10.0.1.10 para o
IP:10.0.1.42

Figura 47 -- Resultados da Aplicação 15 do IP:10.0.1.12 para o
IP:10.0.1.40

Figura 48 -- Resultados da Aplicação 16 do IP:10.0.1.13 para o
IP:10.0.1.39

Figura 49 -- Resultados da Aplicação 17 do IP:10.0.1.30 para o
IP:10.0.1.45

# 

# 

# 

# 

LISTA DE TABELAS

Tabela 1 -- Demandas de Vazão, Atraso e Prioridade de tráfego de
diferentes aplicações

Tabela 2 -- Limites de Largura de Banda e Atraso mínimo dos enlaces do
núcleo da rede.

Tabela 3 - Teste de ajuste dos parâmetros do algoritmo ACO (Modelo
ACO+AG).

Tabela 4 - Resultados do teste de ajuste dos parâmetros do algoritmo ACO
(Modelo ACO+AG).

Tabela 5 - Teste de ajuste dos parâmetros do algoritmo ACO (Modelo
ACO+DE).

Tabela 6 - Resultados do teste de ajuste dos parâmetros do algoritmo ACO
(Modelo ACO+DE).

Tabela 7 - Teste de ajuste dos parâmetros do algoritmo AG (Modelo
ACO+AG)

Tabela 8 - Resultados do teste de ajuste dos parâmetros do algoritmo AG

(Modelo ACO+AG).

Tabela 9 - Teste de ajuste dos parâmetros do algoritmo DE (Modelo
ACO+DE)

Tabela 10 - Resultados do teste de ajuste dos parâmetros do algoritmo DE

(Modelo ACO+DE).

Tabela 11 -- Topologia 1: Tipo de Protocolo, Tipo da Aplicação, Demandas
de Vazão e Atraso.

Tabela 12 -- Resultados comparativo de Desempenho entre ACO+AG, ACO+DE e
Dijkstra com 200 iterações.

Tabela 13 -- Resultados comparativo de Desempenho entre ACO+AG, ACO+DE e
Dijkstra com mesmo tempo computacional.

Tabela 14 -- Resultado médio geral comparando a rede otimizada (ACO+AG)
e a rede usando Dijkstra.

# 

LISTA DE QUADROS

Quadro 1 -- Resultados do teste 1 e 2 do Algoritmo ACO.

Quadro 2 -- Taxas constantes de injeção em relação as vazões de
referência.

Quadro 3 -- Rotas encontradas pelos algoritmos ACO+AG.

Quadro 4 -- Rotas encontradas pelo algoritmo Dijkstra.

Quadro 5 -- Largura de Banda utilizada nos enlaces (Mbps).

Quadro 6 -- Resultados da vazão e perda de pacotes entre a rede
otimizada (ACO+AG) e a rede usando Dijkstra em cada aplicação.

Quadro 7 -- Resultados do atraso fim-a-fim e jitter entre a rede
otimizada (ACO+AG) e a rede usando Dijkstra em cada aplicação.

LISTA DE ABREVIATURAS E SIGLAS

ACO Ant Colony Optimization (Algoritmo da Colônia de Formigas)

AG Algoritmo Genético

AODV Ad hoc On-Demand Distance Vector (Vetor de Distâncias Por Demanda
para Redes Ad Hoc)

API Application Programming Interface (Interface de programação de
aplicativos)

ARPA Defense Advanced Research Projects Agency (Agência de Projetos de
Pesquisa Avançada de Defesa)

ATM Asynchronous Transfer Mode (Modo de Transferência Assíncrono)

CMU Carnegie Mellon University (Universidade Carnegie Mellon)

DE Differential Evolution (Evolução Diferencial)

D-ITG Distributed Internet Traffic Generator (Gerador Distribuído de
Tráfego da Internet)

DSDV Destination-Sequenced Distance-Vector (Vetor de Distância
Sequenciado por Destino)

DSR Dynamic Source Routing (Roteamento Dinâmico pela Origem)

ELD Economic Load Dispatch (Problema de Despacho de Carga Econômica)

FO Função Objetivo

FS Features Selection (Seleção de Recursos)

GUI Graphical User Interface (Interface gráfica do usuário)

HTTP Hypertext Transfer Protocol (Protocolo de Transferência de
Hipertexto)

IETF Internet Engineering Task Force (Força-Tarefa de Engenharia da
Internet)

IP Internet Protocol (Protocolo de Internet)

IRTF Internet Research Task Force (Força-Tarefa de Pesquisa na Internet)

JSON JavaScript Object Notation (Notação de Objeto JavaScript)

MIT Massachusetts Institute of Technology (Instituto de Tecnologia de
Massachusetts)

MPLS Multi-Protocol Label Switching (Comutação de Rótulos
Multiprotocolo)

NOS Network Operacional System (Sistema Operacional de Rede)

ONF Open Networking Foundation (Fundação Open Network)

OSPF Open Shortest Path First (Abrir Primeiro o Caminho Mais Curto)

Pc Probabilidade de Cruzamento (Algoritmo AG)

Pcr Probabilidade de Cruzamento (Algoritmo DE)

PCV Problema do Caixeiro-Viajante

Pm Probabilidade de Mutação (Variável do Algoritmo AG)

PSNR Peak Signal-To-Noise Ratio (Relação Sinal-Ruído de Pico)

QoS Quality of Service (Qualidade de Serviço)

SDN Software Defined Networking (Rede Definida por Software)

STP Spanning Tree Protocol (Protocolo de Árvore de Abrangência)

TCP Transport Control Protocol (Protocolo de Controle de Transporte)

TE Traffic Engineering (Engenharia de Tráfego)

TSP Traveling Salesman Problem (Problema do Caixeiro-Viajante)

UCB University of California in Berkeley (Universidade da Califórnia em
Berkeley)

UDP User Datagram Protocol (Protocolo de Datagrama do Usuário

SUMÁRIO

**RESUMO**

**ABSTRACT**

**LISTA DE FIGURAS**

**LISTA DE TABELAS**

**LISTA DE QUADROS**

**LISTA DE ABREVIATURAS E SIGLAS**

#  {#section-5 .TOC-Heading}

[1. INTRODUÇÃO [1](#introdução)](#introdução)

[1.1 Objetivos [1](#objetivos)](#objetivos)

[1.1.1 Objetivo Geral [1](#objetivo-geral)](#objetivo-geral)

[1.1.2 Objetivos Específicos
[2](#objetivos-específicos)](#objetivos-específicos)

[1.3 Justificativa [2](#justificativa)](#justificativa)

[1.4 Estrutura do Trabalho
[2](#estrutura-do-trabalho)](#estrutura-do-trabalho)

[2. REDES DEFINIDAS POR SOFTWARE
[4](#redes-definidas-por-software)](#redes-definidas-por-software)

[2.1 Introdução [4](#introdução-1)](#introdução-1)

[2.1.1 O Conceito de Redes Definidas Por Software
[8](#o-conceito-de-redes-definidas-por-software)](#o-conceito-de-redes-definidas-por-software)

[2.1.2 Desacoplamento do plano de controle e plano de dados
[10](#desacoplamento-do-plano-de-controle-e-plano-de-dados)](#desacoplamento-do-plano-de-controle-e-plano-de-dados)

[2.1.3 A Arquitetura SDN [11](#a-arquitetura-sdn)](#a-arquitetura-sdn)

[2.1.4 O Protocolo OpenFlow
[14](#o-protocolo-openflow)](#o-protocolo-openflow)

[2.1.5 Controladores SDN [14](#controladores-sdn)](#controladores-sdn)

[2.1.6 Aplicações das Redes SDN
[15](#aplicações-das-redes-sdn)](#aplicações-das-redes-sdn)

[2.2 Qualidade de Serviço (QoS)
[16](#qualidade-de-serviço-qos)](#qualidade-de-serviço-qos)

[2.3 Engenharia de Tráfego
[16](#engenharia-de-tráfego)](#engenharia-de-tráfego)

[2.4 Softwares utilizadas na implementação das Redes SDN e dos
Algoritmos de Otimização.
[20](#softwares-utilizadas-na-implementação-das-redes-sdn-e-dos-algoritmos-de-otimização.)](#softwares-utilizadas-na-implementação-das-redes-sdn-e-dos-algoritmos-de-otimização.)

[2.4.1 Mininet [20](#mininet)](#mininet)

[2.4.2 Controlador Floodlight
[21](#controlador-floodlight)](#controlador-floodlight)

[2.4.3 D-ITG [23](#d-itg)](#d-itg)

[2.4.4 SFLOW-RT [23](#sflow-rt)](#sflow-rt)

[2.4.5 MATLAB [24](#matlab)](#matlab)

[2.5 Considerações Finais
[24](#considerações-finais)](#considerações-finais)

[3. MÉTODOS DE OTIMIZAÇÃO
[25](#métodos-de-otimização)](#métodos-de-otimização)

[3.1 Métodos de Otimização Combinatória
[25](#métodos-de-otimização-combinatória)](#métodos-de-otimização-combinatória)

[3.2 O Algoritmo de Dijkstra
[27](#o-algoritmo-de-dijkstra)](#o-algoritmo-de-dijkstra)

[3.3 O Algoritmo de Otimização por Colônia De Formigas -- ACO
[28](#o-algoritmo-de-otimização-por-colônia-de-formigas-aco)](#o-algoritmo-de-otimização-por-colônia-de-formigas-aco)

[3.4 O Algoritmo de Evolução Diferencial (Differential Evolution -- DE)
[31](#o-algoritmo-de-evolução-diferencial-differential-evolution-de)](#o-algoritmo-de-evolução-diferencial-differential-evolution-de)

[3.5 Algoritmos Genéticos - AG
[35](#algoritmos-genéticos---ag)](#algoritmos-genéticos---ag)

[3.6 Trabalhos Relacionados
[37](#trabalhos-relacionados)](#trabalhos-relacionados)

[3.7 Considerações Finais
[41](#considerações-finais-1)](#considerações-finais-1)

[4. O MODELO DE ENGENHARIA DE TRÁFEGO APLICADO ÀS REDES DEFINIDAS POR
SOFTWARE
[42](#o-modelo-de-engenharia-de-tráfego-aplicado-às-redes-definidas-por-software)](#o-modelo-de-engenharia-de-tráfego-aplicado-às-redes-definidas-por-software)

[4.1 Método Proposto [42](#método-proposto)](#método-proposto)

[4.2 Modelo Geral de Engenharia de tráfego em SDN
[43](#modelo-geral-de-engenharia-de-tráfego-em-sdn)](#modelo-geral-de-engenharia-de-tráfego-em-sdn)

[4.3 Modelagem do Problema de Engenharia de Tráfego
[44](#modelagem-do-problema-de-engenharia-de-tráfego)](#modelagem-do-problema-de-engenharia-de-tráfego)

[4.4 Modelo de Otimização utilizando as Heurísticas ACO e DE
[46](#modelo-de-otimização-utilizando-as-heurísticas-aco-e-de)](#modelo-de-otimização-utilizando-as-heurísticas-aco-e-de)

[4.4.1 Algoritmo ACO - AntNet com parâmetros de largura de banda
[48](#algoritmo-aco---antnet-com-parâmetros-de-largura-de-banda)](#algoritmo-aco---antnet-com-parâmetros-de-largura-de-banda)

[4.4.2 Algoritmo DE aplicado a seleção de rotas
[50](#algoritmo-de-aplicado-a-seleção-de-rotas)](#algoritmo-de-aplicado-a-seleção-de-rotas)

[4.5 Modelo de Otimização utilizando ACO e AG
[52](#modelo-de-otimização-utilizando-aco-e-ag)](#modelo-de-otimização-utilizando-aco-e-ag)

[4.5.1 Algoritmo AG aplicado a seleção de rotas
[53](#algoritmo-ag-aplicado-a-seleção-de-rotas)](#algoritmo-ag-aplicado-a-seleção-de-rotas)

[4.6 Modelo de comparação utilizando o algoritmo de Dijkstra
[54](#modelo-de-comparação-utilizando-o-algoritmo-de-dijkstra)](#modelo-de-comparação-utilizando-o-algoritmo-de-dijkstra)

[4.7 Considerações Finais
[54](#considerações-finais-2)](#considerações-finais-2)

[5. IMPLEMENTAÇÕES DOS ALGORITMOS DE OTIMIZAÇÃO E REDE SDN
[55](#implementações-dos-algoritmos-de-otimização-e-rede-sdn)](#implementações-dos-algoritmos-de-otimização-e-rede-sdn)

[5.1 Propriedades da Topologia
[55](#propriedades-da-topologia)](#propriedades-da-topologia)

[5.2 Implementação e ajustes dos parâmetros do algoritmo de roteamento
ACO
[58](#implementação-e-ajustes-dos-parâmetros-do-algoritmo-de-roteamento-aco)](#implementação-e-ajustes-dos-parâmetros-do-algoritmo-de-roteamento-aco)

[5.2.1 Teste 1: Ajuste dos parâmetros do algoritmo ACO (Modelo ACO+AG)
[59](#teste-1-ajuste-dos-parâmetros-do-algoritmo-aco-modelo-acoag)](#teste-1-ajuste-dos-parâmetros-do-algoritmo-aco-modelo-acoag)

[5.2.2 Teste 2: Teste de ajuste dos parâmetros do algoritmo ACO (Modelo
ACO+DE)
[61](#teste-2-teste-de-ajuste-dos-parâmetros-do-algoritmo-aco-modelo-acode)](#teste-2-teste-de-ajuste-dos-parâmetros-do-algoritmo-aco-modelo-acode)

[5.3 Testes e ajustes dos parâmetros dos algoritmos AG e DE
[64](#testes-e-ajustes-dos-parâmetros-dos-algoritmos-ag-e-de)](#testes-e-ajustes-dos-parâmetros-dos-algoritmos-ag-e-de)

[5.3.1 Teste 3: Ajuste dos parâmetros do algoritmo AG (Modelo ACO+AG)
[64](#teste-3-ajuste-dos-parâmetros-do-algoritmo-ag-modelo-acoag)](#teste-3-ajuste-dos-parâmetros-do-algoritmo-ag-modelo-acoag)

[5.3.2 Teste 4: Ajuste dos parâmetros do algoritmo DE (Modelo ACO+DE)
[66](#teste-4-ajuste-dos-parâmetros-do-algoritmo-de-modelo-acode)](#teste-4-ajuste-dos-parâmetros-do-algoritmo-de-modelo-acode)

[5.4 Implementação da rede SDN
[68](#implementação-da-rede-sdn)](#implementação-da-rede-sdn)

[5.4.1 Geração dos comandos POST via código Matlab
[70](#geração-dos-comandos-post-via-código-matlab)](#geração-dos-comandos-post-via-código-matlab)

[5.4.2 Injeção de tráfego na rede utilizando o D-ITG
[72](#injeção-de-tráfego-na-rede-utilizando-o-d-itg)](#injeção-de-tráfego-na-rede-utilizando-o-d-itg)

[5.4.3 Sflow-rt [74](#sflow-rt-1)](#sflow-rt-1)

[5.5 Considerações Finais
[77](#considerações-finais-3)](#considerações-finais-3)

[6. RESULTADOS [78](#resultados)](#resultados)

[6.1 Resultados Comparativos dos algoritmos
[78](#resultados-comparativos-dos-algoritmos)](#resultados-comparativos-dos-algoritmos)

[6.1.1 Resultados comparativo considerando limite de iterações
[78](#resultados-comparativo-considerando-limite-de-iterações)](#resultados-comparativo-considerando-limite-de-iterações)

[6.1.2 Resultados comparativo considerando limite de tempo computacional
[80](#resultados-comparativo-considerando-limite-de-tempo-computacional)](#resultados-comparativo-considerando-limite-de-tempo-computacional)

[6.1.3 Resultados previstos do atraso e vazão considerando as rotas
selecionadas
[82](#resultados-previstos-do-atraso-e-vazão-considerando-as-rotas-selecionadas)](#resultados-previstos-do-atraso-e-vazão-considerando-as-rotas-selecionadas)

[6.2 Resultados da Otimização Implementados na Rede SDN
[85](#resultados-da-otimização-implementados-na-rede-sdn)](#resultados-da-otimização-implementados-na-rede-sdn)

[6.2.1 Resultados comparativos entre a rede otimizada e a rede usando
Dijkstra.
[85](#resultados-comparativos-entre-a-rede-otimizada-e-a-rede-usando-dijkstra.)](#resultados-comparativos-entre-a-rede-otimizada-e-a-rede-usando-dijkstra.)

[6.3 Considerações Finais
[90](#considerações-finais-4)](#considerações-finais-4)

[7. CONCLUSÕES [92](#conclusões)](#conclusões)

[7.3 Dificuldades Encontradas
[94](#dificuldades-encontradas)](#dificuldades-encontradas)

[7.4 Limitações do Estudo
[94](#limitações-do-estudo)](#limitações-do-estudo)

[7.5 Trabalhos Futuros [94](#trabalhos-futuros)](#trabalhos-futuros)

**REFERÊNCIAS**

**APÊNDICE**

# 1. INTRODUÇÃO

O número de usuários da internet em todo o mundo, segundo um relatório
anual publicado pela União Internacional de Telecomunicações (ITU,
2017), vem alcançando um crescimento considerável. Dados desse relatório
indicavam que no ano 2000 o número de usuários era de 400 milhões de
pessoas e que em 2017 esse número já era da ordem de 3,578 bilhões de
pessoas.

O aumento de usuários e da importância da internet como uma ferramenta
para um crescente número de serviços, são fatores que vem gerando um
enorme tráfego de dados nesta e nas mais diversas redes de computadores
públicas e privadas. Isto resulta numa demanda cada vez maior por novas
tecnologias que permitam atender a um número crescente de usuários que
desejam obter acesso aos serviços, informações, relacionamentos e
conteúdos diversos dessas redes com certos níveis de exigência de
qualidade de serviço (QoS). A pesquisa e estudo dessas tecnologias são
alvo de diversos pesquisadores que trabalham no desenvolvimento de
métodos capazes de melhorar o tráfego de dados e prover bons níveis de
QoS aos atuais e futuros usuários da internet. Uma dessas diversas áreas
de pesquisa é voltada ao campo da otimização, onde busca-se melhorar o
tráfego de dados na rede sem a necessidade de grandes investimentos em
infraestrutura, através de uma utilização mais "inteligente" e eficaz da
rede.

Nesse sentido as Redes Definidas por Software (SDN, *Software Defined
Networking)* vem sendo utilizadas como uma ferramenta de Engenharia de
Tráfego (TE, *Traffic Engineering).* O Paradigma SDN possibilita o
encaminhamento dos pacotes por rotas direcionadas e, desta forma,
permitindo abordagens com o uso de otimização no roteamento dos dados.

## 1.1 Objetivos

### 1.1.1 Objetivo Geral

O Objetivo geral deste trabalho é otimizar o uso dos recursos de uma
rede SDN utilizando engenharia de tráfego considerando os requisitos de
QoS das aplicações da rede.

### 1.1.2 Objetivos Específicos

\- Estudar o problema de engenharia de tráfego aplicados às Redes SDN;

\- Formular um modelo matemático para o problema de otimização do uso
dos recursos de uma rede SDN considerando restrições e requisitos de QoS
das aplicações;

\- Propor heurísticas de otimização para o modelo formulado;

\- Implementar o algoritmo de Dijkstra para obtenção das rotas de menor
caminho;

\- Analisar o desempenho das heurísticas de otimização e do algoritmo de
Dijkstra e avaliar os resultados obtidos com a implementação destas em
uma rede SDN.

## 1.3 Justificativa

As principais justificativas para o presente trabalho são: crescimento
da internet, aumento no número de usuários, o acesso facilitado pelas
novas tecnologias, a demanda de novos conteúdos multimídia e a
consequente mudança no padrão do tráfego de determinados tipos de dados.
Nesse contexto de novas e maiores demandas, faz-se necessário o uso de
ferramentas para otimização dos recursos de infraestrutura da rede para
satisfazer os critérios de QoS. Assim o estudo de algoritmos de
roteamento mais eficazes no processo de otimização aplicados às redes
SDN são de grande importância para a investigação de diferentes métodos
e a busca por melhores desempenhos.

## 1.4 Estrutura do Trabalho

Esta dissertação está organizada da seguinte forma. O capítulo 2
apresenta as Redes Definidas por Software mostrando um resumo sobre
redes de computadores, conceitos sobre SDN, requisitos de QoS,
engenharia de tráfego e ferramentas de implementação de redes SDN. O
capítulo 3 apresenta os métodos de otimização, algoritmos utilizados e
também alguns resumos de trabalhos relacionados ao presente trabalho; o
capítulo 4 apresenta a descrição do modelo de engenharia de tráfego
aplicada às redes SDN e a descrição dos algoritmos escolhidos; o
capítulo 5 apresenta as implementações dos algoritmos e testes de
ajustes de parâmetros destes, ainda no capítulo 5 é apresentado a
implementação da rede SDN; o capítulo 6 apresenta os resultados obtidos
com as simulações dos algoritmos de Otimização e resultados de
desempenho da rede SDN emulada usando rotas calculadas por estes
algoritmos; e finalmente, o capítulo 7 apresenta as conclusões,
comentário dos resultados, dificuldades encontradas, limitações do
estudo e trabalhos futuros.

# 2. REDES DEFINIDAS POR SOFTWARE

Neste capítulo é apresentada, uma introdução aos conceitos de redes SDN
utilizadas neste trabalho. Inicialmente, na seção 2.1 é realizado uma
introdução com breve histórico das redes e na sequência a descrição do
conceito de Rede Definida por Software. A seção 2.2 descreve o conceito
de Qualidade de Serviço e a seção 2.3 descreve o conceito de Engenharia
de Tráfego. Na seção 2.4 são descritas as ferramentas utilizadas na
emulação de uma rede SDN: Mininet, Floodlight, D-ITG e sFlow-rt.
Finalizando o capítulo na seção 2.5 são realizadas as considerações
finais.

## 2.1 Introdução

As redes de computadores surgiram da necessidade do estabelecimento de
meios que permitissem a comunicação entre os computadores e os demais
equipamentos e periféricos. Quando não existiam os computadores digitais
e seus sistemas de telecomunicação, a comunicação entre máquinas
calculadoras e computadores analógicos já era realizada por usuários
humanos através do carregamento e troca de instruções entre eles.

Em 1940, George Stibitz desenvolveu uma ideia de acesso remoto e
múltiplo a um computador conectado por linhas telefônicas. Ele usou uma
máquina de teletipo para enviar instruções para um conjunto de problemas
de cálculos matemáticos escritos a partir de seu Computador em Hanover
(USA) para a sua calculadora na cidade de Nova York e recebeu os
resultados de volta (DALAKOV, 2013).

Com o advento do telefone e posteriormente a criação da rede mundial de
telefonia comutada por circuitos ou Public Switched Telephone Network,
tornou-se possível que máquinas como a de Stibitz pudessem utilizar a
rede de telefonia e se comunicar a grandes distâncias. Posteriormente
tem-se a invenção do rádio e alguns anos depois a invenção da televisão,
o que resultou em outra rede, que suportava o envio de sons e imagens
através de ondas eletromagnéticas (TELECO, 2016).

No entanto a história das redes de computadores inicia de fato na década
de 60, quando ainda a rede telefônica era a rede de comunicação mais
importante. Nesta rede os sinais eram transmitidos via comutação de
circuitos usando taxa constante. Nessa época foram criados os primeiros
terminais interativos, que permitiam ao usuário acessar remotamente os
imensos computadores da época (KUROSE & ROSS, 2010).

Ainda durante essa década (anos 60) é que foi idealizada uma grande rede
de comunicação. Pensando uma maneira de transformar a comutação de
circuitos em uma comutação de pacotes, três grupos de pesquisadores de
forma isolada realizaram seus estudos nessa mesma época. Grupos
liderados por Leonard Kleinrock, Paul Baran, Donald Davies e Lawrence
Roberts, desenvolveram independentemente conceitos de sistemas de redes
os quais usavam datagramas ou pacotes, que podiam ser usados em uma rede
de comutação de pacotes entre sistemas de computadores (DALAKOV, 2013).
Primeiramente em 1961, Leonard Kleinrock, trabalhando nos laboratórios
do MIT (Massachusetts Institute of Technology - EUA) usou a teoria das
filas, para realizar a comutação de pacotes baseada no tráfego em
rajadas. Por volta de 1964, Paul Baran do Rand Institute começou a
estudar o uso da comutação de pacotes para a segurança da transmissão de
voz em redes militares. Enquanto isso na Inglaterra, Donald Davies e
Roger Scantlebury desenvolviam ideias sobre a comutação de pacotes no
National Physical Laboratory. Segundo Kurose e Ross (2010) estes
trabalhos, juntamente com o de Lawrence Roberts (MIT) líder do projeto
na ARPA (Agência de Projetos de Pesquisa Avançada - EUA) foram
determinantes para o salto de desenvolvimento dos conceitos e
componentes da futura rede que se chamaria internet.

Uma parcela significativa de tudo o que foi desenvolvido durante essa
época tinha objetivo de atender a objetivos militares em função da
necessidade da descentralização geográfica da informação, pois nessa
época o mundo ainda vivenciava a Guerra Fria.

Por volta de 1967, Lawrence Roberts publicou a ARPANET (Advanced
Research Projects Agency Network), precursora da grande rede mundial (a
Internet), sendo a primeira rede de computadores por comutação de
pacotes (KUROSE & ROSS, 2010). Posteriormente, ao combinar os protocolos
TCP e IP, em 1973, a ARPANET ganhou escalabilidade e a capacidade de
incluir sistemas de arquiteturas diversas e logo, o crescimento do
número de usuários tornou-se exponencial. Em meados da década de 80, as
pessoas começaram a ver um conjunto de redes como uma inter-rede e, mais
tarde, como a Internet (TANENBAUM, 2003).

O desenvolvimento de microcomputadores com maior capacidade de
processamento permitiu a instalação de considerável poder computacional
em diversas localizações, ao invés da concentração em poucos locais
(PISKE, 2012). Com a chegada da Web e dos navegadores com interface
gráfica na década de 90, tem-se enfim a inclusão dos usuários domésticos
na rede, e o início do fenômeno comercial e cultural que se tornou a
Internet.

Apresentado o desenvolvimento histórico das redes de computadores ao
longo de algumas décadas. Agora são apresentadas as motivações de
mudança e evolução das redes atuais devido aos problemas enfrentados
atualmente em função do crescimento das redes.

Nesse contexto pode-se afirmar que crescimento das redes de computadores
resultou em um grande aumento do número de conexões e no tráfego de
dados. Principalmente devido ao aumento de usuários, dispositivos e
novas aplicações, tornando assim as grandes redes difíceis de serem
gerenciadas e configuradas devido a sua grande complexidade e dinamismo.
Estas redes geralmente compõem um grande número de switches, roteadores,
firewalls e vários tipos de dispositivos com um grande número de eventos
ocorrendo simultaneamente. Infelizmente nas redes convencionais atuais
esses dispositivos de rede são normalmente caixas pretas verticalmente
integradas, ou seja, são dispositivos que cuidam de todo o processo e
encaminhamento e gestão dos pacotes de forma independente através de
algoritmos especiais e sem que os administradores da rede tenham
acesso/controle ao seu firmware de forma fácil e usando linguagem de
alto nível (KIM & FEAMSTER, 2013). Em geral estes dispositivos são
componentes dedicados de hardware/software proprietários em geral
constituídos de CIAEs (Circuitos Integrados de Aplicação Específica) (HU
et al., 2014).

Estes dispositivos são em sua maioria sistemas proprietários com
desenvolvimento fechado variando de um fornecedor para outro. Portanto
tornou-se extremamente difícil de introduzir e implantar novos
protocolos. As \"atualizações\" de novos métodos e comandos de
configuração são geralmente ditadas unilateralmente por esses
fornecedores. Enquanto isso, requisitos para mais funcionalidades e
políticas de rede são cada vez mais complexas e continuam a expandir-se
(KIM & FEAMSTER, 2013).

Os administradores de redes que são responsáveis pela configuração da
rede, aplicando várias políticas de alto nível e respondendo a uma ampla
gama de eventos que podem ocorrer na rede (por exemplo, mudanças de
tráfego, intrusões, etc.), tem se deparado com um enorme desafio ao
realizar esta tarefa. Esse processo tornou-se incrivelmente difícil
porque a implementação dessas políticas de alto nível exige
especificá-las em termos de códigos distribuídos nos diferentes
dispositivos usando comandos de baixo nível (KIM & FEAMSTER, 2013).

Além disso, existe outro problema que é a limitação dos dispositivos de
rede atuais quando submetidos a grandes taxas de tráfego. Estes
dispositivos precisam tratar de forma distinta um conjunto de diferentes
tipos de pacotes com base na sua natureza e conteúdo. Em função das
características das redes IPs convencionais que tratam todo o tráfego
entrante de forma igualitária, isto pode resultar em uma considerável
queda na QoS oferecidas a essas aplicações. Assim os dispositivos de
rede atuais não têm a flexibilidade de lidar com diferentes tipos de
pacotes com vários conteúdos por causa da implementação hardwarizada
subjacente das regras de roteamento (HU et al., 2014).

Então, pode-se concluir que, com as mudanças no padrão do tráfego devido
ao uso de novas aplicações, tecnologias, dispositivos, grande quantidade
de informações e serviços cada vez mais complexos e exigentes, tornou-se
imperativo e necessário que a Internet evolua para abordar esses novos
desafios. Além disso, as redes, que compõem a estrutura central da
Internet, precisariam ser capazes de se adaptar a esse novo cenário, no
entanto essas redes tradicionais não possuem essa flexibilidade e não
podem ser facilmente reprogramadas ou reconfiguradas.

O conceito de uma estrutura distribuída com diversos dispositivos
autônomos permitiu o crescimento das redes, mas infelizmente, esse
conceito que foi benéfico anteriormente se tornou atualmente uma
limitação ao crescimento delas. Esse grande aumento na dimensão e
complexidade das redes impactou na eficiência do gerenciamento,
escalabilidade e também nos custos.

Sabe-se que atualmente quase toda a nossa sociedade depende em maior ou
menor proporção da internet e dos serviços derivados dela, sendo
relevante a sua enorme base de implantação e o fato de ser considerada
parte da infraestrutura crítica da nossa sociedade (assim como
transporte e redes elétricas). Sendo assim, qualquer mudança na sua
estrutura pode não ser bem vista entre os administradores de redes,
devido ao fato destes não arriscarem a implementação de novos serviços
que possam indisponibilizar, mesmo que por pouco tempo, o uso da rede,
ou que não sejam efetivamente melhores. Assim, a Internet torna-se
extremamente difícil de evoluir tanto em termos de infraestrutura
física, quanto em seus protocolos e desempenho (NUNES et al., 2014).

Essas dificuldades levaram diversos pesquisadores a afirmar que a
arquitetura de redes de computadores em geral e a rede mundial (a
Internet) atingiram um nível de amadurecimento que as tornaram pouco
flexíveis. A expressão usada em muitos casos é que a Internet está
calcificada (ossified, em inglês), referindo-se ao processo que
substitui cartilagens (mais elásticas) por ossos ao longo do
envelhecimento dos seres vivos (GUEDES et al., 2012).

Algumas das necessidades atuais só podem ser solucionadas com mudanças
estruturais, portanto é necessária uma nova arquitetura para atender os
requisitos atuais e os requisitos das futuras aplicações que serão ainda
propostas.

Uma possível solução para este problema é a implementação das regras de
gerenciamento de dados como módulos de software em vez de
incorporando-os em hardware. Este método permite que os administradores
da rede tenham mais controle sobre o tráfego da rede e, portanto, tem um
grande potencial para melhorar grandemente o desempenho da rede em
termos de uso eficiente de recursos.

### 2.1.1 O Conceito de Redes Definidas Por Software

Esse conceito de redes fazendo o uso de software ou redes programáveis
foi proposta como uma maneira de facilitar a evolução das redes
tradicionais, sendo então definida de forma inovadora e tecnológica e
sendo chamada de Redes Definidas por Software (Redes SDN). Seu conceito
foi originalmente proposto pela Nicira Networks com base em seu
desenvolvimento anterior nas universidades americanas de Stanford, CMU,
UCB e Princeton (HU et al., 2014).

O termo SDN foi originalmente inventado para representar as ideias e
trabalhar em torno de um protocolo chamado de OpenFlow (detalhado em
2.2.5), sendo um novo paradigma de rede em que o hardware de
encaminhamento é desacoplado das decisões de controle, com objetivo de
fornecer serviços abertos, controlados pelo usuário por meio do
gerenciamento do hardware de encaminhamento (geralmente switches ou
roteadores).

A Figura 1 mostra a separação das camadas da arquitetura SDN. O plano de
gerenciamento (usuários e aplicativos), plano de controle e o plano de
dados respectivamente.

![](media/image1.png){width="4.949916885389326in"
height="3.4180479002624673in"}

Figura 1 -- Camadas da arquitetura SDN.

Fonte: Adaptado de KREUTZ et al. (2015).

Em SDN, a lógica de controle baseada em software é implementada em um
controlador (plano de controle) com conhecimento global do estado da
rede, enquanto os dispositivos de rede tornam-se simples dispositivos de
encaminhamento de pacotes (plano de dados) que podem ser programados
através de uma interface do controlador (KIM & FEAMSTER, 2013).

A principal ideia é permitir que os desenvolvedores de software que
dependam de recursos da rede, obtenham acesso a esses recursos de
maneira fácil, da mesma forma que eles já fazem no caso de recursos
computacionais. A grande vantagem do uso de um software controlador da
rede ou mesmo um sistema operacional da rede (NOS) é poder trabalhar em
um nível mais alto de abstração. Dessa forma, pode-se observar que um
sistema assim pode oferecer uma plataforma de controle/interface que
facilite a programação centralizada e uniforme de toda a rede e que
forneça abstrações que permitam o desenvolvimento de funções, serviços e
aplicativos de rede mais sofisticados. Assim vários aplicativos podem
tirar proveito das mesmas informações de rede e a integração de
diferentes aplicativos se tornaria mais direta, além de tornar as
políticas da rede mais consistentes e efetivas (MCKEOWN et al.,2008).

Essa mudança de paradigma traz vários benefícios e promete simplificar
drasticamente a gestão das redes e a habilitação de inovações, gerando
uma considerável evolução em comparação com ao modelo de redes atual. É
muito mais fácil de implementar novas ideias na rede através de um
programa ou software, devido a maior facilidade de modificar e manipular
dados via programação ao invés de ter que usar um conjunto restrito de
comandos em dispositivos de rede proprietários (KIM & FEAMSTER, 2013).

Para melhor entendimento sobre o conceito de SDN é importante entender
os conceitos de plano de controle e plano de dados. Pode-se defini-los
da seguinte maneira:

O Plano de Controle é onde se executa os códigos dos protocolos de
roteamento e se determinam as rotas para onde serão encaminhados os
pacotes. Após obter essa informação, ela deve ser preenchida na tabela
de encaminhamento a ser utilizada pelo plano de dados.

Plano de dados é responsável por lidar com o encaminhamento dos pacotes
que chegam ao dispositivo e, por meio de uma regra simples, verificar na
tabela de encaminhamento do dispositivo para qual interface o mesmo
deverá ser encaminhado.

### 2.1.2 Desacoplamento do plano de controle e plano de dados

Nas redes atuais os dispositivos de encaminhamento têm no seu
firmware/hardware o plano de controle e o plano de dados acoplados e
centralizados naquele dispositivo.

Em contraste, o conceito de SDN desacopla o plano de controle dos
dispositivos de rede e cria-se uma entidade externa chamada de
controlador SDN.

Na Figura 2 (a) é mostrado o modelo de redes tradicionais em que
dispositivos de encaminhamento (switches e/ou roteadores) possuem o
plano de controle embutidos individualmente.

![](media/image2.png){width="5.90625in" height="4.739583333333333in"}

Figura 2 -- Desacoplamento do plano de controle e plano de dados.

Fonte: Adaptado de NUNES et al. (2014).

Na Figura 2 (b) é mostrada uma rede SDN com um controle da rede
desacoplado dos dispositivos de encaminhamento. Dessa forma, todo o
controle fica centralizado naquele controlador. As linhas sólidas
definem os enlaces do plano de dados e as linhas tracejadas os enlaces
do plano de controle. O plano de controle pode enviar comandos para os
planos de dados do hardware (switches ou roteadores). Este paradigma
fornece uma visão de toda a rede e ajuda a fazer mudanças globalmente.

### 2.1.3 A Arquitetura SDN

Para identificação dos diferentes elementos do conceito SDN apresenta-se
na Figura 3 a definição das camadas do modelo de arquitetura SDN e os
seus principais componentes.

![](media/image3.png){width="5.905555555555556in"
height="3.229861111111111in"}

Figura 3 - Visão Geral da arquitetura SDN.

Fonte: Adaptado de AKYILDIZ et al. (2016).

Segundo a ONF (Open Networking Foundation - Fundação responsável pela
padronização do protocolo OpenFlow) a arquitetura SDN é constituída
pelos seguintes componentes e camadas (GIESEN & OLIVEIRA, 2017):

- Camada de Aplicação:

> É o conjunto de aplicações dos usuários que utilizam os serviços SDN.
> A comunicação entre a camada de aplicação e a camada de controle é
> realizada através da Northbound API (Application Programming
> Interface), cuja finalidade é simplificar a implementação de serviços
> de rede comuns, por exemplo, roteamento, multicast, monitoramento,
> segurança, controle de acesso, gerenciamento de largura de banda,
> engenharia de tráfego, QoS, eficiência energética, etc.

- Camada de Controle:

> A camada de controle pode ser vista como o \"cérebro da rede' e dentro
> dessa camada está o controlador SDN que fornece a funcionalidade de
> controle logicamente centralizado, supervisionando o comportamento de
> encaminhamento de dados através de uma interface aberta (OpenFlow). A
> comunicação entre a camada de controle e a camada de dados é realizada
> através da Southbound API (protocolo OpenFlow) que envia as
> informações que definem a programação dos dispositivos de
> encaminhamento. O Plano de controle possui visão global de toda a
> rede.

- Camada de dados (Infraestrutura):

> A Camada de dados consiste na infraestrutura de rede composta pelos
> elementos de rede e dispositivos de encaminhamento (Switches OpenFlow
> (OF) e Roteadores) que representam o plano de dados e realizam o
> tratamento e o direcionamento de pacotes.

Na arquitetura SDN, utilizando o protocolo OpenFlow, os dispositivos de
encaminhamento ou o switch OpenFlow contém uma ou mais tabelas de fluxo
e uma camada de abstração que se comunica de forma segura com um
controlador via protocolo OpenFlow. As tabelas de fluxo consistem em
entradas de fluxo, cada uma das quais determina como os pacotes
pertencentes a um fluxo serão processados ​​e encaminhados. A comunicação
entre controlador e switch ocorre através do protocolo OpenFlow, que
define um conjunto de mensagens que podem ser trocadas entre essas
entidades através de um canal seguro. Usando o protocolo OpenFlow, um
controlador remoto pode, por exemplo, adicionar, atualizar ou excluir
entradas de fluxo das tabelas dos switches. Isso pode acontecer de forma
reativa (em resposta a uma chegada de pacote) ou proativamente (KIM &
FEAMSTER, 2013).

A comunicação entre as camadas da arquitetura SDN é realizada por meio
das seguintes APIs: Southbound API e Northbound API (JARSCHEL et al.,
2014). A Southbound API representa a interface de comunicação entre o
plano de controle e o plano de dados, ou seja, a comunicação entre a
camada de controle (controlador SDN) e camada de infraestrutura
(dispositivos de encaminhamento). Essa interface também define o
protocolo de comunicação entre os dispositivos de encaminhamento e os
elementos do plano de controle. Este protocolo formaliza o método como o
controle e os elementos do plano de dados interagem. A Northbound API
permite a troca de informações entre a camada de aplicações que estão
sendo executadas e o controlador SDN ou Sistema operacional de rede do
inglês NOS (Network Operacional System), ou seja, uma interface comum
para o desenvolvimento de aplicações. Ainda não há uma padronização para
esta interface.

Além desses conceitos de camadas e APIs tem-se também fisicamente na
rede os dispositivos de encaminhamento que são dispositivos baseados em
hardware ou software que executam um conjunto de operações elementares.
Os dispositivos de encaminhamento possuem um conjunto de instruções bem
definidas (por exemplo, regras de fluxo) necessários para realizar
tratamento dos pacotes de entrada. São exemplos de dispositivos de
encaminhamentos os Switches OpenFlow (OF) e os Roteadores.

### 2.1.4 O Protocolo OpenFlow

Existe uma série de protocolos padrão para uso de SDN em aplicações
reais. Um dos protocolos padrão mais populares é chamado OpenFlow e foi
proposto por um grupo de pesquisadores de Stanford como um protocolo SDN
padrão. Ele usa código aberto para controlar controladores e switches
SDN universais e atualmente muitos projetos têm sido propostos com o uso
do OpenFlow (HU et al., 2014).

OpenFlow é uma das interfaces SDN mais comuns do Southbound API. Muitos
fornecedores, incluindo HP, NEC, NetGear e IBM, produzem switches de
rede com capacidade para OpenFlow disponíveis no mercado. A Open
Networking Foundation (ONF) é responsável pela padronização do protocolo
OpenFlow. Há uma variedade de controladores OpenFlow, por exemplo, NOX,
POX, Floodlight e Maestro (KIM & FEAMSTER, 2013).

### 2.1.5 Controladores SDN 

Ao realizar a gestão da rede SDN é necessário a utilização do chamado
Controlador SDN ou Sistema operacional de rede (NOS). Esse elemento é
muito importante e necessário em virtude de ser a ponte que permite os
desenvolvedores realizarem abstrações de mais alto nível para realizar
gestão e controle da rede sem ter que usar a linguagem de baixo nível
dos dispositivos de encaminhamento, sendo esse um dos pontos
fundamentais do paradigma SDN. Dessa maneira é possível desenvolver
programas que além de ter uma visão detalhada e unificada da rede, podem
inclusive implementar funcionalidades para a tomada de decisões em
relação ao funcionamento e controle da rede com um todo (NUNES et al.,
2014).

O Controlador SDN concentra a comunicação com todos os elementos
programáveis da rede, ele traduz a política de rede em regras reais de
encaminhamento de pacotes. O controlador de rede estabelece uma conexão
para cada switch compatível com OpenFlow através desse protocolo, e
insere, exclui ou modifica as regras de encaminhamento de pacotes em
switches através desta conexão. O controlador de rede também reage a
eventos de pacotes e eventos de troca de conexão que provêm de switches
(KIM & FEAMSTER, 2013).

É importante lembrar que a camada de controle pode consistir em um ou
vários controladores, dependendo da escala da rede. Se estiver usando
múltiplos controladores, eles podem formar um peer-to-peer de alta
velocidade, em uma confiável rede de controle distribuída (HU et al.,
2014).

### 2.1.6 Aplicações das Redes SDN

Segundo Nunes et al. (2014) as Redes SDN atualmente estão atraindo
atenção significativa tanto da academia, assim como da indústria. Um
grupo de operadores de rede, provedores de serviços e fornecedores
criaram recentemente o Open Network Foundation, uma organização
orientada para a indústria, para promova SDN e padronize o protocolo
OpenFlow. Do lado o interesse acadêmico, foi criado o OpenFlow Network
Research Center com foco na pesquisa SDN. Há também foram esforços de
padronização no SDN no IETF e IRTF e outras organizações produtoras de
padrões. O campo de rede definida pelo software é bastante recente,
ainda crescendo a um ritmo muito rápido. Ainda assim, são importantes
desafios de pesquisa a serem abordados.

Em Hu et al. (2014) é comentado exemplos de aplicações do SDN e
OpenFlow. São elas: Pesquisas voltadas para a Internet, conexões em
zonas rurais, atualização de servidores e datacenters, deslocamento de
dispositivos móveis e máquinas virtuais sem fio.

## 2.2 Qualidade de Serviço (QoS)

A QoS é um conjunto de tecnologias que fornecem a capacidade de
gerenciar o tráfego de rede de maneira econômica e aprimorar as
experiências do usuário em diversos ambientes e plataformas. É utilizada
para mensurar a qualidade dos serviços oferecidos por uma rede de
comunicações, ou seja, medir o quanto ela é capaz de atender às
expectativas de seus usuários através dos serviços que a mesma oferece.
Esse conceito, inicialmente focado na rede, evoluiu para uma noção mais
ampla, contemplando as múltiplas camadas da interação usuário-sistema.

Segundo Cisco Systems (2006) o objetivo da QoS é fornecer um serviço de
rede melhor e mais previsível, fornecendo largura de banda, atraso,
jitter e perdas de pacotes dentro um nível aceitável. Quando
inteligentemente e corretamente aplicada a QoS consegue fornecer
desempenho consistente e previsível. Esse desempenho é obtido através de
ferramentas que gerenciam o congestionamento da rede, a formação de
novas rotas de tráfego utilizando conjunto de enlaces de maneira mais
eficiente, e por fim, definindo políticas de tráfego em toda a rede.

## 2.3 Engenharia de Tráfego

A Engenharia de Tráfego (Traffic Engineering ou TE) é um processo de
organização e controle dos fluxos de dados em uma rede que está ligado à
otimização de desempenho e melhor utilização de seus recursos para,
assim, evitar congestionamentos causados por uma utilização desigual da
rede (DIAS et al., 2003). Um dos principais objetivos da engenharia de
tráfego é fazer com que a operação de troca de dados na rede seja
eficiente e confiável concomitante com a melhoria de seu desempenho.

Considerando o alto valor dos equipamentos e das necessidades atuais do
mercado, a Engenharia de Tráfego já é considerada fundamental em redes
de grande porte, onde a qualidade de serviço tem se tornado cada vez
mais necessária em virtude da necessidade de atender um público cada vez
mais exigente e ávido por uso de dados multimídia (GIMENEZ et al. 2006).
O uso inteligente da TE pode resultar em melhorias para a rede como:
redução de congestionamentos, uso mais eficiente dos recursos de rede,
desempenho das aplicações, aumento de rendimento da rede, melhores
garantias de QoS e maior satisfação dos usuários. A Figura 4 mostra um
exemplo de diferentes rotas definidas com o uso de engenharia de
tráfego.

![](media/image4.png){width="5.322916666666667in"
height="4.1285520559930005in"}

Figura 4 -- Diferentes rotas definidas pela Engenharia de Tráfego (TE).

Na Figura 4 é mostrado um exemplo do uso da Engenharia de Tráfego numa
rede IP. Nesta rede os usuários com origens nos nós 1, 2 e 3 necessitam
realizar a transferência de diferentes tipos de dados até os nós 7, 8 e
9. Nesse caso, os nós 1, 2 e 3 necessitam realizar o envio e recebimento
dos dados de voz, vídeo e dados respectivamente. Com essas informações a
respeito da necessidade dos usuários (origem, destino e tipo de dado)
deve-se empregar a TE como forma de permitir aos usuários realizar o
tráfego dos seus dados na rede de forma satisfatória. Nessa topologia de
rede é possível realizar essas 3 conexões de diversas formas, por
exemplo:

1.  Sem a existência da TE: Os pacotes oriundos dessas aplicações seriam
    encaminhados pelo menor caminho -- R10 -- R13, podendo ocorrer
    congestionamento de pacotes e prejudicando a qualidade de serviço
    QoS oferecida as aplicações de voz, dados e vídeos.

2.  Com o uso da TE:

> \- O host 1 pode-se ligar ao 7 passando pelos Roteadores 10 (R10),
> 13(R13) e chegar ao host de destino 7.
>
> \- O host 2 pode-se ligar ao 8 passando pelos Roteadores 10 (R10),
> 11(R11), 12(R12), 13(R13) e chegar ao host de destino 8.
>
> \- O host 3 pode-se ligar ao 7 passando pelos Roteadores 10 (R10),
> 14(R14), 13(R13) e chegar ao host de destino 9.

Nesse exemplo relativamente simples é possível verificar que as soluções
são várias, com conexões utilizando rotas exclusivas ou compartilhadas,
usando 3 caminhos diferentes ou um mesmo caminho. No entanto conforme as
redes aumentam em tamanho, complexidade de topologia, número de usuários
e dispositivos de encaminhamento se faz necessário o uso da TE como
ferramenta para melhorar o desempenho da rede considerando as suas
restrições físicas e a demanda de recursos por parte dos usuários e
aplicações.

A TE permite que o controle dos fluxos de dados em uma rede, seja
realizado de forma mais eficiente, com objetivo de melhorar a utilização
de seus recursos e prover melhor desempenho aos usuários. A Figura 5
mostra a evolução da Engenharia de tráfego em diferentes redes de
computadores.

![](media/image5.png){width="7.537824803149606in"
height="3.896551837270341in"}

Figura 5 -- Engenharia de Tráfego (TE) do passado para o futuro.

Fonte: AKYILDIZ et al. (2014).

Conforme a Figura 5, segundo Akyildiz et al. (2014) a TE tem sido
amplamente explorada nas redes de dados passadas e atuais, com
tecnologias como ATM, IP e MPLS. No entanto, os paradigmas de redes
passadas e atuais, bem como suas correspondentes soluções TE estão
desvantagem em relação aos paradigmas de redes da próxima geração e seu
gerenciamento de rede devido a duas razões principais. Primeiro, os
aplicativos atuais da Internet exigem uma arquitetura de rede capaz de
reagir em tempo real e ser escalável para uma grande quantidade de
tráfego. A arquitetura deve ser capaz de classificar uma variedade de
tipos de tráfego de diferentes aplicações, e para fornecer um adequado e
específico serviço para cada tipo de tráfego em um período de tempo
muito curto (ou seja, da ordem de milissegundos). Em segundo lugar,
diante do rápido crescimento da computação em nuvem e, portanto, da
demanda de centros de dados de grande escala, um gerenciamento de rede
adequado deve ser capaz de melhorar a utilização de recursos para
melhorar o desempenho do sistema. Assim, novas arquiteturas de rede e
mais ferramentas de TE inteligentes e eficientes são urgentemente
necessárias.

Nesse contexto surge como a arquitetura de rede da próxima geração, as
redes SDN que possuem grandes perspectivas de aplicação em TE. O SDN é
uma arquitetura de rede inovadora que em comparação com as redes
tradicionais, possui muitas vantagens para suportar a TE devido às suas
características distintas, como isolamento de controle e encaminhamento,
controle centralizado global e capacidade de programar o comportamento
da rede (SHU et al., 2016).

O SDN permite alterar o caminho normal que alguns pacotes seguiriam caso
fossem encaminhados pelo esquema convencional, ou seja, pelo caminho
mais curto, escolhido pelo protocolo de roteamento. O controlador SDN
altera as tabelas de encaminhamento dos roteadores e assim pode
direcionar pacotes para certas rotas preestabelecidas, o que não é
possível no esquema de redes convencionais.

O conceito de SDN apresentam vários recursos que possibilitam o uso de
aplicações envolvendo a Engenharia de Tráfego, as redes do futuro vão
fazer uso de forma intensa desta capacidade. Segundo Shu et al. (2016) a
arquitetura de rede tradicional não poderá atender aos requisitos dos
novos sistemas com o desenvolvimento contínuo de aplicação para
computação em nuvem, internet das coisas (IoT), redes sem fio 5G,
Internet veicular, sistemas ciberfísicos e indústria 4.0.

## 2.4 Softwares utilizadas na implementação das Redes SDN e dos Algoritmos de Otimização.

No presente trabalho adotou-se as seguintes ferramentas para implementar
a rede SDN, para geração de tráfego na rede implementada e medir o seu
desempenho.

### 2.4.1 Mininet

O Mininet é um Emulador de redes que foi criado para permitir pesquisas
em SDN (Software Defined Networking) e OpenFlow. O Mininet é capaz de
implantar grandes redes utilizando os recursos limitados de um único
computador ou máquina virtual simples (KAUR & SINGH, 2014).

O Mininet cria redes escalonáveis ​ usando mecanismos de virtualização a
nível de processo, uma forma mais leve de virtualização onde muitos
recursos do sistema são compartilhados. Esses recursos permitem que o
Mininet crie, interaja, personalize e compartilhe os protótipos
rapidamente, proporcionando comodidade e realismo a um custo muito baixo
com precisão, desempenho e escalabilidade (DE OLIVEIRA et al., 2014).

Segundo Keti e Askar (2015) há muitas razões para o uso do emulador
Mininet: Em primeiro lugar, existem apenas alguns dispositivos de rede
disponíveis para o propósito de implementar o padrão SDN, uma vez que
ainda não é uma tecnologia difundida do ponto de vista industrial. Além
disso, a implementação de rede com grande número de dispositivos de rede
é muito difícil e dispendiosa. Portanto, para superar esses problemas, a
estratégia de emulação virtual é a melhor escolha.

Dentro das funcionalidades do Mininet, tem-se também um editor de redes
com interface visual (GUI) chamado de Miniedit. Através do MiniEdit é
possível criar uma rede utilizando apenas o cursor do mouse, criar,
editar e salvar uma determinada topologia, gerar o script em python e
executar simulações desta rede.

#### 2.4.1.1 Script da rede

No software Mininet é possível criar alguns tipos específicos de redes
com topologias mais simples através de comandos dentro do Mininet. No
entanto para criação de topologias mais complexas deve-se utilizar um
código em Python utilizando funções e bibliotecas pertencentes ao
Mininet (GROßMANN & SCHUBERTH, 2013).

### 2.4.2 Controlador Floodlight

[O Controlador
Floodlight](https://www.sdxcentral.com/projects/floodlight/) é
um [controlador
SDN](https://www.sdxcentral.com/sdn/definitions/sdn-controllers/) que
utiliza o protocolo OpenFlow para organizar fluxos de tráfego em
um ambiente de [rede definida por software
(SDN)](https://www.sdxcentral.com/sdn/). Ele é responsável por manter
todas as regras de funcionamento da rede e fornecer as instruções
necessárias sobre como o tráfego deve ser tratado. Isso permite que os
usuários tenham melhor controle sobre suas redes.

O Floodlight possui uma interface GUI baseada na web, concebida por meio
da API REST do controlador. A GUI do Floodlight fornece uma maneira de
os usuários exibirem informações do estado do controlador, dispositivos
de encaminhamento conectados, enlaces entre dispositivos, hosts, fluxos
inseridos nas tabelas de encaminhamento dos dispositivos de
encaminhamento e a topologia geral de rede (AKCAY e YILTAS-KAPLAN,
2017).  Na Figura 6 tem-se a imagem da tela principal da interface GUI
do controlador Floodlight.

![](media/image6.png){width="6.636662292213473in"
height="3.2207786526684163in"}

Figura 6 -- Tela da Interface GUI do Floodlight 

#### 2.4.2.1 API REST

A API REST é uma aplicação do controlador Floodlight baseada na
arquitetura REST (Representational State Transfer) que utiliza de forma
padronizada os recursos e características do protocolo HTTP. Através
dessa API utilizando requisições HTTP pode-se interagir com o
controlador, consultando informações e alterando o estado da rede. Essas
requisições são realizadas utilizando os métodos HTTP: GET, POST, PUT e
DELETE que basicamente correspondem a operações de leitura, criação,
atualização e exclusão respectivamente. Conforme documentação do
controlador Floodlight (FLOODLIGHT DOCUMENTATION, 2018), cada requisição
deve ser encaminhada a um determinado endereço e seu formato deve ser no
formato JSON (JavaScript Object Notation) que é um formato compacto de
troca de dados entre sistemas.

#### 2.4.2.2 Static Entry Pusher

O Static Entry Pusher é um módulo do controlador Floodlight, que
utilizando a API REST, permite que um usuário insira manualmente fluxos
e grupos de fluxos em uma rede openflow. Na Figura 7 tem-se um conjunto
de comandos POST no formato JSON que encaminhados para o módulo Static
Entry Pusher alteram a tabelas dos switches.

+--------------------------------------------------------------------------------+
| curl -X POST -d \'{\"switch\":\"00:00:00:00:00:00:00:17\",                     |
| \"ipv4_src\":\"10.0.1.52\",\"eth_type\":\"0x0800\",\"ipv4_dst\":\"10.0.1.49\", |
| \"name\":\"flow-mod-1\", \"cookie\":\"0\",                                     |
| \"priority\":\"32768\",\"active\":\"true\",\"actions\":\"output=9\"}\'         |
| http://192.168.56.101:8080/wm/staticentrypusher/json                           |
|                                                                                |
| curl -X POST -d \'{\"switch\":\"00:00:00:00:00:00:00:18\",                     |
| \"ipv4_src\":\"10.0.1.52\",\"eth_type\":\"0x0800\",\"ipv4_dst\":\"10.0.1.49\", |
| \"name\":\"flow-mod-2\", \"cookie\":\"0\",                                     |
| \"priority\":\"32768\",\"active\":\"true\",\"actions\":\"output=4\"}\'         |
| http://192.168.56.101:8080/wm/staticentrypusher/json                           |
|                                                                                |
| curl -X POST -d \'{\"switch\":\"00:00:00:00:00:00:00:26\",                     |
| \"ipv4_src\":\"10.0.1.52\",\"eth_type\":\"0x0800\",\"ipv4_dst\":\"10.0.1.49\", |
| \"name\":\"flow-mod-3\", \"cookie\":\"0\",                                     |
| \"priority\":\"32768\",\"active\":\"true\",\"actions\":\"output=6\"}\'         |
| http://192.168.56.101:8080/wm/staticentrypusher/json                           |
|                                                                                |
| curl -X POST -d \'{\"switch\":\"00:00:00:00:00:00:00:27\",                     |
| \"ipv4_src\":\"10.0.1.52\",\"eth_type\":\"0x0800\",\"ipv4_dst\":\"10.0.1.49\", |
| \"name\":\"flow-mod-4\", \"cookie\":\"0\",                                     |
| \"priority\":\"32768\",\"active\":\"true\",\"actions\":\"output=3\"}\'         |
| http://192.168.56.101:8080/wm/staticentrypusher/json                           |
+================================================================================+

Figura 7 -- Comandos POST no formato JSON

### 2.4.3 D-ITG

O D-ITG (Distributed Internet Traffic Generator) é um software para
geração de tráfego no nível de pacote que replica diferentes padrões de
tráfego. Foi desenvolvido pela Traffic, que é um grupo de pesquisa
Italiano que trabalha na área de redes de computadores e multimídia, com
foco em monitoramento de rede e medições. (BOTTA et al., 2012).

O D-ITG suporta geração de tráfego IPv4 e IPv6 e é capaz de gerar
tráfego nas camadas de rede, transporte e aplicações. Segundo Botta et
al. (2012), o D-ITG mostra propriedades interessantes quando comparados
a outros geradores de tráfego.

### 2.4.4 SFLOW-RT

O sFlow-RT é um conjunto de aplicações em JavaScript que incorpora a
tecnologia analítica da empresa InMon, oferecendo medições e
visibilidade em tempo real para redes SDN.

O mecanismo de análise sFlow-RT recebe os fluxos contínuos de telemetria
dos [agentes sFlow](https://sflow-rt.com/agents.php) incorporados em
dispositivos de rede, hosts e aplicativos e os converte em métricas,
acessíveis por meio da API RESTflow. Assim, combinando monitoramento da
rede, hosts e aplicativos em um pipeline analítico integrado, o sFlow-RT
fornece visibilidade dos aplicativos e dos recursos das redes e
servidores necessários para suportar um determinado desempenho
(SFLOW-RT, 2018; AFAQ E REHMAN, 2015).

## 2.4.5 MATLAB

No presente trabalho adotou-se o software MATLAB (MATLAB, 2016) como
forma de implementar os algoritmos de otimização. Todos os algoritmos de
otimização utilizados e desenvolvidos foram implementados usando a
linguagem Matlab no ambiente de desenvolvimento do MATLAB. O MATLAB é um
software comercial de programação e resolução de problemas de
matemática, engenharia e ciências em geral.

## 2.5 Considerações Finais

Foi apresentado neste capítulo, uma introdução aos conceitos de redes de
computadores. Inicialmente foi feito um breve histórico sobre Redes de
Computadores e em seguida foram expostos os conceitos de Rede Definida
por Software (SDN), QoS e TE. Foram apresentados também alguns softwares
utilizados como ferramentas de implementação/emulação das Redes SDN e
dos Algoritmos de Otimização.

No próximo capítulo são apresentados alguns métodos de otimização e
algoritmos que serão utilizados neste trabalho.

# 3. MÉTODOS DE OTIMIZAÇÃO

É apresentada neste capítulo, uma introdução aos conceitos teóricos de
Métodos de Otimização utilizados neste trabalho. Inicialmente, na seção
3.1 é realizado uma introdução aos Métodos de Otimização. A seção 3.2
trata do Algoritmo de Otimização por Colônia De Formigas -- ACO. Na
sequência, na seção 3.3, 3.4, 3.5 são apresentados os algoritmos de
Dijkstra, Evolução Diferencial (DE) e Algoritmo Genético (AG)
respectivamente. A seguir, na seção 3.6 são apresentados alguns
trabalhos relacionados ao tema desta dissertação e na seção 3.7 é
apresentado o software MATLAB de programação científica. Finalmente, na
seção 3.8 são realizadas as considerações finais.

## 3.1 Métodos de Otimização Combinatória

A Otimização Combinatória é um ramo da ciência da computação e da
matemática aplicada que estuda problemas de otimização. É usado
principalmente para analisar sistemas complexos, com o objetivo de
melhorar seu funcionamento. Nos problemas de otimização tem-se uma
função objetivo que dependente das variáveis de decisão e essas
variáveis são delimitados pelas restrições a elas impostas e constituem
um conjunto solução do problema. Quanto a sua formulação, o problema
pode ser de minimização ou de maximização da função objetivo. As
soluções podem ser soluções exatas ou aproximadas. Em
situações/problemas onde as soluções exatas são de difícil resolução
e/ou com alto custo computacional, utilizam-se as chamadas heurísticas
que são métodos que apresentam soluções aproximadas.

> As heurísticas ou algoritmos heurísticos foram desenvolvidos com a
> finalidade de se resolver problemas de elevado nível de complexidade
> em tempo computacional razoável. Ao se pensar em um problema altamente
> combinatório, uma opção seria analisar todas as combinações possíveis
> para conhecer a melhor. Se o problema possui um universo de dados
> pequeno, realmente esta é a maneira correta de se buscar a melhor
> solução, mas os problemas reais, normalmente, possuem um número de
> combinações muito extenso, o que torna inviável a análise de todas as
> combinações, uma vez que o tempo computacional exigido fica
> impraticável. As heurísticas procuram encontrar soluções próximas da
> otimalidade em um tempo computacional razoável\... (CHAVES, 2005).

Os métodos heurísticos não garantem que identificarão soluções ótimas,
mas em geral são capazes de obter soluções próximas da ótima em um tempo
computacional relativamente mais rápido que as técnicas usadas na busca
pelas soluções ótimas.

Como técnicas de soluções exatas pode-se citar, por exemplo, o seguinte
algoritmo:

- Algoritmo de Dijkstra: Desenvolvido por Dijkstra (1959), é um
  algoritmo para encontrar os caminhos mais curtos entre dois nós em um
  grafo. É implementado no presente trabalho.

Como técnicas de obtenção de soluções aproximadas ou heurísticas pode-se
citar, por exemplo, os seguintes algoritmos:

- Algoritmo da Colônia de Formigas (ACO - Ant Colony Optimization):
  Desenvolvido por Marco Dorigo, Vitorio Maniezzo e Alberto Colorni
  (COLORNI, DORIGO E MANIEZZO 1992). É uma heurística baseada em
  população, tendo sido inspirada pelo comportamento das formigas na
  natureza. É implementada no presente trabalho.

- Evolução Diferencial (DE - Differential Evolution): Desenvolvido por
  Rainer Storn e Kenneth Price (STORN e PRICE, 1997) como uma
  alternativa dos algoritmos genéticos com objetivo de se obter
  resultados mais rápidos e eficientes em problemas de otimização. É uma
  heurística baseada em conceitos matemáticos, que não faz uso de
  derivadas, e visa solucionar problemas de otimização contínua e
  discreta. É implementada no presente trabalho.

- Algoritmo Genético -- AG: Desenvolvida por Holland (1975), é uma
  heurística inspirada no processo de seleção natural, comumente usados
  ​​para gerar soluções de alta qualidade para problemas de otimização e
  busca, confiando em operadores bio-inspirados, como mutação, crossover
  e seleção. É implementada no presente trabalho.

Conforme Andrade (2008), o problema do roteamento de uma rede como
vários nós e com certas restrições como fluxo, atraso, etc. é
considerado um problema de grande complexidade que pertence à classe
NP-Completo, o que significa que esse tipo de problema não possui
solução exata em tempo computacional razoável, tornando a sua solução
exata muitas vezes inviável na prática.

No presente trabalho serão utilizadas a seguintes heurísticas: ACO, DE e
AG. A seguir são apresentados esses algoritmos e explicado o
funcionamento de cada um deles.

## 3.2 O Algoritmo de Dijkstra

O algoritmo de Dijkstra é usado para encontrar os caminhos mais curtos
entre dois nós em um grafo. Foi concebido por Edsger Wube Dijkstra em
1956 e publicado em 1959 (DIJKSTRA, 1959). É um algoritmo
determinístico, ou seja, é uma técnica de solução exata para o problema
do caminho mais curto num grafo dirigido ou não dirigido com arestas de
peso não negativo. O problema do caminho mais curto (Shortest-Path
Problem), também conhecido como problema do caminho mínimo, é muito
conhecido e estudado devido a sua utilização e seu grande potencial de
aplicação em inúmeros problemas de transportes, logística, redes de
computadores e de telecomunicações, entre outros.

O algoritmo de Dijkstra baseia-se num processo de rotulação de caminhos
em grafos com arcos positivos, e posterior classificação dos respectivos
rótulos utilizando indução e ajustes. Este processo inicia pelo nó
origem, de forma ordenada segundo as distâncias a cada um dos nós
adjacentes. Em cada iteração é escolhido um novo nó com rótulo
temporário sendo igual ao menor valor da distância percorrida até este,
que se torna permanente, depois de varrer todos os nós adjacentes a
este. O algoritmo termina quando não existirem nós com rótulos
temporários ou quando o rótulo do nó destino passe a ser permanente. O
pseudo-algoritmo de Dijkstra é apresentado na Figura 8.

+-----------------------------------------------------------------------+
| Pseudo-Algoritmo de Dijkstra                                          |
|                                                                       |
| 1 Cria conjunto de vértices Q                                         |
|                                                                       |
| 2 Para cada vertice v no Grafo Faça                                   |
|                                                                       |
| 3 distancia\[v\] = Infinito                                           |
|                                                                       |
| 4 vertice_anterior\[v\] = Indefinido                                  |
|                                                                       |
| 5 adicione v em Q                                                     |
|                                                                       |
| 6 Fim                                                                 |
|                                                                       |
| 7 distancia\[origem\] = 0                                             |
|                                                                       |
| 8 Enquanto Q é não vazio Faça                                         |
|                                                                       |
| 9 u = vertice em Q com distancia \[u\] mínima                         |
|                                                                       |
| 10 Remove u de Q                                                      |
|                                                                       |
| 11 Para cada vizinho v de u Faça                                      |
|                                                                       |
| 12 alt = distancia\[u\] + tamanho(u, v)                               |
|                                                                       |
| 13 Se alt \< distancia\[v\] Então                                     |
|                                                                       |
| 14 distancia\[v\] = alt                                               |
|                                                                       |
| 15 vertice_anterior\[v\] = u                                          |
|                                                                       |
| 16 Fim                                                                |
|                                                                       |
| 17 Fim                                                                |
|                                                                       |
| 18 Fim                                                                |
|                                                                       |
| 19 Retorne distancia\[\], vertice_anterior\[\]                        |
+=======================================================================+

Figura 8 - Pseudo-Algoritmo de Dijkstra

A complexidade do algoritmo de Dijkstra é O(n²), sendo um algoritmo
eficiente e de fácil implementação computacional. No entanto esse
algoritmo não é capaz de encontrar caminhos mais curtos em presença de
arcos negativos, uma vez que a cada iteração, o vértice examinado com
menor distância acumulada é fechado (GOLDBARG & LUNA, 2005).

O algoritmo de Dijkstra utilizado é de autoria de Joseph Kirk (KIRK,
2017) disponível gratuitamente no repositório File Exchange do site da
MathWork (MATLAB, 2016).

## 3.3 O Algoritmo de Otimização por Colônia De Formigas -- ACO

O algoritmo de Otimização por Colônia de Formigas (ACO - Ant Colony
Optimization) é uma heurística baseada em população, tendo sido
inspirada pelo comportamento das formigas na natureza.

Uma importante característica das formigas é que elas são capazes de
encontrar os caminhos mais curtos entre a colônia e as fontes de
alimentos. O estudo desse comportamento serviu de inspiração para o
desenvolvimento da heurística de colônia de formigas (DORIGO & STÜTZLE,
2004).

O ACO utiliza o conceito de probabilidade, aplicada a resolução de
problemas de roteamento e busca de caminhos mais curtos. Sua ideia
fundamental é baseada no comportamento das formigas ao buscarem
alimentos e ocorre da seguinte maneira: as formigas ao saírem da colônia
iniciam a busca por alimentos seguindo diversas direções de forma
aleatória. Ao encontrarem uma fonte de alimento, elas retornam até a
colônia marcando o caminho com feromônio numa taxa proporcional a
qualidade do caminho e do alimento encontrado. Assim, quando outras
formigas passarem por esses caminhos, vão seguir as rotas de feromônios
e encontrar o alimento. A probabilidade de uma formiga seguir uma
determinada rota é proporcional a concentração de feromônio.

O feromônio possui a propriedade de evaporar-se com o tempo. Por causa
desta característica, caminhos que levam a alimentos que já esgotaram
vão deixar de existir e caminhos mais longos onde a reposição de
feromônio é mais demorada terão concentrações mais baixas do feromônio.

A Figura 9 ilustra o processo de seleção do menor caminho.

![](media/image7.png){width="4.270833333333333in"
height="2.5729166666666665in"}

(a) \(b\) (c)

Figura 9 -- Processo da seleção do menor caminho.

Fonte: Adaptado de CORREIA (2012).

(a) -- Momento inicial: uma determinada formiga retorna ao formigueiro
    após encontrar comida, observem que a rota escolhida por ela não é a
    rota mais curta, não necessariamente.

(b) -- Momento intermediário: outras formigas seguindo o feromônio
    depositado (ou de forma independente) descobrem o alimento e começam
    a transitar nesse intervalo (comida --formigueiro), não
    obrigatoriamente seguindo a mesma rota da 1° formiga. No entanto,
    após um determinado tempo a concentração do feromônio das rotas mais
    longas torna-se inferior ao das rotas mais curtas, isso se deve ao
    fato de que a reposição do feromônio nessas rotas é realizado com um
    intervalo de tempo maior, já que as formigas demoram mais tempo para
    percorrer essas rotas.

(c) -- Momento final: Assim como a probabilidade das formigas seguirem
    uma certa rota é proporcional a concentração do feromônio na rota,
    depois de algum tempo o número de formigas que não utilizam essa
    rota (com concentração de feromônio mais alta) torna-se pequeno.

A formulação do ACO é baseada na probabilidade de uma formiga seguir um
determinado caminho. Esse comportamento é decrito pela Equação 3.1 que
define a probabilidade da formiga k escolher o caminho ij.

![](media/image8.png){width="3.064935476815398in"
height="1.189915791776028in"} (3.1)

Onde: α (alpha) - Parâmetro que indica a importância do feromônio;\
β (beta) - Parâmetro que indica a importância da informação heurística,
nos problemas de roteamento, o custo entre um ponto e outro;

$\tau_{ij}$ - Indica a quantidade de feromônio na aresta ij;

$\eta_{ij}$ = 1/$d_{ij}$ - onde $d_{ij}$ é a distância entre os pontos i
e j;

$N_{i}^{k}$ - Conjunto de todos os caminhos com opção de serem
percorridos;

$P_{ij}^{k}$ - Probabilidade da formiga k escolher o caminho entre os
pontos i e j;

Na Equação 3.2 tem-se a fórmula de atualização (acréscimo e evaporação)
do feromônio.

![](media/image9.png){width="3.2708333333333335in"
height="0.9270833333333334in"} (3.2)

Onde:

ρ (rho) - Parâmetro que regula a taxa de evaporação do feromônio, 0 \< r
\< 1;

m - Número das formigas;

${\mathrm{\Delta}\tau}_{ij}^{k}$ - Quantidade de feromônio adicionado na
trilha entre i e j pela formiga k;

$\tau_{ij}$ - Indica a quantidade de feromônio na aresta ij;

Essa formulação define o comportamento das formigas ao escolherem
determinadas rotas de forma estatística e a atualização do feromônio
como forma de definir quais rotas são consideradas melhores e com
maiores chances de serem selecionadas pelas formigas.

O algoritmo ACO utilizado foi baseado na estrutura do algoritmo AntNet
(DORIGO & STÜTZLE, 2004), no entanto seu código foi inteiramente
desenvolvido de forma independente usando o software Matlab.

## 3.4 O Algoritmo de Evolução Diferencial (Differential Evolution -- DE)

O algoritmo de Evolução Diferencial (DE - Differential Evolution), foi
proposto por Rainer Storn e Kenneth Price (STORN & PRICE, 1997) como uma
alternativa dos algoritmos genéticos com objetivo de se obter resultados
mais rápidos e eficientes em problemas de otimização contínua e
discreta.

A evolução diferencial surgiu das tentativas de Ken Price de resolver o
problema de ajuste de curvas dos polinômios de Chebychev que lhe foi
apresentado por Rainer Storn. Houve um avanço, quando Ken sugeriu a
idéia de usar as diferenças vetoriais para perturbar a população de
vetores. Desde essa ideia seminal, uma discussão animada entre Ken e
Rainer e inúmeras reminiscências e simulações computacionais de ambas as
partes produziram muitas melhorias substanciais que tornaram a DE atual,
uma ferramenta versátil e robusta. Ken e Rainer desejam que o DE seja
desenvolvido e aplicado cada vez mais por cientistas e usuários de todo
o mundo, sendo esse o motivo pelo qual o DE não foi patenteado de forma
alguma (STORN, 2017).

É um algoritmo simples e de fácil entendimento, com poucos parâmetros de
controle. O seu funcionamento é relativamente simples. Basicamente, o DE
acrescenta a diferença ponderada entre dois vetores de população a um
terceiro vetor. Desta forma, nenhuma distribuição de probabilidade
separada necessita ser usada, o que torna o esquema completamente
auto-organizável (STORN, 2017).

O algoritmo DE basicamente é constituído pelas seguintes operações:
Criação da População Inicial, Mutação, Cruzamento, Seleção e Teste de
Convergência. A Figura 10 mostra a sequência dessas operações.

![](media/image10.png){width="5.905555555555556in"
height="1.5770833333333334in"}Figura 10 - Operações do algoritmo DE

A população inicial é gerada de forma aleatória dentro de um intervalo
com limites superior e inferior, conforme descrito na Equação 3.3.

$x_{i} = L_{inf\ } + rand*\ (L_{\sup{- \ }}L_{\inf}$) (3.3)

Na operação de mutação três indivíduos diferentes ($x_{r1},\ x_{r2}$ e
$x_{r3}$ ) são selecionados dentro da população e um novo indivíduo é
criado a partir destes. A diferença entre dois indivíduos($x_{r2}$ e
$x_{r3}$ ) é multiplicada por um fator $F_{1} \in \lbrack 0,1\rbrack$ e
somada ao indivíduo $x_{r1}$, gerando assim um novo indivíduo $v_{i}$
conforme descrito na Equação 3.4 e na Figura 11.

$v_{i} = x_{r1} + F_{1}\left( x_{r2} - x_{r3} \right)$ (3.4)

![](media/image11.png){width="5.11665135608049in"
height="4.6998162729658794in"}

Figura 11 -- Operação de Mutação -- DE

Fonte: Adaptado de Price (2006).

A operação de cruzamento ou recombinação consiste na criação de um novo
indivíduo $u_{i}$ a partir das características de outros dois indivíduos
e segundo uma probabilidade de cruzamento (Pcr). No cruzamento ocorre a
mistura de soluções bem-sucedidas da geração anterior com novos
indivíduos, conforme descrito na Equação 3.5 e na Figura 12.

$u_{i} = \left\{ \begin{array}{r}
v_{i}\ se\ rand \leq Pcr \\
x_{i}senão
\end{array} \right.\$ (3.5)

![](media/image12.png){width="4.9472976815398075in"
height="4.572344706911636in"}

Figura 12 -- Operação de Cruzamento -- DE

Fonte: Adaptado de Price (2006).

Na operação de seleção o algoritmo avalia os novos indivíduos criados
segundo o valor da função objetivo e assim seleciona os que possuem
melhores valores da função objetivo, ou seja, estes indivíduos
correspondem aos melhores conjuntos de rotas conforme será apresentado
no capítulo 4. A operação de seleção é descrita na Equação 3.6.

$x_{i}^{k + 1} = \left\{ \begin{array}{r}
u_{i}^{k}\ se\ f\left( u_{i}^{k} \right) < f\left( x_{i}^{k} \right) \\
x_{i}^{k}\ senão
\end{array} \right.\$ (3.6)

Segundo Alotto (2011) esse esquema ganancioso é a chave para a
convergência rápida do DE.

Posteriormente seguindo a estrutura de repetição do algoritmo DE, os
processos de mutação, cruzamento e seleção são repetidos até que a
convergência seja alcançada ou algum critério de parada seja obedecido.

O algoritmo DE utilizado é baseado na versão open-source de autoria de
S. Mostapha Kalami Heris no projeto: Implementation of Differential
Evolution (DE) in MATLAB (HERIS, 2016a). Este algoritmo foi levemente
modificado de acordo com a necessidade de adequação ao problema
estudado.

## 3.5 Algoritmos Genéticos - AG

Os Algoritmos Genéticos (AG's) são um tipo especial de algoritmos que
são inspirados na biologia evolutiva. Seus principais conceitos são
derivados sobretudo da teoria da evolução de Darwin (Darwin, 1853) que
considera que os indivíduos mais aptos são selecionados e algumas das
suas características são transferidas para as próximas gerações. Foram
concebidos na década de 60 por John Holland (HOLLAND, 1975) e
posteriormente desenvolvidos por um de seus alunos, David E. Goldberg
(GOLDBERG, 1989).

O Algoritmo Genéticos (AG) é constituído pelas seguintes operações:
Criação da População Inicial, Função de Avaliação (Fitness) ou Função
Objetivo, Seleção, Cruzamento, Mutação e Teste de Convergência. A Figura
13 mostra a sequência dessas operações.

![](media/image13.png){width="5.905555555555556in"
height="1.5270833333333333in"}

Figura 13 -- Estrutura básica de um Algoritmo Genético

Assim como no algoritmo DE a população inicial é gerada de forma
aleatória dentro de um intervalo com limites superior e inferior,
conforme descrito na Equação 3.7.

$x_{i} = L_{inf\ } + rand*\ (L_{\sup{- \ }}L_{\inf}$) (3.7)

Na operação de seleção o algoritmo avalia os novos indivíduos criados
segundo os resultados obtidos pela função de avaliação ou função
objetivo e seleciona os que obtiveram melhores resultados, conforme
descrito na Equação 3.8.

$x_{i}^{k + 1} = \left\{ \begin{array}{r}
u_{i}^{k}\ se\ f\left( u_{i}^{k} \right) < f\left( x_{i}^{k} \right) \\
x_{i}^{k}\ senão
\end{array} \right.\$ (3.8)

Na operação de cruzamento ou crossover adotou-se o cruzamento
polarizado, onde é definido uma variável alpha ($\alpha$
$\in \lbrack 0,1\rbrack)$ chamada de coeficiente de multiplicação que
deverá ser multiplicada a dois indivíduos (Pais) gerando outros dois
novos indivíduos (Filhos). Essa operação de cruzamento é realizada ou
não segundo uma probabilidade de cruzamento (Pc). No cruzamento ocorre a
mistura de soluções bem-sucedidas da geração anterior com novos
indivíduos, conforme descrito nas Equações 3.9 e 3.10.

$y_{1} = \alpha*x_{1} + (1 - \ \alpha)*x_{2}$ (3.9)

$y_{2} = \alpha*x_{2} + (1 - \ \alpha)*x_{1}$ (3.10)

Na operação de mutação adotou-se o operdor de mutação real, onde uma
variável sigma ($\sigma$) é definida como uma fração da diferença entre
os valores de limites superior e inferior aceitos pela modelagem do
problema. O valor sigma então é somado a um indivíduo$\ x_{i}$, gerando
assim um novo indivíduo $y_{i}$ conforme descrito nas equações 3.11 e
3.12. Essa operação de mutação é realizada ou não segundo uma
probabilidade de mutação (Pm).

$\sigma = 0.1*\left( L_{\sup{- \ }}L_{\inf} \right)$ (3.11)

$y_{i} = x_{i} + \sigma*\ rand$ (3.12)

O algoritmo genético utiliza o conceito de elitismo, isto é, os
indivíduos com melhores desempenho são mantidos na próxima geração. Os
processos de seleção, mutação, cruzamento são repetidos até que a
convergência seja alcançada ou algum critério de parada seja obedecido.

O algoritmo AG utilizado é baseado na versão open-source de autoria de
S. Mostapha Kalami Heris no projeto: Implementation of Real-Coded
Genetic Algorithm in MATLAB (HERIS, 2016b). Assim como no caso do DE o
algoritmo AG foi levemente modificado de acordo com a necessidade de
adequação ao problema estudado.

## 3.6 Trabalhos Relacionados

A revisão bibliográfica é fundamental e necessária para que primeiro
possa-se saber o que já foi realizado por outros pesquisadores e quais
são as lacunas do conhecimento naquela área, para que assim se possa
seguir numa direção onde seja possível investigar algo que contribua
para o seu desenvolvimento.

Os seguintes trabalhos pesquisados tratam de temas relacionados ao
presente trabalho. Os três primeiros tratam do uso de algoritmos
híbridos de otimização ACO e DE em diversos problemas. Mais outros três
tratam do uso híbrido dos algoritmos de otimização ACO e AG também em
diversos problemas. Outros quatro trabalhos abordam o uso do algoritmo
de otimização ACO aplicado em redes SDN. Por fim é comentado mais um
trabalho voltado para redes SDN com o objetivo de estudar diferentes
abordagens de roteamento e TE para se obter melhores soluções de
desempenho. Segue abaixo um breve resumo dos temas e seus resultados:

Zhang et al. (2008) apresentaram um estudo utilizando em conjunto os
algoritmos ACO (Algoritmo de Colônia de Formigas) e o DE (algoritmo de
evolução diferencial). O uso híbrido dos algoritmos (chamado de DEACO) é
realizado com objetivo de melhorar as deficiências do robusto e versátil
algoritmo ACO em relação a sua tendência de estagnar seus resultados em
torno de uma solução obtida em um dado momento. Nessa proposta o
algoritmo de evolução diferencial (DE) é proposto como uma forma superar
essas limitações. Assim o DE é aplicado para otimizar a trilha de
feromônios do modelo ACO. O algoritmo proposto é testado com o Problema
do Caixeiro Viajante (TSP - Traveling Salesman Problem), e o resultados
experimentais demonstram que o algoritmo híbrido (DEACO) proposto é um
modelo de algoritmo viável e eficaz na resolução de complexos problemas
de otimização.

Rahmat e Musirin (2012) apresentaram um estudo utilizando em conjunto os
algoritmos ACO (Algoritmo de Colônia de Formigas) e o DE (algoritmo de
evolução diferencial) aplicados ao problema de despacho de carga
econômica (ELD). Este problema se refere agendamento das saídas das
unidades geradora que podem satisfazer a demanda de carga de seus
clientes a um custo operacional mínimo na sua geração, sendo um problema
muito importante paras as concessionárias de energia elétrica. Os
resultados obtidos demonstram que o também chamado DEACO é mais
eficiente e rápido do que o ACO e também supera os resultados de outras
técnicas tradicionais aplicadas ao problema.

Khushaba et al. (2008) apresentaram um estudo utilizando em conjunto os
algoritmos ACO (Algoritmo de Colônia de Formigas) e o DE (algoritmo de
evolução diferencial) aplicados a um subproblema do problema de
reconhecimento de padrões que é a seleção de recursos (FS) que visa
reduzir a dimensionalidade do conjunto de recursos através da seleção de
um subconjunto de recursos que executa a melhor classificação
considerando apenas alguns critérios e/ou variáveis. Isso é feito
eliminando recursos irrelevantes e redundantes, proporcionando assim uma
melhor representação dos padrões originais. Embora o ACO tenha provado
ser uma técnica poderosa em diferentes problemas de otimização, ele
ainda precisa de algumas melhorias. Isso se deve ao fato de que ele
constrói suas soluções sequencialmente, e no caso da seleção de recursos
esse comportamento provavelmente não o levará à solução ideal. Os
resultados indicaram a superioridade do algoritmo proposto chamado
ANTDE, obtendo maiores precisões de classificação do que os outros
métodos e técnicas de redução de dimensionalidade.

Zukhri e Paputungan (2013) apresentaram um estudo utilizando em conjunto
o Algoritmo Genético (GA) e o Algoritmo de Otimização de Colônias de
Formigas (ACO) de forma hibrida, criando o chamado GACO e o aplicando ao
problema do Caixeiro Viajante (TSP). Neste método, o AG observa e
preserva a formiga mais apta em cada ciclo e geração e somente as
cidades não visitadas serão avaliadas pela ACO. A partir do resultado
experimental, o desempenho do GACO é significativamente melhor e seu
tempo computacional é compatível com o AG e o ACO.

Ciornei e Kyriakides (2012) apresentaram um estudo no qual propõem a
utilização de um Algoritmo chamado de GAAPI. Esse algoritmo é uma
hibridização entre duas técnicas de otimização: um tipo especial de
algoritmo de otimização de colônia de formigas para domínios contínuos
chamado de API e um algoritmo genético (AG). O algoritmo adota o
comportamento em declive do API (uma característica de alguns algoritmos
de otimização) e a boa disseminação no espaço de solução do AG. Uma
abordagem probabilística e um estudo comparativo empírico foram
apresentados para comprovar a convergência do método proposto na solução
de diferentes classes de problemas complexos de otimização contínua. O
algoritmo mostrou ser eficaz e eficiente para a maioria das funções de
teste.

Carvalho e Yamakami (2008) apresentaram um estudo no qual propõe uma
nova Meta-heurística Híbrida de Sistema de Colônia de Formigas (ACS) e
Algoritmos Genéticos (AG) para resolver o Problema do Caixeiro Viajante
(PCV) ou Traveling Salesman Problem (TSP). Essa nova heurística é
chamada de ACS+AG-PCV e visa obter bons resultados ao contornar a
questão da complexidade do TSP.

Lin et al. (2017) apresentou um estudo aplicando o algoritmo ACO
(Algoritmo de Colônia de Formigas) em Redes SDN. Considerando que o
paradigma SDN fornece as vantagens de desacoplar o plano de controle e
dados (encaminhamento). Assim os pacotes são classificados em fluxos e a
decisão de roteamento é baseada nesses fluxos. Uma vez que o ACO tem o
potencial de trabalhar dessa forma, então é proposto nesse estudo um
modelo ACO dentro da perspectiva de Redes SDN. Foi então realizado
testes desse modelo comparando o índice de entrega de pacotes, o atraso
fim-a-fim e a eficiência energética. Além disso o ACO foi comparado com
três protocolos de roteamento, a saber, AODV (Vetor de Distâncias Por
Demanda para Redes Ad hoc), DSDV (Vetor de Distância Sequenciado por
Destino) e DSR (Roteamento Dinâmico pela Origem), simulando redes wifi
(de sensores sem fio) com tráfego de diferentes densidades. Os
resultados mostram que o ACO não só é eficiente em termos de energia,
mas também possui o maior índice de entrega de pacotes e o menor tempo
de chegada de pacotes em tráfego de baixa densidade. No entanto o ACO
não funciona bem em relação a entrega de pacotes e ao atraso fim-a-fim
no caso de tráfego de alta densidade, portanto concluindo que o ACO é
mais adequado para ser usado no tráfego de baixa densidade.

Wang et al. (2016) apresentou um estudo sobre o balanceamento de carga
em Redes SDN sendo proposto um novo algoritmo baseado no algoritmo ACO,
sendo chamado de algoritmo de balanceamento de carga de enlaces baseado
em Otimização de Colônia de Formigas. O algoritmo usa o método de busca
do ACO e leva em consideração como fatores de impacto o atraso, perda de
pacotes e carga (vazão) utilizada nos enlaces. Selecionando os nós
baseado nessas informações para realizar o balanceamento de carga dos
enlaces e reduzir o atraso de transmissão fim-a-fim. Os resultados
obtidos demonstram que o método proposto tem um melhor desempenho no
balanceamento de carga da rede e na melhoria da QoS. Além de aumentar a
estabilidade e a rapidez do reencaminhamento do tráfego.

Dobrijevic e Santl (2015) apresentou um estudo com um modelo utilizando
otimização de colônias de formigas (ACO) para encaminhamento de fluxo em
ambientes de rede SDN. Explorando uma visão de rede global e a
flexibilidade da configuração fornecida pelo conceito SDN, a abordagem
também utiliza modelos de estimativa de qualidade de experiência (QoE) e
procura maximizar a QoE do usuário para serviços multimídia. Uma versão
Java do algoritmo é implementada e integrada no controlador SDN
OpenDaylight para programar as seleções do caminho. Os resultados da
avaliação indicam melhorias promissoras de QoE nessa abordagem em
relação ao roteamento de caminho mais curto, bem como baixo tempo de
execução do algoritmo.

Parsaei et al. (2017) apresentou um estudo onde propõe um novo método de
engenharia de tráfego heurístico para aplicação de telecirurgia usando o
algoritmo ACO (Ant Colony Optimization) em uma rede SDN. O novo
paradigma SDN permitiu e facilitou o aprovisionamento de Qualidade de
Serviço (QoS) em muitas aplicações, inclusive em telecirurgias, em que
um cirurgião realiza uma cirurgia no paciente remotamente usando redes
de telecomunicações, sendo necessário transmissão de vídeo com alta
qualidade. Este tipo de aplicativo necessita do fornecimento de um
caminho de comunicação rápido e adequado entre o cirurgião e o paciente.
Os resultados da avaliação do desempenho mostraram que o método proposto
é melhor do que o protocolo OSPF. O método proposto melhora os três
parâmetros de QoS importantes, o atraso médiofim-a-fim em 56,3%, a taxa
de perda de pacotes em 50,5% e o PSNR (Relação sinal-ruído de pico) em
1,33.

Tomovic et al. (2015) apresentou um estudo analisando a adequação de
diferentes algoritmos de roteamento para a configuração dinâmica de
túneis de tráfego com garantias de desempenho nas redes SDN. Foram
consideradas duas restrições de roteamento: largura de banda e atraso
fim-a-fim. Foi utilizada também a taxa de rejeição de largura de banda,
que é comumente utilizado como indicador de desempenho para algoritmos
de roteamento QoS, no contexto SDN de computação de baixo tempo é
apontado como requisito importante. O conceito de decisões
centralizadas, proporcionam uma maior flexibilidade de controle e
permitem a implementação de mecanismos de roteamento sofisticados. Os
resultados demonstram que os algoritmos com limites de largura de banda
que utilizam informações sobre pares origem-destino (S-D) podem aumentar
significativamente a capacidade da rede.

## 3.7 Considerações Finais

Foi apresentado neste capítulo, uma introdução aos conceitos de métodos
de otimização combinatória. Foram apresentados os algoritmos Dijkstra,
ACO, DE e AG que serão utilizados neste trabalho. Em seguida foram
apresentados 11(onze) trabalhos relacionados e realizado um resumo de
cada um deles.

No próximo capítulo é apresentado os modelos de engenharia de tráfego
aplicada às redes SDN.

# O MODELO DE ENGENHARIA DE TRÁFEGO APLICADO ÀS REDES DEFINIDAS POR SOFTWARE

Neste capítulo é proposto o Modelo da engenharia de tráfego aplicada às
redes definidas por software utilizando os algoritmos de otimização:
ACO, DE e AG. Inicialmente, na seção 4.1 é apresentado o Método Proposto
sobre a implementação hibrida dos algoritmos de otimização. A seguir, na
seção 4.2 é apresentado o Modelo Geral de Engenharia de tráfego em SDN e
na seção 4.3 é tratada a Modelagem Matemática e sua Função Objetivo. Em
seguida na seção 4.4 e 4.5 são apresentas os modelos implementados
utilizando as heurísticas ACO+DE e ACO+AG respectivamente. Finalizando o
capítulo na seção 4.6 são realizadas algumas considerações finais.

## 4.1 Método Proposto

No presente trabalho foi proposto a utilização de dois modelos de
otimização híbrida (ACO+AG e ACO+DE) em que são usadas duas heurísticas
distintas em cada modelo. Em um primeiro momento é necessário encontrar
as possíveis rotas para as diversas aplicações e usuários. No entanto,
configurar o algoritmo ACO para somente obter rotas viáveis já
considerando as diversas restrições e prioridades resultaria na obtenção
de um menor conjunto de rotas e tornaria o conjunto de soluções mais
restrito e menos flexível, além de tornar o algoritmo ACO mais complexo.
Em função disso uma alternativa encontrada foi a utilização de dois
algoritmos distintos, ou seja, a utilização de uma estratégia híbrida.
Numa primeira etapa é utilizado o algoritmo ACO para encontrar um
conjunto de rotas e numa segunda etapa o algoritmo (AG ou DE) é
utilizado para selecionar as melhores rotas considerando as restrições
da rede e prioridade das aplicações e usuários. Além disso utilizou-se o
algoritmo de roteamento de Dijkstra como padrão de comparação de
desempenho dos modelos adotados.

Essa abordagem com utilização de mais de um algoritmo como forma de
resolver problemas de otimização é amplamente utilizada, como pode ser
verificado nos trabalhos relacionados do capítulo 3.

## 4.2 Modelo Geral de Engenharia de tráfego em SDN

Os modelos de otimização adotados neste trabalho têm como objetivo a sua
aplicação no âmbito das Redes Definidas por Software (SDN) que é um
paradigma com formidável capacidade de implementação da Engenharia de
Tráfego, sendo um dos objetivos principais do trabalho. A Figura 14
mostra o modelo de Engenharia de Tráfego em SDN.

![](media/image14.png){width="5.697916666666667in"
height="4.643293963254593in"}

Figura 14 -- Modelo Geral de Engenharia de tráfego em SDN

Fonte: Adaptado de LOBATO et al. (2014).

No modelo apresentado na Figura 14 observa-se que a partir de uma dada
demanda dos usuários e aplicações pertencentes à rede, é criada um
conjunto de rotas otimizadas. Essas rotas obtidas alimentam o
controlador SDN para que sejam realizadas as modificações necessárias
para um melhor desempenho da rede. Essa tarefa é efetuada da seguinte
maneira: inicialmente o melhor conjunto de rotas obtidas por um dos
modelos (ACO+DE ou ACO+AG) é enviado ao controlador. O controlador ao
receber essa nova configuração da rede, deve alterar as tabelas de
fluxos do plano de dados dos dispositivos de encaminhamento
(comutadores). Assim uma nova configuração de rotas é estabelecida e o
funcionamento da rede é otimizado.

O presente trabalho considera que essas alterações no gerenciamento da
rede devem ser efetuadas de maneira off-line, isto é, considerando o
padrão de fluxo diário da rede ou sob uma determinada demanda do
administrador da. O sistema define as novas rotas e realiza a alteração
da rede em horários com menores quantidades de fluxos de dados. Essa
medida é importante como forma de minimizar os impactos das interrupções
das conexões em momentos de maior utilização da rede pelos usuários.
Além disso a implementação de um sistema de otimização on-line
necessitaria da realização de amostragens em tempo real dos fluxos de
tráfego na rede, não sendo objetivo do presente trabalho.

## 4.3 Modelagem do Problema de Engenharia de Tráfego

## 

A modelagem proposta tem objetivo de representar matematicamente o
problema em questão e apresentar a função objetivo, suas restrições e as
variáveis de decisão.

Nessa modelagem matemática adaptou-se o modelo utilizado por Dias (2004)
que considera as variáveis de largura de banda, atraso fim-a-fim e
adicionou-se a prioridade da conexão e número de conexões estabelecidas
como variáveis a serem consideradas no modelo. Nesse modelo a topologia
da rede é modelada por um grafo direcionado G = (V, E), onde V = {1, . .
., n} corresponde aos nós e E = {1, . . ., m} aos enlaces da rede. Os
algoritmos de otimização escolhem as melhores configurações no espaço de
busca para cada caminho onde serão direcionados os fluxos das aplicações
dos usuários da rede.

A função objetivo (FO) ou função de aptidão (fitness) utilizada na
avaliação das soluções é uma função ponderada com diferentes pesos para
cada uma das necessidades das aplicações/usuários, sendo definido pela
Equação 4.1.

Função Objetivo de maximização

$\mathbf{FO = \ }\sum_{\mathbf{k = 1}}^{\mathbf{L}}{\mathbf{\delta}_{\mathbf{k}}\mathbf{y}_{\mathbf{k}}}\mathbf{+ \ }\mathbf{p}_{\mathbf{1}}\sum_{\mathbf{k = 1}}^{\mathbf{L}}\mathbf{y}_{\mathbf{k}}\mathbf{+ \ \ }\mathbf{p}_{\mathbf{2}}\sum_{\mathbf{k = 1}}^{\mathbf{L}}\mathbf{w}_{\mathbf{k}}\mathbf{+ \ }\mathbf{p}_{\mathbf{3}}\sum_{\mathbf{k = 1}}^{\mathbf{L}}\mathbf{t}_{\mathbf{k}}$
(4.1)

Sujeito às seguintes restrições:

$\mathbf{y}_{\mathbf{k}} \in \{\mathbf{0},\mathbf{1}\}$ $k = 1,...,L$
(4.2)

$\mathbf{y}_{\mathbf{k}} = \mathbf{0}$ Se o caminho k não atende essa
aplicação (4.3)

$\mathbf{y}_{\mathbf{k}} = \mathbf{1}$ Se o caminho k atende essa
aplicação (4.4)

$\mathbf{w}_{\mathbf{k}} \in \{\mathbf{0},\mathbf{1}\}$ $k = 1,...,L$
(4.5)

$\mathbf{w}_{\mathbf{k}} = \mathbf{0}$ Se
$\sum_{\left( \mathbf{i},\mathbf{j} \right) \in \mathbf{E}}^{}{\sum_{\mathbf{k} = \mathbf{1}}^{\mathbf{L}}{\mathbf{\lambda}_{\mathbf{k}}{\bullet \mathbf{x}}_{\mathbf{ij}}^{\mathbf{k}}} > \ \mathbf{\mu}_{\mathbf{ij}}}$
$\forall(i,j) \in E$ (4.6)

$\mathbf{w}_{\mathbf{k}} = \mathbf{1}$ Se
$\sum_{\left( \mathbf{i},\mathbf{j} \right) \in \mathbf{E}}^{}{\sum_{\mathbf{k} = \mathbf{1}}^{\mathbf{L}}{\mathbf{\lambda}_{\mathbf{k}}{\bullet \mathbf{x}}_{\mathbf{ij}}^{\mathbf{k}}} \leq \ \mathbf{\mu}_{\mathbf{ij}}}$
$\forall(i,j) \in E$ (4.7)

$\mathbf{t}_{\mathbf{k}} \in \{\mathbf{0},\mathbf{1}\}$ $k = 1,...,L$
(4.8)

$\mathbf{t}_{\mathbf{k}} = \mathbf{0}$ se
$\sum_{\left( \mathbf{i},\mathbf{j} \right) \in \mathbf{E}}^{}{\sum_{\mathbf{k} = \mathbf{1}}^{\mathbf{L}}{\mathbf{c}_{\mathbf{ij}}{\bullet \mathbf{x}}_{\mathbf{ij}}^{\mathbf{k}}} > \ \mathbf{h}_{\mathbf{k}}}$
$\forall(i,j) \in E$ (4.9)

$\mathbf{t}_{\mathbf{k}} = \mathbf{1}$ se
$\sum_{\left( \mathbf{i},\mathbf{j} \right) \in \mathbf{E}}^{}{\sum_{\mathbf{k} = \mathbf{1}}^{\mathbf{L}}{\mathbf{c}_{\mathbf{ij}}{\bullet \mathbf{x}}_{\mathbf{ij}}^{\mathbf{k}}} \leq \ \mathbf{h}_{\mathbf{k}}}$
$\forall(i,j) \in E$ (4.10)

$\mathbf{x}_{\mathbf{ij}}^{\mathbf{k}} \in \{\mathbf{0},\mathbf{1}\}$
$\forall(i,j) \in E$ (4.11)

$\mathbf{x}_{\mathbf{ij}}^{\mathbf{k}} = \mathbf{0}$ Se o caminho k não
está roteado no enlace (i, j). (4.12)

$\mathbf{x}_{\mathbf{ij}}^{\mathbf{k}} = \mathbf{1}$ Se o caminho k está
roteado no enlace (i, j). (4.13)

Onde:

**k** é o número de rotas ou caminhos a serem configurados.

$\mathbf{\lambda}_{\mathbf{k}}$ é a vazão (taxa de transmissão) em Mbps
do k-ésimo caminho.

$\mathbf{\mu}_{\mathbf{ij}}$ é a capacidade de transmissão (largura de
banda) de um enlace (i, j), medido em Mbps.

$\mathbf{c}_{\mathbf{ij}}$ corresponde ao atraso de transmissão em um
determinado caminho.

$\mathbf{h}_{\mathbf{k}}$ é o máximo atraso fim-a-fim, permitido para o
k-ésimo caminho, medido em ms.

$\mathbf{\delta}_{\mathbf{k}}$ é um parâmetro introduzido na função
objetivo para indicar a importância do k-ésimo fluxo de dados, que será
encaminhado no k-ésimo caminho, denominado parâmetro de prioridade da
conexão, o qual atua como elemento de diferenciação de serviços.

$\mathbf{y}_{\mathbf{k}}$ é a variável de seleção do caminho k que
determina se aquele caminho foi selecionado ou não, assumindo valores de
0 ou 1.

$\mathbf{t}_{\mathbf{k}}$ é a variável de seleção que determina se o
caminho k possui atraso abaixo do atraso máximo. Assume valores de 0 ou
1.

$\mathbf{w}_{\mathbf{k}}$ é a variável de seleção que determina se o
caminho k possui capacidade de largura de banda em todos os seus enlaces
que suportem a vazão dessa aplicação. Assume valores de 0 ou 1.

$\mathbf{x}_{\mathbf{ij}}^{\mathbf{k}}$ é a variável que indica se o
caminho k está ou não roteado no enlace (i, j). Assume valores de 0 ou
1.

$\mathbf{p}_{\mathbf{1}}$, $\mathbf{p}_{\mathbf{2}}$ e
$\mathbf{p}_{\mathbf{3}}$: são respectivamente os pesos relativos a
importância de conexões estabelecidas, conexões com larguras de banda
suficientes e conexões com atrasos aceitáveis. No modelo é adotado
$\mathbf{p}_{\mathbf{1}}$ = 3, $\mathbf{p}_{\mathbf{2}}$ = 2 e
$\mathbf{p}_{\mathbf{3}}$ = 1 diferenciando a importância de cada uma
destas variáveis consideradas. Lembrando que no primeiro termo da
equação 4.1 a variável $\mathbf{\delta}_{\mathbf{k}}$ faz o papel do
peso ou importância daquela conexão.

O objetivo da otimização é uma tarefa de maximizar a função objetivo,
visando encontrar os melhores valores para estas variáveis de decisão.
Estas por sua vez estão sujeitas a restrições, não podendo ser atribuído
a elas quaisquer valores.

## 4.4 Modelo de Otimização utilizando as Heurísticas ACO e DE

No primeiro modelo implementado neste trabalho adotou-se os algoritmos
ACO e DE como forma de otimizar o roteamento dos pacotes da rede
respeitando algumas restrições. A Figura 15 apresenta o modelo de
otimização proposto.

![](media/image15.png){width="6.508366141732283in"
height="2.7291666666666665in"}

Figura 15 -- Modelo de otimização utilizando as heurísticas ACO e DE.

Conforme mostra a Figura 15, o modelo consiste na utilização de dois
algoritmos (ACO e DE) que trabalham de forma sequencial e recebem
informações sobre a rede (topologia/restrições/prioridades), para
calcularem e obterem as soluções otimizadas sobre o roteamento da rede.
O algoritmo de geração de rotas (ACO) recebe as informações das rotas,
bem como as demandas dos usuários e aplicações e assim calcula um
conjunto de rotas distintas que podem ou não ser selecionadas como
soluções. Em seguida o algoritmo de otimização (AG ou DE) utiliza o
conjunto de rotas encontradas pelo algoritmo anterior e seleciona um
conjunto solução de rotas adequadas, ou seja, as rotas que melhor
atendem os requisitos das aplicações da rede em termos de vazão, atraso
fim-a-fim, prioridade e quantidade de conexões estabelecidas.

Ao final após avaliação utilizando a função objetivo a melhor solução no
tempo de execução disponível é retornada. Nem sempre a solução
encontrada é uma solução ótima. A seguir é mostrado o funcionamento dos
algoritmos ACO e DE.

### 4.4.1 Algoritmo ACO - AntNet com parâmetros de largura de banda

Usando a formulação matemática descrita na seção 3.2 é construída a
lógica do algoritmo ACO implementado no chamado modelo AntNet (DORIGO &
STÜTZLE, 2004). Optou-se por esse modelo por ser mais adequado ao
problema de roteamento. Segundo Dorigo e Stützle (2004), o AntNet é um
algoritmo projetado para ajudar a resolver problemas de roteamento em
redes de telecomunicações. O roteamento basicamente se refere as
atividades necessárias para orientar o fluxo do nó origem para o nó
destino, sendo considerado um importante problema e de difícil
resolução. A Figura 16 mostra o pseudo-código da versão do algoritmo ACO
para geração das rotas iniciais.

+-----------------------------------------------------------------------+
| Pseudo-Algoritmo ACO -- Baseado no Modelo AntNet                      |
|                                                                       |
| Entrada:  origem; destino; LarguraBanda; numero_de_formigas;          |
| numero_de_iteracoes;                                                  |
|                                                                       |
| Rho = 0.05; alpha = 1; beta = 1;                                      |
|                                                                       |
| Q: Taxa_de_Feromônio; A: Matriz_do_Grafo_da Rede; D:                  |
| Matriz_de_Distancias;                                                 |
|                                                                       |
| Saída: Conjunto_de_rotas;                                             |
|                                                                       |
| 1\. Tau0 = Q / (Media( D )); % Feromonio inicial                      |
|                                                                       |
| 2\. Tau = Tau0 \* A; % Matriz de Feromonio                            |
|                                                                       |
| 3\. Conjunto_de_rotas = \[ \]; P = \[ \];                             |
|                                                                       |
| 4\. VetorRota\[1\] = origem                                           |
|                                                                       |
| 5\. Para it = 1:numero_de_iteracoes                                   |
|                                                                       |
| 6\. Para j = 1:numero_de_formigas faça % Caminho de ida               |
|                                                                       |
| 7\. Enquanto (pos_atual \<\> destino) faça                            |
|                                                                       |
| 8\. P = Tau\[pos_atual\]\^alpha \* eta\[pos_atual\]\^beta;            |
|                                                                       |
| 9\. P = P/Soma(P);                                                    |
|                                                                       |
| 10\. prox_pos = Roleta(P);                                            |
|                                                                       |
| 11\. VetorRota\[j\] = prox_pos;                                       |
|                                                                       |
| 12\. pos_atual = prox_pos;                                            |
|                                                                       |
| 13\. Fim                                                              |
|                                                                       |
| 14\. RetirarLoops(VetorRota);                                         |
|                                                                       |
| 15\. Fim                                                              |
|                                                                       |
| 16\. Para k = 1:numero_de_formigas faça % Caminho de volta            |
|                                                                       |
| 17\. Para l = 1:tamanho(VetorRota\[k\]) faça                          |
|                                                                       |
| 18\. Tau = Tau + Q1\*LarguraBanda;                                    |
|                                                                       |
| 19\. Fim                                                              |
|                                                                       |
| 20\. Fim                                                              |
|                                                                       |
| 21\. Tau = (1 -- Rho) \* Tau; % Evaporação do feromônio               |
|                                                                       |
| 22\. Conjunto_de_rotas = concatena(Conjunto_de_rotas                  |
| ,VetorRota\[it\]);                                                    |
|                                                                       |
| 23\. Fim                                                              |
|                                                                       |
| 24\. Retorne Conjunto_de_Rotas                                        |
+=======================================================================+

Figura 16 - Pseudo-Algoritmo ACO.

Conforme descrito na Figura 16, o algoritmo AntNet encontra caminhos em
um grafo a partir de um nó origem em direção a um nó destino. No AntNet
tem-se uma estrutura de loop com a função de distribuir as formigas pelo
grafo (Caminho de ida: linha 6 a 15) utilizando a probabilidade P (linha
8) de seguir determinada direção (baseda na matriz de feromônio -- TAU e
na matriz de distância - ETA). O sorteio considerando essa probabilidade
é realizada usando um método de roleta (linha 10). Posteriormente é
utilizada uma função RetirarLoops (linha 14) para retirar os caminhos
que possuem loops desnecessários (caminhos que possuem nós repetidos).
Além da rotina de distribuição das formigas (Caminho de ida), temos uma
outra rotina responsável pelo retorno das formigas (Caminho de volta:
linha 16 a 20), essa estrutura é responsável pela função de atualização
da tabela de feromônio, que no caso do presente trabalho é atualizada de
forma proporcional ao valor de largura de banda daquela rota. Além
dessas duas estruturas de repetição internas, o AntNet possui uma
estrutura de repetição externa (linha 5 a 23) que executa um determinado
número de iterações do algoritmo e a cada ciclo atualiza a evaporação do
feromônio (linha 21). Realizada a descrição do algoritmo ACO é
apresentada a seguir a estrutura do algoritmo DE.

###  

### 

### 

### 

### 

### 

### 

### 

### 

### 

### 

### 4.4.2 Algoritmo DE aplicado a seleção de rotas

Usando a formulação matemática e os conceitos a respeito do Algoritmo DE
que foram descritos no item 3.4, foi construída a sua lógica conforme
mostrado na Figura 17.

+-----------------------------------------------------------------------+
| Pseudo-Algoritmo DE                                                   |
|                                                                       |
| Entrada:  M: Tamanho Da População; N: Dimensão da Variável;           |
|                                                                       |
| beta_min e beta_max: Intervalo da Probabilidade de Mutação;           |
|                                                                       |
| Pcr: Probabilidade De Cruzamento; Condição De Parada;                 |
|                                                                       |
| Saída: Melhor_Indivíduo;                                              |
|                                                                       |
| 1\. T = 1;                                                            |
|                                                                       |
| 2\. Cria População Inicial Aleatória P(T) = {X(T,I); I = 1,2,\...,M}; |
| % X(T,I) Individuo Da População                                       |
|                                                                       |
| 3\. Avalia População F (P(T));                                        |
|                                                                       |
| 4\. Enquanto: Condição De Parada Não Satisfeita Faça                  |
|                                                                       |
| 5\. Para I = 1: M                                                     |
|                                                                       |
| 6\. Seleciona Aleatoriamente(R1,R2,R3) $\mathbf{\in}$ 1,\...,M;       |
|                                                                       |
| 7\. Seleciona Aleatoriamente S(I) $\mathbf{\in}$ 1,\...,N;            |
|                                                                       |
| 8\. Para J = 1:N                                                      |
|                                                                       |
| 9\. Se Rand(0,1) \< Pcr Ou J = S(I) Então                             |
|                                                                       |
| 10\. BETA = Rand (beta_min,beta_max)                                  |
|                                                                       |
| 11\. U(T,I,J) = X(T,R1)+ BETA\*(U(T,R2)- U(T,R3))                     |
|                                                                       |
| 12\. Senão                                                            |
|                                                                       |
| 13\. U(T,I,J) = X(T,I,J);                                             |
|                                                                       |
| 14\. Fim                                                              |
|                                                                       |
| 15\. Fim                                                              |
|                                                                       |
| 16\. Fim                                                              |
|                                                                       |
| 17\. Para I = 1: M                                                    |
|                                                                       |
| 18\. Se F (U(T,I)) \< F (X(T,I)) Então                                |
|                                                                       |
| 19\. X(T+1,I) = U(T,I);                                               |
|                                                                       |
| 20\. Senão                                                            |
|                                                                       |
| 21\. X(T+1,I) = X(T,I);                                               |
|                                                                       |
| 22\. Fim                                                              |
|                                                                       |
| 23\. Fim                                                              |
|                                                                       |
| 24\. T = T + 1;                                                       |
|                                                                       |
| 25\. Fim                                                              |
|                                                                       |
| 26\. Retorne Melhor_Indivíduo;                                        |
+=======================================================================+

Figura 17 - Pseudo-Algoritmo DE - Fonte: Adaptado de Araújo (2016)

Conforme descrito na Figura 17, o funcionamento do algoritmo DE é
baseado na escolha de melhores soluções que são avaliadas usando uma
função de avaliação ou função de aptidão (fitness). As melhores soluções
são selecionadas e substituem as soluções anteriores. Os novos
indivíduos são gerados pelos processos de mutação e cruzamento, através
de uma soma vetorial aleatória entre indivíduos da população. O DE
implementado trabalha com números reais que são arrendondados para gerar
indivíduos que são vetores de números inteiros.

Ao final do algoritmo é retornado o melhor indivíduo, sendo este um
vetor de números inteiros de tamanho N que é a dimensão da variável do
problema. Na modelagem adotada para o problema de engenharia de tráfego
a variável N é o número de conexões demandadas simultaneamente pelos
usuários da rede, que no caso da equação 4.1 é também a variável L.

Então dessa forma os indivíduos retornados pelos algoritmos AG e DE são
vetores inteiros que fazem referência a determinadas conexões
anteriormente calculadas pelo ACO.

Lembrando que o algoritmo ACO calcula um número maior de rotas em
relação às rotas demandadas pelos usuários da rede, isto é, para cada
conexão com uma determinada origem e destino, são calculadas várias
opções de rotas. Esta disponibilidade de rotas é proposital e o que
torna possível a sua seleção pelos algoritmos de otimização AG e DE
usando a função objetivo ou função de avaliação, obtêm-se o fitness
(aptidão) de cada indivíduo que determina sua nota com base nos
critérios de QOS adotados: largura de banda, atraso fim-a-fim e
adicionou-se a prioridade da conexão e número de conexões estabelecidas.

Assim nesta implementação pretende-se obter indivíduos que fazem
referência a um conjunto solução das rotas que satisfaçam as exigências
e demandas dos usuários e aplicações da rede.

## 4.5 Modelo de Otimização utilizando ACO e AG

No segundo modelo implementado adotou-se os algoritmos ACO e AG para
otimizar o roteamento dos pacotes da rede. A Figura 18 apresenta o
segundo modelo de otimização proposto.

![](media/image16.png){width="6.449163385826772in" height="2.71875in"}

Figura 18 -- Modelo de otimização utilizando as heurísticas ACO e AG.

O modelo apresentado na Figura 18 utiliza de forma híbrida dois
algoritmos, a única diferença em relação ao modelo anterior é que o
algoritmo responsável pela seleção das rotas é o Algoritmo Genético (AG)
em substituição ao algoritmo DE. Esse modelo é escolhido como forma de
compararmos o desempenho dos algoritmos DE e AG no processo de
otimização das rotas a serem selecionadas. Assim como anteriormente foi
realizada a descrição do algoritmo DE aplicado a seleção de rotas,
realiza-se então a descrição do algoritmo AG aplicado a seleção de
rotas.

### 4.5.1 Algoritmo AG aplicado a seleção de rotas

Usando a formulação matemática e os conceitos a respeito do Algoritmo AG
que foram descritos no item 3.5, é construída a sua lógica conforme
detalhado na Figura 19.

+----------------------------------------------------------------------+
| Pseudo-Algoritmo Ag                                                  |
|                                                                      |
| Entrada:  M: Tamanho Da População; N: Dimensão Da Variável;          |
|                                                                      |
| Pm: Probabilidade De Mutação; Pc: Probabilidade De Cruzamento;       |
| Condição De Parada;                                                  |
|                                                                      |
| Saída: Melhor_Indivíduo;                                             |
|                                                                      |
| 1\. T = 0; P = Ø;                                                    |
|                                                                      |
| 2\. Inicializa (P(T),M,N);                                           |
|                                                                      |
| 3\. Avalia-se F(P(T));                                               |
|                                                                      |
| 4\. Enquanto: Condição De Parada Não Satisfeita Faça                 |
|                                                                      |
| 5\. T = T + 1;                                                       |
|                                                                      |
| 6\. S(T) = Selecao(P(T-1));                                          |
|                                                                      |
| 7\. Q(T) = Cruzamento(S(T),Pc);                                      |
|                                                                      |
| 8\. Q(T)' = Mutacao(Q(T),Pm);                                        |
|                                                                      |
| 9\. Q(T)' = Avalia-se F(Q(T)');                                      |
|                                                                      |
| 10\. P(T) = Substituicao(P(T-1) U Q(T)');                            |
|                                                                      |
| 11\. Fim                                                             |
|                                                                      |
| 12\. Retorne Melhor_Indivíduo;                                       |
+======================================================================+

Figura 19 - Pseudo-Algoritmo DE - Fonte: Adaptado de Michalewicz (1996).

Conforme descrito na Figura 19, o algoritmo AG gera uma população
inicial aleatória de indivíduos P (Cada indivíduo é um conjunto de
Rotas) que é avaliada. A partir do valor da função de aptidão ou fitness
computado para cada indivíduo, seleciona-se os indivíduos (Seleção) para
posterior cruzamento e mutação, gerando uma população de soluções
filhas. Os operadores utilizados são: cruzamento polarizado e mutação
real. Sendo que a cada operação os valores são arrendondados e ao final
deve-se obter indivívuos que são vetores de números inteiros.

No AG assim como no DE o indivíduo é um vetor de números inteiros de
tamanho N, onde N é número de conexões demandadas simultaneamente pelos
usuários da rede. Dessa forma o AG obtém um indivíduo que faz referência
a um conjunto de melhores rotas selecionadas (otimizadas) segundo
critérios considerados pela função objetivo (FO) ou função de aptidão
(fitness).

## 

## 4.6 Modelo de comparação utilizando o algoritmo de Dijkstra

## 

Segundo Kurose e Ross (2010) o OSPF (Open Shortest Path First) é
principal algoritmo de roteamento das redes IP atuais, tendo como base
do seu funcionamento o algoritmo de Dijkstra, o qual define o menor
caminho entre os nós (dispositivos) de um grafo (rede). Em função disso
utilizou-se o algoritmo de Dijkstra para comparação de desempenho em
relação aos modelos (ACO+DE e ACO+AG) propostos no presente trabalho.
Posteriormente realiza-se a implementação de uma rede SDN otimizada
utilizando rotas do modelo ACO+DE ou ACO+AG e uma rede SDN utilizando
rotas geradas pelo Dijkstra.

## 4.7 Considerações Finais

Foi apresentado neste capítulo, o Modelo da engenharia de tráfego
aplicada às redes definidas por software utilizando os algoritmos de
otimização: ACO+DE e ACO+AG. Posteriormente foram apresentados o Método
Proposto sobre a implementação hibrida dos algoritmos de otimização, o
Modelo Geral de Engenharia de tráfego em SDN e a Modelagem Matemática do
problema. Por fim é apresentado os modelos implementados utilizando as
heurísticas ACO+DE e ACO+AG e o modelo de comparação utilizando o
algoritmo de Dijkstra.

No próximo capítulo são realizadas as implementações dos algoritmos de
otimização e da rede SDN.

# IMPLEMENTAÇÕES DOS ALGORITMOS DE OTIMIZAÇÃO E REDE SDN

Neste capítulo são apresentados os algoritmos de otimização
implementados e os resultados dos testes e ajustes de parâmetros dos
algoritmos ACO, AG e DE. Inicialmente, na seção 5.1 é apresentada a
topologia escolhida a qual servirá de base para os testes do presente
trabalho. Na seção 5.2 é realizada a apresentação da implementação e
ajustes dos parâmetros do algoritmo de roteamento ACO. Na seção 5.3 são
apresentados os testes e ajustes dos parâmetros dos algoritmos AG e DE.
Na seção 5.4 é apresentada a implementação da rede SDN. Finalmente, na
seção 5.5 são realizadas algumas considerações finais.

##  5.1 Propriedades da Topologia

Nessa implementação optou-se por utilizar uma rede SDN usando a
topologia mostrada na Figura 20. A topologia possui complexidade
intermediária com um total de 52 nós e 66 enlaces (links) bidirecionais
que permitem a conexão entre todos os nós da rede.

![](media/image17.png){width="5.399066054243219in"
height="4.302083333333333in"}

Figura 20 -- Topologia adotada - Fonte: Adaptado de Maia (2006).

Na Figura 20, do total de 52 nós, 36 correspondem a hosts (Do 1 ao 13 e
do 30 ao 52) e 16 correspondem a dispositivos de encaminhamento que
podem ser switches ou roteadores (Do 14 ao 29). Essa topologia foi uma
das adotadas no trabalho de Maia (2006) para otimização do roteamento de
pacotes utilizando lógica nebulosa para criação de novas rotas numa rede
MPLS, considerando requisitos de QoS.

Na topologia da Figura 20 é realizado um teste de simulação com um total
de 17 aplicações, como proposto por Maia (2006), para demonstrar a
capacidade dos algoritmos de realizar a TE para um conjunto de
aplicações com diferentes exigências de Vazão, Atraso e Prioridade de
tráfego, conforme descrito na Tabela 1. Essas informações são restrições
do problema em termos do tipo de aplicação utilizada por determinados
usuários que necessitam de uma dada conexão com origem, destino,
prioridade e determinados limites mínimos de vazão com um máximo de
atraso fim-a-fim.

Tabela 1 -- Demandas de Vazão, Atraso e Prioridade de tráfego de
diferentes aplicações

  -------------- --------- --------- ---------- ------------ --------------
    Aplicação    Origem    Destino   Vazão      Atraso (ms)  Prioridade
                                     (Mbps)                  

   Dados (Ftp0)  52        49        0,256      \< 1000      0

   Dados (Ftp1)  1         33        0,256      \< 1000      0

      Vídeo0     2         51        1,744      \< 150       0

      Vídeo1     3         50        1,256      \< 150       5

   Dados (Ftp2)  4         37        0,256      \< 1000      0

   Dados (Ftp3)  31        36        0,256      \< 1000      0

   Dados (Ftp4)  32        46        0,256      \< 1000      0

       Voz0      5         48        0,512      \< 150       5

       Voz1      6         47        0,512      \< 150       5

   Dados (Ftp5)  7         34        0,256      \< 1000      0

      Vídeo2     8         44        1,256      \< 150       5

      Vídeo3     9         43        1,256      \< 150       0

       Voz2      11        41        0,512      \< 150       5

   Dados (Ftp6)  10        42        0,256      \< 1000      0

       Voz3      12        40        0,512      \< 150       5

   Dados (Ftp7)  13        39        0,256      \< 1000      0

   Dados (Ftp8)  30        45        0,256      \< 1000      0
  -------------- --------- --------- ---------- ------------ --------------

Na Tabela 2 tem-se a relação dos enlaces da parte interna ou núcleo
desta topologia com suas respectivas capacidades de vazão e atraso.
Estes enlaces são as ligações entre os dispositivos de encaminhamento da
rede.

Tabela 2 -- Limites de Largura de Banda e Atraso mínimo dos enlaces do
núcleo da Rede.

  ------------------------------------------------------------------------
  Nó de origem      Nó de destino     Largura de banda    Atraso mínimo
                                      (Mbps)              (ms)
  ----------------- ----------------- ------------------- ----------------
  14                15                2                   30

  14                16                2                   20

  14                20                2                   30

  15                21                2                   20

  16                20                2                   20

  17                16                2                   20

  17                18                2                   10

  17                19                2                   30

  17                25                2                   10

  18                26                2                   10

  19                20                2                   20

  19                23                2                   20

  19                24                2                   20

  19                25                2                   40

  20                21                2                   20

  20                22                2                   10

  20                23                2                   10

  21                22                2                   20

  22                29                2                   10

  23                22                2                   20

  23                24                2                   10

  23                28                2                   20

  23                29                2                   20

  24                25                2                   30

  24                27                2                   30

  24                28                2                   10

  25                26                2                   30

  25                27                2                   10

  26                27                2                   10

  27                28                2                   80
  ------------------------------------------------------------------------

Para os demais enlaces periféricos dessa topologia foi também adotado um
valor de largura de banda igual a 2 Mbps e para os atrasos mínimos foi
adotado o valor de 1 ms.

## 5.2 Implementação e ajustes dos parâmetros do algoritmo de roteamento ACO

Após realizada a modelagem dos grafos da topologia adotada, bem como o
tratamento e entrada de dados das informações sobre largura, atraso,
prioridade e aplicações/usuários foi realizada a implementado os modelos
descritos no capítulo 3. Após a implementação dos modelos, é importante
ajustar os seus parâmetros para avaliar quais valores estes devem
assumir para que se obtenha um melhor desempenho dos algoritmos.

Os testes foram realizados com a seguinte metodologia: define-se os
parâmetros que devem ser variados em cada um dos algoritmos e executa-se
100 vezes para cada configuração, ao final calcula-se a média, o
desvio-padrão, o máximo e o mínimo dos valores obtidos pela função
objetivo. Após realização dos testes com todas as variações de
parâmetros (diferentes configurações), deve-se avaliar o teste com
melhor desempenho e adotar seus parâmetros para aquele algoritmo. Os
testes 1 e 2 foram realizados para validar os parâmetros do algoritmo
ACO. Os testes 3 e 4 foram realizados para validar os parâmetros dos
algoritmos AG e DE respectivamente.

### 

### 

### 

### 

### 

### 

### 5.2.1 Teste 1: Ajuste dos parâmetros do algoritmo ACO (Modelo ACO+AG)

Este teste foi realizado com 16 variações de parâmetros do algoritmo
ACO, sendo 4 variações do parâmetro números de formigas e 4 no número de
iterações. Para cada nova configuração foram realizadas 100 execuções.
Na Tabela 3 tem-se a relação dos parâmetros utilizados neste teste. Os
parâmetros iniciais utilizados no algoritmo AG foram os mesmos valores
utilizados em Heris (2016b).

Tabela 3 - Teste de ajuste dos parâmetros do algoritmo ACO (Modelo
ACO+AG).

+-----------------------------+----------------------------------------+
| ACO - Número de parâmetros  | 2 parâmetros com 4 variações cada.     |
| a serem testados:           |                                        |
+:===========================:+========================================+
| ACO - Parâmetros a serem    | Número de Iterações assumindo valores  |
| avaliados (variáveis):      | de 50,100,150 e 200.                   |
|                             |                                        |
|                             | Número de Formigas assumindo valores   |
|                             | de 50,100,150 e 200.                   |
+-----------------------------+----------------------------------------+
| ACO - Parâmetros fixos:     | Alpha (Peso do Feromônio) = 1;         |
|                             |                                        |
|                             | Beta (Peso da Heurística) = 1;         |
|                             |                                        |
|                             | Rho (Taxa de evaporação) = 0.05;       |
+-----------------------------+----------------------------------------+
| AG - Parâmetros fixos:      | Número de Iterações = 200;             |
|                             |                                        |
|                             | Tamanho da População = 50;             |
|                             |                                        |
|                             | Pm (Probabilidade de mutação) = 0.7;   |
|                             |                                        |
|                             | Mu (Taxa de mutação) = 0.1;            |
|                             |                                        |
|                             | Pc (Probabilidade de cruzamento) =     |
|                             | 0.3;                                   |
|                             |                                        |
|                             | Gamma (Fator Extra de cruzamento) =    |
|                             | 0.4;                                   |
+-----------------------------+----------------------------------------+

A Figura 21 contempla o comportamento dos valores médios da função
objetivo para 16 variações do algoritmo ACO (Modelo ACO+AG).

Os resultados mostrados na Figura 21 mostram que o melhor valor da
função objetivo foi obtido quando o parâmetro do número de iterações é
igual a 200 e quando o parâmetro do número de formigas assume valor
igual a 50.

![](media/image18.png){width="7.4311209536307965in"
height="3.5416666666666665in"}

Figura 21 -- Gráfico de desempenho do modelo ACO+AG variando os
parâmetros do Algoritmo ACO: Número de Formigas e Iterações.

Na Tabela 4 é apresentado o melhor resultado obtido no teste 1, bem como
os respectivos valores dos parâmetros avaliados. Estes resultados foram
calculados com base nos valores obtidos pela função objetivo.

Tabela 4 - Resultados do teste de ajuste dos parâmetros do algoritmo ACO
(Modelo ACO+AG).

  -----------------------------------------------------------------------
      Melhor valor médio da função     128,0008
               objetivo:               
  ------------------------------------ ----------------------------------
     Desvio padrão do valor médio:     3,4672

    Máximo valor da função objetivo:   132

    Mínimo valor da função objetivo:   108

    **Valor do parâmetro: Número de    **50**
               Formigas**              

    **Valor do parâmetro: Número de    **200**
              Iterações**              
  -----------------------------------------------------------------------

### 

### 

### 

### 5.2.2 Teste 2: Teste de ajuste dos parâmetros do algoritmo ACO (Modelo ACO+DE)

Este teste foi realizado com 16 variações de parâmetros do algoritmo
ACO, sendo 4 variações do parâmetro números de formigas e 4 no número de
iterações. Para cada nova configuração foram realizadas 100 execuções.
Na Tabela 5 tem-se a relação dos parâmetros utilizados neste teste. Os
parâmetros iniciais utilizados no algoritmo DE foram os mesmos valores
utilizados em Heris (2016a).

Tabela 5 - Teste de ajuste dos parâmetros do algoritmo ACO (Modelo
ACO+DE).

+------------------------------+---------------------------------------+
| ACO - Número de parâmetros a | 2 parâmetros com 4 variações cada.    |
| serem testados:              |                                       |
+:============================:+=======================================+
| ACO - Parâmetros a serem     | Número de Iterações assumindo valores |
| avaliados (variáveis):       | de 50,100,150 e 200.                  |
|                              |                                       |
|                              | Número de Formigas assumindo valores  |
|                              | de 50,100,150 e 200.                  |
+------------------------------+---------------------------------------+
| ACO - Parâmetros fixos:      | Alpha (Peso do Feromônio) = 1;        |
|                              |                                       |
|                              | Beta (Peso da Heurística) = 1;        |
|                              |                                       |
|                              | Rho (Taxa de evaporação) = 0.05;      |
+------------------------------+---------------------------------------+
| DE - Parâmetros fixos:       | Número de Iterações = 200;            |
|                              |                                       |
|                              | Tamanho da População = 50;            |
|                              |                                       |
|                              | Beta_min (Menor valor da Prob. de     |
|                              | Mutação) = 0.2;                       |
|                              |                                       |
|                              | Beta_max (Maior valor da Prob. de     |
|                              | Mutação) = 0.8;                       |
|                              |                                       |
|                              | Pcr (Probabilidade de cruzamento) =   |
|                              | 0.2;                                  |
+------------------------------+---------------------------------------+

A partir da Figura 22 é possível avaliarmos o comportamento dos valores
médios da função objetivo para 16 variações do algoritmo ACO (Modelo
ACO+DE).

Assim como no teste anterior (ACO+AG), é possível observar que o melhor
valor da função objetivo foi obtido quando o parâmetro do número de
iterações é igual a 200 e quando o parâmetro do número de formigas
assume valor igual a 50.

![](media/image19.png){width="7.409722222222222in"
height="3.5314676290463693in"}

Figura 22 -- Gráfico de desempenho do modelo ACO+DE variando os
parâmetros do Algoritmo ACO: Número de Formigas e Iterações.

Na Tabela 6 é apresentado o melhor resultado obtido no teste 2, bem como
os respectivos valores dos parâmetros avaliados. Estes resultados foram
calculados com base nos valores obtidos pela função objetivo.

Tabela 6 - Resultados do teste de ajuste dos parâmetros do algoritmo ACO
(Modelo ACO+DE).

  -----------------------------------------------------------------------
      Melhor valor médio da função      126,7940
                objetivo:               
  ------------------------------------- ---------------------------------
      Desvio padrão do valor médio:     2,9457

    Máximo valor da função objetivo:    132

    Mínimo valor da função objetivo:    106

     **Valor do parâmetro: Número de    **50**
               Formigas**               

     **Valor do parâmetro: Número de    **200**
               Iterações**              
  -----------------------------------------------------------------------

No Quadro 1 temos os resultados nos testes 1 e 2 de ajustes do algoritmo
ACO, nele tem-se os resultados obtidos pelos modelos ACO+AG e ACO+DE
para cada uma das configurações de parâmetros testados.

Quadro 1 -- Resultados do teste 1 e 2 do Algoritmo ACO

+----------+-----+--------+-------------------------------------------------------------------------------------------------------------------------------+
|          |     |        | ACO - Número de Iterações                                                                                                     |
+==========+=====+========+===============+===============+===============+===============+===============+===============+===============+===============+
|          |     |        | 50                            | 100                           | 150                           | 200                           |
+----------+-----+--------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+
|          |     |        | AG            | DE            | AG            | DE            | AG            | DE            | AG            | DE            |
+----------+-----+--------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+
| ACO -    | 50  | Média  | 127,656       | 126,7101      | 127,6621      | 126,5132      | 127,419       | 126,5024      | 128,0008      | 126,794       |
| Número   |     |        |               |               |               |               |               |               |               |               |
| de       |     |        |               |               |               |               |               |               |               |               |
| Formigas |     |        |               |               |               |               |               |               |               |               |
|          |     +--------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+
|          |     | Desvio | 3,5171        | 3,1076        | 3,533         | 3,0445        | 3,7804        | 3,1247        | 3,4672        | 2,9457        |
|          |     +--------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+
|          |     | Max    | 132           | 130           | 132           | 130           | 132           | 130           | 132           | 132           |
|          |     +--------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+
|          |     | Min    | 107           | 105           | 105           | 108           | 106           | 106           | 108           | 106           |
|          +-----+--------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+
|          | 100 | Média  | 127,3966      | 125,9854      | 127,3387      | 126,1278      | 127,6712      | 126,1536      | 127,8165      | 126,1601      |
|          |     +--------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+
|          |     | Desvio | 4,0977        | 3,4324        | 3,7103        | 3,281         | 3,778         | 3,1273        | 3,9254        | 3,1904        |
|          |     +--------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+
|          |     | Max    | 132           | 130           | 132           | 130           | 132           | 132           | 132           | 132           |
|          |     +--------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+
|          |     | Min    | 104           | 105           | 105           | 105           | 106           | 106           | 105           | 106           |
|          +-----+--------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+
|          | 150 | Média  | 127,672       | 126,3426      | 127,5029      | 126,3084      | 127,4062      | 126,1267      | 127,4687      | 126,0244      |
|          |     +--------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+
|          |     | Desvio | 3,6812        | 3,1544        | 3,8379        | 3,1418        | 3,5811        | 3,1677        | 3,9514        | 3,1382        |
|          |     +--------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+
|          |     | Max    | 132           | 130           | 132           | 130           | 132           | 130           | 132           | 132           |
|          |     +--------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+
|          |     | Min    | 106           | 104           | 104           | 101           | 105           | 106           | 104           | 106           |
|          +-----+--------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+
|          | 200 | Média  | 127,4688      | 126,0899      | 127,6092      | 125,9203      | 127,2663      | 125,9325      | 127,3769      | 125,9528      |
|          |     +--------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+
|          |     | Desvio | 3,9483        | 3,2968        | 3,7957        | 3,2879        | 4,1333        | 3,3398        | 4,3952        | 3,6993        |
|          |     +--------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+
|          |     | Max    | 132           | 130           | 132           | 130           | 132           | 130           | 132           | 132           |
|          |     +--------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+
|          |     | Min    | 104           | 106           | 103           | 105           | 102           | 104           | 101           | 100           |
+----------+-----+--------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+

Conforme os resultados do Quadro 1 pode-se verificar que os valores de
desempenho médio do algoritmo AG foram levemente superiores ao do
algoritmo DE em todos os 16 diferentes cenários testados. Da mesma
maneira, os valores de fitness máximos do AG também foram superiores aos
do DE em todos os 16 testes, apesar dos valores de fitness mínimos do AG
serem inferiores aos do DE na maioria dos 16 testes.

## 5.3 Testes e ajustes dos parâmetros dos algoritmos AG e DE

Após o ajuste implementado no algoritmo ACO foram realizados os testes
nos algoritmos AG e DE. Assim, mantendo-se fixo os melhores valores
obtidos nos testes 1 e 2 realizados para o algoritmo ACO, pode-se
realizar nos itens seguintes os ajustes dos parâmetros dos algoritmos.

### 5.3.1 Teste 3: Ajuste dos parâmetros do algoritmo AG (Modelo ACO+AG)

Este teste foi realizado com 100 variações de parâmetros do algoritmo
AG. Cada variação foi executada 100 vezes, sendo 10 variações do
parâmetro: Probabilidade de mutação e 10 variações do parâmetro:
Probabilidade de cruzamento. Cada variação foi executada 100 vezes. Na
Tabela 7 temos a relação dos parâmetros utilizados neste teste.

Tabela 7 - Teste de ajuste dos parâmetros do algoritmo AG (Modelo
ACO+AG)

+------------------------------+---------------------------------------+
| AG - Número de parâmetros a  | 2 parâmetros com 10 variações cada.   |
| serem testados:              |                                       |
+:============================:+=======================================+
| AG - Parâmetros a serem      | Probabilidade de mutação (Pm)         |
| avaliados (variáveis):       | assumindo valores de 0.1,             |
|                              | 0.2,0.3,0.4, 0.5, 0.6, 0.7, 0.8, 0.9, |
|                              | 1.                                    |
|                              |                                       |
|                              | Probabilidade de cruzamento (Pc)      |
|                              | assumindo valores de 0.1, 0.2, 0.3,   |
|                              | 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 e 1.     |
+------------------------------+---------------------------------------+
| AG - Parâmetros fixos:       | Número de Iterações = 200;            |
|                              |                                       |
|                              | Tamanho da População = 50;            |
|                              |                                       |
|                              | Mu (Taxa de mutação) = 0.1;           |
|                              |                                       |
|                              | Gamma (Fator extra de cruzamento) =   |
|                              | 0.4;                                  |
+------------------------------+---------------------------------------+
| ACO - Parâmetros fixos:      | Número de Iterações: 200;             |
|                              |                                       |
|                              | Número de Formigas: 50;               |
|                              |                                       |
|                              | Alpha (Peso do Feromônio) = 1;        |
|                              |                                       |
|                              | Beta (Peso da Heurística) = 1;        |
|                              |                                       |
|                              | Rho (Taxa de evaporação) = 0.05;      |
+------------------------------+---------------------------------------+

A partir da Figura 23 é possível avaliarmos o comportamento dos valores
médios da função objetivo para 100 variações do algoritmo AG (Modelo
ACO+AG). Como resultado tem-se que o melhor valor da função objetivo é
obtido quando os parâmetros probabilidade de mutação e probabilidade de
cruzamento assumem valores iguais a 0,9.

![](media/image20.png){width="7.603772965879265in"
height="3.6239523184601925in"}

Figura 23 -- Gráfico de desempenho dos algoritmos ACO+AG variando os
parâmetros de probabilidade de mutação (Pm) e probabilidade de
cruzamento (Pc) do algoritmo AG.

Na Tabela 8 é apresentado o melhor resultado obtido no teste 3, bem como
os respectivos valores dos parâmetros avaliados.

Tabela 8 - Resultados do teste de ajuste dos parâmetros do algoritmo AG

(Modelo ACO+AG).

  -----------------------------------------------------------------------
      Melhor valor médio da função objetivo:     128,9678
  ---------------------------------------------- ------------------------
          Desvio padrão do valor médio:          3,1802

         Máximo valor da função objetivo:        132

         Mínimo valor da função objetivo:        106

  **Valor do parâmetro: Probabilidade de mutação **0,9**
                      (Pm)**                     

      **Valor do parâmetro: Probabilidade de     **0,9**
                cruzamento (Pc)**                
  -----------------------------------------------------------------------

### 5.3.2 Teste 4: Ajuste dos parâmetros do algoritmo DE (Modelo ACO+DE)

Este teste foi realizado com 100 variações de parâmetros do algoritmo
DE. Cada variação foi executada 100 vezes, variando somente o parâmetro
de probabilidade de cruzamento (Pcr), em virtude do algoritmo DE adotado
ter o parâmetro Beta (Prob. de Mutação) randômico entre dois intervalos
(Beta_min e Beta_max). Na Tabela 9 temos a relação dos parâmetros
utilizados neste teste.

Tabela 9 - Teste de ajuste dos parâmetros do algoritmo DE (Modelo
ACO+DE)

+--------------------------------+-------------------------------------+
| DE - Número de parâmetros a    | 1 parâmetros com 100 variações.     |
| serem testados:                |                                     |
+:==============================:+=====================================+
| DE - Parâmetros a serem        | Probabilidade de cruzamento (Pcr)   |
| avaliados (variáveis):         | assumindo valores de 0.01 até 1,    |
|                                | acrescidos de 0.01.                 |
+--------------------------------+-------------------------------------+
| DE - Parâmetros fixos:         | Número de Iterações = 200;          |
|                                |                                     |
|                                | Tamanho da População = 50;          |
|                                |                                     |
|                                | Beta_min (Menor valor da Prob. de   |
|                                | Mutação) = 0.2; Beta_max (Maior     |
|                                | valor da Prob. de Mutação) = 0.8;   |
+--------------------------------+-------------------------------------+
| ACO - Parâmetros fixos:        | Número de Iterações: 200;           |
|                                |                                     |
|                                | Número de Formigas: 50;             |
|                                |                                     |
|                                | Alpha (Peso do Feromônio) = 1;      |
|                                |                                     |
|                                | Beta (Peso da Heurística) = 1;      |
|                                |                                     |
|                                | Rho (Taxa de evaporação) = 0.05;    |
+--------------------------------+-------------------------------------+

A partir da Figura 24 é possível avaliarmos o comportamento dos valores
médios da função objetivo para 100 variações do algoritmo DE (Modelo
ACO+DE), sendo possível observar que o melhor valor foi obtido quando o
parâmetro de probabilidade de cruzamento assume o valor igual 0,01.

![](media/image21.png){width="7.703834208223972in"
height="3.6716415135608047in"}

Figura 24 -- Gráfico de desempenho dos algoritmos ACO+DE variando o
parâmetro de probabilidade de cruzamento (Pcr) do algoritmo DE.

Na Tabela 10 é apresentado o melhor resultado obtido no teste 4, bem
como o valor do parâmetro avaliado.

Tabela 10 - Resultados do teste de ajuste dos parâmetros do algoritmo DE

(Modelo ACO+DE).

  -----------------------------------------------------------------------
      Melhor valor médio da função objetivo:      127,8924
  ----------------------------------------------- -----------------------
           Desvio padrão do valor médio:          3,6834

         Máximo valor da função objetivo:         132

         Mínimo valor da função objetivo:         105

      **Valor do parâmetro: Probabilidade de      **0,01**
                cruzamento (Pcr)**                
  -----------------------------------------------------------------------

Finalizados os testes e ajustes dos algoritmos de otimização, a etapa
seguinte é realização da implementação da rede SDN.

## 5.4 Implementação da rede SDN

Os resultados das implementações dos algoritmos de otimização (ACO+AG e
ACO+DE) são um conjunto de rotas que devem ser utilizadas no roteamento
da rede SDN a ser implementada no presente trabalho resultando em uma
rede otimizada. Foi implementada também uma outra rede SDN utilizando o
algoritmo de Dijkstra que calcula as rotas sempre considerando o menor
caminho.

A rede utilizando as soluções das rotas encontradas pelo algoritmo de
Dijkstra, será comparada com a rede otimizada. As implementações da rede
SDN otimizada e da rede SDN com Dijkstra foram realizadas através dos
seguintes passos:

\- Por meio do emulador Mininet foi criada uma rede que define todos os
seus dispositivos e outras propriedades como endereços Mac e IP.

\- Na sequência utilizou-se o controlador Floodlight para realizar o
controle da rede através do módulo Static Entry Pusher para alterar as
tabelas de roteamento dos seus dispositivos.

\- Em seguida realizou-se a geração e a medição do tráfego na rede
utilizando o software D-ITG.

\- Por fim utilizou-se algumas funções do sFlow-RT para observação e
verificação do comportamento dos fluxos de dados injetados na rede.

Com as informações da topologia adotada foi então criado um mecanismo
para estabelecer a topologia da rede com seus dispositivos, portas,
enlaces e as suas respectivas propriedades de largura de banda e atraso
conforme a Tabela 2 e a Figura 25 a seguir.

![](media/image22.png){width="6.58441491688539in"
height="4.754808617672791in"}

Figura 25 -- Topologia da rede considerando as portas dos dispositivos
ligando os enlaces Adaptado de Maia (2006).

A Figura 25 difere da Figura 20 pela simbologia utilizada nos
dispositivos de encaminhamento e também pela adição da numeração de cada
uma das portas de todos os dispositivos da rede. Esta informação
adicional é necessária para a criação do conjunto de comandos Post a
serem enviados para o controlador como forma de alterar as tabelas de
encaminhamento e estabelecer rotas específicas a partir dos endereços de
origem e destino dos pacotes. Por exemplo a primeira rota selecionada
pelo ACO+AG no Quadro 3 é a sequência: 52-17-18-26-27-49, isto é, uma
conexão saindo do host 52 e chegando ao host 49 passando pelos
dispositivos de encaminhamento 17, 18, 26 e 27. Essa rota pode ser
estabelecida utilizando os comandos POST da Figura 7 com informações
para alterar as tabelas dos roteadores 17, 18, 26 e 27 informando que
pacotes com endereço IP de origem: 10.0.1.52 (host 52) e IP de destino:
10.0.1.49 (host 49) devem ser encaminhados utilizando as seguintes
etapas:

1° Etapa: No host 52 o pacote deve ser encaminhado para a porta 1 que o
direciona para o dispositivo 17.

2° Etapa: No dispositivo 17 o pacote deve ser encaminhado para a porta 9
que o direciona para o dispositivo 18.

3° Etapa: No dispositivo 18 o pacote deve ser encaminhado para a porta 4
que o direciona para o dispositivo 26.

4° Etapa: No dispositivo 26 o pacote deve ser encaminhado para a porta 6
que o direciona para o dispositivo 27.

5° Etapa: No dispositivo 27 o pacote deve ser encaminhado para a porta 3
que o direciona para o host 49.

Dessa forma é estabelecida a forma como os dados serão enviados do host
52 ao host 49.

### 5.4.1 Geração dos comandos POST via código Matlab

Como forma de realizar-se o controle de rotas no controlador Floodlight
optou-se no presente trabalho pela utilização do módulo Static Entry
Pusher o qual realiza as alterações nas tabelas dos dispositivos de
encaminhamento. No entanto, para isso é necessário a geração dos
comandos POST no formato JSON para posterior envio ao controlador
Floodlight. Em virtude da topologia a ser implementada possuir loops
internos, deve-se ter o devido cuidado de estabelecer e enviar ao
controlador todas as possíveis rotas entre os dispositivos da rede, como
forma de evitar a ocorrência de tempestades de broadcast devido aos
loops de comutação. A solução desse problema utilizando o Protocolo STP
(Spanning Tree Protocol) limita alguns enlaces da rede e em função disso
foi descartada.

Em virtude da necessidade do estabelecimento de caminhos (rotas) entre
os dispositivos da rede, optou-se pela criação de um script usando
Matlab que funciona seguinte forma: A partir da topologia da Figura 25
foi criada uma matriz de adjacência que considera os números das portas
entre os dispositivos como o valor que define a existência de uma
conexão, ou seja, para valores diferentes de 0 a conexão existe e se
estabelece atráves da porta informada naquela posição da matriz, para
valores iguais a 0 a conexão não existe. Em seguida calcula-se as rotas
entre todos os dispositivos utilizando o algoritmo de Dijkstra e então a
partir desse conjunto de rotas, aliado ao conhecimento das portas de
cada dispositivo obtida da matriz de adjacência, pode-se gerar a
sequência de comandos POST. Esse conjunto de comandos POST ao ser
enviado ao controlador por meio do módulo Static Entry Pusher é
suficiente para configurar todas as rotas dentro da rede SDN que utiliza
Dijkstra.

Para se obter a rede com rotas otimizadas, deve-se inserir essas rotas
otimizadas (calculadas via ACO+AG ou ACO+DE) substituindo uma parcela de
rotas calculadas via algoritmo de Dijkstra e assim no momento da geração
dos comandos POST essas rotas já estarão atualizadas e sendo
reconhecidas e assim será obtida a rede SDN otimizada.

![](media/image23.png){width="6.46875in" height="5.03792760279965in"}

Figura 26 -- Tela do Floodlight mostrando as tabelas do Switch 17.

Conforme a Figura 26 pode-se, por meio da interface GUI do Floodlight,
verificar as tabelas de encaminhamento do Swicth 17 preenchidas com
regras de roteamento.

### 5.4.2 Injeção de tráfego na rede utilizando o D-ITG

A partir da Tabela 11 é definido o conjunto de aplicações a serem
simuladas na rede SDN implementada. Cada uma dessas aplicações necessita
de um tipo de fluxo de dados (TCP ou UDP) e um valor referente à vazão
mínima e o atraso máximo. Os tráfegos gerados pelo software D-ITG (BOTTA
et al., 2012) para simular cada uma das aplicações devem ser gerados de
forma simultânea. O tamanho dos pacotes foi definido como sendo o
tamanho padrão de 512 bytes.

Tabela 11 -- Tipo de Protocolo, Tipo da Aplicação, Demandas de Vazão e
Atraso.

  ------------ -------------- ---------- ---------- ---------- ----------
   Protocolo   Aplicação      Origem     Destino    Vazão      Atraso
                                                    (Mbps)     (ms)

      TCP      Dados          0          49         0,256      \< 1000

      TCP      Dados          1          33         0,256      \< 1000

      UDP      Vídeo          2          51         1.744      \< 150

      UDP      Vídeo          3          50         1,256      \< 150

      TCP      Dados          4          37         0,256      \< 1000

      TCP      Dados          31         36         0,256      \< 1000

      TCP      Dados          32         46         0,256      \< 1000

      UDP      Voz            5          48         0,512      \< 150

      UDP      Voz            6          47         0,512      \< 150

      TCP      Dados          7          34         0,256      \< 1000

      UDP      Vídeo          8          44         1,256      \< 150

      UDP      Vídeo          9          43         1,256      \< 150

      UDP      Voz            11         41         0,512      \< 150

      TCP      Dados          10         42         0,256      \< 1000

      UDP      Voz            12         40         0,512      \< 150

      TCP      Dados          13         39         0,256      \< 1000

      TCP      Dados          30         45         0,256      \< 1000
  ------------ -------------- ---------- ---------- ---------- ----------

Os fluxos gerados foram selecionados como sendo do tipo: taxa constante
(pacotes/segundo), ou seja, os valores dos fluxos variam pouco em função
do tempo. Em função do valor da vazão mínima de cada aplicação,
calculou-se o valor da taxa constante (pacotes/segundo), considerando o
tamanho do pacote (512 bytes). Conforme Quadro 2 utilizou-se as
seguintes taxas constantes de injeção de fluxos.

Quadro 2 -- Taxas constantes de injeção em relação as vazões de
referência

  -----------------------------------------------------------------------
   Vazão em Mbps  Taxa constante de injeção         Tamanho do pacote
   (referência)   (pacotes/segundo)                 (Bytes)
  --------------- --------------------------------- ---------------------
        256       64                                512

        512       128                               512

       1256       314                               512

       1744       436                               512
  -----------------------------------------------------------------------

Na Figura 27 é mostrada a tela do Mininet mostrando 5 pequenas janelas
(do total de 17 em execução) dos hostes executando os comandos de fluxo
do D-ITG. Na janela maior de fundo branco tem-se os valores medidos
sendo apresentados como resultados calculados pelo D-ITG.

![](media/image24.png){width="7.072916666666667in"
height="4.9703379265091865in"}

Figura 27 -- Tela do Mininet mostrando hostes executando os comandos de
fluxo do D-ITG

### 5.4.3 Sflow-rt

### 

Por meio das aplicações do sFlow-RT pode-se visualizar os fluxos gerados
na rede SDN. Na Figura 28 é mostrada a tela do aplicativo Flow Trend que
apresenta o fluxo dos dados injetados na rede ao longo do tempo e seus
respectivos IPs de origem e destino. Nela é possível visualizar a
sobreposição dos fluxos de dados que foram executados de forma
simultânea na rede.

![](media/image25.png){width="9.269734251968504in"
height="6.20819116360455in"}

Figura 28 -- Tela do sFlow-RT (Flow Trend) mostrando vários fluxos
injetados na rede

Na Figura 29 é mostrada a tela do aplicativo Top Flows que representa os
maiores fluxos presentes na rede em termos de vazão.

![](media/image26.png){width="8.749971566054244in"
height="5.754180883639545in"}

Figura 29 -- Tela do sFlow-RT (Top Flows) mostrando vários fluxos
injetados na rede.

Na Figura 29 tem-se a representação dos fluxos na forma de gráfico de
barras, na seguinte ordem: iniciando dos maiores para os menores fluxos
de dados. Do lado esquerdo são mostrados o IP de origem e destino de
cada fluxo.

## 5.5 Considerações Finais

Neste capítulo realizou-se a implementação dos algoritmos para a
topologia escolhida e ao mesmo tempo foi feito alguns testes que
serviram para encontrar melhores valores de parâmetros. Além disso,
pôde-se avaliar o desempenho do algoritmo AG em relação ao algoritmo DE
em 16 cenários diferentes. Foi realizada também a implementação/emulação
da rede SDN utilizando o Mininet e o controlador Floodlight.

No próximo capítulo é realizada a análise dos resultados obtidos pelos
algoritmos de otimização e também os resultados obtidos pela
implementação da rede SDN.

# 6. RESULTADOS

São apresentados neste capítulo os resultados obtidos na análise de
desemepenho dos algoritmos de otimização propostos neste trabalho.
Inicialmente, na seção 6.1 é avaliado o desempenho entre os algoritmos
ACO+AG, ACO+DE e o algoritmo de Dijkstra.

Na seção 6.2 são apresentados os resultados da implementação utilizando
as soluções (rotas) obtidas pelo modelo ACO+AG ou ACO+DE na rede SDN, a
qual denominou-se rede otimizada. Esta rede otimizada é então comparada
com uma rede que utiliza o algoritmo de Dijkstra. Finalizando o capítulo
na seção 6.3 são realizadas algumas considerações finais.

## 6.1 Resultados Comparativos dos algoritmos

## 

Foram realizadas duas comparações de desempenho dos algoritmos de
otimização. A primeira foi uma simulação com limite de 200 iterações e a
segunda foi considerando o limite de tempo computacional de
aproximadamente 12 segundos para os algoritmos de otimização (ACO+AG e
ACO+DE) e o algoritmo de Dijkstra. Considerando os resultados obtidos,
foi selecionada a melhor solução e realizada a análise de atraso e de
vazão.

### 6.1.1 Resultados comparativo considerando limite de iterações

Em virtude dos algoritmos objetos desse estudo possuirem um
comportamento estatístico, se faz necessário realizar as execuções em um
maior número de vezes para se obter um conjunto de resultados médios que
sirvam de comparação. A Figura 30 mostra a evolução do valor médio da
função objetivo ou fitness médio dos algoritmos para um conjunto de 100
execuções.

![](media/image27.png){width="7.143513779527559in"
height="3.4935061242344707in"}

Figura 30 -- Comparativo de Desempenho entre ACO+AG, ACO+DE e Dijkstra
para 100 execuções com 200 iterações.

Conforme a Figura 30 os resultados de comparações de desempenho entre os
algoritmos, pode-se observar o melhor resultado do ACO+AG, sendo seguido
pelo ACO+DE e ambos superando o Dijkstra. O desempenho do algoritmo de
Dijkstra é constante pois o seu conjunto de rotas é fixo, ou seja, para
cada aplicação é calculada apenas uma única opção de rota que resulte no
caminho mais curto entre a origem e destino no grafo desta rede. A
Tabela 12 apresenta um resumo do desempenho dos algoritmos considerando
o valor médio, desvio-padrão e o valor máximo da função objetivo.

Tabela 12 -- Resultados comparativo de Desempenho entre ACO+AG, ACO+DE e
Dijkstra com 200 iterações.

  -----------------------------------------------------------------------
        Algoritmo       Valor Médio (DESVIO-PADRÃO)     Valor Máximo
  --------------------- ------------------------------- -----------------
         ACO+AG         126.7390 (4.4657)               132

         ACO+DE         123.7188 (4.9143)               129

        DIjkstrA        120 (0)                         120
  -----------------------------------------------------------------------

Conforme pode ser observado na Tabela 12, o algoritmo ACO+AG obteve um
valor do fitness médio 2,44% maior que o do ACO+DE e 5.62% maior que do
Dijkstra. O algoritmo ACO+DE obteve um resultado de 3,10% superior ao do
Dijkstra. Nessa simulação o ACO+AG conseguiu atingir uma solução ótima
com fitness (valor da função objetivo) igual a 132.

### 6.1.2 Resultados comparativo considerando limite de tempo computacional

O gráfico da Figura 31 ilustra a evolução do valor médio da função
objetivo ou fitness médio entre os algoritmos quando executados 100
vezes. Pode-se observar que o melhor resultado é obtido pelo ACO+AG,
sendo seguido pelo ACO+DE e pelo Dijkstra.

![](media/image28.png){width="7.159502405949256in"
height="3.493507217847769in"}

Figura 31 - Comparativo de Desempenho entre ACO+AG, ACO+DE e Dijkstra
para 100 execuções com tempo computacional de 12 segundos cada.

Assim como ocorre na comparação considerando o número de iterações igual
200, nessa segunda comparação considerando o tempo computacional para a
execução dos algoritmos, tem-se novamente o ACO+AG com um desempenho
levemente superior ao ACO+DE, sendo que ambos apresentam resultados
consideravelmente melhores que o Dijkstra. A Tabela 13 apresenta um
resumo do desempenho dos algoritmos considerando o valor médio,
desvio-padrão e o valor máximo.

Tabela 13 -- Resultados comparativo de Desempenho entre ACO+AG, ACO+DE e
Dijkstra com mesmo tempo computacional.

  ------------------------------------------------------------------------
       Algoritmo       Valor Médio (DESVIO-PADRÃO)       Valor Máximo
  -------------------- --------------------------------- -----------------
         ACO+AG        125.2196 (4.7538)                 132

         ACO+DE        124.1720 (4.4961)                 129

        DiJkstrA       120 (0)                           120
  ------------------------------------------------------------------------

Conforme pode ser observado na Tabela 13, assim como na simulação
considerando limite de 200 iterações, o algoritmo ACO+AG obteve um
melhor valor de fitness médio. Nesta simulação o ACO+AG obteve um valor
de 0,84% superior ao do ACO+DE e 4,35% superior ao do Dijkstra. Além
disso o algoritmo ACO+DE obteve um resultado de 3,48% superior ao
Dijkstra.

Nessa segunda simulação o ACO+AG também conseguiu uma solução ótima com
fitness igual a 132. No entanto é importante ressaltar que quando são
executadas as simulações utilizando o modelo ACO+DE com um maior número
de iteração, uma solução ótima também é alcançada por esse modelo. Assim
é possível afirmar que para a topologia adotada considerando um conjunto
de 17 aplicações e suas respectivas restrições, os modelos ACO+DE e
ACO+AG foram capazes de convergir para uma solução ótima (FO = 132),
isto é, conseguem obter uma solução que atenda todos as conexões e os
requisitos de vazão, atraso e prioridade de tráfego.

### 6.1.3 Resultados previstos do atraso e vazão considerando as rotas selecionadas 

Com o resultado do fitness alcançando uma solução ótima (FO = 132)
pode-se concluir que as rotas criadas pelo ACO e selecionadas pelos
algoritmos de otimização obedecem às demandas e restrições da rede. Isto
significa que a aplicação da TE permite que os requisitos de QoS sejam
atendidos.

#### 

#### 6.1.3.1 Análise do atraso fim-a-fim previsto

No Quadro 3 é apresentado o conjunto de rotas (caminhos) encontradas
pelos algoritmos ACO+AG como melhor solução (ótima) obtida para a
topologia adotada e o atraso fim-a-fim previsto para a cada uma destas
rotas. Conforme é possível verificar, os valores de atraso ficam dentro
da faixa de atraso máximo permitido. O cálculo do atraso previsto é
realizado pela soma dos atrasos associados a cada mudança de nó (vide
Tabela 2). Por exemplo o atraso previsto para a rota 5 é calculado pelo
atraso associado a comunicação entre os enlaces 4, 17, 18, 26, 27, 28,
23, 22, 21 e 37 nesta ordem. Para esta rota utilizando a Tabela 2 tem-se
a seguinte soma de atrasos: 1 + 10 + 10 + 10 + 80 + 20 + 20 + 20 + 1 =
172 milissegundos (ms). Observe que enlaces de 4-17 e 21-37 possuem
atraso igual a 1 ms e não constam na tabela devido a serem enlaces
periféricos da rede, no entanto, todos os enlaces do núcleo da rede
constam na Tabela 2.

Quadro 3 -- Rotas encontradas pelos algoritmos ACO+AG

+----+---------------------------------------------------------------------------------------------------------------------------------+---------+----------+--------+
| N° | Rotas Selecionadas (Nós)                                                                                                        | Qtd     | Atraso   | Atraso |
|    |                                                                                                                                 | Enlaces | Previsto | Máx    |
|    |                                                                                                                                 |         | (ms)     | (ms)   |
+:==:+============+============+============+============+============+============+============+============+============+============+=========+==========+========+
| 1  | 52         | 17         | 18         | 26         | 27         | 49         | \-         | \-         | \-         | \-         | 6       | 32       | 1000   |
+----+------------+------------+------------+------------+------------+------------+------------+------------+------------+------------+---------+----------+--------+
| 2  | 1          | 17         | 25         | 27         | 26         | 33         | \-         | \-         | \-         | \-         | 6       | 32       | 1000   |
+----+------------+------------+------------+------------+------------+------------+------------+------------+------------+------------+---------+----------+--------+
| 3  | 2          | 17         | 25         | 24         | 28         | 51         | \-         | \-         | \-         | \-         | 6       | 52       | 150    |
+----+------------+------------+------------+------------+------------+------------+------------+------------+------------+------------+---------+----------+--------+
| 4  | 3          | 17         | 16         | 20         | 19         | 23         | 24         | 27         | 50         | \-         | 9       | 122      | 150    |
+----+------------+------------+------------+------------+------------+------------+------------+------------+------------+------------+---------+----------+--------+
| 5  | 4          | 17         | 18         | 26         | 27         | 28         | 23         | 22         | 21         | 37         | 10      | 172      | 1000   |
+----+------------+------------+------------+------------+------------+------------+------------+------------+------------+------------+---------+----------+--------+
| 6  | 31         | 18         | 26         | 27         | 24         | 23         | 22         | 21         | 36         | \-         | 9       | 102      | 1000   |
+----+------------+------------+------------+------------+------------+------------+------------+------------+------------+------------+---------+----------+--------+
| 7  | 32         | 18         | 17         | 19         | 23         | 28         | 46         | \-         | \-         | \-         | 7       | 82       | 1000   |
+----+------------+------------+------------+------------+------------+------------+------------+------------+------------+------------+---------+----------+--------+
| 8  | 5          | 17         | 18         | 26         | 27         | 48         | \-         | \-         | \-         | \-         | 6       | 32       | 1000   |
+----+------------+------------+------------+------------+------------+------------+------------+------------+------------+------------+---------+----------+--------+
| 9  | 6          | 17         | 19         | 23         | 24         | 27         | 47         | \-         | \-         | \-         | 7       | 92       | 150    |
+----+------------+------------+------------+------------+------------+------------+------------+------------+------------+------------+---------+----------+--------+
| 10 | 7          | 14         | 20         | 19         | 17         | 18         | 26         | 34         | \-         | \-         | 8       | 102      | 1000   |
+----+------------+------------+------------+------------+------------+------------+------------+------------+------------+------------+---------+----------+--------+
| 11 | 8          | 14         | 20         | 22         | 44         | \-         | \-         | \-         | \-         | \-         | 5       | 42       | 150    |
+----+------------+------------+------------+------------+------------+------------+------------+------------+------------+------------+---------+----------+--------+
| 12 | 9          | 14         | 15         | 21         | 22         | 29         | 43         | \-         | \-         | \-         | 7       | 82       | 150    |
+----+------------+------------+------------+------------+------------+------------+------------+------------+------------+------------+---------+----------+--------+
| 13 | 11         | 14         | 16         | 20         | 23         | 29         | 41         | \-         | \-         | \-         | 7       | 72       | 150    |
+----+------------+------------+------------+------------+------------+------------+------------+------------+------------+------------+---------+----------+--------+
| 14 | 10         | 14         | 20         | 23         | 22         | 29         | 42         | \-         | \-         | \-         | 7       | 72       | 1000   |
+----+------------+------------+------------+------------+------------+------------+------------+------------+------------+------------+---------+----------+--------+
| 15 | 12         | 14         | 15         | 21         | 20         | 23         | 29         | 40         | \-         | \-         | 8       | 102      | 1000   |
+----+------------+------------+------------+------------+------------+------------+------------+------------+------------+------------+---------+----------+--------+
| 16 | 13         | 14         | 20         | 21         | 22         | 39         | \-         | \-         | \-         | \-         | 6       | 72       | 150    |
+----+------------+------------+------------+------------+------------+------------+------------+------------+------------+------------+---------+----------+--------+
| 17 | 30         | 15         | 21         | 20         | 19         | 24         | 28         | 45         | \-         | \-         | 8       | 92       | 150    |
+----+------------+------------+------------+------------+------------+------------+------------+------------+------------+------------+---------+----------+--------+

No Quadro 4 tem-se o conjunto de rotas calculadas utilizando o algoritmo
de Dijkstra e o atraso associado a cada uma delas. É possível verificar
que o valores de atraso foram menores que a solução anterior, isso
deve-se ao fato que o algoritmo de Dijkstra obtêm as rotas mais curtas
entre dois nós e consequentemente o atraso-fim-a-fim entre os enlaces
(links) também é menor.

Quadro 4 -- Rotas encontradas pelo algoritmo Dijkstra

+----+-----------------------------------------------------------------------------------+---------+----------+--------+
| N° | Rotas Selecionadas (Nós)                                                          | Qtd     | Atraso   | Atraso |
|    |                                                                                   | Enlaces | Previsto | Máx    |
|    |                                                                                   |         | (ms)     | (ms)   |
+:==:+===========+===========+===========+===========+===========+===========+===========+=========+==========+========+
| 1  | 52        | 17        | 25        | 27        | 49        | \-        | \-        | 5       | 22       | 1000   |
+----+-----------+-----------+-----------+-----------+-----------+-----------+-----------+---------+----------+--------+
| 2  | 1         | 17        | 18        | 26        | 33        | \-        | \-        | 5       | 22       | 1000   |
+----+-----------+-----------+-----------+-----------+-----------+-----------+-----------+---------+----------+--------+
| 3  | 2         | 17        | 25        | 24        | 28        | 51        | \-        | 6       | 52       | 150    |
+----+-----------+-----------+-----------+-----------+-----------+-----------+-----------+---------+----------+--------+
| 4  | 3         | 17        | 25        | 27        | 50        | \-        | \-        | 5       | 22       | 150    |
+----+-----------+-----------+-----------+-----------+-----------+-----------+-----------+---------+----------+--------+
| 5  | 4         | 17        | 19        | 20        | 21        | 37        | \-        | 6       | 72       | 1000   |
+----+-----------+-----------+-----------+-----------+-----------+-----------+-----------+---------+----------+--------+
| 6  | 31        | 18        | 17        | 19        | 20        | 21        | 36        | 7       | 82       | 1000   |
+----+-----------+-----------+-----------+-----------+-----------+-----------+-----------+---------+----------+--------+
| 7  | 32        | 18        | 26        | 27        | 28        | 46        | \-        | 6       | 102      | 1000   |
+----+-----------+-----------+-----------+-----------+-----------+-----------+-----------+---------+----------+--------+
| 8  | 5         | 17        | 25        | 27        | 48        | \-        | \-        | 5       | 22       | 1000   |
+----+-----------+-----------+-----------+-----------+-----------+-----------+-----------+---------+----------+--------+
| 9  | 6         | 17        | 25        | 27        | 47        | \-        | \-        | 5       | 22       | 150    |
+----+-----------+-----------+-----------+-----------+-----------+-----------+-----------+---------+----------+--------+
| 10 | 7         | 14        | 20        | 19        | 25        | 26        | 34        | 7       | 122      | 1000   |
+----+-----------+-----------+-----------+-----------+-----------+-----------+-----------+---------+----------+--------+
| 11 | 8         | 14        | 15        | 21        | 22        | 44        | \-        | 6       | 72       | 150    |
+----+-----------+-----------+-----------+-----------+-----------+-----------+-----------+---------+----------+--------+
| 12 | 9         | 14        | 15        | 21        | 22        | 29        | 43        | 7       | 82       | 150    |
+----+-----------+-----------+-----------+-----------+-----------+-----------+-----------+---------+----------+--------+
| 13 | 11        | 14        | 15        | 21        | 22        | 29        | 41        | 7       | 82       | 150    |
+----+-----------+-----------+-----------+-----------+-----------+-----------+-----------+---------+----------+--------+
| 14 | 10        | 14        | 15        | 21        | 22        | 29        | 42        | 7       | 82       | 1000   |
+----+-----------+-----------+-----------+-----------+-----------+-----------+-----------+---------+----------+--------+
| 15 | 12        | 14        | 15        | 21        | 22        | 29        | 40        | 7       | 82       | 1000   |
+----+-----------+-----------+-----------+-----------+-----------+-----------+-----------+---------+----------+--------+
| 16 | 13        | 14        | 15        | 21        | 22        | 39        | \-        | 6       | 72       | 150    |
+----+-----------+-----------+-----------+-----------+-----------+-----------+-----------+---------+----------+--------+
| 17 | 30        | 15        | 21        | 22        | 23        | 28        | 45        | 7       | 82       | 150    |
+----+-----------+-----------+-----------+-----------+-----------+-----------+-----------+---------+----------+--------+

#### 6.1.3.2 Análise da vazão prevista

No Quadro 5 é apresentada a relação de todos os enlaces internos (não
periféricos) da rede e suas respectivas capacidades máximas de largura
de banda, bem como a utilização dos enlaces da rede pelos algoritmos
ACO+AG e Dijkstra. É possível perceber que a utilização dos enlaces por
parte do ACO+AG é distribuída de forma mais homogênea e balanceada, não
tendo nenhum enlace com capacidade máxima de largura de banda
ultrapassada e com apenas dois enlaces não sendo utilizados (19-25 e
25-26). No entanto a solução obtida utilizando o algoritmo de Dijkstra
ultrapassa a capacidade máxima de largura de banda em 6 enlaces (14-15,
15-21, 17-25, 21-22, 22-29 e 25-27) e não utiliza nenhuma conexão em um
total de 10 enlaces (14-16, 16-17, 16-20, 19-23, 19-24, 20-22, 20-23,
23-24, 23-29 e 24-27.). Importante considerar que os algoritmos de
otimização realizam um bom balanceamento de carga nos enlaces da rede.

Quadro 5 -- Largura de Banda utilizada nos enlaces (Mbps)

+----+---------+---------+------------------------------------------+------------------------------------------+
| N° | enlaces | Largura | Solução utilizando ACO + AG              | Solução utilizando Dijkstra              |
|    |         | banda   |                                          |                                          |
|    |         | Max     |                                          |                                          |
|    |         |         +-----------+-----------+------------------+-----------+-----------+------------------+
|    |         |         | N°        | Vazão     | Vazão/L.Banda(%) | N°        | Vazão     | Vazão/L.Banda(%) |
|    |         |         | Conexões  | Utilizada |                  | Conexões  | Utilizada |                  |
+:==:+=========+=========+===========+===========+==================+===========+===========+==================+
| 1  | 14-15   | 2       | 2         | 1,712     | 86%              | 6         | 3,936     | 197%             |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+
| 2  | 14-16   | 2       | 1         | 0,512     | 26%              | 0         | 0         | 0%               |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+
| 3  | 14-20   | 2       | 4         | 1,968     | 98%              | 1         | 0,256     | 13%              |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+
| 4  | 15-21   | 2       | 3         | 1,968     | 98%              | 7         | 4,192     | 210%             |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+
| 5  | 16-17   | 2       | 1         | 1,2       | 60%              | 0         | 0         | 0%               |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+
| 6  | 16-20   | 2       | 2         | 1,712     | 86%              | 0         | 0         | 0%               |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+
| 7  | 17-18   | 2       | 5         | 1,536     | 77%              | 2         | 0,512     | 26%              |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+
| 8  | 17-19   | 2       | 3         | 1,024     | 51%              | 2         | 0,512     | 26%              |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+
| 9  | 17-25   | 2       | 2         | 2         | 100%             | 5         | 4,224     | 211%             |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+
| 10 | 18-26   | 2       | 5         | 1,536     | 77%              | 2         | 0,512     | 26%              |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+
| 11 | 19-20   | 2       | 3         | 1,712     | 86%              | 3         | 0,768     | 38%              |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+
| 12 | 19-23   | 2       | 3         | 1,968     | 98%              | 0         | 0         | 0%               |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+
| 13 | 19-24   | 2       | 1         | 0,256     | 13%              | 0         | 0         | 0%               |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+
| 14 | 19-25   | 2       | 0         | 0         | 0%               | 1         | 0,256     | 13%              |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+
| 15 | 20-21   | 2       | 3         | 1,024     | 51%              | 2         | 0,512     | 26%              |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+
| 16 | 20-22   | 2       | 1         | 1,2       | 60%              | 0         | 0         | 0%               |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+
| 17 | 20-23   | 2       | 3         | 1,28      | 64%              | 0         | 0         | 0%               |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+
| 18 | 21-22   | 2       | 4         | 1,968     | 98%              | 7         | 4,192     | 210%             |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+
| 19 | 22-23   | 2       | 3         | 0,768     | 38%              | 1         | 0,256     | 13%              |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+
| 20 | 22-29   | 2       | 2         | 1,456     | 73%              | 4         | 2,48      | 124%             |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+
| 21 | 23-24   | 2       | 3         | 1,968     | 98%              | 0         | 0         | 0%               |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+
| 22 | 23-28   | 2       | 2         | 0,512     | 26%              | 1         | 0,256     | 13%              |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+
| 23 | 23-29   | 2       | 2         | 1,024     | 51%              | 0         | 0         | 0%               |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+
| 24 | 24-25   | 2       | 1         | 1,744     | 87%              | 1         | 1,744     | 87%              |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+
| 25 | 24-27   | 2       | 3         | 1,968     | 98%              | 0         | 0         | 0%               |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+
| 26 | 24-28   | 2       | 2         | 2         | 100%             | 1         | 1,744     | 87%              |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+
| 27 | 25-26   | 2       | 0         | 0         | 0%               | 1         | 0,256     | 13%              |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+
| 28 | 25-27   | 2       | 1         | 0,256     | 13%              | 4         | 2,48      | 124%             |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+
| 29 | 26-27   | 2       | 5         | 1,536     | 77%              | 1         | 0,256     | 13%              |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+
| 30 | 27-28   | 2       | 1         | 0,256     | 13%              | 1         | 0,256     | 13%              |
+----+---------+---------+-----------+-----------+------------------+-----------+-----------+------------------+

## 

## 6.2 Resultados da Otimização Implementados na Rede SDN

## 

Após realização da avaliação das soluções obtidas pelos algoritmos de
otimização, torna-se necessário realizar a implementação e testes numa
rede SDN.

Denominou-se rede otimizada a rede SDN que utiliza uma solução de rotas
calculadas pelo algoritmo ACO+AG. O desempenho desta rede foi então
comparado com a obtida por outra rede que utiliza uma solução de rotas
calculada pelo algoritmo de Dijkstra.

Os testes de emulação da Redes SDN foram realizados utilizando o D-ITG
para fazer a injeção simultânea do tráfego das 17 aplicações nas redes.
Então é realizada a análise dos relatórios das medições produzidas pelo
D-ITG em termos dos critérios de QoS. Devido ao grande número de
injeções de tráfegos necessários a cada teste a ser emulado, optou-se
pela realização de apenas 5 testes para cada rede.

### 6.2.1 Resultados comparativos entre a rede otimizada e a rede usando Dijkstra.

O gráfico da Figura 32 apresenta os resultados médios de desempenho das
17 aplicações em 5 testes realizados para cada uma das redes (rede
otimizada e rede usando Dijkstra), sendo possível verificar o desempenho
destas redes em termos de vazão, atraso fim-a-fim, jitter e perda de
pacotes.

![](media/image29.png){width="7.029183070866142in" height="4.6875in"}

Figura 32 -- Resultado médio dos cinco testes realizados para a Rede
Otimizada (ACO+AG e ACO+DE) e a Rede usando Dijkstra.

Os dados presentes na Figura 32 mostram que: os seguintes resultados:

\- A vazão média obtida na rede otimizada é superior (acima de 500 kbps)
à rede usando Dijkstra (abaixo de 400 kbps) para todos os cinco testes.

\- O atraso fim-a-fim médio é inferior (próximo de 0 segundo) na rede
otimizada em relação a rede usando Dijkstra (próximo de 10 segundos)
para todos os cinco testes.

\- O jitter médio também é inferior (próximo de 0,01 segundo) na rede
otimizada em relação a rede usando Dijkstra (próximo ou acima de 0,06
segundos) para todos os cinco testes.

\- A média de perda de pacotes é inferior (próximo de 0 %) na rede
otimizada em relação a rede usando Dijkstra (próximo de 8 %) para todos
os cinco testes.

Na Tabela 14 é apresentado os resultados médios gerais comparando a rede
otimizada e a rede usando Dijkstra. Por esta Tabela possível verificar
que a vazão média da rede otimizada é 34% (trinta e quatro por cento)
maior que a rede usando Dijkstra. O valor do atraso fim-a-fim médio da
rede otimizada é em torno de 51 vezes inferior ao da rede usando
Dijkstra. O valor do jitter médio da rede otimizada é em torno de 7,5
vezes inferior ao da rede usando Dijkstra e por fim o valor médio da
perda de pacotes da rede otimizada é em torno de 510 vezes inferior ao
da rede usando Dijkstra.

Tabela 14 -- Resultado médio geral comparando a rede otimizada (ACO+AG)
e a rede usando Dijkstra.

  -----------------------------------------------------------------------
           DADOs          Otimizada               Dijkstra
  ----------------------- ----------------------- -----------------------
   Vazão Média (Kbit/s)   517.3307                384.7603

     Atraso Médio (s)     0.2109                  10.7962

     Jitter Médio (s)     0.0093                  0.0697

   Percentual de Pacotes  0.0168                  8.5747
       Perdidos (%)                               
  -----------------------------------------------------------------------

No Quadro 6 é apresentado a relação dos resultados de vazão e perda de
pacotes entre as redes comparadas para cada uma das 17 aplicações
injetadas nestas. Neste quadro tem-se também o valor de referência da
vazão desejável para aquela aplicação, bem como o tipo da aplicação,
origem e destino.

Pelos dados presentes no Quadro 6 é possível verificar que algumas das
aplicações (2, 3, 5, 6, 7 e 10) da rede otimizada apresentam desempenho
inferior, em termos de vazão, as da rede usando Dijkstra. No entanto
essa diferença é pequena em termos percentuais (0.97%) quando comparada
com o restante das aplicações (1, 4, 8, 9, 11, 12, 13, 14, 15, 16 e 17)
nas quais a diferença da vazão é considerável. Os valores de vazão das
aplicações das duas redes foram inferiores aos valores de referência de
vazões desejáveis para aquelas aplicações, possivelmente isso se deve ao
alto nível de tráfego ocupando a rede simultaneamente.

Quadro 6 -- Resultados da vazão e perda de pacotes entre a rede
otimizada (ACO+AG) e a rede usando Dijkstra em cada aplicação.

<table style="width:100%;">
<colgroup>
<col style="width: 4%" />
<col style="width: 7%" />
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 10%" />
<col style="width: 12%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;">N°</th>
<th style="text-align: center;">Figura</th>
<th style="text-align: center;">Aplicação</th>
<th style="text-align: center;">Origem</th>
<th style="text-align: center;">Destino</th>
<th style="text-align: center;"><p>Vazão</p>
<p>(referência)</p></th>
<th style="text-align: center;">Vazão (Otimizada)</th>
<th style="text-align: center;">Vazão (Dijkstra)</th>
<th style="text-align: center;">Perda de Pacotes(%) (Otimizada)</th>
<th style="text-align: center;">Perda de Pacotes(%) (Dijkstra)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">33</td>
<td style="text-align: center;">Dados</td>
<td style="text-align: center;">0</td>
<td style="text-align: center;">49</td>
<td style="text-align: center;">256</td>
<td style="text-align: center;">250,31</td>
<td style="text-align: center;">222,56</td>
<td style="text-align: center;">0,0000</td>
<td style="text-align: center;">0,00</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">34</td>
<td style="text-align: center;">Dados</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">33</td>
<td style="text-align: center;">256</td>
<td style="text-align: center;">250,37</td>
<td style="text-align: center;">251,86</td>
<td style="text-align: center;">0,0000</td>
<td style="text-align: center;">0,00</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">35</td>
<td style="text-align: center;">Vídeo</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">51</td>
<td style="text-align: center;">1744</td>
<td style="text-align: center;">1405,01</td>
<td style="text-align: center;">1440,20</td>
<td style="text-align: center;">0,0000</td>
<td style="text-align: center;">0,00</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">36</td>
<td style="text-align: center;">Vídeo</td>
<td style="text-align: center;">3</td>
<td style="text-align: center;">50</td>
<td style="text-align: center;">1256</td>
<td style="text-align: center;">1072,53</td>
<td style="text-align: center;">822,81</td>
<td style="text-align: center;">0,0000</td>
<td style="text-align: center;">0,00</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">37</td>
<td style="text-align: center;">Dados</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">37</td>
<td style="text-align: center;">256</td>
<td style="text-align: center;">250,33</td>
<td style="text-align: center;">251,77</td>
<td style="text-align: center;">0,0000</td>
<td style="text-align: center;">0,00</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;">38</td>
<td style="text-align: center;">Dados</td>
<td style="text-align: center;">31</td>
<td style="text-align: center;">36</td>
<td style="text-align: center;">256</td>
<td style="text-align: center;">250,25</td>
<td style="text-align: center;">251,87</td>
<td style="text-align: center;">0,0000</td>
<td style="text-align: center;">0,00</td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td style="text-align: center;">39</td>
<td style="text-align: center;">Dados</td>
<td style="text-align: center;">32</td>
<td style="text-align: center;">46</td>
<td style="text-align: center;">256</td>
<td style="text-align: center;">250,18</td>
<td style="text-align: center;">251,83</td>
<td style="text-align: center;">0,0000</td>
<td style="text-align: center;">0,00</td>
</tr>
<tr>
<td style="text-align: center;">8</td>
<td style="text-align: center;">40</td>
<td style="text-align: center;">Voz</td>
<td style="text-align: center;">5</td>
<td style="text-align: center;">48</td>
<td style="text-align: center;">512</td>
<td style="text-align: center;">482,21</td>
<td style="text-align: center;">465,14</td>
<td style="text-align: center;">0,0000</td>
<td style="text-align: center;">3,38</td>
</tr>
<tr>
<td style="text-align: center;">9</td>
<td style="text-align: center;">41</td>
<td style="text-align: center;">Voz</td>
<td style="text-align: center;">6</td>
<td style="text-align: center;">47</td>
<td style="text-align: center;">512</td>
<td style="text-align: center;">482,73</td>
<td style="text-align: center;">401,26</td>
<td style="text-align: center;">0,0000</td>
<td style="text-align: center;">0,00</td>
</tr>
<tr>
<td style="text-align: center;">10</td>
<td style="text-align: center;">42</td>
<td style="text-align: center;">Dados</td>
<td style="text-align: center;">7</td>
<td style="text-align: center;">34</td>
<td style="text-align: center;">256</td>
<td style="text-align: center;">249,85</td>
<td style="text-align: center;">251,88</td>
<td style="text-align: center;">0,1054</td>
<td style="text-align: center;">0,00</td>
</tr>
<tr>
<td style="text-align: center;">11</td>
<td style="text-align: center;">43</td>
<td style="text-align: center;">Vídeo</td>
<td style="text-align: center;">8</td>
<td style="text-align: center;">44</td>
<td style="text-align: center;">1256</td>
<td style="text-align: center;">1066,53</td>
<td style="text-align: center;">688,52</td>
<td style="text-align: center;">0,0865</td>
<td style="text-align: center;">36,63</td>
</tr>
<tr>
<td style="text-align: center;">12</td>
<td style="text-align: center;">44</td>
<td style="text-align: center;">Vídeo</td>
<td style="text-align: center;">9</td>
<td style="text-align: center;">43</td>
<td style="text-align: center;">1256</td>
<td style="text-align: center;">1070,25</td>
<td style="text-align: center;">707,21</td>
<td style="text-align: center;">0,0000</td>
<td style="text-align: center;">34,44</td>
</tr>
<tr>
<td style="text-align: center;">13</td>
<td style="text-align: center;">45</td>
<td style="text-align: center;">Voz</td>
<td style="text-align: center;">11</td>
<td style="text-align: center;">41</td>
<td style="text-align: center;">512</td>
<td style="text-align: center;">482,45</td>
<td style="text-align: center;">306,19</td>
<td style="text-align: center;">0,0000</td>
<td style="text-align: center;">36,26</td>
</tr>
<tr>
<td style="text-align: center;">14</td>
<td style="text-align: center;">46</td>
<td style="text-align: center;">Dados</td>
<td style="text-align: center;">10</td>
<td style="text-align: center;">42</td>
<td style="text-align: center;">256</td>
<td style="text-align: center;">249,66</td>
<td style="text-align: center;">10,71</td>
<td style="text-align: center;">0,0000</td>
<td style="text-align: center;">0,07</td>
</tr>
<tr>
<td style="text-align: center;">15</td>
<td style="text-align: center;">47</td>
<td style="text-align: center;">Voz</td>
<td style="text-align: center;">12</td>
<td style="text-align: center;">40</td>
<td style="text-align: center;">512</td>
<td style="text-align: center;">482,15</td>
<td style="text-align: center;">21,31</td>
<td style="text-align: center;">0,0000</td>
<td style="text-align: center;">0,00</td>
</tr>
<tr>
<td style="text-align: center;">16</td>
<td style="text-align: center;">48</td>
<td style="text-align: center;">Dados</td>
<td style="text-align: center;">13</td>
<td style="text-align: center;">39</td>
<td style="text-align: center;">256</td>
<td style="text-align: center;">249,55</td>
<td style="text-align: center;">161,43</td>
<td style="text-align: center;">0,0935</td>
<td style="text-align: center;">34,97</td>
</tr>
<tr>
<td style="text-align: center;">17</td>
<td style="text-align: center;">49</td>
<td style="text-align: center;">Dados</td>
<td style="text-align: center;">30</td>
<td style="text-align: center;">45</td>
<td style="text-align: center;">256</td>
<td style="text-align: center;">250,28</td>
<td style="text-align: center;">34,38</td>
<td style="text-align: center;">0,0000</td>
<td style="text-align: center;">0,02</td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td></td>
<td></td>
<td></td>
<td style="text-align: center;">Média</td>
<td style="text-align: center;">580,2353</td>
<td style="text-align: center;">517,3307</td>
<td style="text-align: center;">384,7603</td>
<td style="text-align: center;">0,0168</td>
<td style="text-align: center;">8,5747</td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td></td>
<td></td>
<td></td>
<td style="text-align: center;">Desvio-Padrão</td>
<td style="text-align: center;">465,8391</td>
<td style="text-align: center;">371,8967</td>
<td style="text-align: center;">349,3084</td>
<td style="text-align: center;">0,0364</td>
<td style="text-align: center;">15,0033</td>
</tr>
</tbody>
</table>

Ainda em relação ao Quadro 6 é possível verificar que em termos de
perdas de pacotes a rede otimizada tem um desempenho superior ao da rede
usando Dijkstra, sendo superior em 16 das 17 aplicações. Somente na
aplicação (10) que possui uma pequena perda de pacotes de 0.1%.

Da mesma forma como no Quadro 6, no Quadro 7 é apresentado a relação dos
resultados de atraso fim-a-fim e jitter entre as redes para cada uma das
17 aplicações. Assim como no quadro anterior tem-se neste quadro o valor
de referência atraso fim-a-fim desejável para aquela aplicação, além do
tipo da aplicação, origem, destino e o número da Figura referente a essa
aplicação, o qual pode ser visualizada no apêndice.

Quadro 7 -- Resultados do atraso fim-a-fim e jitter entre a rede
otimizada (ACO+AG) e a rede usando Dijkstra em cada aplicação.

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;">N°</th>
<th style="text-align: center;">Figura</th>
<th style="text-align: center;">Aplicação</th>
<th style="text-align: center;">Origem</th>
<th style="text-align: center;">Destino</th>
<th style="text-align: center;"><p>Atraso fim-a-fim (s)</p>
<p>(referência)</p></th>
<th style="text-align: center;">Atraso fim-a-fim (s) (Otimizada)</th>
<th style="text-align: center;">Atraso fim-a-fim (s) (Dijkstra)</th>
<th style="text-align: center;">Jitter (s) (Otimizada)</th>
<th style="text-align: center;">Jitter (s) (Dijkstra)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">33</td>
<td style="text-align: center;">Dados</td>
<td style="text-align: center;">0</td>
<td style="text-align: center;">49</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0,0539</td>
<td style="text-align: center;">5,4526</td>
<td style="text-align: center;">0,0154</td>
<td style="text-align: center;">0,0292</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">34</td>
<td style="text-align: center;">Dados</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">33</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0,0537</td>
<td style="text-align: center;">0,0427</td>
<td style="text-align: center;">0,0154</td>
<td style="text-align: center;">0,0167</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">35</td>
<td style="text-align: center;">Vídeo</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">51</td>
<td style="text-align: center;">0,150</td>
<td style="text-align: center;">0,0546</td>
<td style="text-align: center;">0,0644</td>
<td style="text-align: center;">0,0012</td>
<td style="text-align: center;">0,0012</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">36</td>
<td style="text-align: center;">Vídeo</td>
<td style="text-align: center;">3</td>
<td style="text-align: center;">50</td>
<td style="text-align: center;">0,150</td>
<td style="text-align: center;">0,1354</td>
<td style="text-align: center;">7,1648</td>
<td style="text-align: center;">0,0049</td>
<td style="text-align: center;">0,0085</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">37</td>
<td style="text-align: center;">Dados</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">37</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0,2057</td>
<td style="text-align: center;">0,1021</td>
<td style="text-align: center;">0,0205</td>
<td style="text-align: center;">0,0196</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;">38</td>
<td style="text-align: center;">Dados</td>
<td style="text-align: center;">31</td>
<td style="text-align: center;">36</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0,1354</td>
<td style="text-align: center;">0,1544</td>
<td style="text-align: center;">0,0209</td>
<td style="text-align: center;">0,0204</td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td style="text-align: center;">39</td>
<td style="text-align: center;">Dados</td>
<td style="text-align: center;">32</td>
<td style="text-align: center;">46</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0,0881</td>
<td style="text-align: center;">0,1040</td>
<td style="text-align: center;">0,0031</td>
<td style="text-align: center;">0,0017</td>
</tr>
<tr>
<td style="text-align: center;">8</td>
<td style="text-align: center;">40</td>
<td style="text-align: center;">Voz</td>
<td style="text-align: center;">5</td>
<td style="text-align: center;">48</td>
<td style="text-align: center;">0,150</td>
<td style="text-align: center;">0,0345</td>
<td style="text-align: center;">3,5509</td>
<td style="text-align: center;">0,0019</td>
<td style="text-align: center;">0,0049</td>
</tr>
<tr>
<td style="text-align: center;">9</td>
<td style="text-align: center;">41</td>
<td style="text-align: center;">Voz</td>
<td style="text-align: center;">6</td>
<td style="text-align: center;">47</td>
<td style="text-align: center;">0,150</td>
<td style="text-align: center;">0,1128</td>
<td style="text-align: center;">5,7557</td>
<td style="text-align: center;">0,0107</td>
<td style="text-align: center;">0,0164</td>
</tr>
<tr>
<td style="text-align: center;">10</td>
<td style="text-align: center;">42</td>
<td style="text-align: center;">Dados</td>
<td style="text-align: center;">7</td>
<td style="text-align: center;">34</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0,5306</td>
<td style="text-align: center;">0,1244</td>
<td style="text-align: center;">0,0038</td>
<td style="text-align: center;">0,0019</td>
</tr>
<tr>
<td style="text-align: center;">11</td>
<td style="text-align: center;">43</td>
<td style="text-align: center;">Vídeo</td>
<td style="text-align: center;">8</td>
<td style="text-align: center;">44</td>
<td style="text-align: center;">0,150</td>
<td style="text-align: center;">0,4724</td>
<td style="text-align: center;">4,4476</td>
<td style="text-align: center;">0,0021</td>
<td style="text-align: center;">0,0017</td>
</tr>
<tr>
<td style="text-align: center;">12</td>
<td style="text-align: center;">44</td>
<td style="text-align: center;">Vídeo</td>
<td style="text-align: center;">9</td>
<td style="text-align: center;">43</td>
<td style="text-align: center;">0,150</td>
<td style="text-align: center;">0,1534</td>
<td style="text-align: center;">4,4079</td>
<td style="text-align: center;">0,0023</td>
<td style="text-align: center;">0,0018</td>
</tr>
<tr>
<td style="text-align: center;">13</td>
<td style="text-align: center;">45</td>
<td style="text-align: center;">Voz</td>
<td style="text-align: center;">11</td>
<td style="text-align: center;">41</td>
<td style="text-align: center;">0,150</td>
<td style="text-align: center;">0,0747</td>
<td style="text-align: center;">4,3821</td>
<td style="text-align: center;">0,0019</td>
<td style="text-align: center;">0,0024</td>
</tr>
<tr>
<td style="text-align: center;">14</td>
<td style="text-align: center;">46</td>
<td style="text-align: center;">Dados</td>
<td style="text-align: center;">10</td>
<td style="text-align: center;">42</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0,6078</td>
<td style="text-align: center;">61,7454</td>
<td style="text-align: center;">0,0206</td>
<td style="text-align: center;">0,6113</td>
</tr>
<tr>
<td style="text-align: center;">15</td>
<td style="text-align: center;">47</td>
<td style="text-align: center;">Voz</td>
<td style="text-align: center;">12</td>
<td style="text-align: center;">40</td>
<td style="text-align: center;">0,150</td>
<td style="text-align: center;">0,1876</td>
<td style="text-align: center;">49,9390</td>
<td style="text-align: center;">0,0107</td>
<td style="text-align: center;">0,2819</td>
</tr>
<tr>
<td style="text-align: center;">16</td>
<td style="text-align: center;">48</td>
<td style="text-align: center;">Dados</td>
<td style="text-align: center;">13</td>
<td style="text-align: center;">39</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0,4927</td>
<td style="text-align: center;">4,2379</td>
<td style="text-align: center;">0,0032</td>
<td style="text-align: center;">0,0027</td>
</tr>
<tr>
<td style="text-align: center;">17</td>
<td style="text-align: center;">49</td>
<td style="text-align: center;">Dados</td>
<td style="text-align: center;">30</td>
<td style="text-align: center;">45</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0,1911</td>
<td style="text-align: center;">31,8598</td>
<td style="text-align: center;">0,0203</td>
<td style="text-align: center;">0,1617</td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td></td>
<td></td>
<td></td>
<td style="text-align: center;">Média</td>
<td style="text-align: center;">0,6</td>
<td style="text-align: center;">0,2109</td>
<td style="text-align: center;">10,7962</td>
<td style="text-align: center;">0,0093</td>
<td style="text-align: center;">0,0697</td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td></td>
<td></td>
<td></td>
<td style="text-align: center;">Desvio-Padrão</td>
<td style="text-align: center;">0,424264</td>
<td style="text-align: center;">0,1833355</td>
<td style="text-align: center;">18,05741</td>
<td style="text-align: center;">0,007619</td>
<td style="text-align: center;">0,153235</td>
</tr>
</tbody>
</table>

Observando os resultados do Quadro 7 pode-se aferir que os valores de
atraso fim-a-fim e jitter da rede otimizada foram, em sua maioria,
inferiores ao da rede usando Dijkstra. Além disso os valores de atraso
fim-a-fim em 14 do total de 17 aplicações da rede otimizada não
ultrapassam os valores máximos de referência. Por outro lado, os valores
de atraso fim-a-fim da rede usando Dijkstra ultrapassam os valores
máximos de referência na maioria das aplicações, em 11 do total de 17
aplicações.

Os gráficos ilustrando o comportamento das 17 aplicações testadas na
rede SDN são detalhadas no apêndice nas Figuras de número 41 ao 57.

## 6.3 Considerações Finais

## 

Nesse capítulo foram apresentados os resultados comparativos entre os
algoritmos ACO+AG, ACO+DE e o algoritmo de Dijkstra. As simulações com
os algoritmos levaram em conta os seguintes critérios como forma de
avaliar o desempenho dos algoritmos:

\- limite do número de iterações: sendo realizadas simulações com 200
iterações

\- limite do tempo de execução: sendo realizadas simulações com tempo de
aproximadamente 12 segundos.

Os resultados comparativos entre os algoritmos de otimização demonstram
que os algoritmos ACO+AG são superiores em desempenho ao ACO+DE nas duas
simulações consideradas. No caso da simulação considerando limite do
número de iterações, o ACO+AG obteve um melhor desempenho da função
objetivo, com resultado de 2,44% maior que o ACO+DE. Na comparação com o
Dijkstra e considerando a média da função objetivo, o ACO+AG obteve um
valor de 5.62% maior. Já o ACO+DE obteve um resultado de 3,10% superior.

No caso da simulação considerando o mesmo tempo computacional o ACO+AG
obteve com relação à média da função objetivo um valor de 0,84% maior
que o ACO+DE. Ainda na mesma comparação o ACO+AG obteve um valor de
4,35% maior que o Dijkstra. Por outro lado, o ACO+DE obteve um resultado
de 3,48% superior ao Dijkstra.

Após estas simulações foi realizada uma análise de previsão do atraso e
da vazão para um conjunto das melhores rotas calculadas pelo ACO+AG e
outra solução utilizando uma solução do algoritmo de Dijkstra.

A análise de vazão utilizando uma solução ótima obtida pelo ACO+AG
demonstra melhores resultados em termos de balanceamento de carga e
ocupação homogênea dos enlaces que a solução encontrada via Dijkstra e
além disso respeita as limitações de largura de banda em todos os
enlaces. A análise do atraso fim-a-fim previsto demonstra que a solução
ótima obtida respeita também o máximo atraso fim-a-fim solicitado pelas
aplicações.

Após implementação e configuração da rede SDN foram realizados cinco
testes com a geração e medição de tráfego na rede utilizando o software
D-ITG. Os resultados obtidos foram então analisados comparando o
desempenho de uma rede otimizada (ACO+AG e ACO+DE) com uma rede usando
Dijkstra (Dijkstra). Esses resultados demonstram que a rede otimizada
que utiliza uma solução ótima calculada pelo ACO+AG, apresentam
desempenho consideravelmente superior da usando Dijkstra em termos dos
requisitos de QoS considerados (vazão, atraso fim-a-fim, jitter e perda
de pacotes.) A rede otimizada obteve os seguintes resultados em relação
a rede usando Dijkstra: vazão média 34% maior, atraso fim-a-fim médio 51
vezes menor, jitter médio 7,5 vezes menor e perda de pacotes média 510
vezes menor.

No próximo capítulo são realizadas as conclusões sobre o presente
trabalho.

# 7. CONCLUSÕES

Este trabalho propôs realizar a otimização do uso dos recursos de uma
rede SDN utilizando engenharia de tráfego considerando os requisitos de
QoS das aplicações da rede. Esse objetivo geral foi alcançado através da
implementação e obtenção dos seguintes objetivos específicos: estudar o
problema de engenharia de tráfego aplicados às Redes SDN; formular o
modelo para o problema de otimização do uso dos recursos de uma rede SDN
considerando restrições e requisitos de QoS das aplicações; propor
heurísticas de otimização para o modelo formulado; [implementar o
algoritmo de menor caminho de Dijkstra;]{.mark} comparar o desempenho
das heurísticas de otimização e do algoritmo de Dijkstra; avaliar os
resultados obtidos com a implementação da otimização em uma rede SDN.

Após a realização de uma revisão bibliográfica referente aos temas de
Redes Definidas por Software, Engenharia de tráfego, Qualidade de
Serviço e diferentes técnicas de Otimização; foi formulado um modelo de
Engenharia de Tráfego aplicada às Redes Definidas por Software. Sendo
proposto o uso de duas heurísticas híbridas (ACO+AG e ACO+DE) aplicadas
aos modelos de TE que posteriormente foram implementados na rede SDN
otimizada.

Os algoritmos foram comparados e os resultados monstram que os
algoritmos ACO+AG possuem melhores resultados em termos de convergência
e busca da solução ótima em comparação aos algoritmos ACO+DE com
desempenho de 2,44% e 0,84% maiores considerando o valor médio da função
objetivo para as simulações com mesmo número de iterações e mesmo tempo
computacional respectivamente. No entanto os algoritmos ACO+DE também
alcançam a convergência para uma solução ótima quando executados com um
maior de iterações, assim um melhor ajuste nos seus parâmetros
possivelmente pode fazê-los obter resultados similares ao ACO+AG.

Ainda é possível concluir que ambos os algoritmos (ACO+AG e ACO+DE)
produziram melhores resultados que o algoritmo de Dijkstra. Para a
simulação com mesmo número de iterações, o ACO+AG e ACO+DE tiveram
desempenhos respectivos de 5,62% e 3,10% maiores que o Dijkstra
considerando o valor médio da função objetivo. Para a simulação
considerando o tempo de execução computacional o ACO+AG obteve um
desempenho considerando o valor médio da função objetivo de 4.35% maior
que o Dijkstra. Nessa mesma simulação o ACO+DE obteve um resultado 3,48%
superior ao Dijkstra. Sugerindo que essa implementação híbrida é
eficiente e robusta e implica em novas alternativas para resolução de
problemas de roteamento na área de redes de computadores e possivelmente
outras áreas.

Ao analisarmos os resultados obtidos pelos algoritmos DE e AG
trabalhando em conjunto com ACO nos dois modelos implementados, pode-se
dizer que o uso conjunto desses 3 algoritmos foi realizado de forma
satisfatória e cumpriu adequadamente a tarefa de roteamento e
otimização, resultando em um uso efetivo da TE atendendo aos requisitos
de QoS.

Os resultados obtidos pelos algoritmos de otimização foram emulados numa
rede SDN. A avaliação de desempenho da TE foi realizada levando-se em
conta os critérios de QoS e foram executadas de forma simultânea na rede
SDN utilizando medições fim-a-fim, sendo que os parâmetros utilizados
para a avaliação do desempenho foram: vazão, atraso fim-a-fim, jitter e
perda de pacotes.

Uma capacidade importante da otimização da rede foi obter resultados em
termos de balanceamento de carga de forma indireta, já que não foi
objeto de estudo no presente trabalho. O balacemanto foi obtido através
da otimização que considera como boas as soluções que respeitam os
valores de largura de banda dos enlaces.

No entanto a principal contribuição deste trabalho, além da proposição
do uso de algoritmos de otimização híbridos, é a implementação da TE em
uma rede SDN de forma consistente. Os resultados obtidos com a
implantação/emulação da rede SDN reforçam a capacidade do paradigma SDN
como tecnologia capaz de permitir um uso gerenciável da rede.

Como forma de comparar o desempenho da rede SDN otimizada realizou-se a
implementação do algoritmo de Dijkstra e usando seu conjunto de rotas
foi criada uma rede SDN. [Essa rede usando Dijkstra simula o
comportamento de uma rede que usa o protocolo OSPF.]{.mark}

Os resultados das cinco simulações mostraram que a rede otimizada
fazendo uso da TE através das rotas encontradas pelos algoritmos de
otimização, possue melhores resultados em termos de desempenho e
critérios de QoS que a rede usando Dijkstra. A rede otimizada obteve os
seguintes resultados em relação a usando Dijkstra: vazão média 34%
maior, atraso fim-a-fim médio 51 vezes menor, jitter médio 7,5 vezes
menor e perda de pacotes média 510 vezes menor.

Dessa forma os resultados sugerem que a implementação dos algoritmos de
otimização foi realizada de forma satisfatória e cumpriu adequadamente a
tarefa de roteamento, resultando em um uso efetivo da TE atendendo aos
requisitos de QoS da rede SDN.

## 7.3 Dificuldades Encontradas

No presente estudo foi encontrada uma grande dificuldade em estabelecer
um parâmetro de comparação dos trabalhos correlatos, devido à ausência
de informações e parâmetros envolvidos nas simulações e testes, bem como
detalhes dos algoritmos utilizados e formas de análise distintas. Não
foram encontrados na literatura trabalhos utilizando os algoritmos
ACO+DE e ACO+AG em Redes SDN.

Outra dificuldade encontrada foi a realização da implementação,
configuração e realização de testes da rede SDN usando os softwares
Mininet, Floodlight e D-ITG.

## 7.4 Limitações do Estudo 

A principal limitação deste estudo refere-se ao fato do modelo da rede
SDN não ter sido implementado numa rede formada por equipamentos e
aplicações reais.

Outra limitação do estudo é referente ao gerenciamento proposto na rede
ser realizado de maneira off-line e não on-line (tempo real).

## 7.5 Trabalhos Futuros

## 

Trabalhos futuros podem explorar os seguintes pontos:

\- A implementação e emulação dos modelos em outras topologias e outras
exigências de tráfego como forma de comparar seu desempenho.

\- Realização de um estudo sobre o dimensionamento dos enlaces e SDN.

\- Realizar a injeção de fluxos de dados multimídia levando em conta os
seus respectivos modelos e comportamento não constantes ao longo do
tempo.

\- Implementar e avaliar a otimização aplicada a TE em uma rede formada
por equipamentos e aplicações reais.

\- Realizar testes e a ajustes de sensibilidade nos parâmetros da
heurística ACO+DE como forma de identificar possíveis melhorias no
algoritmo.

\- Uma proposta de estudo de otimização multiobjetivo para o problema.

\- Uma proposta de estudo comparativo entre os seguintes algoritmos: DE
Aleatório x AG Aleatório x Dijkstra x ACO+DE x ACO+AG x Dijkstra+AG x
Dijkstra+DE.

**REFERÊNCIAS**

AFAQ, M; REHMAN, S.; SONG, Wang-Cheol. Large flows detection, marking,
and mitigation based on sFlow standard in SDN. 멀티미디어학회논문지, v.
18, n. 2, p. 189-198, 2015.

AKCAY, H.; YILTAS-KAPLAN, D. Web-Based User Interface for the Floodlight
SDN Controller. Int. J. Advanced Networking and Applications, v. 8, n.
05, p. 3175-3180, 2017.

AKYILDIZ, I. F.; LEE, A.; WANG, P.; LUO, M.; CHOU, W. Research
challenges for traffic engineering in software defined networks. IEEE
Network, v. 30, n. 3, p. 52-58, 2016.

AKYILDIZ, I. F.; LEE, A.; WANG, P.; LUO, M.; CHOU, W. A roadmap for
traffic engineering in SDN-OpenFlow networks. Computer Networks, v. 71,
p. 1-30, 2014.

ALOTTO, P. A hybrid multiobjective differential evolution method for
electromagnetic device optimization. COMPEL-The international journal
for computation and mathematics in electrical and electronic
engineering, v. 30, n. 6, p. 1815-1828, 2011.

ANDRADE, A. V. 2008. Provisionamento de Qualidade de Servico em Redes
MPLS utilizando Algoritmos Bio-inspirados em um Ambiente de Trafego
Auto-Similar. Ph.D. thesis, Universidade Federal de Minas Gerais.

ARAUJO, R. L. Evolução diferencial para problemas de otimização com
restrições lineares. 2016. Dissertação de mestrado, Universidade Federal
de Juiz de Fora - UFJF.

BOTTA, A; DAINOTTI, A; PESCAPÉ, A. A tool for the generation of
realistic network workload for emerging networking scenarios. Computer
Networks, v. 56, n. 15, p. 3531-3547, 2012.

CARVALHO, M. B.; YAMAKAMI, A. Meta-heurística Híbrida de Sistema de
Colônia de Formigas e Algoritmo Genético para o Problema do Caixeiro
Viajante. Trends in Applied and Computational Mathematics, v. 9, n. 1,
p. 31-40, 2008.

CIORNEI, I.; KYRIAKIDES, E. Hybrid ant colony-genetic algorithm (GAAPI)
for global continuous optimization. IEEE Transactions on Systems, Man,
and Cybernetics, Part B (Cybernetics), v. 42, n. 1, p. 234-245, 2012.

CHAVES, A. A. Heurísticas híbridas com busca através de agrupamentos
para o problema do caixeiro viajante com coleta de prêmios. 2005. Tese
de Doutorado. Dissertação de mestrado) Pós-Graduação em Computação
Aplicada, Instituto Nacional de Pesquisas Espaciais (INPE), São José dos
Campos, SP.

CISCO SYSTEMS. *Implementing Cisco Quality of Service* volume
1-2 *version*** **2.2**,** EUA, 2006.

COLORNI, A.; DORIGO, M.; MANIEZZO, V. An Investigation of some
Properties of an\" Ant Algorithm\". In: PPSN. 1992. p. 509-520.

CORREIA, S. L. O. B. 2012. Roteamento em Redes Veiculares Utilizando
Colônias de Formigas e Predição de Mobilidade. UECE -- Universidade
Estadual Do Ceara.

DALAKOV, G. The Dynabook of Alan Kay/Georgi Dalakov. History of
computers, 2013. George Stibitz---remote access to a computer.
Disponível em:
http://history-computer.com/Internet/Dreamers/Stibitz.html Acesso em: 12
dez. 2016.

DARWIN, C. On the origins of species by means of natural selection.
London: Murray, v. 247, p. 1859, 1859.

DE OLIVEIRA, R. L. S.; SCHWEITZER, C. M.; SHINODA, A. A.; PRETE, L. R.
Using mininet for emulation and prototyping software-defined networks.
In: 2014 IEEE Colombian Conference on Communications and Computing
(COLCOM). IEEE, 2014. p. 1-6.

DIAS, R. A. 2004. Engenharia de Trafego em Redes IP sobre Tecnologia
MPLS: Otimizaçao Baseada em Heurısticas. Ph.D. thesis, Universidade
Federal de Santa Catarina.

DIJKSTRA, E. W. A note on two problems in connexion with graphs.
Numerische mathematik, v. 1, n. 1, p. 269-271, 1959.

DOBRIJEVIC, O.; SANTL, M.; MATIJASEVIC, M. Ant colony optimization for
QoE-centric flow routing in software-defined networks. In: 2015 11th
International Conference on Network and Service Management (CNSM). IEEE,
2015. p. 274-278.

DORIGO, M.; STUTZLE, T. Ant Colony Optimization. MIT Press. Cambridge,
MA, 2004.

FLOODLIGHT DOCUMENTATION. Disponível em:

\<https://floodlight.atlassian.net/wiki/spaces/floodlightcontroller/pages/1343557/User+Documentation\>.
Acesso em: 20 out. 2018.

GIESEN, G. F.; OLIVEIRA, F. C.; Abordagem SDN: uma mudança de paradigma
na arquitetura de rede tradicional. Seminário de Redes e Sistemas de
Telecomunicações - INATEL, 2017.

GIMENEZ, E.; VIEIRA, R.; CARDOSO, M.; FERRARI, G. Engenharia de Tráfego
nas Redes MPLS: Uma Análise Comparativa de Seu Desempenho em Função de
Suas Diferentes Implementações. In: World Congress on Computer Science,
Engineering and Techology Education. 2006. p. 570-574.

GOLDBARG, M. C.; LUNA, H. P. L. Otimização combinatória e programação
linear: modelos e algoritmos. Elsevier, 2005.

GOLDBERG, D. E. Genetic algorithms in search, optimization and machine
learning. Alabama: Addison Wesley, 1989. 413p

GROßMANN, M.; SCHUBERTH, S. J. A. Auto-Mininet: Assessing the Internet
Topology Zoo in a Software-Defined Network Emulator. Messung, Mellierung
un Bewertung von Rechensystemen (MMBnet), v. 7, 2013.

GUEDES, D.; VIEIRA, L. F. M.; VIEIRA, M.; RODRIGUES, H.; NUNES, R. V.
Redes Definidas por Software: uma abordagem sistêmica para o
desenvolvimento de pesquisas em Redes de Computadores. Minicursos do
Simpósio Brasileiro de Redes de Computadores-SBRC, v. 30, n. 4, p.
160-210, 2012.

HERIS, S. M. K.. Implementation of Differential Evolution (DE) in
MATLAB. Disponível em:
\<http://yarpiz.com/231/ypea107-differential-evolution\>. Acesso em: 15
abr. 2016.

HERIS, S. M. K. Implementation of Real-Coded Genetic Algorithm in
MATLAB. Disponível em:
\<http://yarpiz.com/23/ypea101-genetic-algorithms\>. Acesso em: 25 fev.
2017.

HOLLAND, J. Adaptation in natural and artificial systems: an
introductory analysis with application to biology. Control and
artificial intelligence, 1975.

HU, F; HAO, Q; BAO, K. A survey on software-defined network and
openflow: From concept to implementation. IEEE Communications Surveys &
Tutorials, v. 16, n. 4, p. 2181-2206, 2014.

ITU -  International Telecommunication Union, 2017. Disponível em:
https://www.itu.int/en/ITU-D/Statistics/Pages/stat/default.aspx.. Acesso
em: 15 mar. 2018.

JARSCHEL, M.; ZINNER, T.; HOßFELD, T.; TRAN-GIA, P.; KELLERER, W.
Interfaces, attributes, and use cases: A compass for SDN. IEEE
Communications Magazine, v. 52, n. 6, p. 210-217, 2014.

KAUR, K; SINGH, J.; GHUMMAN, N. S. Mininet as software defined
networking testing platform. In: International Conference on
Communication, Computing & Systems (ICCCS). 2014. p. 139-42.

KETI, F; ASKAR, S. Emulation of software defined networks using mininet
in different simulation environments. In: Proceedings of the 2015 6th
International Conference on Intelligent Systems, Modelling and
Simulation. IEEE Computer Society. 2015.

KIM, H.; FEAMSTER, N. Improving network management with software defined
networking. IEEE Communications Magazine, v. 51, n. 2, p. 114-119, 2013.

KIRK, J. Dijkstra\'s Minimum Cost Path Algorithm - Repositório File
Exchange do Matlab. Disponível em: \<
https://la.mathworks.com/matlabcentral/fileexchange/20025-dijkstra-s-minimum-cost-path-algorithm\>.
Acesso em: 10 set. 2017.

KHUSHABA, R. N.; AL-ANI, A.; ALSUKKER, A.; AL-JUMAILY, A. A combined ant
colony and differential evolution feature selection algorithm. In:
International Conference on Ant Colony Optimization and Swarm
Intelligence. Springer, Berlin, Heidelberg, 2008. p. 1-12.

KREUTZ, D.; RAMOS, F. M.; VERISSIMO, P. E.; ROTHENBERG, C. E.;
AZODOLMOLKY, S.; UHLIG, S. Software-defined networking: A comprehensive
survey. Proceedings of the IEEE, v. 103, n. 1, p. 14-76, 2015.

KUROSE, J. F.; ROSS, K. W. Redes de Computadores e a Internet. São
Paulo: Person, 2010.

LIN, T.; CHEN, Y.; CHANG, H. An Ant Colony Optimization Routing Strategy
for Wireless Sensor Networks: A SDN-like Perspective. Journal of
Computers, v. 28, n. 4, p. 103-113, 2017.

LOBATO, A. G. P.; DA ROCHA FIGUEIREDO, U.; LOPEZ, M. A.; DUARTE, O. C.
M. B. Uma arquitetura elástica para prevenç ao de intrusao em redes
virtuais usando redes definidas por software. XXXII Simpósio Brasileiro
de Redes de Computadores e Sistemas Distribuídos-SBRC 2014, p. 1-14,
2014.

MAIA, N. A. 2006. Engenharia de Tráfego em domínio MPLS utilizando
técnicas de Inteligência Computacional. Programa de Pós-Graduação em
Engenharia Elétrica, UFMG, 2006.

MATLAB. Math Works, Inc. Disponível em: \<http://www.mathworks.com/\>
Acesso em: 01 mai. 2016.

MCKEOWN, N.; ANDERSON, T.; BALAKRISHNAN, H.; PARULKAR, G.; PETERSON, L.;
REXFORD, J.; SHENKER, S.; TURNER, J. OpenFlow: enabling innovation in
campus networks. ACM SIGCOMM Computer Communication Review, v. 38, n. 2,
p. 69-74, 2008.

MICHALEWICZ, Z. Genetic algorithms + data structures = evolutionary
programming. Springer. 1996.

NUNES, B. A. A.; MENDONCA, M.; NGUYEN, X.; OBRACZKA, K.; TURLETTI, T. A
survey of software-defined networking: Past, present, and future of
programmable networks. IEEE Communications Surveys & Tutorials, v. 16,
n. 3, p. 1617-1634, 2014.

PARSAEI, M. R.; MOHAMMADI, R.; JAVIDAN, R. A new adaptive traffic
engineering method for telesurgery using ACO algorithm over Software
Defined Networks. European Research in Telemedicine/La Recherche
Européenne en Télémédecine, v. 6, n. 3-4, p. 173-180, 2017.

PISKE, R. B. Introdução à informática: visando um mundo da máquina.
Editora Barauna, 2012.

PRICE, K.; STORN, R. M.; LAMPINEN, J. A. Differential evolution: a
practical approach to global optimization. Springer Science & Business
Media, 2006.

RAHMAT, N. A.; MUSIRIN, I. Differential evolution ant colony
optimization (DEACO) technique in solving economic load dispatch
problem. In: Power Engineering and Optimization Conference (PEDCO)
Melaka, Malaysia, 2012 Ieee International. IEEE, 2012. p. 263-268.

SFLOW-RT. Disponível em: \<http://sflow-rt.com/index.php\>. Acesso em:
22 out. 2018.

STORN, R.; PRICE, K. Differential evolution--a simple and efficient
heuristic for global optimization over continuous spaces. Journal of
global optimization, v. 11, n. 4, p. 341-359, 1997.

STORN, R. M. Differential Evolution. Rainer Storn\'s Home Page.
Disponível em: \<http://www1.icsi.berkeley.edu/\~storn/code.html\>.
Acesso em: 10 nov. 2017.

TANENBAUM, A. S. Redes de computadoras. Pearson Educación, 2003.

TOMOVIC, S.; RADUSINOVIC, I.; PRASAD, N. Performance comparison of QoS
routing algorithms applicable to large-scale SDN networks. In: EUROCON
2015-International Conference on Computer as a Tool (EUROCON), IEEE.
IEEE, 2015. p. 1-6.

WAN, J; TANG, S.; SHU, Z.; LI, D.; WANG, S.; IMRAN, M.; VASILAKOS, A. V.
Software-defined industrial internet of things in the context of
industry 4.0. IEEE Sensors Journal, v. 16, n. 20, p. 7373-7380, 2016.

WANG, C.; ZHANG, G.; XU, H.; CHEN, H. An ACO-based Link Load-Balancing
Algorithm in SDN. In: Cloud Computing and Big Data (CCBD), 2016 7th
International Conference on. IEEE, 2016. p. 214-218.

ZHANG, X.; DUAN, H.; JIN, J. DEACO: Hybrid ant colony optimization with
differential evolution. In: Evolutionary Computation, 2008. CEC
2008.(IEEE World Congress on Computational Intelligence). IEEE Congress
on. IEEE, 2008. p. 921-927.

ZUKHRI, Z.; PAPUTUNGAN, I.V. A hybrid optimization algorithm based on
genetic algorithm and ant colony optimization. International Journal of
Artificial Intelligence & Applications, v. 4, n. 5, p. 63, 2013.

**APÊNDICE A**

**Figuras dos gráficos dos resultados das aplicações comparando a rede
otimizada e a rede usando Dijkstra**

O desempenho das aplicações de 1 a 17 para os 5 testes realizados são
apresentados pelos gráficos das Figuras 33, 34, 35, 36, 37, 38, 39, 40,
41, 42, 43, 44, 45, 46, 47, 48 e 49 respectivamente.

![](media/image30.png){width="5.905555555555556in"
height="3.9381944444444446in"}

Figura 33 -- Resultados da Aplicação 1 do IP:10.0.1.52 (origem) para o
IP:10.0.1.49 (destino)

![](media/image31.png){width="5.905555555555556in"
height="3.9381944444444446in"}

Figura 34 -- Resultados da Aplicação 2 do IP:10.0.1.1 (origem) para o
IP:10.0.1.33 (destino)

![](media/image32.png){width="5.905555555555556in"
height="3.9381944444444446in"}

Figura 35 -- Resultados da Aplicação 3 do IP:10.0.1.2 (origem) para o
IP:10.0.1.51 (destino)

![](media/image33.png){width="5.905555555555556in"
height="3.9381944444444446in"}

Figura 36 -- Resultados da Aplicação 4 do IP:10.0.1.3 (origem) para o
IP:10.0.1.50 (destino)

![](media/image34.png){width="5.905555555555556in"
height="3.9381944444444446in"}

Figura 37 -- Resultados da Aplicação 5 do IP:10.0.1.4 (origem) para o
IP:10.0.1.37 (destino)

![](media/image35.png){width="5.905555555555556in"
height="3.9381944444444446in"}

Figura 38 -- Resultados da Aplicação 6 do IP:10.0.1.31 (origem) para o
IP:10.0.1.36 (destino)

![](media/image36.png){width="5.905555555555556in"
height="3.9381944444444446in"}

Figura 39 -- Resultados da Aplicação 7 do IP:10.0.1.32 (origem) para o
IP:10.0.1.46 (destino)

![](media/image37.png){width="5.905555555555556in"
height="3.9381944444444446in"}

Figura 40 -- Resultados da Aplicação 8 do IP:10.0.1.5 (origem) para o
IP:10.0.1.48 (destino)

![](media/image38.png){width="5.905555555555556in"
height="3.9381944444444446in"}

Figura 41 -- Resultados da Aplicação 9 do IP:10.0.1.6 (origem) para o
IP:10.0.1.47 (destino)

![](media/image39.png){width="5.905555555555556in"
height="3.9381944444444446in"}

Figura 42 -- Resultados da Aplicação 10 do IP:10.0.1.7 (origem) para o
IP:10.0.1.34 (destino)

![](media/image40.png){width="5.905555555555556in"
height="3.9381944444444446in"}

Figura 43 -- Resultados da Aplicação 11 do IP:10.0.1.8 (origem) para o
IP:10.0.1.44 (destino)

![](media/image41.png){width="5.905555555555556in"
height="3.9381944444444446in"}

Figura 44 -- Resultados da Aplicação 12 do IP:10.0.1.9 (origem) para o
IP:10.0.1.43 (destino)

![](media/image42.png){width="5.905555555555556in"
height="3.9381944444444446in"}

Figura 45 -- Resultados da Aplicação 13 do IP:10.0.1.11 (origem) para o
IP:10.0.1.41 (destino)

![](media/image43.png){width="5.905555555555556in"
height="3.9381944444444446in"}

Figura 46 -- Resultados da Aplicação 14 do IP:10.0.1.10 (origem) para o
IP:10.0.1.42 (destino)

![](media/image44.png){width="5.905555555555556in"
height="3.9381944444444446in"}

Figura 47 -- Resultados da Aplicação 15 do IP:10.0.1.12 (origem) para o
IP:10.0.1.40 (destino)

![](media/image45.png){width="5.905555555555556in"
height="3.9381944444444446in"}

Figura 48 -- Resultados da Aplicação 16 do IP:10.0.1.13 (origem) para o
IP:10.0.1.39 (destino)

![](media/image46.png){width="5.905555555555556in"
height="3.9381944444444446in"}

Figura 49 -- Resultados da Aplicação 17 do IP:10.0.1.30 (origem) para o
IP:10.0.1.45 (destino)

**APÊNDICE B**

**Código da rede implementada em SDN**

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Código Python da Topologia da Rede

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

#!/usr/bin/python

from mininet.net import Mininet

from mininet.node import RemoteController, OVSSwitch

from mininet.cli import CLI

from mininet.log import setLogLevel, info

from mininet.link import TCLink

def emptyNet():

net = Mininet( topo=None, build=False )

info( \'\*\*\* Adding controller\\n\' )

net.addController(\'c0\',
controller=RemoteController,ip=\"192.168.56.101\",port=6653)

info( \'\*\*\* Adding hosts\\n\' )

h1 = net.addHost(\'h1\', ip=\'10.0.1.1\', mac=\"00:00:00:00:00:01\" )

h2 = net.addHost(\'h2\', ip=\'10.0.1.2\', mac=\"00:00:00:00:00:02\" )

h3 = net.addHost(\'h3\', ip=\'10.0.1.3\', mac=\"00:00:00:00:00:03\" )

h4 = net.addHost(\'h4\', ip=\'10.0.1.4\', mac=\"00:00:00:00:00:04\" )

h5 = net.addHost(\'h5\', ip=\'10.0.1.5\', mac=\"00:00:00:00:00:05\" )

h6 = net.addHost(\'h6\', ip=\'10.0.1.6\' , mac=\"00:00:00:00:00:06\" )

h7 = net.addHost(\'h7\', ip=\'10.0.1.7\', mac=\"00:00:00:00:00:07\" )

h8 = net.addHost(\'h8\', ip=\'10.0.1.8\' , mac=\"00:00:00:00:00:08\" )

h9 = net.addHost(\'h9\', ip=\'10.0.1.9\' , mac=\"00:00:00:00:00:09\" )

h10 = net.addHost(\'h10\', ip=\'10.0.1.10\' , mac=\"00:00:00:00:00:10\"
)

h11 = net.addHost(\'h11\', ip=\'10.0.1.11\' , mac=\"00:00:00:00:00:11\"
)

h12 = net.addHost(\'h12\', ip=\'10.0.1.12\' , mac=\"00:00:00:00:00:12\"
)

h13 = net.addHost(\'h13\', ip=\'10.0.1.13\' , mac=\"00:00:00:00:00:13\"
)

h30 = net.addHost(\'h30\', ip=\'10.0.1.30\' , mac=\"00:00:00:00:00:30\"
)

h31 = net.addHost(\'h31\', ip=\'10.0.1.31\' , mac=\"00:00:00:00:00:31\"
)

h32 = net.addHost(\'h32\', ip=\'10.0.1.32\' , mac=\"00:00:00:00:00:32\"
)

h33 = net.addHost(\'h33\', ip=\'10.0.1.33\' , mac=\"00:00:00:00:00:33\"
)

h34 = net.addHost(\'h34\', ip=\'10.0.1.34\' , mac=\"00:00:00:00:00:34\"
)

h35 = net.addHost(\'h35\', ip=\'10.0.1.35\' , mac=\"00:00:00:00:00:35\"
)

h36 = net.addHost(\'h36\', ip=\'10.0.1.36\' , mac=\"00:00:00:00:00:36\"
)

h37 = net.addHost(\'h37\', ip=\'10.0.1.37\' , mac=\"00:00:00:00:00:37\"
)

h38 = net.addHost(\'h38\', ip=\'10.0.1.38\' , mac=\"00:00:00:00:00:38\"
)

h39 = net.addHost(\'h39\', ip=\'10.0.1.39\' , mac=\"00:00:00:00:00:39\"
)

h40 = net.addHost(\'h40\', ip=\'10.0.1.40\' , mac=\"00:00:00:00:00:40\"
)

h41 = net.addHost(\'h41\', ip=\'10.0.1.41\' , mac=\"00:00:00:00:00:41\"
)

h42 = net.addHost(\'h42\', ip=\'10.0.1.42\' , mac=\"00:00:00:00:00:42\"
)

h43 = net.addHost(\'h43\', ip=\'10.0.1.43\' , mac=\"00:00:00:00:00:43\"
)

h44 = net.addHost(\'h44\', ip=\'10.0.1.44\' , mac=\"00:00:00:00:00:44\"
)

h45 = net.addHost(\'h45\', ip=\'10.0.1.45\' , mac=\"00:00:00:00:00:45\"
)

h46 = net.addHost(\'h46\', ip=\'10.0.1.46\' , mac=\"00:00:00:00:00:46\"
)

h47 = net.addHost(\'h47\', ip=\'10.0.1.47\' , mac=\"00:00:00:00:00:47\"
)

h48 = net.addHost(\'h48\', ip=\'10.0.1.48\' , mac=\"00:00:00:00:00:48\"
)

h49 = net.addHost(\'h49\', ip=\'10.0.1.49\' , mac=\"00:00:00:00:00:49\"
)

h50 = net.addHost(\'h50\', ip=\'10.0.1.50\' , mac=\"00:00:00:00:00:50\"
)

h51 = net.addHost(\'h51\', ip=\'10.0.1.51\' , mac=\"00:00:00:00:00:51\"
)

h52 = net.addHost(\'h52\', ip=\'10.0.1.52\' , mac=\"00:00:00:00:00:52\"
)

info( \'\*\*\* Adding switch\\n\' )

s14 = net.addSwitch(\'s14\', cls=OVSSwitch , mac=\"00:00:00:00:00:14\" ,
dpid=\"0000000000000014\")

s15 = net.addSwitch(\'s15\', cls=OVSSwitch , mac=\"00:00:00:00:00:15\" ,
dpid=\"0000000000000015\")

s16 = net.addSwitch(\'s16\', cls=OVSSwitch , mac=\"00:00:00:00:00:16\" ,
dpid=\"0000000000000016\")

s17 = net.addSwitch(\'s17\', cls=OVSSwitch , mac=\"00:00:00:00:00:17\" ,
dpid=\"0000000000000017\")

s18 = net.addSwitch(\'s18\', cls=OVSSwitch , mac=\"00:00:00:00:00:18\" ,
dpid=\"0000000000000018\")

s19 = net.addSwitch(\'s19\', cls=OVSSwitch , mac=\"00:00:00:00:00:19\" ,
dpid=\"0000000000000019\")

s20 = net.addSwitch(\'s20\', cls=OVSSwitch , mac=\"00:00:00:00:00:20\" ,
dpid=\"0000000000000020\")

s21 = net.addSwitch(\'s21\', cls=OVSSwitch , mac=\"00:00:00:00:00:21\" ,
dpid=\"0000000000000021\")

s22 = net.addSwitch(\'s22\', cls=OVSSwitch , mac=\"00:00:00:00:00:22\" ,
dpid=\"0000000000000022\")

s23 = net.addSwitch(\'s23\', cls=OVSSwitch , mac=\"00:00:00:00:00:23\" ,
dpid=\"0000000000000023\")

s24 = net.addSwitch(\'s24\', cls=OVSSwitch , mac=\"00:00:00:00:00:24\" ,
dpid=\"0000000000000024\")

s25 = net.addSwitch(\'s25\', cls=OVSSwitch , mac=\"00:00:00:00:00:25\" ,
dpid=\"0000000000000025\")

s26 = net.addSwitch(\'s26\', cls=OVSSwitch , mac=\"00:00:00:00:00:26\" ,
dpid=\"0000000000000026\")

s27 = net.addSwitch(\'s27\', cls=OVSSwitch , mac=\"00:00:00:00:00:27\" ,
dpid=\"0000000000000027\")

s28 = net.addSwitch(\'s28\', cls=OVSSwitch , mac=\"00:00:00:00:00:28\" ,
dpid=\"0000000000000028\")

s29 = net.addSwitch(\'s29\', cls=OVSSwitch , mac=\"00:00:00:00:00:29\" ,
dpid=\"0000000000000029\")

info( \'\*\*\* Creating links\\n\' )

\## controller - switch (s4)

##net.addLink( h0, s4 )

\## host - switch

\# Hosts ligados ao s17

net.addLink(h1, s17, port1 = 1, port2 = 1, cls=TCLink, bw=2,
delay=\'1ms\')

#, cls=TCLink, bw=2, delay=\'1ms\', loss=10 )

net.addLink(h2, s17, port1 = 1, port2 = 2, cls=TCLink, bw=2,
delay=\'1ms\')

net.addLink(h3, s17, port1 = 1, port2 = 3, cls=TCLink, bw=2,
delay=\'1ms\')

net.addLink(h4, s17, port1 = 1, port2 = 4, cls=TCLink, bw=2,
delay=\'1ms\')

net.addLink(h5, s17, port1 = 1, port2 = 5, cls=TCLink, bw=2,
delay=\'1ms\')

net.addLink(h6, s17, port1 = 1, port2 = 6, cls=TCLink, bw=2,
delay=\'1ms\')

net.addLink(h52, s17, port1 = 1, port2 = 7, cls=TCLink, bw=2,
delay=\'1ms\')

\# Hosts ligados ao s14

net.addLink(h7, s14, port1 = 1, port2 = 1, cls=TCLink, bw=2,
delay=\'1ms\')

net.addLink(h8, s14, port1 = 1, port2 = 2, cls=TCLink, bw=2,
delay=\'1ms\')

net.addLink(h9, s14, port1 = 1, port2 = 3, cls=TCLink, bw=2,
delay=\'1ms\')

net.addLink(h10, s14, port1 = 1, port2 = 4, cls=TCLink, bw=2,
delay=\'1ms\')

net.addLink(h11, s14, port1 = 1, port2 = 5, cls=TCLink, bw=2,
delay=\'1ms\')

net.addLink(h12, s14, port1 = 1, port2 = 6, cls=TCLink, bw=2,
delay=\'1ms\')

net.addLink(h13, s14, port1 = 1, port2 = 7, cls=TCLink, bw=2,
delay=\'1ms\')

\# Hosts ligados ao s15

net.addLink(h30, s15, port1 = 1, port2 = 1, cls=TCLink, bw=2,
delay=\'1ms\')

\# Hosts ligados ao s18

net.addLink(h31, s18, port1 = 1, port2 = 1, cls=TCLink, bw=2,
delay=\'1ms\')

net.addLink(h32, s18, port1 = 1, port2 = 2, cls=TCLink, bw=2,
delay=\'1ms\')

\# Hosts ligados ao s21

net.addLink(h37, s21, port1 = 1, port2 = 1, cls=TCLink, bw=2,
delay=\'1ms\')

net.addLink(h36, s21, port1 = 1, port2 = 2, cls=TCLink, bw=2,
delay=\'1ms\')

\# Hosts ligados ao s26

net.addLink(h33, s26, port1 = 1, port2 = 1, cls=TCLink, bw=2,
delay=\'1ms\')

net.addLink(h34, s26, port1 = 1, port2 = 2, cls=TCLink, bw=2,
delay=\'1ms\')

net.addLink(h35, s26, port1 = 1, port2 = 3, cls=TCLink, bw=2,
delay=\'1ms\')

\# Hosts ligados ao s22

net.addLink(h38, s22, port1 = 1, port2 = 1, cls=TCLink, bw=2,
delay=\'1ms\')

net.addLink(h39, s22, port1 = 1, port2 = 2, cls=TCLink, bw=2,
delay=\'1ms\')

net.addLink(h44, s22, port1 = 1, port2 = 3, cls=TCLink, bw=2,
delay=\'1ms\')

\# Hosts ligados ao s27

net.addLink(h47, s27, port1 = 1, port2 = 1, cls=TCLink, bw=2,
delay=\'1ms\')

net.addLink(h48, s27, port1 = 1, port2 = 2, cls=TCLink, bw=2,
delay=\'1ms\')

net.addLink(h49, s27, port1 = 1, port2 = 3, cls=TCLink, bw=2,
delay=\'1ms\')

net.addLink(h50, s27, port1 = 1, port2 = 4, cls=TCLink, bw=2,
delay=\'1ms\')

\# Hosts ligados ao s28

net.addLink(h45, s28, port1 = 1, port2 = 1, cls=TCLink, bw=2,
delay=\'1ms\')

net.addLink(h46, s28, port1 = 1, port2 = 2, cls=TCLink, bw=2,
delay=\'1ms\')

net.addLink(h51, s28, port1 = 1, port2 = 3, cls=TCLink, bw=2,
delay=\'1ms\')

\# Hosts ligados ao s29

net.addLink(h40, s29, port1 = 1, port2 = 1, cls=TCLink, bw=2,
delay=\'1ms\')

net.addLink(h41, s29, port1 = 1, port2 = 2, cls=TCLink, bw=2,
delay=\'1ms\')

net.addLink(h42, s29, port1 = 1, port2 = 3, cls=TCLink, bw=2,
delay=\'1ms\')

net.addLink(h43, s29, port1 = 1, port2 = 4, cls=TCLink, bw=2,
delay=\'1ms\')

\## switches

##switchList = (s1, s2, s3, s4)

\## net.addLink(switchList\[index\], switchList\[index2\])

\## switches

net.addLink(s14, s15, port1 = 8, port2 = 2, cls=TCLink, bw=2,
delay=\'30ms\')

net.addLink(s14, s16, port1 = 9, port2 = 1, cls=TCLink, bw=2,
delay=\'20ms\')

net.addLink(s14, s20, port1 = 10, port2 = 1, cls=TCLink, bw=2,
delay=\'30ms\')

net.addLink(s15, s21, port1 = 3, port2 = 3, cls=TCLink, bw=2,
delay=\'20ms\')

net.addLink(s16, s17, port1 = 2, port2 = 8, cls=TCLink, bw=2,
delay=\'20ms\')

net.addLink(s16, s20, port1 = 3, port2 = 2, cls=TCLink, bw=2,
delay=\'20ms\')

net.addLink(s17, s18, port1 = 9, port2 = 3, cls=TCLink, bw=2,
delay=\'10ms\')

net.addLink(s17, s19, port1 = 10, port2 = 1, cls=TCLink, bw=2,
delay=\'30ms\')

net.addLink(s17, s25, port1 = 11, port2 = 1, cls=TCLink, bw=2,
delay=\'10ms\')

net.addLink(s18, s26, port1 = 4, port2 = 4, cls=TCLink, bw=2,
delay=\'10ms\')

net.addLink(s19, s20, port1 = 2, port2 = 3, cls=TCLink, bw=2,
delay=\'20ms\')

net.addLink(s19, s23, port1 = 3, port2 = 1, cls=TCLink, bw=2,
delay=\'20ms\')

net.addLink(s19, s24, port1 = 4, port2 = 1, cls=TCLink, bw=2,
delay=\'20ms\')

net.addLink(s19, s25, port1 = 5, port2 = 2, cls=TCLink, bw=2,
delay=\'40ms\')

net.addLink(s20, s21, port1 = 4, port2 = 4, cls=TCLink, bw=2,
delay=\'20ms\')

net.addLink(s20, s22, port1 = 5, port2 = 4, cls=TCLink, bw=2,
delay=\'10ms\')

net.addLink(s20, s23, port1 = 6, port2 = 2, cls=TCLink, bw=2,
delay=\'10ms\')

net.addLink(s21, s22, port1 = 5, port2 = 5, cls=TCLink, bw=2,
delay=\'20ms\')

net.addLink(s22, s23, port1 = 6, port2 = 3, cls=TCLink, bw=2,
delay=\'20ms\')

net.addLink(s22, s29, port1 = 7, port2 = 5, cls=TCLink, bw=2,
delay=\'10ms\')

net.addLink(s23, s24, port1 = 4, port2 = 2, cls=TCLink, bw=2,
delay=\'10ms\')

net.addLink(s23, s28, port1 = 5, port2 = 4, cls=TCLink, bw=2,
delay=\'20ms\')

net.addLink(s23, s29, port1 = 6, port2 = 6, cls=TCLink, bw=2,
delay=\'20ms\')

net.addLink(s24, s25, port1 = 3, port2 = 3, cls=TCLink, bw=2,
delay=\'30ms\')

net.addLink(s24, s27, port1 = 4, port2 = 5, cls=TCLink, bw=2,
delay=\'30ms\')

net.addLink(s24, s28, port1 = 5, port2 = 5, cls=TCLink, bw=2,
delay=\'10ms\')

net.addLink(s25, s26, port1 = 4, port2 = 5, cls=TCLink, bw=2,
delay=\'30ms\')

net.addLink(s25, s27, port1 = 5, port2 = 6, cls=TCLink, bw=2,
delay=\'10ms\')

net.addLink(s26, s27, port1 = 6, port2 = 7, cls=TCLink, bw=2,
delay=\'10ms\')

net.addLink(s27, s28, port1 = 8, port2 = 6, cls=TCLink, bw=2,
delay=\'80ms\')

info( \'\*\*\* Starting network\\n\')

net.start()

#info(\'\*\*\* Set ip address to switch\\n\')

s14.cmd(\'ifconfig s1 10.0.1.14\')

s15.cmd(\'ifconfig s2 10.0.1.15\')

s16.cmd(\'ifconfig s3 10.0.1.16\')

s17.cmd(\'ifconfig s4 10.0.1.17\')

s18.cmd(\'ifconfig s1 10.0.1.18\')

s19.cmd(\'ifconfig s2 10.0.1.19\')

s20.cmd(\'ifconfig s3 10.0.1.20\')

s21.cmd(\'ifconfig s4 10.0.1.21\')

s22.cmd(\'ifconfig s1 10.0.1.22\')

s23.cmd(\'ifconfig s2 10.0.1.23\')

s24.cmd(\'ifconfig s3 10.0.1.24\')

s25.cmd(\'ifconfig s4 10.0.1.25\')

s26.cmd(\'ifconfig s1 10.0.1.26\')

s27.cmd(\'ifconfig s2 10.0.1.27\')

s28.cmd(\'ifconfig s3 10.0.1.28\')

s29.cmd(\'ifconfig s4 10.0.1.29\')

info(\'\*\*\* Enable spanning tree\\n\')

s14.cmd(\'ovs-vsctl set bridge s14 stp-enable=true\')

s15.cmd(\'ovs-vsctl set bridge s15 stp-enable=true\')

s16.cmd(\'ovs-vsctl set bridge s16 stp-enable=true\')

s17.cmd(\'ovs-vsctl set bridge s17 stp-enable=true\')

s18.cmd(\'ovs-vsctl set bridge s18 stp-enable=true\')

s19.cmd(\'ovs-vsctl set bridge s19 stp-enable=true\')

s20.cmd(\'ovs-vsctl set bridge s20 stp-enable=true\')

s21.cmd(\'ovs-vsctl set bridge s21 stp-enable=true\')

s22.cmd(\'ovs-vsctl set bridge s22 stp-enable=true\')

s23.cmd(\'ovs-vsctl set bridge s23 stp-enable=true\')

s24.cmd(\'ovs-vsctl set bridge s24 stp-enable=true\')

s25.cmd(\'ovs-vsctl set bridge s25 stp-enable=true\')

s26.cmd(\'ovs-vsctl set bridge s26 stp-enable=true\')

s27.cmd(\'ovs-vsctl set bridge s27 stp-enable=true\')

s28.cmd(\'ovs-vsctl set bridge s28 stp-enable=true\')

s29.cmd(\'ovs-vsctl set bridge s29 stp-enable=true\')

info( \'\*\*\* Running CLI\\n\' )

CLI( net )

info( \'\*\*\* Stopping network\' )

net.stop()

if \_\_name\_\_ == \'\_\_main\_\_\':

setLogLevel( \'info\' )

emptyNet()

**APÊNDICE C**

Variáveis da rede da topologia 1 (top1): topologia, demandas, atrasos e
vazões.

O código variaveis_de_entrada.m é responsável por chamar as variáveis
que são normalmente são carregadas na memória usando os seguintes
comandos, quando se tem os arquivos ".mat".

load(\'top_1_maia_52_65_30_CordMod.mat\');

load(\'tab_atraso_top_1_maia.mat\');

load(\'tab_demanda_aplic_top_1_maia.mat\');

load(\'tab_vazao_top_1_maia.mat\');

Na falta destes aquivos, pode-se utilizar o script:
variaveis_de_entrada.m para geração destes ou das variáveis de
interesse: A, xy, AT, VA e tds.

Algoritmos responsáveis pela criação e seleção de rotas.

Diagrama dos algoritmos e suas respectivas dependências de variáveis e
funções:

1\. ACODEeACOAG_14.m (script principal) necessita do arquivo:
Var_test13.xlsx

2\.

3\. mgrafos14g.m (função do algoritmo AntNet) necessita dos arquivos:
".mat" citados acima.

4\. Roleta.m

5\. FuncDistancia.m

6\.

7\. agaco811.m (função do algoritmo AG)

8\. linkc5.m

9\. Crossover2.m

10\. Mutate2.m

11\.

12\. deaco311.m (função do algoritmo DE)

13\. linkc5.m

14\.

15\. mgrafos14dijkstra.m (função do algoritmo de Dijksta) necessita dos
arquivos: ".mat"

16\. dijkstra.m (Algoritmo de Dijksta)

Algoritmo para plotagem de rotas

Gráfico_pos_de_2_subplot.m (script de plotagem das rotas da topologia).

Necessita do arquivo: \'top_1_maia_52_65_30_CordMod.mat\' para
carregamento das variáveis: A e xy.

Necessita do conjunto de rotas otimizadas encontradas pelos algoritmos
de ACO+AG ou ACO+DE.

Algoritmo para geração do arquivo ".sh" para configuração das redes pelo
controlador Floodlight

CodigosCurl2.m (script de geração do código JSON que configura o
controlador).

Necessita da matriz de adjacência das portas entre os dispositivos de
encaminhamento e também do conjunto de rotas otimizadas encontradas
pelos algoritmos de ACO+AG ou ACO+DE.

Faz leitura e escrita em arquivos de texto ".txt" que deve ser
configurado.

Faz chamada da função dijkstra.m (Algoritmo de Dijksta).

**Códigos em Matlab dos algoritmos utilizados:**

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

variaveis_de_entrada.m

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\% Matrizes de grafos

\% Variáveis A e xy da topologia 1

\% carregadas pelo arquivo: \'top_1_maia_52_65_30_CordMod.mat\'

\% no comando: load(\'top_1_maia_52_65_30_CordMod.mat\');

\% Matriz de \[x,y\] da topologia 1

xy = \[ 0.1160 0.9428

0.0390 0.9428

0.0390 0.8347

0.0390 0.7393

0.0390 0.6455

0.0390 0.5533

0.0390 0.4404

0.0390 0.3339

0.0390 0.2337

0.0390 0.1399

0.0390 0.0461

0.1160 0.0461

0.1929 0.0461

0.1929 0.2337

0.3284 0.2337

0.1929 0.4404

0.1929 0.7393

0.4581 0.8347

0.4581 0.5533

0.4581 0.4404

0.4581 0.2337

0.6383 0.2337

0.6383 0.4404

0.6383 0.5533

0.4581 0.7393

0.6383 0.8347

0.7968 0.7393

0.7968 0.5533

0.7968 0.2337

0.3284 0.0461

0.4891 0.9428

0.4271 0.9428

0.5763 0.9428

0.6383 0.9428

0.7003 0.9428

0.4891 0.0461

0.4271 0.0461

0.6383 0.0461

0.5763 0.0461

0.7968 0.0461

0.9575 0.0461

0.9575 0.2337

0.9575 0.3339

0.7003 0.0461

0.9575 0.4404

0.9575 0.5533

0.9575 0.7393

0.9575 0.8347

0.9575 0.9428

0.7968 0.9428

0.9575 0.6455

0.1929 0.9428\];

\% A é a Matriz de Grafo da topologia 1

A = \[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 1 1 1 1 1 1 1 0 1 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 1 0 1 1 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 1 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 0 1 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 1 0 0 0 0 0 1 0 0 0 0 0 0 0
0 1 1 0 0 0 0 1 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 1 0 1 0 0 0 1 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 1 0 1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 1 0 1 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 1 0 0 0 0 0 1 1 1 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 1 1 1 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 1 0 0 0 0 1 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\];

\% O arquivo: \'top_1_maia_52_65_30_CordMod.mat\'

\% pode ser gerado através do seguinte comando:

\% save(\'top_1_maia_52_65_30_CordMod.mat\',\'A\',\'xy\');

\% para depois ser carregado usando o comando:

\% load(\'top_1_maia_52_65_30_CordMod.mat\');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\% Variável AT da topologia 1

\% carregadas pelo arquivo: \'tab_atraso_top_1_maia.mat\'

\% no comando: load(\'tab_atraso_top_1_maia.mat\');

\% AT é a Tabela (Matriz) de atrasos da topologia 1

AT = \[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 1 1 1 1 1 1 1 0 30 20 0 0 0 30 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 30 0 0 0 0 0 0 20 0 0 0 0 0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 20 0 0 20 0 0 20 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 20 0 10 30 0 0 0 0 0 10 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 10 0 0 0 0 0 0 0 0 10 0 0 0 0 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 30 0 0 20 0 0 20 20 40 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 30 0 20 0 0 20 0 20 10 10 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 20 0 0 0 0 20 0 20 0 0 0 0 0 0 0 0 0 0 0 0 0
1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 10 20 0 20 0 0 0 0 0 10 0 0 0 0 0
0 0 0 1 1 0 0 0 0 1 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 20 10 0 20 0 10 0 0 0 20 20 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 20 0 0 0 10 0 30 0 30 10 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 10 0 40 0 0 0 0 30 0 30 10 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 10 0 0 0 0 0 0 30 0 10 0 0 0 0 0 1 1 1
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 30 10 10 0 80 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 20 10 0 0 80 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 1 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 10 20 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\];

\% O arquivo: \'tab_atraso_top_1_maia.mat\'

\% pode ser gerado através do seguinte comando:

\% save(\'tab_atraso_top_1_maia.mat\',\'AT\');

\% para depois ser carregado usando o comando:

\% load(\'tab_atraso_top_1_maia.mat\');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\% Variável VA da topologia 1

\% carregadas pelo arquivo: \'tab_vazao_top_1_maia.mat\'

\% no comando: load(\'tab_vazao_top_1_maia.mat\');

\% VA é a Tabela (Matriz) de vazões da topologia 1

VA = \[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 2 2 2 2 2 2 2 0 2 2 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 2 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

2 2 2 2 2 2 0 0 0 0 0 0 0 0 0 2 0 2 2 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 2 0 0 0 0 2 2 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 2 0 0 2 2 2 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 2 0 0 2 0 2 2 2 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 2 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 2
2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 0 2 0 0 0 0 0 2 0 0 0 0 0 0 0
0 2 2 0 0 0 0 2 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 0 2 0 2 0 0 0 2 2 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 2 0 2 0 2 2 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 2 0 0 0 0 2 0 2 2 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 2 0 2 0 0 0 0 0 2 2 2 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 2 0 2 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 2 2 2 2 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 0 0 2 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 2 2 0 0 0 0 2 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 2 2 2 2 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\];

\% O arquivo: \'tab_vazao_top_1_maia.mat\'

\% pode ser gerado através do seguinte comando:

\% save(\'tab_vazao_top_1_maia.mat\',\'VA\');

\% para depois ser carregado usando o comando:

\% load(\'tab_vazao_top_1_maia.mat\');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\% Variável tds da topologia 1

\% carregadas pelo arquivo: \'tab_demanda_aplic_top_1_maia.mat\'

\% no comando: load(\'tab_demanda_aplic_top_1_maia.mat\');

\% tds é a Tabela (Matriz) de demandas das aplicações da topologia 1

tds = \[52 49 0.256000000000000 1000 0;

1 33 0.256000000000000 1000 0;

2 51 1.74400000000000 150 0;

3 50 1.20000000000000 150 5;

4 37 0.256000000000000 1000 0;

31 36 0.256000000000000 1000 0;

32 46 0.256000000000000 1000 0;

5 48 0.512000000000000 150 5;

6 47 0.512000000000000 150 5;

7 34 0.256000000000000 1000 0;

8 44 1.20000000000000 150 5;

9 43 1.20000000000000 150 0;

11 41 0.512000000000000 150 5;

10 42 0.256000000000000 1000 0;

12 40 0.512000000000000 150 5;

13 39 0.256000000000000 1000 0;

30 45 0.256000000000000 1000 0\];

\% O arquivo: \'tab_demanda_aplic_top_1_maia.mat\'

\% pode ser gerado através do seguinte comando:

\% save(\'tab_demanda_aplic_top_1_maia.mat\',\'tds\');

\% para depois ser carregado usando o comando:

\% load(\'tab_demanda_aplic_top_1_maia.mat\');

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

mgrafos14g.m

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\% Matrizes de grafos

%clear all;

%clc;

function\[stds,tm,mrotas,VA,n,tds\] = mgrafos14g(nAnt,MaxIt,top)

tic;

tic;

\% alocando os grafos, demanda de aplicações e valores de largura de
banda e atraso

\% numa matriz de referência

if top == 1

%load(\'top_1_maia_52_65_30.mat\');

load(\'top_1_maia_52_65_30_CordMod.mat\');

load(\'tab_atraso_top_1_maia.mat\');

load(\'tab_demanda_aplic_top_1_maia.mat\');

load(\'tab_vazao_top_1_maia.mat\');

end

if top == 2

%load(\'top_2_NTTnet_57_165.mat\');

load(\'top_2_NTTnet_57_165_CordMod.mat\');

load(\'tab_atraso_top_2_NTTnet.mat\');

%load(\'tab_demanda_aplic_top_2_NTTnet.mat\');

%load(\'tab_demanda_aplic_top_2_NTTnet_2.mat\');

load(\'tab_demanda_aplic_top_2_NTTnet_4.mat\');

load(\'tab_vazao_top_2_NTTnet.mat\');

end

disp(\'\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\')

x = xy(:,1)\';

y = xy(:,2)\';

n=length(x);

D = A;

\% msol = \[64 85 56 81 3 9 67 49 73 46 15 30 13 1 95 39 43\]

mrotas = \[\]; %Matriz de Rotas

\[stds,\~\] = size(tds);

\% loop de rotas para cada aplicacao de tds

for cf = 1:stds

disp(cf);

%nVar = n;

%nAnt=10; % Numero de formigas

Q=1;

Q1=0.5/32; %0.1 % indice de feromonio da largura de banda

Q2=25\*10; %25 % indice de feromonio do atraso de pacotes

%Q1=0.5;

%Q2=25;

tau0=10\*Q/(n\*mean(D(:))); % Feromonio inicial

%tau=tau0\*ones(n,n); % Matriz de Feromonio

tau=tau0\*A; % Matriz de Feromonio

alpha=1; % Peso Exponencial de Feromonio

beta=1; % Peso Exponencial de Heuristica

rho=0.05; % Taxa de evaporacao

eta=1./D; %nij Matriz de Informacao Heuristica

\% P=tau(i,:).\^alpha.\*eta(i,:).\^beta;

dest = tds(cf,2); %destino

orig = tds(cf,1); %origem

rota = orig; % primeira posição da rota

\% tratameto do eta

for i=1:n

for j=1:n

if eta(i,j) == Inf

eta(i,j) = 0;

end

end

end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%nAnt=200; % Numero de formigas

MelhorDistancia = Inf;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

for it=1:MaxIt % Máximo de iteraçoes

VetRotas = zeros(nAnt,n+4);

\% loop de formigas ida

for j = 1:nAnt

%disp(j)

atual = orig;

conti = 1;

while (atual \~= dest)

P = tau(atual,:).\^alpha.\*eta(atual,:).\^beta;

P = P/sum(P);

ds = Roleta(P);

atual = ds;

conti = conti + 1;

%disp(conti);

%disp(cf);

%disp(ds);

rota(1,conti) = ds;

end

tr = length(rota);

l = 1;

while l \<= tr;

%disp(\'tr\')

%disp(tr)

%disp(\'rota\')

%disp(rota)

%disp(\'busca\')

%disp(rota(1,l))

fr = find(rota == rota(1,l));

if \~isempty(fr)

ir = fr(1,end);

rota = horzcat(rota(1,1:l),rota(1,ir+1:tr));

end

tr = length(rota);

l = l + 1;

end

Distancia = FuncDistancia(rota,D);

%disp(Distancia)

if Distancia \< MelhorDistancia

MelhorDistancia=Distancia;

\% disp(\'MD\')

\% disp(Distancia)

end

%disp(\'rota\')

%disp(rota)

tr2 = length(rota);

VetRotas(j,1:tr2) = rota;

VetRotas(j,n+1) = tr2;

VetRotas(j,n+2) = Distancia;

VetRotas(j,n+3) = sum(rota);

VetRotas(j,n+4) = prod(rota);

\% número da rota a ser calculada a mínima vazão e o atraso total

vetvazao = \[\];

vetatraso = \[\];

i = 1;

while i \< tr2

vetvazao(i) = VA(rota(i),rota(i+1));

vetatraso(i) = AT(rota(i),rota(i+1));

i = i + 1;

end

VetRotas(j,n+5) = sum(vetatraso); % atraso total da rota

VetRotas(j,n+6) = min(vetvazao); % vazão mínima da rota

VetRotas(j,n+7) = cf; %??

end

%disp(\'MelhorDistancia\')

%disp(MelhorDistancia)

%{

\[S,I\] = sort(VetRotas(:,14:15));

VetRSel = VetRotas(I(1,2),:);

contsel = 2;

for j = 1:(nAnt-1)

if (S(j,:) \~= S(j+1,:))

VetRSel = VetRotas(I(1,2),:);

contsel = contsel + 2;

end

end

%}

\% loop de formigas volta

for k=1:nAnt

\% disp(\'formiga\')

\% disp(k)

\% disp(VetRotas(k,1:9))

for m=1:(VetRotas(k,n+1)- 1)

i=VetRotas(k,m);

j=VetRotas(k,m+1);

\% Atualizacao do Feromonio

%tau(i,j)=tau(i,j)+Q/VetRotas(k,n+2); % considerando distancia

%tau(i,j)=tau(i,j)+Q1\*tds(cf,3)\*VetRotas(k,n+6)+
Q2\*(tds(cf,3)/100)/VetRotas(k,n+5);%\*tds() % considerando largura de
banda e atraso

tau(i,j)=tau(i,j)+10\*Q1\*tds(cf,3)\*VetRotas(k,n+6);%+
Q2\*(tds(cf,3)/100)/VetRotas(k,n+5);%\*tds() % considerando largura de
banda

%disp(\'teste\')

%disp(\[i j\])

%disp(tau(i,j))

%disp(Q/VetRotas(k,n+2))

end

end

\% Update Phromones

%tau(i,j)=tau(i,j)+Q/ant(k).Cost;

\% Evaporation

tau=(1-rho)\*tau;

%pause();

end

\[S,I\] = sort(VetRotas(:,n+3:n+4));

VetRSel = VetRotas(I(1,1),:);

contacumulated = 1;

contsel = 2;

for j = 1:(nAnt-1)

if (S(j,:) \~= S(j+1,:))

VetRSel(contsel,:) = VetRotas(I(j+1,1),:);

VetRSel(contsel-1,n) = contacumulated;

contacumulated = 0;

contsel = contsel + 1;

end

contacumulated = contacumulated + 1;

end

disp(\'rotas distintas\');

\[lv,\~\] = size(VetRSel);

disp(lv);

VetRSel(lv,n) = nAnt - sum(VetRSel(:,n));

\[\~, I2\]=sort(VetRSel(:,n+2));

VetRSel=VetRSel(I2,:);

%x = \[11 11 2 1; 2, 5, 6, 10\];

%y = \[44 44 1 1; 9 8 11 3\];

disp(\'fase final\')

\% ligando e desligando o gráfico

grafico = 0;

if grafico == 1

figure;

gplot(A,xy)

hold on;

\% muda a cor do grafo a ser plotado

%plotvetx = \[\]

cores = zeros(lv,3);

cores = \[1 0 0;1 1 0;0 1 0;0 1 1;1 0 1;1 1 1;0 0 0;\];

if lv \> 7

for cs = 8:lv

cores(cs,:) = 0.5\*rand(1,3);

end

else

cores = \[1 0 0;1 1 0;0 1 0;0 1 1;1 0 1;1 1 1;0 0 0;\];

end

for j = 1:5%lv % número da rota a serem plotadas

plotvetx = \[\];

plotvety = \[\];

i = 1;

while i \<= n

if VetRSel(j,i)\~= 0

plotvetx(i) = x(VetRSel(j,i));

plotvety(i) = y(VetRSel(j,i));

contsel = contsel + 2;

else

i = n + 1;

end

i = i + 1;

end

plot(plotvetx,plotvety,\'color\',cores(j,:),\'LineWidth\',VetRSel(j,n))

end

title(\'Melhores Rotas\',\'FontSize\',10);

\% escrevendo os nós no gráfico

for i = 1:n

text(x(i),y(i),num2str(i),\'FontSize\',14)

end

\% histograma das distancias

vetresult = zeros(1,n);

for i = 1:n

vetresult(1,i) = length(find(VetRotas(:,n+2)==i));

end

figure;

bar(vetresult);

ylabel(\'número de formigas\',\'FontSize\',10);

xlabel(\'número de nós\',\'FontSize\',10);

title(\'Histograma das Rotas\',\'FontSize\',10);

end

%{

for j = 1:lv % número da rota a ser calculada a mínima vazão e o atraso
total

vetvazao = \[\];

vetatraso = \[\];

i = 1;

while i \<= n-3

if VetRSel(j,i+1)\~= 0

vetvazao(i) = VA(VetRSel(j,i),VetRSel(j,i+1));

vetatraso(i) = AT(VetRSel(j,i),VetRSel(j,i+1));

else

i = n + 1;

end

i = i + 1;

end

VetRSel(j,n-1) = min(vetvazao);

VetRSel(j,n-2) = sum(vetatraso);

end

%}

mrotas = vertcat(mrotas,VetRSel);

disp(cf);

toc;

end

\[tm,\~\] = size(mrotas);

vtm = 1:tm;

mrotas = horzcat(mrotas,vtm\');

toc;

end

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

ACODEeACOAG_14.m

  -----------------------------------------------------------------------
   ACO f   ACO it   AG it    AG pop   N testes Pc       Pm       pCR
  -------- -------- -------- -------- -------- -------- -------- --------
     50    200      200      50       100      0,9      0,9      0,01

  -----------------------------------------------------------------------

Tabela: Var_test13.xlsx

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

%Testes_ACO+DE e ACOAG

%tic;

clear all

tic;

%filename = \'C:\\Users\\joaop\\Desktop\\Trabalhos
Novos\\Var_test13.xlsx\';

%filename = \'C:\\Users\\joaop\\Desktop\\Trabalhos Novos\\Arquivos
Matlab\\Var_test13.xlsx\';

filename = \'C:\\Users\\joaop\\Desktop\\Trabalhos Novos\\Arquivos
Matlab\\Codigos_padronizados\\Var_test13.xlsx\';

%filename = \'C:\\Users\\joaop\\Desktop\\Trabalhos Novos\\Arquivos
Matlab\\Codigos_padronizados\\Var_test15.xlsx\';

VarTest = xlsread(filename);

%Topologias:

%top = 1; %Topologia 1

top = 2; %Topologia 2

\[lvt,\~\] = size(VarTest);

for k = 1:lvt % tipos diferentes de testes a serem realizados

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%Parâmetros de inicialização

nAnt = VarTest(k,1);

MaxIt = VarTest(k,2);

niter = VarTest(k,3);

%niterDE = 200;%800;%VarTest(k,3);

%niterAG = 114;%500;%VarTest(k,3)/1.6;

niterDE = VarTest(k,3);

niterAG = VarTest(k,3);

nPop = VarTest(k,4);

ntests = VarTest(k,5);

%AG

%pc=0.8;

%pm=0.3;

pc = VarTest(k,6);

pm = VarTest(k,7);

%DE

%pCR=0.2;

pCR = VarTest(k,8);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%executar o ACO

%mgrafos11

\% funcao ACO

if k == 1

\[stds,tm,mrotas,VA,n,tds\] = mgrafos14g(nAnt,MaxIt,top);

else

if ((VarTest(k,1) \~= VarTest(k-1,1))&&(VarTest(k,2) \~=
VarTest(k-1,2)))

\[stds,tm,mrotas,VA,n,tds\] = mgrafos14g(nAnt,MaxIt);

end

end

\% valor inicial de rotas aleatorias

rotas_sel = round((tm-1)\*rand(1,stds)+1);

\% funcao de avaliacao

%linkc(rotas_sel,mrotas,VA,n,tds)

%teste

\% linkc(round((tm-1)\*rand(1,stds)+1),mrotas,VA,n,tds)

%executar o AG e DE 100 vezes

%niter = 300; % número de interações dos algoritmos

%ntests = 10; % número de teste realizados

time_ag = zeros(niterAG,ntests);

res_ag = zeros(niterAG,ntests);

time_de = zeros(niterDE,ntests);

res_de = zeros(niterDE,ntests);

aviso = 1;

for i=1:ntests

%tic;

\[BestSol,pop,BestCost,Tempoexec\] =
agaco811(tm,rotas_sel,mrotas,VA,n,tds,niterAG,nPop,pc,pm);

res_ag(1:niterAG,i) = BestCost;

time_ag(1:niterAG,i) = Tempoexec;

%toc;

%tic;

\[BestSol2,pop2,BestCost2,Tempoexec2\] =
deaco311(tm,rotas_sel,mrotas,VA,n,tds,niterDE,nPop,pCR);

res_de(1:niterDE,i) = BestCost2;

time_de(1:niterDE,i) = Tempoexec2;

\% se aviso = 1 o algoritmo para(stop), ao encontrar uma solução ótima.

\% se aviso = 0 o algoritmo prossegue até executar todas as execuções

\% definidas no arquivos .xlsx (excel)

if aviso == 0

if BestCost(niterAG,1) == 132 %valor ótimo da FO

load handel.mat;

sound(y, Fs); % som de aviso

break

end

if BestCost2(niterDE,1) == 132 %valor ótimo da FO

load gong.mat;

sound(y, Fs); % som de aviso

break

end

end

%toc;

end

%{

\[stdsDj,tmDj,mrotasDj,VADj,nDj,tdsDj\] = mgrafos14dijkstra(top);

rsl2 = 1:stds;

\[resfinalDj,vetlinks4Dj,vetpntDj,pfinalDj\] =
linkc6(rsl2,mrotasDj,VA,n,tds,stds,tmDj);

maxrota = max(mrotasDj(:,nDj+1));

mrotasform = zeros(stdsDj,maxrota+4);

mrotasform(:,1:maxrota) = mrotasDj(:,1:maxrota);

mrotasform(:,maxrota+1) = mrotasDj(:,nDj+1);

mrotasform(:,maxrota+2) = mrotasDj(:,nDj+5);

mrotasform(:,maxrota+4) = mrotasDj(:,nDj+7);

\[\~,IDj\] = sort(mrotasform(:,maxrota+3));

mrotasform2 = mrotasform(IDj,:);

mrotasform(:,maxrota+3) = tdsDj(:,4);

%}

%solucoesgerais(:,:,2\*k-1) = res_ag;

%solucoesgerais(:,:,2\*k) = res_de;

solucoesgerais1(:,:,k) = res_ag;

solucoesgerais2(:,:,k) = res_de;

solucoesgerais3(:,:,k) = time_ag;

solucoesgerais4(:,:,k) = time_de;

res_de_m = zeros(niterDE,1);

for i = 1:niterDE

res_de_m(i) = mean(res_de(i,:));

end

res_ag_m = zeros(niterAG,1);

for i = 1:niterAG

res_ag_m(i) = mean(res_ag(i,:));

end

time_de_m = zeros(niterDE,1);

for i = 1:niterDE

time_de_m(i) = mean(time_de(i,:));

end

time_ag_m = zeros(niterAG,1);

for i = 1:niterAG

time_ag_m(i) = mean(time_ag(i,:));

end

\% 1 exec

tf = 30;

figure

plot(res_de(:,1),\'\--b\',\'LineWidth\',4);

grid on;

hold on;

plot(res_ag(:,1),\'r\',\'LineWidth\',4);

djk = ones(niter,1)\*120; % 120 nota de Dijkstra na topologia 1 e 119 na
top 2

plot(djk,\'-.k\',\'LineWidth\',4);

%plot(res_dja_m,\'k\',\'LineWidth\',2);

%plot(res_djd_m,\'g\',\'LineWidth\',2);

xlabel(\'Número de Iterações\',\'FontSize\',tf);

ylabel(\'Média do Valor da Função Objetivo\',\'FontSize\',tf);

title(\'ACO+DE x ACO+AG x Dijkstra\',\'FontSize\',tf);

legend(\'ACO+DE\',\'ACO+AG\',\'Dijkstra\',\'FontSize\',tf,\'Location\',\'southeast\')%
\'southwest\' \'northeast\'

set(gca,\'fontsize\',tf)

%média de 100 exec

tf = 30;

figure

plot(res_de_m,\'\--b\',\'LineWidth\',4);

grid on;

hold on;

plot(res_ag_m,\'r\',\'LineWidth\',4);

djk = ones(niter,1)\*120; % 120 nota de Dijkstra na topologia 1 e 119 na
top 2

plot(djk,\'-.k\',\'LineWidth\',4);

%plot(res_dja_m,\'k\',\'LineWidth\',2);

%plot(res_djd_m,\'g\',\'LineWidth\',2);

xlabel(\'Número de Iterações\',\'FontSize\',tf);

ylabel(\'Média do Valor da Função Objetivo\',\'FontSize\',tf);

title(\'ACO+DE x ACO+AG x Dijkstra\',\'FontSize\',tf);

legend(\'ACO+DE\',\'ACO+AG\',\'Dijkstra\',\'FontSize\',tf,\'Location\',\'southeast\')%
\'southwest\' \'northeast\'

set(gca,\'fontsize\',tf)

%{

figure;

plot(Tempoexec,BestCost,\'r\',\'LineWidth\',2);

grid on;

hold on;

plot(Tempoexec2,BestCost2,\'b\',\'LineWidth\',2);

xlabel(\'Tempo de Execução(seg)\',\'FontSize\',12);

ylabel(\'Valor da Função Objetivo\',\'FontSize\',12);

%title(\'Valor da Função Objetivo x Tempo de
execução\',\'FontSize\',16);

title(\'ACO+DE x ACO+AG\',\'FontSize\',10);

legend(\'ACO+AG\',\'ACO+DE\',\'Location\',\'southwest\')% \'southeast\'
\'northeast\'

%}

\% tempo

tf = 30;

figure

plot(time_de_m,res_de_m,\'\--b\',\'LineWidth\',4);

grid on;

hold on;

plot(time_ag_m,res_ag_m,\'r\',\'LineWidth\',4);

djk = ones(niterDE,1)\*120;

plot(time_de_m,djk,\'-.k\',\'LineWidth\',4);

%plot(res_dja_m,\'k\',\'LineWidth\',2);

%plot(res_djd_m,\'g\',\'LineWidth\',2);

xlabel(\'Tempo Médio de Execução (s)\',\'FontSize\',tf);

ylabel(\'Média do Valor da Função Objetivo\',\'FontSize\',tf);

title(\'ACO+DE x ACO+AG x Dijkstra\',\'FontSize\',tf);

legend(\'ACO+DE\',\'ACO+AG\',\'Dijkstra\',\'FontSize\',tf,\'Location\',\'southeast\')%
\'southwest\' \'northeast\'

set(gca,\'fontsize\',tf)

\% resultado de 1 exec

tf = 30;

figure

plot(time_de(:,ntests),res_de(:,ntests),\'\--b\',\'LineWidth\',4);

grid on;

hold on;

plot(time_ag(:,ntests),res_ag(:,ntests),\'r\',\'LineWidth\',4);

djk = ones(niterDE,1)\*120;

plot(time_de(:,ntests),djk,\'-.k\',\'LineWidth\',4);

%plot(res_dja_m,\'k\',\'LineWidth\',2);

%plot(res_djd_m,\'g\',\'LineWidth\',2);

xlabel(\'Tempo de Execução (s)\',\'FontSize\',tf);

ylabel(\'Valor da Função Objetivo\',\'FontSize\',tf);

title(\'ACO+DE x ACO+AG x Dijkstra\',\'FontSize\',tf);

legend(\'ACO+DE\',\'ACO+AG\',\'Dijkstra\',\'FontSize\',tf,\'Location\',\'southeast\')%
\'southwest\' \'northeast\'

set(gca,\'fontsize\',tf)

%{

disp(\'média, desvio, max e min AG\')

mean2(res_ag)

std2(res_ag)

max(max(res_ag))

min(min(res_ag))

disp(\'média,desvio, max e min DE\')

mean2(res_de)

std2(res_de)

max(max(res_de))

min(min(res_de))

disp(\'média,desvio,max e min AG ultima linha\')

mean(res_ag(end,:))

std(res_ag(end,:))

max(res_ag(end,:))

min(res_ag(end,:))

disp(\'média,desvio,max e min DE ultima linha\')

mean(res_de(end,:))

std(res_de(end,:))

max(res_de(end,:))

min(res_de(end,:))

%}

%toc;

end

load chirp.mat;

sound(y, Fs);

toc;

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

deaco311.m

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

function\[BestSol,pop,BestCost,Tempoexec\] =
deaco311(tm,rotas_sel,mrotas,VA,n,tds,niter,nPop,pCR)

%clc; %rotas_sel,mrotas,VA,n,tds

%clear;

%close all;

tic;

%function\[BestSol,pop\] = de4()

\[stds,\~\] = size(tds); % Tamamho das variaveis

CostFunction=@(rotas_sel) linkc5(rotas_sel,mrotas,VA,n,tds,stds,tm); %
F.O.

\[stds,\~\] = size(tds); % Tamamho das variaveis

nVar=stds; % Numero de variaveis

VarSize=\[1 nVar\]; % Matriz variaveis de decisão

VarMin=1; % valor mínimo da variavel de decisao

VarMax= tm; % valor maximo da variavel de decisao

%%DE Parametros

MaxIt = niter;

TExexc = niter/10; % tempo de execução

%MaxIt=300; % Número of Iterations

%nPop=50; % Tamanho da Populacao

beta_min=0.2; % Menor peso do fator de escala

beta_max=0.8; % Maior peso do fator de escala

%pCR=0.2; % Probabilidade de cruzamento

nplot = 200;

%% Inicializacao

empty_individual.Position=\[\];

empty_individual.Cost=\[\];

BestSol.Cost=-inf;

pop=repmat(empty_individual,nPop,1);

for i=1:nPop

pop(i).Position=round(unifrnd(VarMin,VarMax,VarSize));

pop(i).Cost=CostFunction(pop(i).Position);

if pop(i).Cost\>BestSol.Cost

BestSol=pop(i);

end

end

BestCost=zeros(MaxIt,1);

Tempoexec=zeros(MaxIt,1);

%% DE Loop Principal

for it=1:MaxIt

for i=1:nPop

x=pop(i).Position;

A=randperm(nPop);

A(A==i)=\[\];

a=A(1);

b=A(2);

c=A(3);

\% Mutacao

%beta=unifrnd(beta_min,beta_max);

beta=round(unifrnd(beta_min,beta_max,VarSize));

y=pop(a).Position+beta.\*(pop(b).Position-pop(c).Position);

y = round(y);

y = max(y, VarMin);

y = min(y, VarMax);

\% Cruzamento

z=zeros(size(x));

j0=randi(\[1 numel(x)\]);

for j=1:numel(x)

if j==j0 \|\| rand\<=pCR

z(j)=y(j);

else

z(j)=x(j);

end

end

NewSol.Position=z;

NewSol.Cost=CostFunction(NewSol.Position);

if NewSol.Cost\>pop(i).Cost

pop(i)=NewSol;

if pop(i).Cost\>BestSol.Cost

BestSol=pop(i);

end

end

end

\% Atulizando melhor valor

BestCost(it)=BestSol.Cost;

Tempoexec(it) = toc;

\% Imprimindo informacoes

disp(\[\'Iterações \' num2str(it) \': Função de avaliação = \'
num2str(BestCost(it)) \': Tempo = \' num2str(toc)\]);

%{

if it == nplot

if it == 200

pause(3);

figure;

end

plot(1:it,BestCost(1:it),\'r\',\'LineWidth\',2,\'DisplayName\',\'ACO +
DE\');

%semilogy(BestCost,\'r\',\'LineWidth\',2,\'DisplayName\',\'Função
Objetivo\');

%semilogy(BestCost, \'LineWidth\', 2);

ylabel(\'Valores da Função Objetivo\',\'FontSize\',10);

xlabel(\'Número de Iterações\',\'FontSize\',10);

title(\'Resultados com Restrições\',\'FontSize\',10);

grid on;

hold on;

nplot = nplot + 200;

end

%}

%toc;

end

%{

figure;

plot(BestCost,Tempoexec,\'k\',\'LineWidth\',2);

grid on;

xlabel(\'Tempo de Execução\',\'FontSize\',12);

ylabel(\'Valor da Função Objetivo\',\'FontSize\',12);

title(\'Valor Mínimo da F.O. x Tempo de execução\',\'FontSize\',16);

%}

%toc;

end

%% plotando Resultados

%{

figure;

plot(BestCost,\'r\',\'LineWidth\',2,\'DisplayName\',\'Função
Objetivo\');

%semilogy(BestCost,\'r\',\'LineWidth\',2,\'DisplayName\',\'Função
Objetivo\');

%semilogy(BestCost, \'LineWidth\', 2);

ylabel(\'Valores da Função Objetivo\',\'FontSize\',10);

xlabel(\'Número de Iterações\',\'FontSize\',10);

title(\'Resultados com Restrições\',\'FontSize\',10);

grid on;

%hold on

%plot(1:n,ee1.results\',\'r\',\'LineWidth\',lw,\'DisplayName\',strcat(\'EE -
n =\',num2str(esc)));

%grid on

%plot(1:n,sa1.BestCost,\'b\',\'LineWidth\',lw,\'DisplayName\',strcat(\'SA -
n =\',num2str(esc)));

%plot(1:n,ag1.Mvfo,\'k\',\'LineWidth\',lw,\'DisplayName\',strcat(\'AG -
n = \',num2str(esc)));

%-rs cor original

legend(\'Location\',\'southeast\')

legend(\'show\')

%}

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

agaco811.m

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

function\[BestSol,pop,BestCost,Tempoexec\] =
agaco811(tm,rotas_sel,mrotas,VA,n,tds,niter,nPop,pc,pm)

%clc;

%clear;

%close all;

tic;

%% Problem Definition

\[stds,\~\] = size(tds); % Tamamho das variaveis

CostFunction=@(rotas_sel) linkc5(rotas_sel,mrotas,VA,n,tds,stds,tm); %
F.O.

nVar=stds; % Numero de variaveis

VarSize=\[1 nVar\]; % Decision Variables Matrix Size

VarMin=1; % Lower Bound of Variables

VarMax= tm; % Upper Bound of Variables

%% GA Parameters

MaxIt = niter;

%MaxIt=300; % Maximum Number of Iterations

%nPop=50; % Population Size

%pc=0.8; % Crossover Percentage

nc=2\*round(pc\*nPop/2); % Number of Offsprings (also Parnets)

gamma=0.4; % Extra Range Factor for Crossover

%pm=0.3; % Mutation Percentage

nm=round(pm\*nPop); % Number of Mutants

mu=0.1; % Mutation Rate

%{

ANSWER=questdlg(\'Choose selection method:\',\'Genetic Algorith\',\...

\'Roulette Wheel\',\'Tournament\',\'Random\',\'Roulette Wheel\');

UseRouletteWheelSelection=strcmp(ANSWER,\'Roulette Wheel\');

UseTournamentSelection=strcmp(ANSWER,\'Tournament\');

UseRandomSelection=strcmp(ANSWER,\'Random\');

%}

metodo_sorteio = 1; % Roleta==1, Torneio==2 e Random==3

if metodo_sorteio == 1

beta=8; % Selection Pressure

end

if metodo_sorteio == 2

TournamentSize=3; % Tournamnet Size

end

%pause(0.01); % Due to a bug in older versions of MATLAB

%% Initialization

empty_individual.Position=\[\];

empty_individual.Cost=\[\];

pop=repmat(empty_individual,nPop,1);

for i=1:nPop

\% Initialize Position

\% -\> arrendondar o valor de pop inicial

pop(i).Position=round(unifrnd(VarMin,VarMax,VarSize));

%pop(i).Position=(unifrnd(VarMin,VarMax,VarSize)); %original

\% Evaluation

pop(i).Cost=CostFunction(pop(i).Position);

end

\% Sort Population

\% -\> arrendondar o valor de pop

%round

Costs=\[pop.Cost\];

\[Costs, SortOrder\]=sort(Costs);

pop=pop(SortOrder);

\% Store Best Solution

BestSol=pop(1);

\% Array to Hold Best Cost Values

BestCost=zeros(MaxIt,1);

\% Store Cost

WorstCost=pop(end).Cost;

%% Main Loop

BestCost=zeros(MaxIt,1);

Tempoexec=zeros(MaxIt,1);

for it=1:MaxIt

\% Calculate Selection Probabilities

if metodo_sorteio == 1

P=exp(-beta\*Costs/WorstCost);

P=P/sum(P);

end

\% Crossover

popc=repmat(empty_individual,nc/2,2);

for k=1:nc/2

\% Select Parents Indices

if metodo_sorteio == 1

i1=RouletteWheelSelection(P);

i2=RouletteWheelSelection(P);

end

if metodo_sorteio == 2

i1=TournamentSelection(pop,TournamentSize);

i2=TournamentSelection(pop,TournamentSize);

end

if metodo_sorteio == 3

i1=randi(\[1 nPop\]);

i2=randi(\[1 nPop\]);

end

\% Select Parents

p1=pop(i1);

p2=pop(i2);

\% Apply Crossover

%\[popc(k,1).Position,
popc(k,2).Position\]=round(Crossover(p1.Position,p2.Position,gamma,VarMin,VarMax));

\[popc(k,1).Position,
popc(k,2).Position\]=Crossover2(p1.Position,p2.Position,gamma,VarMin,VarMax);
%original

\% Evaluate Offsprings

popc(k,1).Cost=CostFunction(popc(k,1).Position);

popc(k,2).Cost=CostFunction(popc(k,2).Position);

end

popc=popc(:);

\% Mutation

popm=repmat(empty_individual,nm,1);

for k=1:nm

\% Select Parent

i=randi(\[1 nPop\]);

p=pop(i);

\% Apply Mutation

popm(k).Position=(Mutate2(p.Position,mu,VarMin,VarMax));

\% Evaluate Mutant

popm(k).Cost=CostFunction(popm(k).Position);

end

\% -\> arrendondar o valor de pop

%round

\% Create Merged Population

pop=\[pop

popc

popm\]; %#ok

\% Sort Population

Costs=\[pop.Cost\];

%disp(Costs)

%\[Costs, SortOrder\]=sort(Costs);

\[Costs, SortOrder\]=sort(Costs,\'descend\'); % do maior p/ o menor

%disp(Costs)

pop=pop(SortOrder);

%disp(pop(1).Cost)

%disp(pop(end).Cost)

\% Update Worst Cost

WorstCost=max(WorstCost,pop(end).Cost);

%WorstCost=min(WorstCost,pop(1).Cost); % alteracao pior resultado

\% Truncation

pop=pop(1:nPop);

Costs=Costs(1:nPop);

\% Store Best Solution Ever Found

BestSol=pop(1);

%BestSol=pop(end); % alteracao melhor resultado

\% disp(\'BestSol\')

\% disp(BestSol)

\% disp(\'pause\')

\% pause()

\% Atulizando melhor valor

BestCost(it)=BestSol.Cost;

Tempoexec(it) = toc;

\% Imprimindo informacoes

disp(\[\'Iterações \' num2str(it) \': Função de avaliação = \'
num2str(BestCost(it))\]);

end

%% Results

%{

figure;

plot(BestCost,\'LineWidth\',2);

%semilogy(BestCost,\'LineWidth\',2);

grid on;

xlabel(\'Simulações\',\'FontSize\',12);

ylabel(\'Valor da Função Objetivo\',\'FontSize\',12);

title(\'AG - Valor Mínimo da F.O. a cada simulação\',\'FontSize\',16);

toc;

%}

%plot(BestCost\',\'LineWidth\',2,\'DisplayName\',\'ACO + AG\');

%legend(\'ACO + DE\',\'ACO + AG\')

%{

figure;

plot(BestCost,Tempoexec,\'k\',\'LineWidth\',2);

grid on;

xlabel(\'Tempo de Execução\',\'FontSize\',12);

ylabel(\'Valor da Função Objetivo\',\'FontSize\',12);

title(\'Valor Mínimo da F.O. x Tempo de execução\',\'FontSize\',16);

toc;

%}

end

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

linkc5.m

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

%linkscompartilhados

\% calcula a nota das rotas selecionadas.

function\[pfinal\] = linkc5(rotas_sel,mrotas,VA,n,tds,stds,tm)

%tic;

%disp(tds);

%\[stds,\~\] = size(tds);

%\[tm,\~\] = size(mrotas);

%rotas_sel = round((tm-1)\*rand(1,stds)+1);

%rotas_sel = msol;

%rotas_sel = \[ 1, 25, 47, 59, 63, 77, 98, 112, 132, 151, 176, 186, 189,
195, 204, 210, 228\];

\% tamanho stds

%matlinks = zeros(stds,2\*(max(mrotas(rotas_sel(:),n+1))));

%matlinks2 = mrotas(rotas_sel(:),1:10)

matlinks = zeros(stds,(max(mrotas(rotas_sel(:),n+1))+1));

matlinks(:,1:(max(mrotas(rotas_sel(:),n+1)))) =
mrotas(rotas_sel(:),1:(max(mrotas(rotas_sel(:),n+1))));

\% mrotas(rotas_sel(:),n+1)

%vetconec = zeros(stds,1);

\% busca de links compartilhados por rotas diferentes

\% loop de procura das vazoes das rotas selecionadas

\% tamanho stds

for ii = 1:stds

for jj = 1:stds

if ((tds(jj,1) == matlinks(ii,1)) && (tds(jj,2) ==
matlinks(ii,mrotas(rotas_sel(ii),n+1))))

matlinks(ii,end) = tds(jj,3);

end

end

end

\% número de elementos do vetor de links

mo = (mrotas(rotas_sel(:),n+1) - ones(stds,1));

%nvl = sum((mrotas(rotas_sel(:),n+1) - ones(stds,1)));

nvl = sum(mo);

\% dois links + vazao

vetlinks = zeros(nvl,3);

contlivl = 1;

for ii = 1:stds

jj = 1;

while jj \<= (mrotas(rotas_sel(ii),n+1)-1)

vetlinks(contlivl,1:2) = matlinks(ii,jj:jj+1);

vetlinks(contlivl,3) = matlinks(ii,end);

jj = jj + 1;

contlivl = contlivl + 1;

end

end

vtemp = 0;

for ii = 1:nvl

if(vetlinks(ii,1)\> vetlinks(ii,2))

vtemp = vetlinks(ii,1);

vetlinks(ii,1) = vetlinks(ii,2);

vetlinks(ii,2) = vtemp;

end

end

%\[Av,Iv\] = sort(vetlinks(:,1));

%Rankeando

\[\~,IL\] = sort(vetlinks(:,1));

vetlinks2 = vetlinks(IL,:);

\[\~,IL\] = sort(vetlinks2(:,2));

vetlinks2 = vetlinks2(IL,:);

\[\~,IL\] = sort(vetlinks2(:,1));

vetlinks2 = vetlinks2(IL,:);

vetlinks3 = zeros(nvl,5);

vetlinks3(:,1:3) = vetlinks2;

\% variavel logica indicando primeira vez daquele link repetido

vlk = 0;

for ii = 1:(nvl-1)

if(vetlinks3(ii,1) == vetlinks3(ii+1,1) && vetlinks3(ii,2) ==
vetlinks3(ii+1,2) && vlk == 0)

vlk = ii;

vetlinks3(vlk,4) = vetlinks3(vlk,3) + vetlinks3(vlk+1,3);

vetlinks3(vlk,5) = 2;

else

if (vetlinks3(ii,1) == vetlinks3(ii+1,1) && vetlinks3(ii,2) ==
vetlinks3(ii+1,2))

vetlinks3(vlk,4) = vetlinks3(vlk,4) + vetlinks3(ii+1,3);

vetlinks3(vlk,5) = vetlinks3(vlk,5) + 1;

else

vlk = 0;

%vetlinks3(ii,5) = 1;

end

end

end

vetlinks4 = zeros(nvl,6);

contlivl = 1;

ii = 1;

while ii \<= nvl

if (vetlinks3(ii,5) == 0)

vetlinks4(contlivl,1:3) = vetlinks3(ii,1:3);

vetlinks4(contlivl,4) = 1;

contlivl = contlivl + 1;

else

vetlinks4(contlivl,1:2) = vetlinks3(ii,1:2);

vetlinks4(contlivl,3) = vetlinks3(ii,4);

vetlinks4(contlivl,4) = vetlinks3(ii,5);

contlivl = contlivl + 1;

ii = ii + vetlinks3(ii,5) - 1;

end

ii = ii + 1;

end

pneglargb = 0;

for ij = 1:nvl

if (vetlinks4(ij,1) == 0)

break;

end

vetlinks4(ij,5) = VA(vetlinks4(ij,1),vetlinks4(ij,2));

vetlinks4(ij,6) = vetlinks4(ij,5) - vetlinks4(ij,3);

if vetlinks4(ij,6) \< 0

pneglargb = pneglargb + 1;

end

end

%disp(ij)

vetlinks4 = vetlinks4(1:(ij-1),:);

\% pontuacao relativa às conexões estabelecidas

vetpnt = zeros(1,stds);

for pnt = 1:stds

vetpnt(1,mrotas(rotas_sel(pnt),n+7)) = 1;

end

\% pontuacao relativa ao atraso

pontnegat = 0;

at = 1;

while at \<= stds

\% disp(mrotas(rotas_sel(at),n+5)); disp(\'-\>\');disp(tds(at,4));

if mrotas(rotas_sel(at),n+5) \> tds(at,4)

pontnegat = pontnegat + 1;

end

at = at + 1;

end

pontprior = zeros(stds,3);

pontprior(:,1) = vetpnt\';

pontprior(:,2) = tds(:,5);

pontprior(:,3) = (pontprior(:,2)).\*(pontprior(:,1));

sumpprior = sum(pontprior(:,3));

%pfinal = pontlksucess - pontnegat - pnegprior;

%pfinal = 3\*sum(vetpnt) + stds - pontnegat + sum(tds(:,5)) -
pnegprior + 8\*2 - clk\*2;

\% CP = Conexoes com prioridade

\% C = Conexoes estabelecidas

\% CL = Conexoes com largura de banda suficientes

\% CA = Conexoes sem atraso

\% FO = 5\*(CP) + 3\*(Soma(C)) + 2\*(CL) + 1\*(CA);

pfinal = sumpprior + 3\*sum(vetpnt) + 2\*(stds - pneglargb) + 1\*(stds -
pontnegat);

%disp(\'pfinal\');

%disp(pfinal);

%toc;

end

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

grafico_pos_de_2_subplot.m

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\% ligando e desligando o gráfico

grafico = 1;

if grafico == 1

figure;

gplot(A,xy)

hold on;

\%

x = xy(:,1)\';

y = xy(:,2)\';

\% escrevendo os nós no gráfico

for i = 1:n %n-1 para depois adicionar o zero no lugar do 52

text(xy(i,1),xy(i,2),num2str(i),\'FontSize\',14)

end

\[stds,\~\] = size(tds);

\% muda a cor do grafo a ser plotado

%plotvetx = \[\]

cores = zeros(stds,3);

cores = \[1 0 0;1 1 0;0 1 0; 1 0 1;0.5 0.5 0.5;0.2 0.2
0.2;0.545098039215686 0 0;0.490196078431373 0.149019607843137
0.803921568627451;1 0.270588235294118 0;1 0.925490196078431
0.545098039215686;0.329411764705882 1
0.623529411764706;0.282352941176471 0.462745098039216
1;0.392156862745098 0.584313725490196
0.929411764705882;0.372549019607843 0.619607843137255
0.627450980392157;0 0.392156862745098 0;0.933333333333333
0.231372549019608 0.231372549019608;0.635247068149657 0.217510481741708
0.383218744674291;\];

if stds \> length(cores)

for cs = 9:stds

cores(cs,:) = rand(1,3);%\*\[0;0.5;0.5\];

end

else

cores = \[1 0 0;1 1 0;0 1 0; 1 0 1;0.5 0.5 0.5;0.2 0.2
0.2;0.545098039215686 0 0;0.490196078431373 0.149019607843137
0.803921568627451;1 0.270588235294118 0;1 0.925490196078431
0.545098039215686;0.329411764705882 1
0.623529411764706;0.282352941176471 0.462745098039216
1;0.392156862745098 0.584313725490196
0.929411764705882;0.372549019607843 0.619607843137255
0.627450980392157;0 0.392156862745098 0;0.933333333333333
0.231372549019608 0.231372549019608;0.635247068149657 0.217510481741708
0.383218744674291;\];

%cores = \[1 0 0;1 1 0;0 1 0;0 1 1;1 0 1;0.5 0.5 0.5;0 0 0;\];

end

%msol = \[1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17\];

msol = BestSol.Position; %ans.Position;

%mrotas = mrotasSolOtima1306;

\[\~,I\] = sort(mrotas(:,59));

mrotas = mrotasSolOtima1306(I,:);

mrotasel = \[\];

contmenos = 8; %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

for j = 14:17;%stds%17! % número da rota a serem plotadas

plotvetx = \[\];

plotvety = \[\];

i = 1;

mrotasel = vertcat(mrotasel,mrotas(msol(j),:));

while i \<= n

if mrotas(msol(j),i)\~= 0

plotvetx(i) = x(mrotas(msol(j),i));

plotvety(i) = y(mrotas(msol(j),i));

%contsel = contsel + 2;

else

i = n + 1;

end

i = i + 1;

end

subplot(2,2,j-13)

plot(plotvetx,plotvety,\'color\',cores(j,:),\'LineWidth\',contmenos)%mrotas(msol(j),n+6)

%contmenos = contmenos - 2.5;

hold on;

gplot(A,xy)

\% pause()

\% escrevendo os nós no gráfico

for i = 1:n %n-1 para depois adicionar o zero no lugar do 52 ou n outros
casos

text(x(i),y(i),num2str(i),\'FontSize\',14)

end

title(strcat(\'Rota:\',num2str(j)),\'FontSize\',14);

title(\'Rota\',\'FontSize\',14);

end

%title(\'Rotas\',\'FontSize\',10);

%{

\% escrevendo os nós no gráfico

for i = 1:n %n-1 para depois adicionar o zero no lugar do 52

text(xy(i,1),xy(i,2),num2str(i),\'FontSize\',14)

end

%}

\%

\% escrevendo os nós no gráfico

for i = 1:n %n-1 para depois adicionar o zero no lugar do 52

text(x(i),y(i),num2str(i),\'FontSize\',14)

end

%}

text(x(52),y(52),num2str(0),\'FontSize\',14) % para depois adicionar o
zero no lugar do 52

\%

end

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

FuncDistancia.m

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

function \[L\] = FuncDistancia(rota,D)

n=length(rota);

L=0;

for i=1:n-1

L=L+D(rota(1,i),rota(1,i+1));

end

end

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Crossover2.m

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\% Copyright (c) 2015, Yarpiz (www.yarpiz.com)

\% All rights reserved. Please read the \"license.txt\" for license
terms.

\%

\% Project Code: YPEA101

\% Project Title: Implementation of Real-Coded Genetic Algorithm in
MATLAB

\% Publisher: Yarpiz (www.yarpiz.com)

\%

\% Developer: S. Mostapha Kalami Heris (Member of Yarpiz Team)

\%

\% Contact Info: sm.kalami@gmail.com, info@yarpiz.com

function \[y1, y2\]=Crossover2(x1,x2,gamma,VarMin,VarMax)

alpha=unifrnd(-gamma,1+gamma,size(x1));

y1=alpha.\*x1+(1-alpha).\*x2;

y2=alpha.\*x2+(1-alpha).\*x1;

y1=max(y1,VarMin);

y1=min(y1,VarMax);

y2=max(y2,VarMin);

y2=min(y2,VarMax);

\% arrendondamento

y1 = round(y1);

y2 = round(y2);

end

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Mutate2.m

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

function y=Mutate2(x,mu,VarMin,VarMax)

nVar=numel(x);

nmu=ceil(mu\*nVar);

nmu = 1; % alteração pra evitar erros

j=randsample(nVar,nmu);

sigma=0.1\*(VarMax-VarMin);

%{

disp(\'\[nVar,nmu,j,sigma,x\]\')

disp(nVar)

disp(nmu)

disp(j)

disp(sigma)

disp(x)

%}

y=x;

\% sigma\*randn(size(j))

y(j)=x(j)+sigma\*randn(size(j));

y=max(y,VarMin);

y=min(y,VarMax);

\% arrendondamento

y = round(y);

end

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Roleta.m

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

function j=Roleta(P)

r=rand;

C=cumsum(P);

j=find(r\<=C,1,\'first\');

end

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

mgrafos14dijkstra.m

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

function\[stds,tm,mrotas,VA,n,tds\] = mgrafos14dijkstra(top)

\% Matrizes de grafos

%clear all;

%clc;

\% alocando os grafos, demanda de aplicações e valores de largura de
banda e atraso

\% numa matriz de referência

if top == 1

%load(\'top_1_maia_52_65_30.mat\');

load(\'top_1_maia_52_65_30_CordMod.mat\');

load(\'tab_atraso_top_1_maia.mat\');

load(\'tab_demanda_aplic_top_1_maia.mat\');

load(\'tab_vazao_top_1_maia.mat\');

end

if top == 2

%load(\'top_2_NTTnet_57_165.mat\');

load(\'top_2_NTTnet_57_165_CordMod.mat\');

load(\'tab_atraso_top_2_NTTnet.mat\');

%load(\'tab_demanda_aplic_top_2_NTTnet.mat\');

%load(\'tab_demanda_aplic_top_2_NTTnet_2.mat\');

load(\'tab_demanda_aplic_top_2_NTTnet_4.mat\');

load(\'tab_vazao_top_2_NTTnet.mat\');

end

disp(\'\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\')

x = xy(:,1)\';

y = xy(:,2)\';

n=length(x);

D = A;

%msol = \[234 188 178 207 57 211 73 1 198 128 193 138 159 103 99 52
36\];

\% msol = \[64 85 56 81 3 9 67 49 73 46 15 30 13 1 95 39 43\]

\[costs,paths\] = dijkstra(A,xy);

\[stds,\~\] = size(tds);

%mrotas = \[\]; %Matriz de Rotas

mrotas = zeros(stds,n+7);

\% loop de rotas para cada aplicacao de tds

for cf = 1:stds

disp(cf);

dest = tds(cf,2); %destino

orig = tds(cf,1); %origem

rota = (paths{orig,dest});

%disp(\'rota\')

%disp(rota)

tr2 = length(rota);

mrotas(cf,1:tr2) = rota;

mrotas(cf,n+1) = length(paths{orig,dest});%tr2;

mrotas(cf,n+2) = length(paths{orig,dest})+1;

mrotas(cf,n+3) = sum(rota);

mrotas(cf,n+4) = prod(rota);

\% número da rota a ser calculada a mínima vazão e o atraso total

vetvazao = \[\];

vetatraso = \[\];

i = 1;

while i \< tr2

vetvazao(i) = VA(rota(i),rota(i+1));

vetatraso(i) = AT(rota(i),rota(i+1));

i = i + 1;

end

mrotas(cf,n+5) = sum(vetatraso); % atraso total da rota

mrotas(cf,n+6) = min(vetvazao); % vazão mínima da rota

mrotas(cf,n+7) = cf; % contador do stds ou número da rota procurada

%x = \[11 11 2 1; 2, 5, 6, 10\];

%y = \[44 44 1 1; 9 8 11 3\];

disp(\'fase final\')

end

\[tm,\~\] = size(mrotas);

vtm = 1:tm;

mrotas = horzcat(mrotas,vtm\');

end

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

dijkstra.m

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\% DIJKSTRA Calculate Minimum Costs and Paths using Dijkstra\'s
Algorithm

\%

\% Filename: dijkstra.m

\% Description: Given vertices and edge connections for a graph
(represented by

\% either adjacency matrix or edge list) and edge costs that are greater

\% than zero, this function computes the shortest path from one or more

\% starting nodes to one or more termination nodes.

\% Author:

\% Joseph Kirk

\% jdkirk630@gmail.com

\% Date: 02/27/15

\% Release: 2.0

\%

\% Inputs:

\% \[AorV\] Either A or V where

\% A is a NxN adjacency matrix, where A(I,J) is nonzero (=1)

\% if and only if an edge connects point I to point J

\% NOTE: Works for both symmetric and asymmetric A

\% V is a Nx2 (or Nx3) matrix of x,y,(z) coordinates

\% \[xyCorE\] Either xy or C or E (or E3) where

\% xy is a Nx2 (or Nx3) matrix of x,y,(z) coordinates (equivalent to V)

\% NOTE: only valid with A as the first input

\% C is a NxN cost (perhaps distance) matrix, where C(I,J) contains

\% the value of the cost to move from point I to point J

\% NOTE: only valid with A as the first input

\% E is a Px2 matrix containing a list of edge connections

\% NOTE: only valid with V as the first input

\% E3 is a Px3 matrix containing a list of edge connections in the

\% first two columns and edge weights in the third column

\% NOTE: only valid with V as the first input

\% \[SID\] (optional) 1xL vector of starting points

\% if unspecified, the algorithm will calculate the minimal path from

\% all N points to the finish point(s) (automatically sets SID = 1:N)

\% \[FID\] (optional) 1xM vector of finish points

\% if unspecified, the algorithm will calculate the minimal path from

\% the starting point(s) to all N points (automatically sets FID = 1:N)

\% \[showWaitbar\] (optional) a scalar logical that initializes a
waitbar if nonzero

\%

\% Outputs:

\% \[costs\] is an LxM matrix of minimum cost values for the minimal
paths

\% \[paths\] is an LxM cell array containing the shortest path arrays

\%

\% Note:

\% If the inputs are \[A,xy\] or \[V,E\], the cost is assumed to be (and
is

\% calculated as) the point-to-point Euclidean distance

\% If the inputs are \[A,C\] or \[V,E3\], the cost is obtained from
either

\% the C matrix or from the edge weights in the 3rd column of E3

\%

\% Usage:

\% \[costs,paths\] = dijkstra(A,xy)

\% -or-

\% \[costs,paths\] = dijkstra(A,C)

\% -or-

\% \[costs,paths\] = dijkstra(V,E)

\% -or-

\% \[costs,paths\] = dijkstra(V,E3)

\% -or-

\% \[costs,paths\] = dijkstra( \... ,SID,FID)

\% -or-

\% \[costs,paths\] = dijkstra( \... ,SID,FID,true)

\%

\% Example:

\% % Calculate the (all pairs) shortest distances and paths using
\[A,xy\] inputs

\% n = 7; A = zeros(n); xy = 10\*rand(n,2)

\% tri = delaunay(xy(:,1),xy(:,2));

\% I = tri(:); J = tri(:,\[2 3 1\]); J = J(:);

\% IJ = I + n\*(J-1); A(IJ) = 1

\% \[costs,paths\] = dijkstra(A,xy)

\%

\% Example:

\% % Calculate the (all pairs) shortest distances and paths using
\[A,C\] inputs

\% n = 7; A = zeros(n); xy = 10\*rand(n,2)

\% tri = delaunay(xy(:,1),xy(:,2));

\% I = tri(:); J = tri(:,\[2 3 1\]); J = J(:);

\% IJ = I + n\*(J-1); A(IJ) = 1

\% a = (1:n); b = a(ones(n,1),:);

\% C = round(reshape(sqrt(sum((xy(b,:) - xy(b\',:)).\^2,2)),n,n))

\% \[costs,paths\] = dijkstra(A,C)

\%

\% Example:

\% % Calculate the (all pairs) shortest distances and paths using
\[V,E\] inputs

\% n = 7; V = 10\*rand(n,2)

\% I = delaunay(V(:,1),V(:,2));

\% J = I(:,\[2 3 1\]); E = \[I(:) J(:)\]

\% \[costs,paths\] = dijkstra(V,E)

\%

\% Example:

\% % Calculate the (all pairs) shortest distances and paths using
\[V,E3\] inputs

\% n = 7; V = 10\*rand(n,2)

\% I = delaunay(V(:,1),V(:,2));

\% J = I(:,\[2 3 1\]);

\% D = sqrt(sum((V(I(:),:) - V(J(:),:)).\^2,2));

\% E3 = \[I(:) J(:) D\]

\% \[costs,paths\] = dijkstra(V,E3)

\%

\% Example:

\% % Calculate the shortest distances and paths from the 3rd point to
all the rest

\% n = 7; V = 10\*rand(n,2)

\% I = delaunay(V(:,1),V(:,2));

\% J = I(:,\[2 3 1\]); E = \[I(:) J(:)\]

\% \[costs,paths\] = dijkstra(V,E,3)

\%

\% Example:

\% % Calculate the shortest distances and paths from all points to the
2nd

\% n = 7; A = zeros(n); xy = 10\*rand(n,2)

\% tri = delaunay(xy(:,1),xy(:,2));

\% I = tri(:); J = tri(:,\[2 3 1\]); J = J(:);

\% IJ = I + n\*(J-1); A(IJ) = 1

\% \[costs,paths\] = dijkstra(A,xy,1:n,2)

\%

\% Example:

\% % Calculate the shortest distance and path from points \[1 3 4\] to
\[2 3 5 7\]

\% n = 7; V = 10\*rand(n,2)

\% I = delaunay(V(:,1),V(:,2));

\% J = I(:,\[2 3 1\]); E = \[I(:) J(:)\]

\% \[costs,paths\] = dijkstra(V,E,\[1 3 4\],\[2 3 5 7\])

\%

\% Example:

\% % Calculate the shortest distance and path between two points

\% n = 1000; A = zeros(n); xy = 10\*rand(n,2);

\% tri = delaunay(xy(:,1),xy(:,2));

\% I = tri(:); J = tri(:,\[2 3 1\]); J = J(:);

\% D = sqrt(sum((xy(I,:)-xy(J,:)).\^2,2));

\% I(D \> 0.75,:) = \[\]; J(D \> 0.75,:) = \[\];

\% IJ = I + n\*(J-1); A(IJ) = 1;

\% \[cost,path\] = dijkstra(A,xy,1,n)

\% gplot(A,xy,\'k.:\'); hold on;

\% plot(xy(path,1),xy(path,2),\'ro-\',\'LineWidth\',2); hold off

\% title(sprintf(\'Distance from %d to %d = %1.3f\',1,n,cost))

\%

\% Web Resources:

\% \<a
href=\"http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm\"\>Dijkstra\'s
Algorithm\</a\>

\% \<a
href=\"http://en.wikipedia.org/wiki/Graph\_%28mathematics%29\"\>Graphs\</a\>

\% \<a href=\"http://en.wikipedia.org/wiki/Adjacency_matrix\"\>Adjacency
Matrix\</a\>

\%

\% See also: gplot, gplotd, gplotdc, distmat, ve2axy, axy2ve

\%

function \[costs,paths\] = dijkstra(AorV,xyCorE,SID,FID,showWaitbar)

narginchk(2,5);

\% Process inputs

\[n,nc\] = size(AorV);

\[m,mc\] = size(xyCorE);

if (nargin \< 3)

SID = (1:n);

elseif isempty(SID)

SID = (1:n);

end

L = length(SID);

if (nargin \< 4)

FID = (1:n);

elseif isempty(FID)

FID = (1:n);

end

M = length(FID);

if (nargin \< 5)

showWaitbar = (n \> 1000 && max(L,M) \> 1);

end

\% Error check inputs

if (max(SID) \> n \|\| min(SID) \< 1)

eval(\[\'help \' mfilename\]);

error(\'Invalid \[SID\] input. See help notes above.\');

end

if (max(FID) \> n \|\| min(FID) \< 1)

eval(\[\'help \' mfilename\]);

error(\'Invalid \[FID\] input. See help notes above.\');

end

\[E,cost\] = process_inputs(AorV,xyCorE);

\% Reverse the algorithm if it will be more efficient

isReverse = false;

if L \> M

E = E(:,\[2 1\]);

cost = cost\';

tmp = SID;

SID = FID;

FID = tmp;

isReverse = true;

end

\% Initialize output variables

L = length(SID);

M = length(FID);

costs = zeros(L,M);

paths = num2cell(NaN(L,M));

\% Create a waitbar if desired

if showWaitbar

hWait = waitbar(0,\'Calculating Minimum Paths \... \');

end

\% Find the minimum costs and paths using Dijkstra\'s Algorithm

for k = 1:L

\% Initializations

iTable = NaN(n,1);

minCost = Inf(n,1);

isSettled = false(n,1);

path = num2cell(NaN(n,1));

I = SID(k);

minCost(I) = 0;

iTable(I) = 0;

isSettled(I) = true;

path(I) = {I};

\% Execute Dijkstra\'s Algorithm for this vertex

while any(\~isSettled(FID))

\% Update the table

jTable = iTable;

iTable(I) = NaN;

nodeIndex = find(E(:,1) == I);

\% Calculate the costs to the neighbor nodes and record paths

for kk = 1:length(nodeIndex)

J = E(nodeIndex(kk),2);

if \~isSettled(J)

c = cost(I,J);

empty = isnan(jTable(J));

if empty \|\| (jTable(J) \> (jTable(I) + c))

iTable(J) = jTable(I) + c;

if isReverse

path{J} = \[J path{I}\];

else

path{J} = \[path{I} J\];

end

else

iTable(J) = jTable(J);

end

end

end

\% Find values in the table

K = find(\~isnan(iTable));

if isempty(K)

break

else

\% Settle the minimum value in the table

\[\~,N\] = min(iTable(K));

I = K(N);

minCost(I) = iTable(I);

isSettled(I) = true;

end

end

\% Store costs and paths

costs(k,:) = minCost(FID);

paths(k,:) = path(FID);

if showWaitbar && \~mod(k,ceil(L/100))

waitbar(k/L,hWait);

end

end

if showWaitbar

delete(hWait);

end

\% Reformat outputs if algorithm was reversed

if isReverse

costs = costs\';

paths = paths\';

end

\% Pass the path as an array if only one source/destination were given

if L == 1 && M == 1

paths = paths{1};

end

\%
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

function \[E,C\] = process_inputs(AorV,xyCorE)

if (n == nc)

if (m == n)

A = AorV;

A = A - diag(diag(A));

if (m == mc)

\% Inputs = (A,cost)

C = xyCorE;

E = a2e(A);

else

\% Inputs = (A,xy)

xy = xyCorE;

E = a2e(A);

D = ve2d(xy,E);

C = sparse(E(:,1),E(:,2),D,n,n);

end

else

eval(\[\'help \' mfilename\]);

error(\'Invalid \[A,xy\] or \[A,C\] inputs. See help notes above.\');

end

else

if (mc == 2)

\% Inputs = (V,E)

V = AorV;

E = xyCorE;

D = ve2d(V,E);

C = sparse(E(:,1),E(:,2),D,n,n);

elseif (mc == 3)

\% Inputs = (V,E3)

E3 = xyCorE;

E = E3(:,1:2);

C = sparse(E(:,1),E(:,2),E3(:,3),n,n);

else

eval(\[\'help \' mfilename\]);

error(\'Invalid \[V,E\] or \[V,E3\] inputs. See help notes above.\');

end

end

end

end

\% Convert adjacency matrix to edge list

function E = a2e(A)

\[I,J\] = find(A);

E = \[I J\];

end

\% Compute Euclidean distance for edges

function D = ve2d(V,E)

VI = V(E(:,1),:);

VJ = V(E(:,2),:);

D = sqrt(sum((VI - VJ).\^2,2));

end

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

CodigosCurl2.m

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

%Matriz de Adjacencia das portas de comunicação entre os Hosts e
Switches

C = \...

\[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 1 2 3 4 5 6 7 0 8 9 0 0 0 10 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 3 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 2 0 0 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

1 2 3 4 5 6 0 0 0 0 0 0 0 0 0 8 0 9 10 0 0 0 0 0 11 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 7;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 1 2 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 2 0 0 3 4 5 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 2 0 0 3 0 4 5 6 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 3 0 0 0 0 4 0 5 0 0 0 0 0 0 0 0 0 0 0 0 0 2
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 4 5 0 6 0 0 0 0 0 7 0 0 0 0 0 0 0
0 1 2 0 0 0 0 3 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 2 0 3 0 4 0 0 0 5 6 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 2 0 3 0 4 5 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 2 0 0 0 0 3 0 4 5 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0 5 0 6 0 0 0 0 0 1 2 3 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 5 6 7 0 8 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 2 3 4 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 4 5 0 0 6 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 2 0 0 0 0 3 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 5 6 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 2 3 4 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;\...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\];

\%

%Dados a serem alterados no arquivo JSON: switch, ip origem, ip dst, N.
do fluxo, porta de saída

%Exemplo \[17,52,49,1,9\];

load(\'top_1_maia_52_65_30_CordMod.mat\')

tic;

\% Algoritmo de Djikstra

\[costs,paths\] = dijkstra(A,xy);

toc;

%{

vet_sol = \[1 52 17 18 26 27 49 0 0 0 0 6;2 1 17 25 27 26 33 0 0 0 0 6;3
2 17 25 24 28 51 0 0 0 0 6;\...

4 3 17 16 20 19 23 24 27 50 0 9;5 4 17 18 26 27 28 23 22 21 37 10;6 31
18 26 27 24 23 22 21 36 0 9;\...

7 32 18 17 19 23 28 46 0 0 0 7;8 5 17 18 26 27 48 0 0 0 0 6;9 6 17 19 23
24 27 47 0 0 0 7;\...

10 7 14 20 19 17 18 26 34 0 0 8;11 8 14 20 22 44 0 0 0 0 0 5;12 9 14 15
21 22 29 43 0 0 0 7;\...

13 11 14 16 20 23 29 41 0 0 0 7;14 10 14 20 23 22 29 42 0 0 0 7;15 12 14
15 21 20 23 29 40 0 0 8;\...

16 13 14 20 21 22 39 0 0 0 0 6;17 30 15 21 20 19 24 28 45 0 0 8\];

tsol = 17; % tamanho da solução em linhas

%}

rotas_otimizadas = 1;

if (rotas_otimizadas == 1)

vet_sol =\[1 52 17 18 26 27 49 0 0 0 0 6;\...

2 1 17 25 27 26 33 0 0 0 0 6;\...

3 2 17 25 24 28 51 0 0 0 0 6;\...

4 3 17 16 20 19 23 24 27 50 0 9;\...

5 4 17 18 26 27 28 23 22 21 37 10;\...

6 31 18 26 27 24 23 22 21 36 0 9;\...

7 32 18 17 19 23 28 46 0 0 0 7;\...

8 5 17 18 26 27 48 0 0 0 0 6;\...

9 6 17 19 23 24 27 47 0 0 0 7;\...

10 7 14 20 19 17 18 26 34 0 0 8;\...

11 8 14 20 22 44 0 0 0 0 0 5;\...

12 9 14 15 21 22 29 43 0 0 0 7;\...

13 11 14 16 20 23 29 41 0 0 0 7;\...

14 10 14 20 23 22 29 42 0 0 0 7;\...

15 12 14 15 21 20 23 29 40 0 0 8;\...

16 13 14 20 21 22 39 0 0 0 0 6;\...

17 30 15 21 20 19 24 28 45 0 0 8\];

tsol = length(vet_sol);

n=length(xy);

disp(\'aqui\');

%djkc = cell(n,n);

%djkc(:,:) = num2cell(zeros(n,n));

for i = 1:tsol;

%djkc(vet_sol(i,2),vet_sol(i,vet_sol(i,end)+1)) =
{vet_sol(i,2:vet_sol(i,end)+1)};

paths(vet_sol(i,2),vet_sol(i,vet_sol(i,end)+1)) =
{vet_sol(i,2:vet_sol(i,end)+1)};

end

end

\% descobrir o tamanho máximo do vetor de rotas de Djikstra

tic;

mlg = 1;

ctr = 1;

for i = 1:n

for j = 1:n

lg = length(paths{i,j});

if (lg \> mlg )

mlg = lg;

end

ctr = ctr + 1;

end

end

toc;

\% construir o vetor com as rotas de Djikstra

rotas = zeros(n\*(n-1),mlg+1);

tic;

ctr = 1;

for i = 1:n

for j = 1:n

if (j \~= i)

lg = length(paths{i,j});

rotas(ctr,1) = ctr;

rotas(ctr,2:lg+1) = paths{i,j};

rotas(ctr,mlg+2) = lg;

ctr = ctr + 1;

end

end

end

toc;

fileID = fopen(\'7388json52_Otimiz1.txt\',\'w\');

vet_sol = rotas;

tsol = length(rotas);

tic;

ctt = 1;

cf = 1;

while ctt \<= tsol

ctt2 = 3;

while ctt2 \<= vet_sol(ctt,end)

str1 = strcat(\'curl -X POST -d
\'\'{\"switch\":\"00:00:00:00:00:00:00:\',num2str(vet_sol(ctt,ctt2)),\...

\'\", \"ipv4_src\":\"10.0.1.\',num2str(vet_sol(ctt,2)),\...

\'\",\"eth_type\":\"0x0800\",\"ipv4_dst\":\"10.0.1.\',num2str(vet_sol(ctt,(vet_sol(ctt,end)+1))),\...

\'\", \"name\":\"flow-mod-\',num2str(cf),\...

\'\", \"cookie\":\"0\",
\"priority\":\"32768\",\"active\":\"true\",\"actions\":\"output=\',num2str(C(vet_sol(ctt,ctt2),vet_sol(ctt,ctt2+1))),\...

\'\"}\'\' http://192.168.56.101:8080/wm/staticentrypusher/json\');

fprintf(fileID,strcat(str1,\'\\r\\n\'));

%disp(str1)

ctt2 = ctt2 + 1;

cf = cf + 1;

end

ctt = ctt + 1;

end

fclose(fileID);

toc;
