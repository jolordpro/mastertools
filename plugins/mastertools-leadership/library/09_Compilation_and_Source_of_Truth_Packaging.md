# 09_Compilation_and_Source_of_Truth_Packaging.md
## Compilation, Packaging & Use as Source of Truth (Claude / External LLM)
### Control / Delivery Document
**Document ID:** CTRL-09  
**Version:** 1.0  
**Status:** Delivery Control Document  
**Last Updated:** 2026-07-23  
**Purpose:** Define how the hardened Leadership RAG Library is packaged, ordered, chunked, and governed when used as a Source of Truth by Claude or other LLMs, and by human implementers.

---

## 1. Canonical File Inventory (Current Hardened Core)

### Control Layer (must be loaded first / highest retrieval priority for rules)
- `00_START_HERE.md` (v1.2)
- `01_Taxonomy_Controlled_Vocabulary.md` (v1.2)
- `02_AI_Coach_Operating_Manual.md` (v1.1)
- `03_Master_Index_and_Reading_Paths.md` (v1.1)
- `04_Retrieval_Playbook_and_Priority.md` (v1.1)
- `05_Contradiction_and_Evidence_Log.md` (v1.0) **NEW**
- `06_Reading_Paths_and_Onboarding.md` (v1.0) **NEW**
- `07_Golden_Questions_and_Retrieval_Tests.md` (v1.0) **NEW**
- `08_Hardening_Addenda_and_Tier2_Backlog.md` (v1.0) **NEW**
- `09_Compilation_and_Source_of_Truth_Packaging.md` (this file)

### Core Canonical Super Pages (domain knowledge)
- `Core_Canonical_Super_Pages/Systems_Thinking_Complex_Adaptive_Systems.md` (SYS-CAS-001 v1.1)
- `Core_Canonical_Super_Pages/Observation_to_Coaching_Bridge_and_Cascade_Health_Dashboard.md` (BRIDGE-001 v1.1)
- `Core_Canonical_Super_Pages/Psychological_Safety_Multi_Layer.md` (SAFE-001 v1.1)
- `Core_Canonical_Super_Pages/Capacity_for_Complexity_and_Enabling_Leadership.md` (CAP-001 v1.1)
- `Core_Canonical_Super_Pages/Resilience_Energy_Management.md` (ENERGY-001 v1.1)
- `Core_Canonical_Super_Pages/AI_Transformation_Leadership.md` (AI-001 v1.1)
- `Core_Canonical_Super_Pages/Dark_Side_Toxic_High_Performers.md` (DARK-001 v1.1)
- `Core_Canonical_Super_Pages/Sponsorship_Systems.md` (SPONSOR-001 v1.1)
- `Core_Canonical_Super_Pages/Generativity_Legacy_Wisdom_Transfer.md` (GEN-001 v1.1)
- `Core_Canonical_Super_Pages/Leadership_Pipeline_Passages.md` (PIPE-001 v1.1)
- `Core_Canonical_Super_Pages/People_Leader_Role_Redesign.md` (PEOPLE-001 v1.1)
- `Core_Canonical_Super_Pages/Board_Fluency_and_Governance.md` (BOARD-001 v1.1)
- `Core_Canonical_Super_Pages/Cultural_Intelligence_and_Context.md` (CQ-001 v1.1)

**Total:** 10 Control documents + 13 Core Canonical Super Pages = 23 source files.

---

## 2. Recommended Load / Retrieval Hierarchy for LLM Use

1. **Governance & Safety Layer (always available):**  
   00_START_HERE → 02_AI_Coach_Operating_Manual → 05_Contradiction_and_Evidence_Log → 04_Retrieval_Playbook

2. **Navigation Layer:**  
   03_Master_Index → 06_Reading_Paths_and_Onboarding → 01_Taxonomy

3. **Meta-Operating System & Action Engine:**  
   SYS-CAS-001 → BRIDGE-001

4. **Substrates (retrieve early on any cascade diagnosis):**  
   SAFE-001 → ENERGY-001 → CAP-001

5. **Domain Super Pages (by situation):**  
   AI-001, DARK-001, SPONSOR-001, GEN-001, PIPE-001, PEOPLE-001, BOARD-001, CQ-001

6. **Quality & Roadmap (as needed):**  
   07_Golden_Questions → 08_Hardening_Addenda → 09 (this file)

---

## 3. Chunking & Metadata Guidance (for RAG Implementation)

Each Super Page already contains:
- Document-level metadata (ID, version, evidence_strength, leadership_level, use_case, cascade_relevance, AI-era criticality, intervention_affinity, coach_conversion_priority, contradictions_flag)
- Section structure aligned to the Mandatory Template (Definition, Frameworks, Behavioral Indicators, Diagnostic Questions, Failure Modes, Person-vs-System, Cascading Implications, AI Coach Notes, Evidence Summary, Cross-Links)

**Recommended chunking approach:**
- Preserve section boundaries (do not split mid-Behavioral-Indicator or mid-Person-vs-System block).
- Tag chunks with: `document_id`, `section_type` (framework / behavioral / diagnostic / failure_mode / person_vs_system / coach_notes / evidence), `evidence_strength`, `leadership_level`, `use_case`.
- Behavioral Indicators and Diagnostic Question Banks are high-value retrieval units — keep them intact or split only by clear sub-cluster.
- Cross-Links and Cascading Implications should remain associated with their source page for accurate synthesis.

**Anti-hallucination rules for the consuming LLM (from 00 and 02):**
- Never invent methods or evidence not present in the retrieved chunks.
- Never upgrade evidence_strength.
- Always surface Person-vs-System bias and Containment vs. Recovery bias when relevant.
- Hold universal cascade-health requirements; apply CQ-001 calibration when cultural context is present.
- Prefer Hybrid sequences recorded on the Super Pages over improvised advice.

---

## 4. Suggested System Prompt / Operating Instructions (Summary)

When this library is used as Source of Truth, the consuming model should be instructed to:
1. Treat Control documents (especially 00, 02, 05) as binding governance.
2. Retrieve and cite Super Pages by Document ID (e.g., `AI-001`, `DARK-001`).
3. Communicate evidence_strength honestly.
4. Default to the Person-vs-System and intervention biases written on each page.
5. Use BRIDGE-001 as the action-conversion engine for observations.
6. Run cultural assumption checks (CQ-001) on contested safety, toxicity, sponsorship, and AI-override diagnoses.
7. Refuse both ethnocentric imposition and cultural relativism that excuses cascade damage.
8. When capacity vs. capability is unclear, diagnose capacity first (PEOPLE-001, ENERGY-001).
9. When multi-layer toxic damage is present, default toward Containment first (DARK-001).
10. Escalate legal, harassment, or integrity issues per 02 Escalation Protocol; do not coach them away.

---

## 5. Packaging Formats

**For immediate use:**
- Directory structure as currently stored in the library folder
- All files Markdown, UTF-8, consistent heading hierarchy

**For external delivery:**
- Zip or repository containing the exact inventory above
- Optional: single concatenated “Library_Source_of_Truth.md” with clear document separators and IDs (for contexts that prefer one file)
- Optional: JSON or YAML manifest listing every file with Document ID, version, evidence_strength, and primary use_case

**Version pin:**  
Core Super Pages are at v1.1 (Hardened). Control documents 05–09 are at v1.0. Future changes must increment versions and update this manifest.

---

## 6. Post-Compilation Validation

Before treating the package as production Source of Truth:
1. Confirm all 23 files are present and readable.
2. Spot-check 5–10 Golden Questions (CTRL-07) for correct primary page retrieval and evidence discipline.
3. Verify 00, 02, and 05 are reachable and authoritative for governance questions.
4. Confirm no Super Page still carries an unhardened “v1.0” residual Tier 1 gap that was intended to be closed (all listed core pages are v1.1 except any explicitly deferred).

---

## 7. Maintenance & Evolution

- New Hardening Addenda → update the relevant Super Page version + CTRL-05 + CTRL-08 + this manifest.
- New Tier 2 Super Pages → add to inventory only after explicit decision per CTRL-08 rules.
- Evidence upgrades require real field or research support and must be recorded in CTRL-05; never silent.

---

**End of CTRL-09 — Compilation and Source of Truth Packaging (v1.0)**

**Library Status:**  
The Leadership RAG Library core is compiled, governed, navigable, testable, and ready for use as a Source of Truth. Residual Hardening Addenda and Tier 2 expansion remain optional and backlog-managed.
