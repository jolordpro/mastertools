# Shakedown — Strategy & Plans Reference

Audits roadmaps, business plans, policies, proposals, budgets, and
operational designs. Challenger asks whether this is the right plan;
Shakedown assumes the direction is set and asks one narrow question: **is
the plan written right?** Its assumptions are stated and evidenced, its
numbers reconcile, its sequence holds, every deliverable has an owner, every
goal has a measure. Whether the plan survives attack (hostile parties, what
success breaks, a red team trying to sink it) is stress-test's question.
Sections 4 and 5 check only that the plan names each risk and its answer;
hand the full attack to stress-test. If the audit keeps finding that the
direction itself is the problem — that's the cluster rule; hand it to
Challenger.

## Contents

1. Assumption audit
2. Sequencing and the critical path
3. Resourcing reality
4. Dependency and counterparty risk (named in the plan?)
5. Downstream and second-order effects (named in the plan?)
6. Measurability and kill criteria
7. Policy, legal, and compliance exposure
8. The document as an instrument
9. What first passes miss (sweep list)

---

## 1. Assumption audit

- Extract every load-bearing assumption — stated and, more importantly,
  unstated. (Unstated ones hide in verbs: "we'll convert the pilot" assumes
  the pilot succeeds, the champion stays employed, and budget exists next
  quarter.)
- For each: what's the evidence, what's the cost if wrong, and is it
  checked *before* or *after* the plan bets on it?
- Flag single-point-of-failure assumptions: one champion, one client, one
  channel, one key person, one vendor.
- Numbers audit: where did each figure come from? Estimates presented as
  data are findings. Totals reconcile; timelines sum; unit economics hold
  at both the pilot scale and the promised scale.

## 2. Sequencing and the critical path

- Map the dependency chain. What is actually on the critical path to the
  milestone, and what merely looks urgent?
- **Slack audit:** where does the timeline absorb a slip? A plan with zero
  slack is a plan that misses; say where it misses first.
- Reversed dependencies: steps scheduled before their prerequisites
  (selling before the demo exists; hiring before the budget clears).
- Long-lead items started late: legal review, procurement, approvals,
  anything involving another organization's clock.
- The week-by-week check near the milestone: the last 20% of the timeline
  carrying 50% of the work is the most common plan defect there is.

## 3. Resourcing reality

- Hours math: does the plan's workload fit inside the actual available
  hours of the actual people, after their existing commitments? Sum it.
- The "who exactly" test: every deliverable has a named owner, not a role
  ("marketing will…" — who?).
- Skill assumptions: does the plan require capabilities the team is
  assumed to have? Flag where the plan quietly depends on learning-while-
  delivering on the critical path.
- Money: burn vs. runway across the plan period; unbudgeted items (tools,
  legal, contractors, travel) that always appear.

## 4. Dependency and counterparty risk (named in the plan?)

- Every external party the plan depends on (client, vendor, platform,
  regulator, partner): what does the plan do if they're slow, change
  terms, or exit? "They won't" is not a mitigation.
- Platform risk: built on someone else's API, policy, or algorithm —
  what's the exposure to their next change?
- Contract state: are the dependencies on handshakes or paper? Handshakes
  on the critical path are High findings.

## 5. Downstream and second-order effects (named in the plan?)

- If this plan succeeds, what does success break? (Capacity: the pilot
  wins and three more clients arrive — can the operation serve them, or
  does success create the failure?)
- Precedents: what does this decision commit future decisions to —
  pricing anchors, service-level expectations, governance patterns that
  will be cited later?
- Incentives created: what behavior does the plan reward, and is that the
  behavior wanted? (Metrics that will be gamed, discounts that train
  clients to wait.)
- Exit and unwind: if this is stopped in six months, what's the cost of
  unwinding — contracts, data, reputation, people?
- Who is affected but not consulted — and do any of them have veto power
  they'll discover later?

## 6. Measurability and kill criteria

- Every goal has a measure, a baseline, and a date — or it's a wish.
  "Grow engagement" is a finding; "X to Y by date, measured how" is a
  goal.
- Kill criteria: what result, by when, means stop or pivot? Plans without
  kill criteria run on sunk cost. Their absence is a Medium finding
  minimum on anything with real spend.
- Review cadence: when does the plan meet its own numbers, and who is in
  the room?

## 7. Policy, legal, and compliance exposure

Mandatory at Full tier for policies, nonprofit/board work, HR-adjacent
plans, and anything regulated:

- Jurisdiction check: does the plan comply with the actual governing law
  of its entity and activities (state nonprofit statutes, employment law,
  data-privacy regimes for the audiences touched)?
- Governance: does anything here exceed the authority of the person or
  body deciding it (board approval needed, quorum rules, conflict-of-
  interest provisions triggered)?
- Duty-bearing roles: clinical, fiduciary, or licensed-professional
  obligations that constrain what the plan can ask of those people.
- Insurance and liability surface: activities the plan adds that the
  current coverage doesn't contemplate.
- Documentation trail: for decisions that may be challenged later, does
  the plan create the record that protects the organization?
- Flag-for-counsel discipline: Shakedown marks legal exposure; it does not
  clear it. Findings in this section recommend review, never sign-off.

## 8. The document as an instrument

The plan is also a document someone must act from:

- Can the owner of each workstream find their commitments without reading
  the whole thing?
- Is there a one-page version of the truth (timeline, owners, numbers)
  that will stay current, or will the plan fork into stale copies?
- Ambiguity scan: every "should," "aim to," "as needed," and "TBD" on the
  critical path is a deferred decision wearing a plan's clothes. List
  them; each needs an owner and a date.

## 9. What first passes miss (sweep list)

Steer the Sweep with these — the plan defects that survive an honest first
audit:

- **Unstated assumptions hiding in verbs** — "we'll convert," "they'll
  renew," "the team will absorb it"; the audit checked the stated
  assumptions and read past the grammar.
- **Single points of failure that wear a team's name** — "marketing owns
  it" concealing that one specific person is the plan.
- **Long-lead items started late** — legal, procurement, approvals,
  anything on another organization's clock; invisible until the dependency
  chain is drawn backward from the milestone.
- **The last 20% carrying 50% of the work** — timeline compression near
  the milestone; each week looks plausible alone.
- **Who is affected but not consulted** — the stakeholder with veto power
  discovered in month four.
- **What success breaks** — capacity, support, pricing precedent; audits
  stress failure and forget to stress the win.
- **Kill criteria absent on the biggest bet** — checked for small
  experiments, waved through on the flagship commitment.
- **The plan's own maintenance** — who updates the document, and does the
  one-page truth exist, or will three stale copies fork by week six?
