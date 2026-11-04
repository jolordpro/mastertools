# 04_Retrieval_Playbook_and_Priority.md
## Retrieval Strategy, Chunking, Priority Weights & RAG Operating Rules
### Leadership & Talent Cascading Knowledge Library
**Version:** 1.2 (Accuracy Reconciliation — July 2026)
**Change Log (v1.1 → v1.2, 2026-07-26):** §2 Tier 2 and §10 no longer reference a Master Behavioral Signals Library or Master Diagnostic Question Bank; neither was built. Both now point to the Super Page §3 and §4 sections. §2 Tier 3 clarified that no separate Hardening Addenda files exist. Aligned with 00_START_HERE v1.3 and 02 v1.2.  
**Status:** Canonical Control Document  
**Parent Documents:** 00_START_HERE.md (v1.3), 01_Taxonomy_Controlled_Vocabulary.md (v1.2), 02_AI_Coach_Operating_Manual.md (v1.2), 03_Master_Index_and_Reading_Paths.md (v1.1)  
**Purpose:** Lock the technical and operational rules for high-precision, anti-hallucination, decision-oriented retrieval so that the AI Coach and any RAG system consistently surface the right Super Pages, the right chunks, and the right multi-hop integrations at the right time — while protecting the cascade and enabling Person-vs-System decisions.

---

## 1. Retrieval Philosophy

Retrieval in this library is not “find similar text.”  
It is **decision-oriented, cascade-protective, person-vs-system-aware retrieval**.

Goals (in strict priority order):
1. Surface the highest-leverage Super Page(s) for the user’s actual need.
2. Prefer chunks that enable Person-vs-System decisions, behavioral specificity, and diagnostic questions.
3. Preserve evidence_strength and contradictions rather than averaging them away.
4. Support multi-hop reasoning via explicit relationships in 01 (max useful depth 2).
5. Never invent. Prefer “library is thin here” over hallucinated completeness.
6. Optimize for Leaders of Leaders under cognitive load (Path K) and crisis (Path F).
7. Enable clean citation and traceability.

---

## 2. Tiered Retrieval Hierarchy (Operational)

**Tier 1 — Must Retrieve First**
- Matching Control Documents (00–04) when the query is about process, rules, or navigation.
- The single best-matching Core Canonical Super Page (by primary construct ownership per 03 and 01).

**Tier 2 — Strongly Preferred**
- Directly linked Super Pages via `related_super_pages` and high-value relationships in 01.
- The §3 Behavioral Indicators Library and §4 Diagnostic Question Bank sections of the matching Super Page (see preference rule in §10).
- Cascade Health Dashboard and Person-vs-System sections of BRIDGE-001 when diagnosis is active.

**Tier 3 — Contextual**
- Adjacent Super Pages.
- Hardening Addenda, where they exist (none are separate files in this package; expansions are folded into the Super Pages themselves — see CTRL-08 §6–§7).
- Lower-priority multi-hop links.

**Hard Rule:** Never answer a library-covered topic from parametric knowledge if a Tier 1 or Tier 2 source exists.

---

## 3. Chunking Strategy (Mandatory for All Super Pages)

### 3.1 Principles
- Chunk by **semantic idea / decision unit**, not by fixed token count.
- Every chunk must be understandable in isolation while carrying enough context to avoid mis-retrieval.
- Prefer smaller, high-precision chunks for behavioral signals, diagnostics, failure modes, and Person-vs-System guidance.
- Larger chunks are acceptable for core frameworks only if they remain focused on one major model or idea.

### 3.2 Practical Granularity Guidance
| Content Type | Preferred Granularity | Example |
|--------------|-----------------------|---------|
| Behavioral signals / red flags | Small (one coherent cluster of 3–8 signals) | “Red flags of Artificial Harmony in Leading Leaders meetings” |
| Diagnostic questions | Small to medium (one diagnostic theme) | “Questions to distinguish safety vs. capacity-for-complexity issues” |
| Person-vs-System guidance | Small to medium (one decision context) | “Person-vs-System criteria when the same at-risk behavior recurs across people” |
| Failure modes / edge cases | Small to medium | “Cascade contagion patterns from uncontained toxic high performers” |
| Core frameworks | Medium (one major model) | “Meadows Leverage Points as applied to cascade health” |
| Integration / cascading implications | Medium | “How Energy depletion cascades into middle-manager safety and judgment” |
| Evidence & residual gaps | Small | “Evidence strength summary + known residual gaps for this domain” |

**Anti-pattern:** Giant mixed chunks that combine framework + 20 signals + 15 questions + failure modes. These destroy precision.

### 3.3 Required Chunk Types
| Chunk Type | Priority | Notes |
|------------|----------|-------|
| `framework` | Medium | Core models and definitions |
| `behavioral_signals` | **Highest** | Positive signals + red flags, level-differentiated |
| `diagnostic` | **Highest** | Question banks |
| `failure_mode` | High | Edge cases, anti-patterns, contagion risks |
| `person_vs_system` | **Highest** | Decision guidance and criteria |
| `integration` | High | Cascading implications and multi-hop links |
| `evidence` | Medium | Evidence strength summary + residual gaps |
| `coach_application` | High | How the AI Coach should use this page |

### 3.4 Chunk Metadata (Required)
Every chunk must carry:
- `document_id`
- `chunk_type`
- `leadership_level`
- `ai_era_criticality`
- `intervention_affinity` (person / system / hybrid / both)
- `evidence_strength`
- `coach_conversion_priority`
- `related_constructs` (controlled vocabulary terms)
- `parent_section`
- `last_hardened` (inherited or chunk-level)

---

## 4. Retrieval Priority Weights (Default)

| Signal | Weight | Rationale |
|--------|--------|-----------|
| Exact construct match (Taxonomy term) | +5 | Precision |
| `chunk_type` = behavioral_signals / diagnostic / person_vs_system | +4 | Highest coach conversion |
| `coach_conversion_priority` = High | +3 | Actionability |
| `ai_era_criticality` = Critical (when query is AI-related) | +3 | Current risk landscape |
| Matching `intervention_affinity` to current Person-vs-System pre-scan | +3 | Decision alignment |
| `evidence_strength` = Strong | +2 | Reliability |
| Explicit multi-hop relationship to already-retrieved Tier 1 page | +2 | Integration |
| `leadership_level` match | +2 | Relevance |
| Recency of `last_hardened` | +1 | Freshness (see philosophy below) |
| `evidence_strength` = Thin | –2 | Caution |
| Generic / low-specificity chunks | –3 | Avoid fluff |
| Actively suppressed chunk types in current mode (see §8) | –5 or exclude | Safety & focus |

**Freshness Philosophy:** Stability of core frameworks is valued. `last_hardened` receives only modest weight so that well-established Strong content is not constantly displaced by minor edits. Major conceptual updates should be accompanied by explicit version notes and Golden Question re-testing.

---

## 5. Mode-Specific Weight Overrides & Suppression Rules

| Mode | Boost | Suppress / Down-rank |
|------|-------|----------------------|
| **Crisis / Toxic (Path F)** | DARK-001, SAFE-001, ENERGY-001, BRIDGE-001 containment & person_vs_system chunks; `failure_mode` | Pure developmental, inspirational, or low-relevance framework chunks |
| **Overwhelmed (Path K)** | ENERGY-001 recovery, single BRIDGE-001 micro person_vs_system or diagnostic chunk | Almost everything else; hard limit on number of chunks |
| **AI-Era** | `ai_era_criticality=Critical`, SAFE-001 (voice about AI), Decision Drift / Judgment Depreciation, Amplified Oversight | Low-AI-relevance developmental content |
| **System Design (Paths C, H, I)** | `intervention_affinity=system` or `hybrid`, integration chunks, cascading implications | Pure person-focused skill chunks unless hybrid is required |
| **Diagnosis (Path B)** | BRIDGE-001 Dashboard + person_vs_system, SAFE/ENERGY/CAP/AI as indicators require | Premature action-design chunks before diagnosis stabilizes |

**Negative Retrieval Rule:** In Crisis and Overwhelmed modes, actively suppress (or heavily penalize) chunks that increase cognitive load without immediate protective value.

---

## 6. Query Understanding & Routing Rules

1. Map user language to controlled vocabulary (01) before retrieval.
2. Classify into Path type (Diagnosis / Design / Crisis / Development / AI-Governance / Meta) using 03.
3. Identify primary Super Page owner of the core construct.
4. Run Person-vs-System pre-scan (02) to set `intervention_affinity` filter preference.
5. **Escalation / Safety Filter:** If query language matches any Escalation trigger (02 / 00) → boost DARK-001 / SAFE-001 / containment chunks, suppress developmental content, and prepare escalation language. Do not perform deep developmental retrieval.
6. If user appears overwhelmed → force Path K retrieval profile.
7. If cultural context unknown → apply conservative bias: prefer chunks that treat voice/challenge/sponsorship as higher power-distance sensitive; surface the assumption.
8. Check for conflicting high-scoring chunks (see §9).

---

## 7. Multi-Hop Retrieval Protocol

When a Tier 1 Super Page is retrieved:
1. Immediately consider its highest-weight relationships from 01.
2. Pre-fetch or rank highly the 1–3 most relevant linked Super Pages or chunks.
3. Surface integration points explicitly rather than treating pages as isolated.
4. Prefer relationship types: enables, requires, threatens/erodes, cascades into, integrates with.
5. Maximum useful multi-hop depth for most responses = 2.
6. If multi-hop surfaces a contradiction → follow §9.

---

## 8. Minimum Viable Retrieval Sets (by Path)

| Path | Minimum Viable Set (must attempt to retrieve) |
|------|-----------------------------------------------|
| **B – Cascade Diagnosis** | BRIDGE-001 (Dashboard + person_vs_system) + at least one substrate (SAFE / ENERGY / CAP) as indicated + diagnostic or behavioral_signals chunk |
| **F – Crisis / Toxic** | DARK-001 (failure_mode + person_vs_system/containment) + SAFE-001 + ENERGY-001 (if contagion risk) |
| **K – Overwhelmed** | ENERGY-001 (recovery) + one micro BRIDGE-001 person_vs_system or diagnostic chunk only |
| **D – AI / Judgment** | AI-001 + SAFE-001 (AI voice/override) + person_vs_system or failure_mode related to Decision Drift |
| **C / H / I – System Design** | Primary design Super Page(s) + SAFE-001 + ENERGY-001 (substrates) + integration chunks |
| **E / J – Development** | PIPE-001 or CAP-001 or BRIDGE-001 + second-order observation / diagnostic chunks + dosage guidance |

If the minimum viable set cannot be satisfied, the Coach must surface the gap rather than proceed with incomplete high-stakes advice.

---

## 9. Handling Conflicting Chunks

When two or more high-scoring chunks conflict (different recommendations, different evidence_strength, or explicit contradiction flags):

1. Prefer the chunk with higher evidence_strength.
2. Prefer the more recently hardened chunk if evidence_strength is equal.
3. Retrieve behavioral signals and diagnostic questions from the Super Page's own §3 and §4 sections (see §10).
4. **Never silently resolve.** Surface the tension to the user using language from 00 Authority hierarchy:  
   “There is a known tension in the library between X and Y. Here is how they relate…”
5. If the conflict is material to a Person-vs-System decision or safety issue, elevate it.

---

## 10. Where Behavioral Signals and Diagnostic Questions Live

- Both live **inside each Super Page** — §3 Behavioral Indicators Library and §4 Diagnostic
  Question Bank, per the Mandatory Template in 00 §5. They are authoritative there.
- Retrieve them as standalone high-priority chunks (see §11 chunking principles); they are
  designed to be understandable in isolation.
- For cross-domain scanning, load the §3/§4 sections of the two or three Super Pages the query
  touches rather than seeking a consolidated view.

> **Note (2026-07-26).** Earlier versions of this section described a
> `Master_Behavioral_Signals_Library.md` and a `Master_Diagnostic_Question_Bank.md` as derived
> convenience views. Neither was ever built. The Super Page sections are the only source, so the
> preference rule they governed is no longer needed.

---

## 11. Golden Questions as Retrieval Tests (Strengthened)

The 15 Golden Questions in 00 are the official retrieval validation set.

**Pass Criteria (per question):**
- Correct primary Super Page(s) appear in Tier 1 results.
- Top-5 chunks include at least two of: `diagnostic`, `person_vs_system`, `behavioral_signals` with High coach_conversion_priority.
- Evidence strength and any contradiction flags are preserved and visible.
- Multi-hop questions surface the correct integrating relationship within top results.
- No hallucinated content is required to answer.

**Regression Rule:** Any Super Page update or ranking change that causes a Golden Question to fail is a release blocker until fixed.  
Log failures and resolutions.

---

## 12. Citation & Traceability Format (Mandatory for Coach)

When drawing on library content, the AI Coach should cite in a lightweight, consistent form:

- Short form (most responses): “per the Observation-to-Coaching Bridge Super Page (person-vs-system section)…” or “per SAFE-001 behavioral signals…”
- Precise form (when traceability matters): “per `BRIDGE-001` / `person_vs_system` / [short section descriptor]”
- Always pair citations with evidence_strength when the claim is material: “(evidence: Strong)” or “(evidence: Emerging — use with caution)”

Never present library content without a conceptual or ID-level citation when the stakes are medium or high.

---

## 13. Anti-Hallucination & Fallback Rules

1. If no Tier 1 or strong Tier 2 chunk scores above threshold → respond with “The library is currently thin / silent on this exact point” + closest available material + residual gap.
2. Never fill gaps with parametric knowledge presented as library content.
3. Always communicate evidence_strength of the primary source used.
4. When contradictions exist → surface them (do not average or choose silently).
5. Prefer “here is the closest framework + how it applies” over invention.
6. In Crisis or Overwhelmed modes, prefer under-retrieval + protection over comprehensive but noisy retrieval.

---

## 14. Special Retrieval Modes (Summary)

- **Crisis / Toxic:** Boost containment & failure modes; suppress developmental noise; escalate on triggers.
- **Overwhelmed (Path K):** Extreme brevity; ENERGY + one micro decision chunk only.
- **AI-Era:** Boost Critical AI constructs + Safety for override + Decision Drift.
- **System Design:** Bias system/hybrid intervention_affinity + integration chunks.
- **Diagnosis:** Stabilize sensing before action-design chunks.

---

## 15. Cultural Context Retrieval Bias (Operationalized)

When cultural context is unknown:
- Prefer chunks that treat voice, challenge, dissent, and sponsorship as potentially higher power-distance sensitive.
- Down-rank or contextualize chunks that assume low power-distance / high psychological-safety norms as universal.
- Always surface the assumption per 02 Cultural Context Protocol.
- Once culture is declared, re-rank and recalibrate.

---

## 16. Worked Retrieval Example (Illustrative)

**User query:** “My directors keep going silent in reviews and I’m seeing the same risk-averse behavior across three teams. I think I need to coach them harder on courage.”

1. **Classification:** Diagnosis + possible system pattern (Path B). Recurrence across people → system bias.
2. **Taxonomy map:** Psychological Safety, Artificial Harmony, Cascade Distortion, Person-vs-System, Enabling Leadership.
3. **Tier 1:** BRIDGE-001 (primary) + SAFE-001.
4. **Pre-scan:** Strong system-generated signal (recurrence) → prefer `intervention_affinity=system/hybrid` and `person_vs_system` chunks.
5. **Multi-hop:** Energy (possible depletion) and Capacity for Complexity also considered.
6. **Ranking:** Boost SAFE-001 behavioral_signals (Artificial Harmony), BRIDGE-001 person_vs_system (recurring pattern rule), diagnostic questions distinguishing safety vs. capacity.
7. **Conflict check:** None material.
8. **Output preparation:** Surface that “coach them harder on courage” is likely the wrong person-focused move; run full Person-vs-System; recommend system diagnosis first.
9. **Citation:** Ready to cite BRIDGE-001 person_vs_system + SAFE-001 Artificial Harmony signals (evidence: Strong/Moderate).

---

## 17. Relationship to Other Control Documents

- **00** defines Super Page Template, metadata, authority, Golden Questions, anti-patterns. This Playbook operationalizes retrieval against them.
- **01** supplies controlled vocabulary and multi-hop map.
- **02** supplies reasoning protocol, Person-vs-System pre-scan, dosage, escalation, and second-order moves that shape filters and ranking.
- **03** supplies Path logic and Super Page ownership. This Playbook executes the retrieval for what 03 decides is needed.

---

## 18. Implementation Notes (for RAG System Builders)

- Prefer hybrid search (dense + keyword/Taxonomy term matching).
- Re-rank with the priority weights in §4 and mode overrides in §5.
- Store full chunk metadata for filtering, explanation, and citation.
- Log Golden Question retrieval performance as a standing quality metric; treat failures as blockers.
- When Super Pages are updated, re-chunk and re-index.
- Support citation of `document_id` + `chunk_type` + section.
- Implement soft filters from the Pre-Response Reasoning Protocol rather than brittle hard exclusion in normal modes.
- Implement hard suppression only in Crisis and Overwhelmed modes.

---

## 19. Maintenance Rules

- Changes to chunking rules, priority weights, special modes, or Golden Question criteria require version bump and user approval (Control Layer Change Protocol).
- New Super Pages must be chunked according to §3 before production.
- Golden Question test suite must be re-run after significant content or ranking changes.
- Residual retrieval failure modes must be logged.
- Conflicting-chunk and minimum-viable-set rules are binding.

---

## 20. Final Retrieval Instruction to the AI Coach

Retrieve as a cascade-protective decision-support system, not as a generic search engine.  
Prefer actionable, high-conversion, evidence-aware, multi-hop-aware chunks.  
Respect minimum viable sets and mode-specific suppression.  
When chunks conflict, surface the tension.  
When the library is thin, say so.  
When the user is overwhelmed or in crisis, retrieve less and protect more.  
Always enable the Person-vs-System decision, second-order observation, and clean citation.

---

**End of 04_Retrieval_Playbook_and_Priority.md (v1.2)**  
**Change Log (v1.0 → v1.1):** Added practical chunk granularity guidance; mode-specific weight overrides + negative retrieval/suppression rules; Minimum Viable Retrieval Sets per Path; Conflicting Chunks resolution protocol; Master vs Super Page preference rule; strengthened Golden Question pass/fail and regression criteria; mandatory Citation & Traceability format; operationalized Cultural Context retrieval bias; retrieval-time Escalation/Safety filter; Freshness philosophy; full worked retrieval example; tightened all sections for implementability and cascade protection.
