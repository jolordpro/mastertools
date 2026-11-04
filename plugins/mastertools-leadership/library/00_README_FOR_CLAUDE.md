# Leadership RAG Library — Source of Truth for Claude
**Package Version:** 1.0  
**Library Status:** Production-ready (Core Super Pages v1.1–v1.2 Hardened)  
**Packaged:** 2026-07-23  

---

## What This Is

A modular, RAG-optimized knowledge library for coaching, assessing, and developing **Leaders of Leaders**. It is designed as a high-fidelity Source of Truth for Claude (or any capable LLM) acting as a professional leadership coach and system designer.

**Primary audience the library serves:**
- Leaders of Leaders (middle → senior)
- Talent / OD / Leadership Development professionals
- Board-facing executives and governance designers
- AI Coach implementers

**Core claim of the library:** Most cascade failures (safety collapse, energy depletion, Adaptive Space starvation, sponsorship distortion, generativity failure, AI judgment neglect) are system and role-design problems as much as individual capability problems. Incomplete Passage 2 transitions, capacity-constrained People Leader roles, and results shields for toxic patterns are primary drivers.

---

## How Claude Must Use This Library

### Binding Governance (always respect)
1. **00_START_HERE.md** — Anti-hallucination rules, retrieval hierarchy, Person-vs-System protocol, escalation criteria.
2. **02_AI_Coach_Operating_Manual.md** — Multi-turn flows, dosage calibration, second-order moves, failure modes.
3. **05_Contradiction_and_Evidence_Log.md** — Evidence-strength boundaries, known tensions, residual gaps. **Never upgrade evidence_strength.**

### Non-Negotiable Operating Rules
- Communicate `evidence_strength` honestly (Strong / Moderate / Emerging). Emerging claims must be labeled as such.
- Default to the **Person-vs-System bias** written on each Super Page. Capacity problems are usually system/role first.
- When multi-layer toxic damage is present → **Containment first** (DARK-001), not endless recovery coaching.
- Hold **universal cascade-health requirements** (safety sufficient for learning, energy surplus, non-toxic high performance, Enabling Leadership, long-term human evaluative capacity, generativity). Calibrate *expression* via CQ-001; never relativize the requirements away.
- Prefer Hybrid sequences recorded on the Super Pages over improvised advice.
- Cite Super Pages by Document ID (e.g., `AI-001`, `PIPE-001`, `DARK-001`).
- Escalate legal, harassment, integrity, or imminent harm issues; do not coach them away.

### Recommended Retrieval Hierarchy
1. Governance: 00 → 02 → 05 → 04
2. Navigation: 06 (Reading Paths) → 01 (Taxonomy)
3. Meta + Action: SYS-CAS-001 → BRIDGE-001
4. Substrates (on any cascade diagnosis): SAFE-001 → ENERGY-001 → CAP-001
5. Domain pages by situation
6. CQ-001 on any contested cultural interpretation

### High-Leverage Entry Points
- Almost any diagnostic/action conversation → start with **BRIDGE-001**
- Passage 2 / new Leader of Leaders struggle → **PIPE-001 + PEOPLE-001 + ENERGY-001**
- AI judgment / “the model said so” → **AI-001 + SAFE-001 + ENERGY-001 + BOARD-001**
- Toxic high performer + results shield → **DARK-001** (Containment bias)
- Board / governance → **BOARD-001**
- Cross-cultural or contested safety/toxicity → **CQ-001** first (assumption-check worksheet)

---

## Package Contents

### Control Layer (load / prioritize for rules)
| File | ID | Purpose |
|------|----|---------|
| 00_START_HERE.md | — | Primary entry + anti-hallucination + Person-vs-System |
| 01_Taxonomy_Controlled_Vocabulary.md | — | Controlled vocabulary |
| 02_AI_Coach_Operating_Manual.md | — | Executable operating system for the AI Coach |
| 03_Master_Index_and_Reading_Paths.md | — | Inventory + original reading paths |
| 04_Retrieval_Playbook_and_Priority.md | — | Retrieval philosophy + conflict resolution |
| 05_Contradiction_and_Evidence_Log.md | CTRL-05 | Evidence boundaries + tensions + residual gaps |
| 06_Reading_Paths_and_Onboarding.md | CTRL-06 | 10 reading paths + role entry points |
| 07_Golden_Questions_and_Retrieval_Tests.md | CTRL-07 | Validation questions + success criteria |
| 08_Hardening_Addenda_and_Tier2_Backlog.md | CTRL-08 | Future polish + Tier 2 backlog |
| 09_Compilation_and_Source_of_Truth_Packaging.md | CTRL-09 | Packaging & load hierarchy |

### Core Canonical Super Pages
| File | Document ID | Version | Focus |
|------|-------------|---------|-------|
| Systems_Thinking_Complex_Adaptive_Systems.md | SYS-CAS-001 | v1.1 | Meta-operating system |
| Observation_to_Coaching_Bridge_and_Cascade_Health_Dashboard.md | BRIDGE-001 | v1.2 | Action-conversion engine + multi-problem starter |
| Psychological_Safety_Multi_Layer.md | SAFE-001 | v1.1 | Multi-layer safety + Artificial Harmony |
| Capacity_for_Complexity_and_Enabling_Leadership.md | CAP-001 | v1.1 | Vertical development + role-complexity fit |
| Resilience_Energy_Management.md | ENERGY-001 | v1.1 | Four-energy model + surplus protection |
| AI_Transformation_Leadership.md | AI-001 | v1.2 | Judgment Loops, Decision Drift, Agent Manager |
| Dark_Side_Toxic_High_Performers.md | DARK-001 | v1.1 | Containment vs. Recovery |
| Sponsorship_Systems.md | SPONSOR-001 | v1.1 | Four acts + cascading sponsorship |
| Generativity_Legacy_Wisdom_Transfer.md | GEN-001 | v1.1 | Durable cascade capacity + reverse flows |
| Leadership_Pipeline_Passages.md | PIPE-001 | v1.1 | Passage 2 three-part transition |
| People_Leader_Role_Redesign.md | PEOPLE-001 | v1.1 | Capacity vs. Capability + “do both” trap |
| Board_Fluency_and_Governance.md | BOARD-001 | v1.2 | Board cascade sensing + AI judgment governance |
| Cultural_Intelligence_and_Context.md | CQ-001 | v1.2 | Universal requirements + cultural calibration + assumption-check worksheet |

**Total: 23 source files.**

---

## Suggested Claude Project / Custom Instructions Snippet

You can paste a shortened version of the following into a Claude Project or system prompt:

```
You are operating with the Leadership RAG Library as your Source of Truth for all leadership, cascade health, talent, AI judgment, and governance questions.

Binding rules:
- Never invent methods or evidence not present in the library.
- Never upgrade evidence_strength (Strong / Moderate / Emerging).
- Apply the Person-vs-System bias written on each Super Page.
- When multi-layer toxic damage is present, default to Containment first (DARK-001).
- Hold universal cascade-health requirements; calibrate expression via CQ-001.
- Cite Document IDs (e.g., AI-001, PIPE-001).
- Use BRIDGE-001 as the primary action-conversion engine.
- On contested cultural diagnoses, run the CQ-001 assumption-check worksheet.

Primary entry points:
- Diagnostic/action → BRIDGE-001
- Passage 2 / new Leaders of Leaders → PIPE-001 + PEOPLE-001 + ENERGY-001
- AI judgment risk → AI-001 + SAFE-001 + ENERGY-001
- Toxic high performer → DARK-001
- Board governance → BOARD-001
- Cultural calibration → CQ-001
```

---

## Validation Status

The library carries **two** Golden Question sets: 15 questions in `00_START_HERE.md` §9, and 16
in `07_Golden_Questions_and_Retrieval_Tests.md` §2 (clusters A–H). Retrieval has been tested twice.

- **2026-07-23 — expert retrieval simulation.** Correct primary Super Page retrieval across the
  tested set, ~8.8/10 average quality, zero evidence upgrades, zero bias failures. Recorded in
  CTRL-05 §6. *Caveat: the detailed source log is not included in this package, and the figure
  originally published as "18/18" matched neither question set. It is retained above as recorded
  but is not independently verifiable from package contents.*
- **2026-07-26 — blind agent pass.** All questions in both sets tested, with the skill deliberately
  not named in any prompt so retrieval routing was exercised alongside answer quality. All passed.
  Logs in `Test_Results/`. Two defects were found and fixed during this pass (an omitted
  toxic-actor cause in the silence differential; unsourced review cadences stated with library
  authority), and five corpus-integrity defects were found and corrected.
- Thin spots (Board Dashboard samples, CQ worksheet, Agent Manager sequence, multi-problem starter)
  expanded in v1.2 passes.
- Residual Hardening Addenda remain optional polish only. See CTRL-08 §7 for items addressed via
  executable skill instruments.

---

**Ready for use.** Load the Control Layer first, then retrieve Super Pages by situation. Treat this package as the authoritative source for cascade-health, Leader-of-Leaders, and AI-era judgment coaching.
