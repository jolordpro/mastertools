# 07_Golden_Questions_and_Retrieval_Tests.md
## Golden Questions, Retrieval Test Set & Validation Protocol
### Control / Quality Document
**Document ID:** CTRL-07  
**Version:** 1.0  
**Status:** Living Control Document  
**Last Updated:** 2026-07-23  
**Purpose:** Provide a structured set of Golden Questions and retrieval tests to validate that the Leadership RAG Library returns accurate, evidence-bounded, Person-vs-System-aware, and culturally calibrated guidance. Used for AI Coach testing, compilation QA, and ongoing hardening.

**Related:** 00_START_HERE, 02_AI_Coach_Operating_Manual, 04_Retrieval_Playbook, 05_Contradiction_and_Evidence_Log, 06_Reading_Paths

---

## 1. Testing Principles

1. **Retrieval must surface the correct primary Super Page(s)** and relevant control documents.
2. **Evidence strength must be respected** — Emerging claims must not be presented as settled.
3. **Person-vs-System diagnosis must appear** with the bias recorded on the Super Page.
4. **Universal cascade-health requirements must be held** while cultural calibration (CQ-001) is applied when context requires it.
5. **Failure modes and red flags** should be retrievable for risk situations.
6. **Multi-page synthesis** should be coherent when a situation spans domains (e.g., AI + Safety + Energy + Board).
7. **No hallucination of methods or evidence** beyond what the library contains.

---

## 2. Golden Question Set (Initial)

### Cluster A — Cascade Diagnosis & Bridge
**A1.** “A Leader of Leaders reports that skip-level signal has gone quiet and people seem agreeable but nothing risky is raised. What should I examine first?”  
**Expected primary:** SAFE-001 (Artificial Harmony), BRIDGE-001, SYS-CAS-001  
**Must include:** Multi-layer sensing, Artificial Harmony vs. healthy respect, Person-vs-System, possible energy or toxic contributors.

**A2.** “How do I convert an observation about declining Adaptive Space into a concrete coaching or system intervention?”  
**Expected primary:** BRIDGE-001, SYS-CAS-001  
**Must include:** Observation-to-Coaching Bridge structure, Person-vs-System, Adaptive Space protection tactics.

### Cluster B — Passage 2 & Role Design
**B1.** “We promoted our best first-line manager to lead other managers. Six months later the cascade under them is struggling and they are still doing a lot of individual-contributor work. What is going on and what should we do?”  
**Expected primary:** PIPE-001, PEOPLE-001, CAP-001, ENERGY-001  
**Must include:** Three-part transition (skills + time + values), incomplete transition patterns, capacity vs. capability, develop/redesign/re-assign tree, energy protection during transition.

**B2.** “Is this a capability problem or a capacity problem for our People Leaders?”  
**Expected primary:** PEOPLE-001, ENERGY-001, PIPE-001  
**Must include:** Capacity audit logic, “do both” trap, role redesign levers before training.

### Cluster C — AI Judgment & Oversight
**C1.** “Our teams are adopting AI tools rapidly. Overrides are rare and people say ‘the model recommended it.’ What risks should we be governing and how?”  
**Expected primary:** AI-001, SAFE-001, ENERGY-001, BOARD-001  
**Must include:** Judgment Loops, Decision Drift, Judgment Depreciation, Amplified Oversight, AI voice safety, energy/cognitive load, board-level decision rights and long-term evaluative capacity. Evidence strength must be communicated as Moderate–Emerging where appropriate.

**C2.** “How do we design Agent Manager capability into our leadership pipeline?”  
**Expected primary:** AI-001, PIPE-001, SPONSOR-001, CAP-001  
**Must include:** Agent Manager skills, Passage requirements, sponsorship of AI judgment capability, capacity for complexity.

### Cluster D — Toxic High Performer
**D1.** “A high-performing leader delivers strong numbers but skip-level feedback and turnover suggest fear. Prior coaching has not produced lasting multi-layer change. Containment or recovery?”  
**Expected primary:** DARK-001, SAFE-001, ENERGY-001, BRIDGE-001  
**Must include:** Containment vs. Recovery decision framework, multi-layer damage criterion, cascade protection during process, system enablers, results shield failure mode. Default bias toward Containment when multi-layer damage is present.

**D2.** “How do we tell tough-but-fair leadership from toxic or justice-variable leadership in a high-performance-orientation culture?”  
**Expected primary:** DARK-001, CQ-001, SAFE-001  
**Must include:** Cascade-damage evidence (not style), cultural calibration, multi-layer safety and justice consistency.

### Cluster E — Sponsorship & Generativity
**E1.** “We say we have sponsorship, but it looks like mentorship and the same people keep getting visibility. How do we build real cascading sponsorship?”  
**Expected primary:** SPONSOR-001, GEN-001, PIPE-001, ENERGY-001  
**Must include:** Four acts, portfolio discipline, reverse flows, light accountability without Goodhart, energy surplus requirement, cascade amplification (sponsors of sponsors).

**E2.** “What does generative legacy actually look like at enterprise level, and how is it different from performative legacy?”  
**Expected primary:** GEN-001, BOARD-001, SPONSOR-001, ENERGY-001  
**Must include:** Durable cascade capacity vs. monuments/storytelling, energy surplus, multi-layer signals, board definition of legacy.

### Cluster F — Board & Governance
**F1.** “What should a board actually sense about cascade health and AI judgment beyond financial and operational dashboards?”  
**Expected primary:** BOARD-001, AI-001, SAFE-001, GEN-001, PIPE-001  
**Must include:** Multi-layer sensing, Cascade Distortion at board interface, AI as judgment system, generative succession data, metric architecture, minimum viable board cascade fluency.

**F2.** “Our board treats culture and leadership quality as soft issues. How do we change that without creating theater?”  
**Expected primary:** BOARD-001, 05_Contradiction_and_Evidence_Log  
**Must include:** Metric and discussion architecture, cascade health as strategic asset, risk of performative board effectiveness.

### Cluster G — Cultural Calibration
**G1.** “We rolled out a global speak-up campaign. In one region it produced face loss and silence. What went wrong and how do we calibrate?”  
**Expected primary:** CQ-001, SAFE-001  
**Must include:** Power distance and face dynamics, ethnocentric imposition risk, adapted voice channels that still produce real risk surface, universal safety requirement held.

**G2.** “How do we avoid both labeling culturally direct leadership as toxic and excusing real fear as ‘just the culture’?”  
**Expected primary:** CQ-001, DARK-001, SAFE-001  
**Must include:** Dual refusal, multi-layer cascade-damage data, toxic-vs-tough differential.

### Cluster H — Cross-Domain / Synthesis Stress Tests
**H1.** “Leaders are exhausted, AI tools are everywhere, skip-level voice is down, and we keep promoting based on previous-level heroics. Where do we start?”  
**Expected primary synthesis:** ENERGY-001, AI-001, SAFE-001, PIPE-001, PEOPLE-001, BRIDGE-001  
**Must include:** Capacity-first diagnosis, Judgment Health risk, Artificial Harmony, incomplete Passage patterns, role redesign, ordered intervention sequence.

**H2.** “What does this library say is non-negotiable for long-term cascade health even when culture, AI, and delivery pressure vary?”  
**Expected primary:** 00_START_HERE, CQ-001, SAFE-001, ENERGY-001, AI-001, GEN-001, 05_Contradiction_and_Evidence_Log  
**Must include:** Universal requirements list, cultural contingency of expression only, evidence boundaries.

---

## 3. Retrieval Validation Checklist (Per Golden Question)

For each test query, score or note:
- [ ] Correct primary Super Page(s) retrieved
- [ ] Relevant supporting pages retrieved
- [ ] Evidence strength communicated accurately (no upgrading)
- [ ] Person-vs-System bias applied correctly
- [ ] Failure modes / red flags surfaced when risk is present
- [ ] Cultural calibration invoked when context requires it
- [ ] No contradiction with CTRL-05 tension resolutions
- [ ] Actionable next steps or diagnostic questions present
- [ ] Multi-page synthesis coherent (for Cluster H)

---

## 4. Initial Test Protocol

1. Run each Golden Question against the library (human expert or AI Coach with retrieval).
2. Record actual retrieved chunks / pages and the response quality against the checklist.
3. Log misses, over-claims, or missing cross-links in CTRL-05 and in a test log.
4. Prioritize Hardening Addenda for any systematic retrieval or reasoning failures.
5. Re-test after hardening.
6. Expand the Golden Question set as new domains or field use cases appear.

---

## 5. Success Criteria for Compilation Readiness

- ≥ 90% of Golden Questions retrieve the correct primary Super Page(s) on first pass.
- Zero instances of evidence-strength upgrading on Emerging claims.
- Person-vs-System and Containment-vs-Recovery biases correctly applied in risk cases.
- Cultural assumption checks appear on contested safety/toxicity/sponsorship items.
- Cross-domain synthesis questions (H1, H2) produce ordered, non-contradictory guidance.

---

**End of CTRL-07 — Golden Questions and Retrieval Tests (v1.0)**  
**Next in sequence:** Hardening Addenda (backlog + any immediate high-priority fixes) and Tier 2 prioritization.
