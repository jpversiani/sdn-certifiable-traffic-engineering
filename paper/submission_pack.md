# Submission pack — Traffic Engineering Optimization in SDN

## Cover letter template

---

**Date:** [Date]

**To:** The Editors, [Journal name]

**Re:** Manuscript submission — *Hybrid Ant-Colony Metaheuristics for QoS-Aware Traffic-Engineering Optimization in Software-Defined Networks*

Dear Editors,

Please consider the enclosed manuscript for publication in [Journal name]. The paper addresses the growing problem of optimizing traffic flow in Software-Defined Networks under Quality-of-Service constraints, a topic of direct relevance to [Journal scope].

The work makes the following contributions:
1. A QoS-aware mathematical model for traffic-engineering routing in SDN;
2. Two hybrid metaheuristics (ACO+GA and ACO+DE) that compute feasible, balanced route sets;
3. A discrete-event simulation framework to quantify the attainable QoS gains;
4. Experiments on a realistic 52-node topology showing +37% throughput and one-order-of-magnitude reductions in delay, jitter and packet loss versus shortest-path routing.

The manuscript is original, has not been published elsewhere, and all experiments are reproducible (code and data are available from the authors on request).

I confirm that the manuscript is in compliance with the journal's submission and ethical guidelines, and that all co-authors have read and approved the manuscript.

Thank you for your consideration.

Sincerely,

João Paulo Versiani Ladeia
Affiliation: [Institution, address]
Email: [email] · ORCID: [orcid]

---

## Suggested target journals (international, indexing in Scopus/Web of Science)

| Journal | Typical scope match | Notes |
|---------|--------------------|-------|
| **IEEE Transactions on Network and Service Management (TNSM)** | Network management / SDN | Strong fit; formal + applied |
| **IEEE Access** (or IEEE Internet of Things Journal) | Broad, open access | Fast, good visibility |
| **Computer Networks** (Elsevier) | Networking, SDN, routing | Strong natural fit |
| **Computer Communications** (Elsevier) | QoS, routing, traffic engineering | Excellent fit |
| **Journal of Network and Computer Applications (JNCA)** | Applied networks | Good fit |
| **Telecommunication Systems** (Springer) | QoS / traffic engineering | Good fit |
| **International Journal of Network Management (IJNM)** | Network management | Good fit |

> **Tip:** contact a *journal* whose scope explicitly mentions SDN / QoS / traffic
> engineering, and always follow its specific author guidelines (template, format,
> abstract word-count, reference style).

---

## Pre-submission checklist

- [ ] Title concise and descriptive
- [ ] Abstract within journal limits (150–250 words) and self-contained
- [ ] Keywords provided (4–6)
- [ ] IMRaD structure (Intro / Background / Model / Method / Results / Discussion / Conclusion)
- [ ] Equations numbered and referenced
- [ ] Tables have titles and are cited in text
- [ ] Figures have captions, are legible and referenced (re-export at ≥300 dpi for print)
- [ ] All references cited in text and formatted in journal style
- [ ] Novelty/secondary-claim flagged in cover letter
- [ ] Ethical statement / conflict-of-interest declared if required
- [ ] Author affiliations, ORCID and contact complete
- [ ] Code/data availability statement added (reproducibility bonus)
- [ ] Statistical significance discussed (add confidence intervals if journal is strict)
- [ ] English proofread (consider a native-speaker or AI proofreading pass)
- [ ] Format exported exactly per journal template (LaTeX or Word)

---

## Optional: reproducibility / data-availability statement (add to Section 5)

> *Reproducibility.* The complete implementation (route generation, metaheuristics,
> objective function and discrete-event network simulator) and the topology data are
> available as open-source Python from the authors upon request. All experiments in
> this paper were produced with a fixed random seed and are fully reproducible on a
> standard workstation.