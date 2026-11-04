# Motion for AI and agent states

The governing principle: **AI expresses intent; the motion system owns mechanics** (ADV 5.1). An agent, a model,
or a product team says "state: tool use, priority: high". The system resolves that to approved tokens, reduced-
motion forms, and examples. Nobody invents keyframes for "thinking". Why: generation is cheap, so the scarce
asset is the system that tells it what belongs (KB-C Part IX), and for AI interfaces motion is part of *trust
design*: users need to know what changed and who or what caused it.

## Contents
1. State grammar
2. Agency map
3. Intent-to-mechanics resolution table
4. Design rules
5. Tokens and cards for AI states
6. Reduced and instant forms
7. Streaming and partial results
8. Multimodal events
9. Context pack for agents that author motion
10. Pipeline and guardrails
11. Anti-patterns
12. Validation

## 1. State grammar (ADV 5.3, KB-C 139)
Start from the product's real state machine, not from a mood. Typical states, in order of a request:

| State | What the person must understand | Motion strategy | Risk to avoid |
|---|---|---|---|
| Listening | the system is receiving input | subtle presence; responsive but stable | fake "brain" activity |
| Interpreting | the task was accepted | minimal acknowledgement | excessive spinner time |
| Planning | actions are being prepared | low-variance activity | pretending to expose hidden reasoning |
| Tool use | the system is acting somewhere | clear attribution of agency (what, where) | ambiguous autonomous change |
| Partial | useful work is arriving | incremental assembly | content storms |
| Waiting | blocked on something (user, external system) | stable expectation cue | anxiety loops |
| Uncertain | outcome not settled | calibrated, restrained state | false confidence |
| Complete | the task resolved | decisive settle | confetti for everything |
| Handoff | control returns to the person | explicit change of agency | silent takeover |
Add product-specific states (error, recovery, interrupted, expired, persistent; CMP C14) with an entry trigger, an
exit trigger, and a motion responsibility each. Interruption is first-class: a user can stop or redirect the agent
at any state, and the motion must retarget, never finish a lie.

Identity precedent: Google's dynamic dots use a reduced dynamic form of the logo for states such as listening,
thinking, replying, confirming, with "controlled spontaneity" from consistent paths, arcs, timing, and easing
(KB-C Part IV). Brand can be the state-communication layer, but only if every state is distinguishable without it.

## 2. Agency map (ADV 5.4)
Map every motion event by causal ownership and give each a distinct treatment:
- **User-caused**: direct, immediate, no latency theater.
- **Agent-caused**: attributed to the system, interruptible when appropriate.
- **External-system-caused**: visually distinct from local user or agent actions.
- **Environment-caused**: ambient, lowest priority.
- **Unknown / uncertain**: no motion that implies certainty.
Motion semantics must change at the moment agency changes (handoff), not after.

## 3. Intent-to-mechanics resolution table
What the AI (or product code) may state, and what the system resolves it to. The third column is what the AI must
not invent.

| AI expresses | System resolves | Do not ask AI to invent |
|---|---|---|
| intent: confirm | `semantic.verb.confirm` | raw cubic-bezier |
| intent: reveal | `semantic.verb.reveal` | arbitrary keyframes |
| state: generating | `ai.state.partial` | a visual metaphor for "thinking" |
| agency: tool use | `ai.state.toolUse` (+ attribution cue) | implementation-specific animation code |
| priority: high | `attention.high` (concurrency ceiling applies) | custom timing from scratch |
| accessibility: reduced | `modes.reduced` + `reducedMotion.strategy` | a slow-motion clone of the default |
| certainty: low | `ai.state.uncertain` | celebratory completion |

## 4. Design rules
1. **Motion must not claim more than the system knows.** Uncertain gets a calibrated, quieter treatment. Progress that is not measurable is not shown as a filling bar.
2. **Do not dramatize hidden reasoning.** Planning is a low-variance activity state, not a light show implying cognition the user cannot inspect.
3. **One attention event at a time.** Concurrency ceiling applies even when several things are happening server-side.
4. **Attribute action.** Tool use shows *what* system acted and *where*; changes the agent makes to the user's content are marked as agent-caused and reversible.
5. **Meaning never lives only in motion.** Pair every state with a text, icon, or role cue; screen readers get status updates immediately (not after animation).
6. **Completion is proportional.** Reserve celebration for rare, meaningful completions; most completions are a short decisive settle.
7. **Waiting must not accumulate anxiety.** No endless pulsing; after a threshold switch to a stable cue plus text, and offer cancel.
8. **Handoff is explicit.** Control returning to the user gets a distinct, brief transition and focus move.

## 5. Tokens and cards for AI states
Create a small family under the semantic tier (names are examples):
`ai.state.listening`, `.interpreting`, `.planning`, `.toolUse`, `.partial`, `.waiting`, `.uncertain`, `.complete`, `.handoff`.
Each is a behavior card (assets/behavior-card-template.md) plus a semantic token with modes. Because these states
include loops, the contract must carry a **loop policy**: `loop: none | bounded(n) | until-state-change`, a maximum
visible duration before the stable fallback, and a stop control or auto-stop. Token notes:
- States that loop use `semantic.easing.loop` (linear) or a low-amplitude spring; mark `performanceClass: continuous`.
- `reducedMotion.strategy` for loops is `static` or `state-only` with textual status; `instant` mode shows the final/stable state.
- `partial` often uses a stagger token with a `maxItems` cap; see token-architecture.md.
- Put the agency attribution cue in the card (what marks agent-caused change) and in the contract's `focus` block.

## 6. Reduced and instant forms
| State | Full | Reduced | Instant |
|---|---|---|---|
| Listening | gentle presence pulse | static indicator | static indicator |
| Planning | low-variance activity | static "working" label | label only |
| Tool use | attributed activity at the target | highlight + label, no travel | label + final state |
| Partial | incremental assembly | content appears per chunk, no motion | content appears |
| Uncertain | restrained state | text qualifier | text qualifier |
| Complete | decisive settle | short fade | state change |
| Handoff | explicit transition + focus move | fade + focus move | focus move |
Reduced motion changes how information is encoded, not just how long it takes (ADV 7.1).

## 7. Streaming and partial results
Prefer semantic component transitions over text-length-dependent keyframes (ADV 7.1). Group arriving chunks into
meaningful units (sentence or block) to avoid content storms; cap concurrent entrances; never re-animate content
already shown; keep scroll position stable unless the user is following; allow the user to interrupt mid-stream
without the layout jumping.

## 8. Multimodal events
Where the product has sound or haptics, define the **event** as the semantic unit (completed, needs-attention,
handoff) with visual, audio, and haptic channels coordinated and each optional (KB-C Part XXXVIII; ADV 22). Sound
must not imply certainty when the state is uncertain; every channel is silence-safe and screen-off-safe where relevant.

## 9. Context pack for agents that author motion (KB-C 139.2)
Give an agent: motion thesis, behavior vocabulary, semantic tokens (JSON), component contracts, anti-patterns,
reduced-motion mappings, runtime targets, approved examples, and an evaluation rubric (the intent / ownership /
hierarchy / timing / physics / choreography / restraint / context / accessibility / implementation / system-fit
scorecard in KB-C Tool 5). A compact `llm` block on tokens (`use`, `avoid`) helps; Primer publishes token usage
rules for LLMs, which is the precedent. The agent's output is a *proposal*, never a system contribution.

## 10. Pipeline and guardrails (KB-C 139.1)
```
PROMPT / INTENT -> CONTEXT PACK -> GENERATE -> VALIDATE -> HUMAN REVIEW -> ADOPT (local) -> PROMOTE (evidence + governance)
```
Validate with the token validator (no new unapproved values), schema and vocabulary checks (no near-synonym
verbs), reduced-motion presence, performance class, and a human pass on brand fit. Generation velocity must not
become governance velocity: a generated animation is cheap; a new system behavior stays expensive enough to need evidence.

## 11. Anti-patterns for AI motion
Content storms; anxiety loops; confetti for everything; silent takeover; theatrical "thinking"; false-confidence
completion; motion that hides latency instead of explaining it; invented near-synonym behaviors from generation;
unbounded loops with no stop; agent changes indistinguishable from user changes.

## 12. Validation
Run these before declaring the state language done: every state reachable in the product has a card and a token;
every looping state has a loop policy and a stop; reduced and instant modes exist and keep meaning; a screen-reader
pass shows status announced without waiting for animation; two reviewers can identify each state in a muted,
stripped-brand capture; the agent-authored sample stays inside the approved vocabulary.
