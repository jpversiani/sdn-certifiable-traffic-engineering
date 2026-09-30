# Otimização de Tráfego em Rede SDN — Port Python

Reimplementación en Python de la tesis

> **Otimização Aplicada ao Problema de Engenharia de Tráfego em Redes
> Definidas por Software** (J. P. Versiani Ladeia, Unimontes, 2018).

Se convirtieron los scripts MATLAB del apéndice a Python y se construyó una
**simulación de red SDN** por eventos discretos (biblioteca `simpy`) que
reproduce la emulación Mininet/Floodlight/D-ITG del trabajo original.

## Estructura

```
deepseek_teste_v1/
├── extract_data.py        # extrae A, AT, VA, xy, tds desde el .docx → topology_data.json
├── topology_data.json     # datos de la topología 1 (52 nodos)
├── sdn/
│   ├── data.py            # carga de la topología
│   ├── dijkstra.py        # port de dijkstra.m (rutas por distancia euclídea)
│   ├── aco.py             # port de mgrafos14g.m (generador AntNet)
│   ├── objective.py       # port de linkc5.m (función objetivo / fitness)
│   ├── ga.py              # port de agaco811.m (Algoritmo Genético)
│   ├── de.py              # port de deaco311.m (Evolución Diferencial)
│   ├── run_optimization.py# orquesta ACO+DE / ACO+AG vs Dijkstra
│   └── netsim.py          # simulador SDN con simpy (vazão, atraso, jitter, perda)
├── run_workflow.py        # ejecuta optimización + simulación + gráficos y CSV
├── requirements.txt
└── output/                # salidas (gráficos PNG + per_application_results.csv)
```

## Instalación

```bash
pip install --target="$PWD/pylib" -r requirements.txt
# o: pip install -r requirements.txt
export PYTHONPATH="$PWD/pylib:$PWD"
```

## Ejecución

```bash
PYTHONPATH="$PWD/pylib:$PWD" python3 run_workflow.py
```

El primer run genera las rutas candidatas del ACO y las guarda en
`cache_mrotas_aco.npy` (~4 min); las siguientes lecturas usan la caché.

## Pipeline experimental (artigo v2, rigor estatístico)

```bash
PYTHONPATH="$PWD/pylib:$PWD" python3 -u experiments/exp1_pools.py     # pools ACO (3 topo x 20 seeds)
PYTHONPATH="$PWD/pylib:$PWD" python3 -u experiments/exp2_sweep.py     # sweep: 3 topo x 5 cargas x 6 metodos x 20 seeds
PYTHONPATH="$PWD/pylib:$PWD" python3 -u experiments/exp3_slices.py    # isolamento de fatias URLLC (simpy)
PYTHONPATH="$PWD/pylib:$PWD" python3 -u experiments/exp4_srv6.py      # estado OpenFlow vs SRv6 medido
PYTHONPATH="$PWD/pylib:$PWD" python3 -u experiments/exp5_stats_figs.py # IC95%, Wilcoxon, figuras
PYTHONPATH="$PWD/pylib:$PWD" python3 -u experiments/exp6_tables.py    # macros/tabelas LaTeX auto-injetadas
PYTHONPATH="$PWD/pylib:$PWD" python3 -u experiments/exp7_qos_sim.py   # QoS simulado por pacote
```

Metodos comparados: Dijkstra, CSPF, Q-learning (baseline DRL-like), ACO+DE,
ACO+GA, ILP exato (pool e multi-commodity flow). Saidas em `results/`
(JSONL/CSV/JSON), figuras em `paper/figures/`, numeros do manuscrito
injetados de `results/macros.tex` e `results/tables/*.tex`.

## Resultados reproducidos de la tesis (topología 1, 52 nodos)

| Método       | Función objetivo |
|--------------|------------------|
| Dijkstra     | **120** (tesis: 120) |
| ACO + DE     | **132** (tesis: óptimo 132) |
| ACO + AG     | **132** (tesis: óptimo 132) |

Métricas de red (simpy): ver tablas en consola y `output/per_application_results.csv`.