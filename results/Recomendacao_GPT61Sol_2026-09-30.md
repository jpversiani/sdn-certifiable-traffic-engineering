# Recomendações de revisão — Artigo "Certifiable Traffic Engineering for SDN"

*Fonte: parecer consolidado (GPT 6.1 Sol), atualizado em 30-09-2026. Contexto: avaliação das versões antiga (sdn_traffic_engineering_v2) e nova (sdn_cc_manuscript), alvo Computer Communications / IEEE Access / IEEE Latin America Transactions.*

## Síntese

A versão nova é a melhor base. Porém, os backbones não resolveram os principais problemas metodológicos da versão antiga. Alguns continuam no texto; outros aparecem quando confrontamos as afirmações com o código.

Para o objetivo — boa revista, aproveitando o trabalho existente, sem transformar a revisão em outro mestrado — a recomendação é:

> **Corrigir o núcleo científico e reduzir as promessas do artigo.** Depois, escolher IEEE Access pelo equilíbrio impacto/esforço, ou fazer uma tentativa delimitada no Computer Communications se valorizar mais o reconhecimento específico na área de redes. IEEE Latin America Transactions é uma alternativa legítima e bem mais barata, mas não uma aceitação garantida.

## Antiga vs. nova

| Critério | Versão antiga | Versão nova |
|---|---|---|
| Diversidade experimental | Uma topologia de estudo + duas sintéticas | Acrescenta GEANT2012 e Germany50 |
| Validade externa | Limitada | Melhor: usa estruturas de redes reais |
| Escalabilidade | Não demonstrada | Continua não demonstrada: 37–52 nós e 17–27 fluxos |
| Contribuição central | Híbrido + certificação, com narrativa dispersa | Melhor enquadramento em certificação |
| Correção das afirmações | Contradições importantes | Algumas permanecem, apesar da ampliação |
| Prontidão para submissão | Não pronta | Melhor base, mas ainda não pronta |

O ganho dos backbones é real: o resultado do GEANT é mais informativo que apenas mostrar que o GA empata com CSPF em cenários fáceis.

Entretanto, é preciso dizer corretamente o que foi validado: **topologias de backbones reais, com demandas sintéticas, capacidades calibradas e atrasos estimados a partir de distâncias geográficas**. Isso não é uma validação com tráfego, capacidades e atrasos operacionais medidos na GEANT.

Avaliação como parecerista: **antiga** — rejeição com incentivo à reformulação; **nova** — potencial de publicação após revisão substancial; para Computer Communications, tenderia a rejeitar a submissão atual pela combinação de inconsistência técnica e novidade insuficientemente demonstrada.

## 1. Contradições entre texto, figuras e números

O texto afirma que o híbrido permanece sem violações em toda a varredura, mas a figura de violações em maia52 mostra o contrário em 1,5×. Resultados salvos:

| Instância/cenário | Execuções factíveis do ACO+GA |
|---|---:|
| maia52, carga nominal | 20/20 |
| maia52, cenário 1,25 | 20/20 |
| maia52, cenário 1,5 | **4/20** |
| GEANT2012, carga nominal | **17/20** |
| GEANT2012, cenário 1,25 | 18/20 |
| GEANT2012, cenário 1,5 | 11/20 |

Portanto, "ótimo em todas as instâncias e replicações" e "sem violações em toda a varredura" precisam desaparecer.

O problema 150 vs. 132 também permanece: a macro `PoolOptFO` contém 150, pois o gerador faz a média dos ótimos de todas as cargas mas usa o número no parágrafo de carga nominal (`exp6_tables.py` linhas 47–50). Não é erro de digitação: é erro de agregação.

## 2. A "certificação exata de min–max" não está garantida pelo código (achado mais importante)

O manuscrito apresenta `min Z`, mas o código resolve `min (Z + 1e-3 * Σ D_k)` (`ilp.py` linhas 188–190). Uma soma ponderada não equivale automaticamente a minimizar primeiro Z e depois desempatar pelo atraso — o solver pode aceitar utilização maior para reduzir atraso. Logo, status "Optimal" certifica o objetivo composto, não o mínimo de Z isoladamente.

Consequência: os valores anunciados como "limites inferiores exatos do gargalo" precisam ser revalidados. Correção localizada:

1. Resolver primeiro apenas `min Z`.
2. Registrar status, limite do solver e gap.
3. Opcionalmente, minimizar atraso em segunda etapa, mantendo Z no ótimo dentro de tolerância declarada.

Exige recalcular os resultados afetados, inclusive a calibração dos backbones.

## 3. O híbrido não otimiza o objetivo revisado

GA e DE maximizam a FO histórica; o ILP-L usa o modelo revisado. Isso é válido **desde que o artigo assuma dois problemas distintos** — mas o resumo sugere que o híbrido resolve a mesma formulação de restrições duras e min–max.

Erro algébrico adicional: com todas as conexões estabelecidas, no código `FO = Σδ_k + 6L − 2·n_over − n_delay` (não `+4L`). Com Σδ=30 e L=17, o máximo é 30+102=132; com 4L produziria 98 (`objective.py` linha 100).

A formulação apresentada no artigo precisa incluir **conservação de fluxo** e a convenção de **capacidade bidirecional**.

## 4. Simulador e otimizador usam convenções diferentes

- O otimizador soma tráfego nos dois sentidos e compara com capacidade compartilhada; o simulador cria recursos separados por direção.
- O simulador fixa 2 Mbps em vez de ler a capacidade da topologia (`netsim.py` 61–67).
- O contador de fila inclui o período de propagação mesmo após liberar a transmissão (`netsim.py` 103–114).
- "Perda" inclui pacotes ainda em trânsito ao encerrar a simulação.
- "Jitter" é o desvio-padrão do atraso — explicitar, não presumir equivalente ao D-ITG.

Não prova que as tendências estejam erradas, mas impede afirmar que os experimentos representam exatamente o mesmo modelo de rede. Corrigir a convenção e repetir os testes de pacotes afetados.

## 5. URLLC, isolamento, SRv6 e DRL superdimensionados na narrativa

- 150 ms e perda de 28,4% não sustentam "URLLC-grade" → chamar de **fluxos sensíveis a atraso** mapeados à classe de serviço.
- Capacidade agregada e filas FIFO **não demonstram isolamento de fatias** → "logical QoS differentiation under shared capacity".
- SRv6 foi **contagem calculada** de regras, não medição de TCAM/hardware → "computed state accounting".
- Q-learning tabular não representa o conjunto dos métodos DRL, nem comprova degradação fora de distribuição.
- GA/DE são estocásticos; não chamar de "otimizadores determinísticos".

A solução de baixo esforço é **reduzir as alegações**, não implementar plataforma 5G/SRv6/DRL inteira.

## 6. O rótulo "1,5× de carga" não é 50% mais tráfego

Nos cenários acima de 1, adicionam-se sessões pequenas: cenário 1,25 → tráfego total ≈ 1,132× o nominal; cenário 1,5 → ≈ 1,264×. É um parâmetro legítimo de crescimento de sessões, mas não deve ser vendido como multiplicador literal da carga agregada — corrigir eixo e metodologia.

## Recomendações a seguir (obrigatório)

1. Corrigir contradições numéricas (132/150, "violation-free", tempos, refs cruzadas).
2. Separar claramente FO histórica e modelo revisado.
3. Completar a formulação matemática (conservação de fluxo, capacidade bidirecional).
4. Incluir o ILP nas comparações de violações.
5. Reduzir alegações de URLLC, isolamento, SRv6 e DRL ao nível dos experimentos.
6. Atualizar trabalhos relacionados (2023–2025: SDN-TE, DRL/GNN-TE, SRv6).
7. Publicar artefato reproduzível (GitHub/Zenodo com DOI) e declarar relação com a dissertação.

## Não obrigatório agora (alto esforço, ganho marginal para o objetivo)

- DQN/PPO/GNN como baseline.
- Bancada SRv6 real (Linux seg6/VPP/FRR).
- TCP, 6G, escalonamento por fatia.
- Redes de 100–500 nós.
- Publicar primeiro em conferência e depois estender para revista.

## Indicadores das revistas (confirmados em fontes oficiais)

| Revista | JIF | Fonte/ressalva | Custo |
|---|---:|---|---:|
| Computer Communications | 4,2 (2025) | BioxBio (secundária); ScienceDirect bloqueou consulta — confirmar no JCR | Não confirmado |
| IEEE Access | 4,2 ("2025 JCR") | Página oficial; ambiguidade entre edição e ano-base | US$ 2.160 + impostos |
| IEEE Latin America Transactions | 1,6 ("2025") | Site oficial; 21% aceitação, 171 dias submissão→aceite | US$ 250 após aceite |

Chances estimadas (subjetivas): CC 5–10% (antiga) / 10–20% (nova) / **25–40% após pacote mínimo**; Access 10–20% / 15–30% / **45–65%**; LATAM 10–25% / 15–30% / **40–60%**.

## Caminho de melhor custo-benefício

1. **Revisão obrigatória** (~1–2 semanas): corrigir ILP-L (lexicográfico) e revalidar certificados; corrigir simulador e repetir experimentos de pacotes; corrigir FO/macro 150/132/tempos/claims de factibilidade; separar os dois objetivos; retirar URLLC/6G e "isolamento garantido"; limitar Q-learning ao baseline implementado; completar matemática e referências; congelar dados por versão e publicar código.
2. **Acréscimo de alto retorno**: pool de k-menores caminhos + mesmo GA (vs. pool ACO+GA); ACO+ILP-P (seleção exata); algumas matrizes adicionais de demanda; tempo separado por estágio. Responde: o ACO agrega valor? O GA é necessário nesta escala? O resultado depende de uma única matriz de tráfego?
3. **Decisão editorial**: Access (melhor equilíbrio, se houver APC); CC (tentativa ambiciosa com reforço experimental); LATAM (alternativa econômica, não automaticamente fácil).

Enquadramento recomendado: **"Avaliação reproduzível de roteamento híbrido, distinguindo limitações do pool, falhas da seleção e referências exatas, em topologias sintéticas e de backbones reais."**