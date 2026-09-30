# Registro de Evolutivas do Projeto: Engenharia de Tráfego Otimizada em Redes SDN

**Autor:** João Paulo Versiani Ladeia (`jpversiani` - joaopauloversiani@hotmail.com)  
**Orientador:** Prof. Dr. Nilton Alves Maia  
**Instituição:** Universidade Estadual de Montes Claros (Unimontes) — Programa de Pós-Graduação em Modelagem Computacional e Sistemas (PPGMCS)  
**Data:** 30 de setembro de 2026  

---

## 1. Visão Geral e Trajetória do Projeto

O projeto teve início com a dissertação de mestrado *"Otimização Aplicada ao Problema de Engenharia de Tráfego em Redes Definidas por Software"* (Unimontes, 2018). O objetivo atual é modernizar, expandir e certificar formalmente os modelos e experimentos para submissão e publicação em periódicos científicos internacionais de alto impacto (**IEEE Access**, **Computer Communications / Elsevier** ou **IEEE Latin America Transactions**).

---

## 2. Linha do Tempo e Marcos Evolutivos

### 📌 Fase 1: Resgate Histórico e Revalidação Empírica (v1)
* **Resgate dos Dados Reais da Dissertação (2018):**
  * Extração e estruturação dos dados experimentais medidos na bancada física emulada (**Mininet 2.2 + Floodlight OpenFlow Controller + D-ITG Traffic Generator**).
  * Topologia de referência `maia52` (52 nós, 66 enlaces, 17 fluxos de aplicações com classes de QoS heterogêneas).
* **Portabilidade e Reprodução Python:**
  * Implementação modular dos algoritmos: Otimização por Colônia de Formigas (AntNet/ACO) para geração de pools de rotas candidatas e Algoritmo Genético (GA) / Evolução Diferencial (DE) para seleção combinatória de caminhos.
  * Confirmação da Função Objetivo clássica ($\mathrm{FO} = 120$ para o baseline Dijkstra vs $\mathrm{FO} = 132$ para a metaheurística híbrida ACO+AG).
* **Geração do Manuscrito Base:** Criação das primeiras versões estruturadas em LaTeX formato IEEE de duas colunas (`sdn_traffic_engineering.tex` e `sdn_artigo_portugues.tex`).

---

### 📌 Fase 2: Modernização Metodológica e Resposta ao Parecer GLM 5.3 Flash (v2)
Com base em avaliação crítica rigorosa de pareceristas de transações IEEE, o projeto foi submetido a uma profunda reformulação conceitual e experimental:

1. **Resolução da Paridade CSPF via *Pool Augmentation*:**
   * A rota do caminho mais curto com restrição de capacidade (CSPF) foi injetada no pool de candidatos de cada fluxo (`sdn/loadmodel.py`).
   * O seletor metaheurístico passa a ser garantidamente **$\ge \mathrm{CSPF}$ por construção**, superando o CSPF sob estresse de carga.
2. **Formulação Matemática com Restrições Duras e Min-Max:**
   * Restrições estritas de capacidade de enlace e atraso máximo por fluxo, com objetivo explícito de balanceamento: minimização da utilização máxima de enlace ($\min Z = \max_{(i,j)} u_{ij}$).
3. **Certificação Exata com Programação Linear Inteira (ILP via HiGHS):**
   * **ILP-P (Pool Exact):** Certificação de que o ACO+AG atinge o ótimo exato do seu espaço de busca ($gap = 0$ em 20/20 sementes na carga nominal).
   * **ILP-L (Binary Multi-Commodity Flow):** Determinação dos limites inferiores físicos de gargalo de enlace na topologia inteira.
4. **Rigor Estatístico em Larga Escala:**
   * Avaliação em 3 topologias (`maia52`, `waxman52`, `gridcore`) $\times$ 5 fatores de carga $\times$ 20 sementes aleatórias com Intervalos de Confiança de 95% (t-Student) e testes pareados não-paramétricos de **Wilcoxon**.
5. **Paradigmas Tecnológicos Contemporâneos (2024–2026):**
   * **Segment Routing sobre IPv6 (SRv6):** Contabilidade de estado demonstrando redução de $2{,}0\times$ a $4{,}2\times$ no número de regras de fluxo dos comutadores intermediários.
   * **Diferenciação de Classes / 5G Network Slicing:** Avaliação em nível de pacote demonstrando manutenção de SLA de 150 ms para fluxos sensíveis a atraso até $2\times$ de tráfego de fundo.
   * **Comparativo com Aprendizado por Reforço:** Implementação de baseline Q-learning demonstrando vulnerabilidade a infactibilidade em topologias esparsas ($40\%$ de falha).
6. **Curvas Dinâmicas de Convergência da FO:**
   * Resgate da dinâmica geracional da Função Objetivo ao longo de 300 gerações com bandas de confiança sombreadas de 95% e teste de ablação (com vs. sem ampliação de pool).

---

### 📌 Fase 3: Refinamento de Rigor Científico e Validação em Backbones Reais (v3 / `sdn_cc_manuscript`)
A partir da consolidação do parecer **GPT 6.1 Sol (30-09-2026)**, foram implementadas melhorias de precisão científica de ponta:

1. **Validação em Backbones Reais de Pesquisa:**
   * Inclusão de redes reais públicas do SNDlib e Internet Topology Zoo: **GEANT2012** (37 nós, 116 enlaces) e **Germany50** (50 nós, 176 enlaces), com coordenadas geográficas, distâncias reais e latências calculadas por propagação em fibra óptica.
2. **Otimização Lexicográfica do ILP (Eliminação de Distorção por Pesos):**
   * Resolução do modelo exato estritamente em duas etapas sequenciais: primeiro minimização pura do gargalo $\min Z$, seguida por desempate de atraso com $Z$ fixado no valor ótimo. Isso garante a exatidão formal dos limites inferiores certificados.
3. **Calibração e Honestidade das Alegações Científicas:**
   * Eliminação de afirmações absolutas infundadas (ex: substituição de "zero violações em toda varredura" pelas taxas reais de factibilidade medidas sob estresse).
   * Precisão na nomenclatura: "fluxos sensíveis a atraso mapeados à classe de serviço" em vez de "URLLC nativo em hardware"; "contabilidade computada de regras" em vez de "medição de TCAM física"; "crescimento de sessões concorrentes" para os cenários $f > 1$.
4. **Geração do Novo Manuscrito de Submissão:**
   * Elaboração de `paper/sdn_cc_manuscript.tex` e compilação do `sdn_cc_manuscript.pdf`, pronto e direcionado para periódicos como *Computer Communications* / *IEEE Access*.

---

## 3. Estrutura do Repositório

```text
├── data/
│   └── backbones/               # Topologias reais GML (GEANT, Germany50, Nobel-EU, etc.)
├── experiments/                 # Scripts da pipeline experimental automatizada (exp1 a exp10b)
├── output/                      # Relatórios e exportações de dados
├── paper/                       # Fontes LaTeX, figuras e PDFs compilados
│   ├── figures/                 # Gráficos em alta resolução (EN)
│   ├── figures/pt/              # Gráficos traduzidos e adaptados (PT)
│   ├── sdn_cc_manuscript.tex    # Manuscrito v3 (Computer Communications / IEEE Access)
│   ├── sdn_cc_manuscript.pdf    # PDF compilado do manuscrito v3
│   ├── sdn_traffic_engineering_v2.tex # Manuscrito v2 em inglês (IEEEtran)
│   ├── sdn_traffic_engineering_v2.pdf # PDF compilado do manuscrito v2 em inglês
│   ├── sdn_artigo_portugues_v2.tex    # Manuscrito v2 em português (IEEEtran)
│   └── sdn_artigo_portugues_v2.pdf    # PDF compilado do manuscrito v2 em português
├── results/                     # Resultados numéricos, pools ACO, JSONs, tabelas e macros LaTeX
├── sdn/                         # Módulos centrais dos algoritmos (ACO, GA, DE, ILP, CSPF, Q-Learn)
├── EVOLUTIVAS_DO_PROJETO.md     # Este documento de registro histórico e técnico
├── README.md                    # Instruções de reprodução e arquitetura do software
└── requirements.txt             # Dependências do ambiente Python
```

---

## 4. Status de Prontidão para Submissão

* **Artigo Principal em Inglês (Refinado v3):** `paper/sdn_cc_manuscript.pdf`
* **Artigo Completo em Português:** `paper/sdn_artigo_portugues_v2.pdf`
* **Pipeline de Reprodutibilidade:** 100% automatizada e verificada via scripts em `experiments/`.
