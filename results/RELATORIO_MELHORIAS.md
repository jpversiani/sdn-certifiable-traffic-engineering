# Relatório de Modernização — Artigo IEEE v2

## O que foi aplicado (mapeado do parecer de revisão)

| # | Melhoria (do parecer) | Status | Onde |
|---|----------------------|--------|------|
| W1/P0-1 | Comparação justa com baseline forte | ✅ CSPF implementado e avaliado; resultado honesto: CSPF atinge FO ótimo no cenário nominal — paper reporta com transparência | `sdn/cspf.py`, sweep |
| W1/P0-1b | Resposta ao "por que não CSPF?" | ✅ **Pool augmentation**: rota CSPF injetada no bloco de cada fluxo → seletor garantidamente ≥ CSPF por construção | `sdn/loadmodel.py::augment_pool_with_cspf` |
| W2/P0-2 | Modelo revisado | ✅ Restrições duras (capacidade/atraso) + objetivo min-max utilization; FO original mantida para continuidade | `sdn/metrics.py`, Eq. 7–9 do paper |
| P0-1c | Certificação exata | ✅ ILP-P (ótimo exato do pool, certifica gap=0 do híbrido) + ILP-L (MCF binário exato, certifica limites inferiores do gargalo Z*) | `sdn/ilp.py` (HiGHS/PuLP) |
| P0-3 | Escala e rigor estatístico | ✅ 3 topologias × 5 cargas × 20 seeds; IC 95% (t-Student) + Wilcoxon pareado | `experiments/exp2_sweep.py`, `sdn/stats_tools.py` |
| W3 | Modelo de carga corrigido | ✅ f≤1 escala demandas; f>1 **adiciona fluxos concorrentes** (crescimento realista, sem overshoot trivial por fluxo) | `sdn/loadmodel.py::loaded_topology` |
| W3 | Metodologia de simulação documentada | ✅ Filas/parâmetros idênticos reportados; sim-vs-bancada reconciliado (bufferbloat = artefato do baseline) | paper §Reconciling |
| P1-5a | SRv6 medido | ✅ Contagem real de regras: 17 SRv6 vs 34–71 OpenFlow (redução 2,0–4,2×), overhead SRH 4–10 SIDs (≤208 B) | `sdn/srv6_state.py`, exp4 |
| P1-5b | Isolamento de fatias | ✅ URLLC mantém SLA 150 ms até background ×2 com roteamento otimizado; Dijkstra viola em todos os níveis | exp3, fig10 |
| P2-6 | Baseline de aprendizado | ✅ Q-learning tabular (estrutura DQN-like) sob mesmo protocolo: igual ao ótimo em topologias densas, falha factibilidade na esparsa (40%) — evidência medida para a cautela DRL | `sdn/qlearn.py` |
| P2-7 | Bibliografia 2020–2025 | ✅ RFCs 8402/8754/8986/9256/4655, 3GPP TS 23.501, ITU-R M.2083, Almasan 2022, Xu 2018, Stampa 2017, Waxman 1988, Watkins 1992, McKeown 2008, P4 2014 | paper v2 |

## Novos módulos de código

- `sdn/loadmodel.py` — modelo de carga (adição de fluxos) + pool extension + CSPF augmentation
- `sdn/ilp.py` — ILP-P (pool, FO exato) e ILP-L (MCF binário, min-max utilization)
- `sdn/metrics.py` — FOv2 (restrições duras), max-util, violações
- `sdn/qlearn.py` — baseline Q-learning com poda de capacidade
- `sdn/srv6_state.py` — contagem de estado OpenFlow vs SRv6
- `sdn/topologies.py` — waxman52, gridcore (52 nós, mesmo perfil de demanda)
- `sdn/stats_tools.py` — IC 95% + Wilcoxon
- `experiments/exp1..exp7` — pipeline reproduzível completa

## Resultados-chave (protocolo: 3 topo × 5 cargas × 20 seeds, GA/DE 300×50)

1. **Certificação de otimalidade**: ILP-P certifica o ótimo do pool; ACO+GA atinge 132 (20/20 seeds) em carga nominal nas 3 topologias — gap = 0.
2. **Limite inferior exato do gargalo**: ILP-L prova Z*=0.872 (carga nominal; +13% de folga) e Z*=0.984/1.000 em f=1.25/1.5 na topologia esparsa — prova de que *nenhum* roteamento mantém todos os enlaces abaixo de 98,4%/100%.
3. **Sob stress (f=1,5, maia52)**: Dijkstra 9 enlaces sobrecarregados (maxu 2,1×), CSPF 4, Q-learning ~2, ACO+GA ≈ 0–1 (atinge ótimo do pool na maioria das seeds); ILP-L factível (Z*=1.000).
4. **Isolamento de fatias**: URLLC mantém 150 ms até background ×2 (otimizado) vs violação em todos os níveis (Dijkstra); perda URLLC 0,9% vs 57% em carga nominal.
5. **SRv6**: estado 17 regras vs 34–71 (2,0–4,2× menos), transit nodes sem estado por fluxo.
6. **Sim vs bancada**: direção idêntica; magnitudes moderadas na simulação — reconciliado como artefato de bufferbloat do baseline.

## Manuscrito

- `paper/sdn_traffic_engineering_v2.tex` — artigo IEEE completo com números auto-injetados (`results/macros.tex`, `results/tables/*.tex`), 7+ páginas, ~20 referências verificadas.
- Compilação: `pdflatex paper/sdn_traffic_engineering_v2.tex` (2×) com o TinyTeX do workspace.