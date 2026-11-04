---
name: capacity-audit
description: Diagnose whether a People Leader problem is capacity (role design) or capability (skill), then produce a capacity audit with a feasibility verdict and role-redesign plan — from the Leadership RAG Library's PEOPLE-001 and PIPE-001. Use when a leader says their managers aren't performing, asks what training or program to buy for the middle layer, describes overloaded or burning-out People Leaders, mentions adding responsibilities without removing any ("do both"), reports a newly promoted manager-of-managers struggling six months in, or asks "is this a capability problem or a capacity problem". Also use for designing or reviewing a People Leader role, span, or decision rights. Not for coaching one person's skill gap when the role itself is sound, individual-contributor workload, or personal burnout support.
---

# Capacity Audit (PEOPLE-001 + PIPE-001)

PEOPLE-001 finds that most organizations treat People Leader underperformance as a capability
problem and respond with training, when many of the failures are capacity problems in the role's
design. This instrument exists to test capacity **before** anyone buys training.

## Find the library

```
python3 -I <this skill>/../leadership-coach/scripts/library.py where
```

Exit 0: the first line printed is `<REPO>`. Exit 3: the library isn't on this machine. Say so once,
don't run this instrument from general knowledge, and give the fix from the `leadership-coach`
skill's "Find the library first" section.

```
<REPO>  = the folder `library.py where` prints
PEOPLE  = <REPO>/Core_Canonical_Super_Pages/People_Leader_Role_Redesign.md
PIPE    = <REPO>/Core_Canonical_Super_Pages/Leadership_Pipeline_Passages.md
ENERGY  = <REPO>/Core_Canonical_Super_Pages/Resilience_Energy_Management.md
CAP     = <REPO>/Core_Canonical_Super_Pages/Capacity_for_Complexity_and_Enabling_Leadership.md
```

## Step 1 — Load and reframe the question

Read `<REPO>/CLAUDE.md`, then the **Binding rules** section of
`<this skill>/../leadership-coach/SKILL.md`. Every rule there binds this instrument; the one most
often broken here is marking your own cadences and counts ("review monthly", "top five
decisions", "30/60/90") as practitioner judgment, since the library sets no general review cadence.

Then `PEOPLE` (§2.1 capacity vs. capability, §2.2 the "do both" trap, §2.3 cascade-critical work,
§2.4 audit method, §2.5 redesign levers, §2.6 sequence, §2.9 the 90-day package), and the rest of
this path's minimum set (Path E, `04_Retrieval_Playbook_and_Priority.md` §8): `ENERGY` for the
depletion stages (§2.4 of `ENERGY`) and the energy protection the role needs, and `CAP` for the
complexity-reduction test that separates a capacity limit from a substrate or design problem.

**If the user opened with "what training should we buy" — do not answer as asked.** Explain that
PEOPLE-001 names treating a capacity problem as a capability problem as the usual misdiagnosis,
and that the audit tests which one this is first. Training bought against a capacity constraint
wastes budget and confirms to the leader that they are the problem.

**If the subject recently moved from managing others to managing managers**, also read `PIPE`
§2.2–§2.3 and run the three-part transition diagnostic: skills, time application, work values.
Ask which of the three is most incomplete right now — that answer drives the support package.
An incomplete Passage 2 and a capacity-starved role look identical from the outside and need
different fixes.

## Step 2 — Run the six-step audit (§2.4 of PEOPLE)

Conduct as an interview plus a data request. Do not estimate on the leader's behalf — ask for
real artifacts.

1. **Time map:** request 1–2 weeks of actual calendar. Categorize every block as previous-level
   work vs. cascade-critical work, expressed as a **percentage**. The percentage is the headline
   finding; get it or name it as missing.
2. **Decision load map:** which decisions route through this role, how many, at what cadence,
   and which of them require this level.
3. **Recovery and surplus check:** is there energy surplus available for the cascade-critical
   work at all? Cross-reference the `ENERGY` §2.4 depletion stages if depletion signals appear.
4. **Metric alignment check:** what is this role measured and rewarded on? If metrics
   reward previous-level work, the role design is fighting the expectation.
5. **AI load check:** has AI-related work (verification, oversight, agent management) been added
   without anything removed?
6. **Feasibility verdict:** **feasible / residual / impossible.** State it plainly. "Impossible"
   is a legitimate and common verdict; do not soften it into "challenging."

## Step 3 — Name the "do both" trap if present

If new expectations were added with nothing removed, name it explicitly as the trap it is (§2.2 of
`PEOPLE`) and state the six predicted consequences the page lists. PEOPLE-001 calls "do both" the
most common and most damaging instruction — being polite about it here helps no one. A positive
indicator in §3 of `PEOPLE` is literally that "do both" gets named and rejected in real
conversations.

## Step 4 — Design the redesign

Select from the nine levers in §2.5 of `PEOPLE` — decision rights, work content and **stop list**,
time architecture, span and structure, support infrastructure, metrics and accountability, energy
and recovery design, AI workflow design, adaptive space protection.

Follow the capacity-before-capability sequence in §2.6 of `PEOPLE`. Capability work is legitimate
— but it comes after, or alongside, a redesign that makes the role feasible.

Assemble the **90-day Minimum Viable Redesign package** (§2.9 of `PEOPLE`). Two elements are
load-bearing and must not be dropped:

- the **stop list, explicitly protected from quiet re-expansion** (name who protects it and how
  it gets reviewed), and
- the **written rejection of unbounded "do both."**

Close with a 90-day review of time allocation and cascade-health signals under the leader.

## Step 5 — Output

Produce an **audit document as a file**, not a chat answer. Structure:

1. Findings per audit step, with the time-map percentage stated numerically.
2. Primary constraint: the one thing most responsible for the gap.
3. **Feasibility verdict:** feasible / residual / impossible.
4. Selected redesign levers with specific changes, not categories.
5. The 90-day package including the protected stop list.
6. **Intervention Mode block** per the library's `CLAUDE.md`. This page carries a strong
   **System** bias — recommending training before a capacity verdict is the named misdiagnosis.
   If you land on Person-focused or Hybrid, justify it against that bias explicitly.
7. Any unavailable data named as a gap, not estimated.

**Where the file goes:** the user's current working directory, or a location they name — never a
temp or scratchpad path. This is a document they will take to whoever owns the role. Ask if the
destination is unclear. If the audit is client-facing, offer a branded version via the
`lord-brand` skill.

**Path K:** an overwhelmed leader gets the five-minute version first, not the six-step audit —
ask "what were you told to stop doing when you took this on?" If the answer is nothing, name the
"do both" trap, agree one stop, and schedule the full audit for when there is capacity to run it.

## Failure modes for this instrument

"Do both" without redesign · capability misdiagnosis · expectation inflation · decision-rights
congestion · span/structure impossibility · AI load without redesign · **redesign theater**
(announced changes that don't alter time, rights, or metrics) · capable leader exit while toxic
performers are retained. Detail in §5 of `PEOPLE`.
