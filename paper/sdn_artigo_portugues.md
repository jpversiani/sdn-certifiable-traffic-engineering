# Meta-heurísticas Híbridas de Colônia de Formigas para Otimização de Engenharia de Tráfego com Requisitos de QoS em Redes Definidas por Software: Formulação, Simulação e Validação em Bancada Experimental

**Autores:** João Paulo Versiani Ladeia e Nilton Alves Maia  
**Filiação:** Programa de Pós-Graduação em Modelagem Computacional e Sistemas (PPGMCS), Universidade Estadual de Montes Claros (Unimontes), Montes Claros – MG, Brasil.  
**Formato:** Padrão IEEE (duas colunas) / Submissão Nacional e Internacional.

---

## Resumo
A proliferação de aplicações multimídia, serviços em nuvem e fluxos de dados massivos impõe rígidos requisitos de Qualidade de Serviço (QoS) às infraestruturas modernas de comunicação. Protocolos de roteamento tradicionais baseados em métricas de menor caminho (como OSPF e IS-IS) sobrecarregam frequentemente enlaces centrais críticos, enquanto rotas alternativas permanecem subutilizadas, provocando retenção severa em filas (*bufferbloat*), perda de pacotes e variação no atraso (*jitter*). As Redes Definidas por Software (SDN) superam tais limitações por meio do desacoplamento e centralização lógica do plano de controle, viabilizando a implementação de Engenharia de Tráfego (TE) dinâmica no nível de fluxos. 

Neste trabalho, formulamos o problema de roteamento com QoS de múltiplos fluxos simultâneos em SDN como um modelo de otimização combinatória restrito por limites de atraso fim-a-fim, capacidade de banda dos enlaces e prioridades diferenciadas de aplicação. Para solucionar este problema NP-difícil, propomos um framework meta-heurístico híbrido em dois estágios: primeiro, o Algoritmo de Colônia de Formigas (ACO), baseado nos princípios do AntNet, explora a topologia e constrói um conjunto diversificado de rotas candidatas sem ciclos; em seguida, o Algoritmo Genético (ACO+AG) ou a Evolu\c{c}ão Diferencial (ACO+DE) executa a seleção combinatória global para definir a alocação ótima de rotas. 

Conduzimos uma avaliação dupla: benchmarks algorítmicos frente aos algoritmos de Dijkstra e CSPF sob múltiplos regimes de carga, combinados com a validação empírica em uma bancada de emulação OpenFlow com 52 switches orquestrados pelo controlador Floodlight e tráfego injetado via D-ITG. Nos testes com 17 aplicações concorrentes, a rede otimizada obteve vazão média 34,45% superior, atraso fim-a-fim médio 51,19 vezes menor (reduzindo a latência acumulada por bufferbloat de 10,80 s para 0,21 s), jitter 7,49 vezes menor e perda de pacotes 510,4 vezes inferior em relação ao roteamento por menor caminho. Testes de estresse de carga confirmam que o otimizador híbrido mantém a ocupação de banda abaixo de 100% sob regimes intensos de tráfego, nos quais abordagens gulosas e de menor caminho sofrem saturação aguda.

**Palavras-chave:** Redes Definidas por Software (SDN), Engenharia de Tráfego (TE), Qualidade de Serviço (QoS), Otimização por Colônia de Formigas (ACO), Algoritmo Genético (AG), Evolução Diferencial (DE), Bufferbloat, Mininet, OpenFlow.

---

## 1. Visão Geral dos Resultados

### 1.1 Tabela de Aptidão Algorítmica (Topologia de 52 Nós)
| Algoritmo de Roteamento | Valor da Função Objetivo ($\mathrm{FO}$) | Enlaces Saturados (> 100%) | Status da Solução |
| :--- | :---: | :---: | :---: |
| **Dijkstra (Menor Caminho)** | 120,0 | 6 | Sub-ótima (Saturação) |
| **Baseline Aleatório** | 112,0 | 10 | Inviável |
| **CSPF (Guloso Sequencial)** | 132,0 | 0 | Ótima (Carga nominal) |
| **ACO + DE** | 132,0 | 0 | **Ótimo Global** |
| **ACO + AG** | **132,0** | **0** | **Ótimo Global** |

### 1.2 Resultados Médios Consolidados na Bancada Experimental (Mininet + Floodlight + D-ITG)
| Métrica Avaliada | Rede Otimizada (ACO+AG) | Rede Dijkstra (Baseline) | Melhoria / Fator de Ganho |
| :--- | :---: | :---: | :---: |
| **Vazão Média (kbps)** | **517,33 ± 371,90** | 384,76 ± 349,31 | **+34,45%** |
| **Atraso Fim-a-Fim Médio (s)** | **0,2109 ± 0.1842** | 10,7962 ± 18,2415 | **51,19× menor** (*Bufferbloat mitigado*) |
| **Jitter Médio (s)** | **0,0093 ± 0,0068** | 0,0697 ± 0,1412 | **7,49× menor** |
| **Perda de Pacotes Média (%)** | **0,0168 ± 0,0364** | 8,5747 ± 15,0033 | **510,4× menor** |

---

## 2. Documentos Gerados
- **Artigo Completo em Português (PDF):** `paper/sdn_artigo_portugues.pdf` (7 páginas, formato IEEE de 2 colunas).
- **Código-fonte LaTeX em Português:** `paper/sdn_artigo_portugues.tex`.
- **Artigo Completo em Inglês (PDF):** `paper/sdn_traffic_engineering.pdf` (7 páginas, formato IEEE Transactions / Access).
- **Código-fonte LaTeX em Inglês:** `paper/sdn_traffic_engineering.tex`.
- **Base BibTeX Completa (30 referências):** `paper/sdn_references.bib`.
- **Figuras em Alta Resolução (PDF e PNG):** `paper/figures/`.
