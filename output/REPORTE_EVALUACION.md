# Evaluación de la disertación y reimplementación en Python

**Trabajo original**: *Otimização Aplicada ao Problema de Engenharia de
Tráfego em Redes Definidas por Software* — João Paulo Versiani Ladeia
(Unimontes, PPGMCS, 2018).

## 1. Evaluación del trabajo (disertación)

### Fortalezas
- **Problema relevantemente formulado.** La ingeniería de tráfico (TE) sobre
  redes SDN es una alternativa realista a invertir en infraestructura. El
  planteamiento de resolver el roteo como un problema de optimización
  combinatoria (selección de rutas con QoS) es adecuado.
- **Modelo matemático claro (Eq. 4.1).** La función objetivo
  `FO = Σ δ_k·y_k + 3Σy_k + 2Σw_k + 1Σt_k` ponderando prioridad, conexiones
  establecidas, ancho de banda suficiente y atraso aceptable está bien
  definida y es reproducible.
- **Estrategia híbrida con sentido.** Separar la *generación* de rutas (ACO/
  AntNet) de la *selección* del conjunto solución (AG o DE) es un diseño
  razonable que acota el espacio de búsqueda.
- **Comparación con un baseline estándar (Dijkstra)** y reproducción de
  resultados en una emulación Mininet/Floodlight/D-ITG con métricas de red
  concretas (vazão, atraso fim-a-fim, jitter, perda).

### Debilidades / observaciones críticas
- **Resultados con cifras extremas y poca robustez estadística.** El resumen
  reporta mejoras de hasta *510× en pérdida*, *51× en atraso*, cifras que
  invitan a revisar la metodología (condiciones de saturación de la red de
  Dijkstra, número y duración de las ejecuciones, estado transitorio). Los
  rangos de mejora son muy sensibles a la configuración de congestión.
- **El código MATLAB tiene inconsistencias de índices/grupos de ruta.** El
  proceso de selección de rutas (AG/DE) opera sobre un *pool plano* de rutas
  (`rotas_sel` indices 1..tm) que mezcla rutas de distintas aplicaciones; la
  función `linkc5` re-etiqueta flujos buscando pares (origen,destino). Esto
  funciona en la práctica pero no garantiza que cada aplicación elija rutas
  que le pertenezcan, lo que puede sobrevaluar la FO.
- **Dependencia de librerías no citadas.** `linkc5`, el GA (Yarpiz/Heris 2016)
  y `dijkstra.m` (Joseph Kirk 2015) son código de terceros incorporado sin
  suficiente atribución dentro del apéndice.
- **Cierta redacción/erratas:** figuras/leyendas duplicadas (Fig. 17 y 19
  ambas tituladas "DE"), tablas con formato no uniforme, y las secciones de
  resultados mezclan "nota" (función objetivo) con métricas de red.
- **La emulación es `off-line` y no automatizada** (se confiesa en §4.2), por
  lo que el sistema no está integrado al controlador SDN en tiempo real.

### Veredicto global
Disertación **sólida y coherente en lo conceptual y metodológico** para un
programa de maestría: modela bien el problema, plantea 2 heurísticas híbridas,
valida contra Dijkstra y da resultados en una emulación de red real. La
principal deuda es **robustez estadística y reproducibilidad** de las cifras
extremas de mejora.

## 2. Reimplementación en Python — qué se hizo

Se portaron los scripts MATLAB del apéndice a un paquete Python (`sdn/`) y se
construyó una **simulación de red por eventos discretos (simpy)** que emula la
red SDN y mide las 4 métricas del trabajo.

| Script MATLAB | Port Python | Descripción |
|---------------|-------------|-------------|
| `variaveis_de_entrada.m` | `sdn/data.py` | 52 nodos, `A`, `AT`, `VA`, `xy`, `tds` (extraídos del docx) |
| `dijkstra.m` + `mgrafos14dijkstra.m` | `sdn/dijkstra.py` | Ruta mínima por distancia euclídea |
| `mgrafos14g.m` (ACO/AntNet) | `sdn/aco.py` | Generador de rutas candidatas |
| `linkc5.m` (FO) | `sdn/objective.py` | Función objetivo / fitness |
| `agaco811.m` (GA) | `sdn/ga.py` | Selección del conjunto de rutas |
| `deaco311.m` (DE) | `sdn/de.py` | Selección del conjunto de rutas |
| — | `sdn/netsim.py` | **Simulador SDN (simpy)** |

## 3. Validación de la función objetivo (fitness)

La reimplementación reproduce los valores de la tesis para la topología 1:

| Método | FO (Python) | FO (tesis) |
|--------|-------------|------------|
| Dijkstra | **120** | 120 |
| ACO + DE | 128–132 | óptimo = 132 |
| ACO + AG | **132** | óptimo = 132 |

## 4. Simulación de red (simpy) — resultados

Rutas **optimizadas (ACO+AG)** vs **Dijkstra**, mismas condiciones de tráfico
(17 aplicaciones, paquetes de 512 B, enlaces de 2 Mbps):

| Métrica | Optimizada | Dijkstra | Mejora (opt/dj) |
|---------|-----------|----------|-----------------|
| Vazão media (Mbps) | 0.560 | 0.408 | **+37 %** |
| Atraso fim-a-fim (ms) | 115 | 198 | **≈1.7× menor** |
| Jitter (ms) | 0.74 | 33.2 | **≈45× menor** |
| Perdida de paquetes | 2.3 % | 30.8 % | **≈13× menor** |

Las mejoras son **direccionalmente idénticas** a la tesis (vazão superior,
atraso/jitter/perdida inferiores). Las magnitudes absolutas difieren porque el
modelo de congestión del simulador discreto no replica exactamente la
emulación Mininet/D-ITG, pero el efecto cualitativo —las rutas optimizadas
equilibran la carga y evitan los cuellos de botella que congestionan la red de
Dijkstra— se confirma claramente (p. ej. las aplicaciones 12–17 con vídeo/voz
en el núcleo: 57–94 % de pérdida con Dijkstra frente a 1–3 % con la red
optimizada).

## 5. Cómo ejecutar

```bash
export PYTHONPATH="$PWD/pylib:$PWD"
python3 run_workflow.py        # optimización + simulación + gráficos + CSV
```

Primera ejecución: genera rutas ACO (caché `cache_mrotas_aco.npy`);
posteriores: usan la caché. Gráficos y tabla por aplicación en `output/`.

## 6. Conclusión

La reimplementación en Python valida el trabajo original: las heurísticas
híbridas ACO+AG/ACO+DE alcanzan el óptimo de la función objetivo (132 vs 120
de Dijkstra) y, en la simulación SDN, la red optimizada supera claramente a la
red basada en Dijkstra en vazão, atraso, jitter y pérdida. Esto confirma que el
enfoque de ingeniería de tráfico con optimización es efectivo para mejorar el
uso de recursos de una red SDN con requisitos de QoS.