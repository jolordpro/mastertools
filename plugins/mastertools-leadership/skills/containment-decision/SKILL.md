---
name: containment-decision
description: Run the Containment vs. Recovery decision for a toxic or dark-side high performer, using the Leadership RAG Library's DARK-001 framework. Use when a leader describes someone who delivers strong results while people around them are afraid, leaving, or silent; Jekyll-and-Hyde or inconsistent-justice leadership ("which version will I get today"); a results shield protecting bad behavior; credit capture or blame displacement; or asks directly "should we coach this person or move them out", "we've coached them for a year and nothing changed", "how do I handle a brilliant jerk". Also use for designing a bounded recovery experiment or a post-containment cascade recovery plan. Not for peer or individual-contributor conflict, a plain low performer, or a leader who is demanding or blunt with no fear or harm around them.
---

# Containment vs. Recovery (DARK-001)

The library's highest-stakes decision instrument. It has a hard default that ordinary coaching
instinct gets wrong — hold it.

## Find the library

```
python3 -I <this skill>/../leadership-coach/scripts/library.py where
```

Exit 0: the first line printed is `<REPO>`. Exit 3: the library isn't on this machine. Say so once,
don't run this instrument from general knowledge, and give the fix from the `leadership-coach`
skill's "Find the library first" section.

```
<REPO> = the folder `library.py where` prints
PAGE   = <REPO>/Core_Canonical_Super_Pages/Dark_Side_Toxic_High_Performers.md
CQ     = <REPO>/Core_Canonical_Super_Pages/Cultural_Intelligence_and_Context.md
```

## Step 1 — Escalation screen, before anything else

Read `<REPO>/CLAUDE.md`, the **Binding rules** section of
`<this skill>/../leadership-coach/SKILL.md` (every rule there binds this instrument), and `PAGE`.

If **legal risk, harassment, or integrity issues** are present → escalate immediately per
`<REPO>/00_START_HERE.md` §7. Do not coach, do not run the framework, do not weigh options. Name
the escalation, give the handoff language, offer to help prepare questions for HR/legal/the
appropriate human. This screen precedes every other step and is non-negotiable (`PAGE` §2.2,
final containment trigger).

If the screen is clear, finish loading this path's minimum set (Path F,
`04_Retrieval_Playbook_and_Priority.md` §8): SAFE-001 for the safety damage around the person,
ENERGY-001 for contagion and the depletion of the people absorbing it, and BRIDGE-001 for the
Person-vs-System test. If you can't reach one, say which and what it leaves open.

## Step 2 — Differential diagnosis before labeling

Run §2.7 of `PAGE`. Four candidate readings, and you must actively test between them:

1. Tough-but-fair leadership
2. Cultural style difference
3. Capacity/role-complexity compensation (someone drowning, not malicious)
4. True toxic high performer

Decide on **cascade-damage evidence, not style**. The test is what happens to the people around
them across layers, not whether they are blunt or demanding.

**If culture is contested or the parties span cultural contexts** → run the five-step
Assumption-Check Worksheet in `CQ` §2.7 (with §2.2 of `CQ` for the universal-vs-contingent split)
*before* applying any toxic label. The library refuses both errors: mislabeling culturally direct
leadership as toxic, and excusing genuine fear as "just the culture." Name that dual refusal
explicitly when it applies. If the culture is unknown, state the higher power-distance assumption
you are making.

Use the micro-behavioral clusters in §2.1 of `PAGE` to gather evidence: results-plus-fear, credit
capture, adaptive space capture, sponsorship distortion, justice variability, multi-layer
contagion, AI opacity shield.

## Step 3 — Apply the decision framework exactly as written

From `PAGE` §2.2 — do not paraphrase these into "it depends":

- **Containment if ANY of the six triggers hold.** Any single one is sufficient.
- **Recovery only if ALL six preconditions hold.** A single failed precondition means recovery is
  not available.

**Default bias: containment first when damage is multi-layer or accelerating**, re-evaluating
recovery later if conditions change. The library sets no interval for that re-evaluation: if you
suggest one, mark it as your judgment. The 60–90 day time box belongs only to a recovery
experiment; never reuse it as a "typical" interval after containment. Endless coaching while the
cascade absorbs damage is a named high-cost failure mode.

Report your reasoning **criterion by criterion:** state each trigger and precondition, the
evidence for or against it, and what evidence is missing. A decision that doesn't show its work on
each criterion is not this instrument.

**Hold the default under pushback.** Users often want permission for another development attempt.
If the criteria say containment, say so, cite DARK-001, and surface the tension rather than
softening the finding (the Containment vs. Recovery tension is logged in
`05_Contradiction_and_Evidence_Log.md` §2.7). The human makes the call — with eyes open, not with a
smoothed-over analysis. Note what the library says the cost of delay is.

## Step 4 — Build the chosen path

**If containment** → the "what good containment looks like" checklist in `PAGE` §2.2 (six
elements: timely decision with cascade-health rationale, tightly bounded scope, immediate
protection of surrounding people, simultaneous enabler diagnosis, cascade recovery support, clean
documentation and no prolonged ambiguity). Then the Post-Containment Cascade Recovery Sequence in
`PAGE` §2.9.

**If recovery** → generate the bounded recovery experiment as a written document from the
seven-element template in `PAGE` §2.2: 3–5 observable behaviors with success metrics; a 60–90 day
time box; a **pre-agreed containment trigger with a named executor**; intensified multi-layer
sensing; an explicit cascade protection plan; developmental coaching focused on second-order
observation and justice consistency; enabler neutralization; and a go/no-go review on multi-layer
behavioral data, not hope or short-term results.

**Always, both paths:**

- **System enabler mapping** (`PAGE` §2.5): which of the eight enablers built and protected this
  pattern, and the paired redesign. Containment without enabler redesign produces the next toxic
  high performer in the same structure. State that consequence explicitly.
- **Cascade protection during the process** (`PAGE` §2.4): the six protected assets: safety,
  energy, adaptive space, sensing, talent, communication.
- If political or resource constraints block the full move, use Minimum Viable Containment &
  Protection (`PAGE` §2.10) rather than doing nothing.

## Step 5 — Output

1. **Decision:** containment or recovery, stated plainly up front.
2. **Criterion-by-criterion evidence table.**
3. **Differential result:** why this is toxicity rather than the three alternatives (and the CQ
   assumption check if it ran).
4. **Intervention Mode block** per the library's `CLAUDE.md`. Note that this page's affinity is
   Hybrid: the person decision and the enabler redesign both belong in the plan.
5. **Enabler redesign list** and **cascade protection plan**.
6. If recovery: the contract as a file. If containment: the recovery sequence as a file.

**Where files go:** write deliverables into the user's current working directory (or a location
they name), never a temp or scratchpad path. These are documents a leader will take into an HR
or executive conversation; a throwaway path makes them unusable. If the working directory is
unclear, ask before writing. Documents in this domain stay deliberately unbranded and sober —
no visual treatment; they may end up in a legal file.

**Path K:** if the leader is themselves depleted or overwhelmed, the decision still gets made.
This is a protection instrument and delay costs the cascade. Deliver it short: the decision,
the two or three criteria that drove it, and the single next move. Full documentation follows once
they have capacity, and check whether they have the capacity to hold a clean process at all
(a named recovery precondition).

## Failure modes for this instrument

Results shield · endless coaching of the uncoachable · delayed containment · containment without
enabler redesign · multi-party collusion (joining a character attack on the absent person) ·
crisis exception forever · post-containment neglect. Detail in §5 of `PAGE`. Protect the dignity
of the absent party throughout — the finding is about cascade damage, not character assassination.
