# Severity

Shared by challenger, shakedown and stress-test. Edit in `core/`, never in a copy.

## One scale

Scored as likelihood × impact × exposure **against the stated milestone**.
The same defect can change level when the milestone changes; say what moved.

| Level | Meaning |
|---|---|
| **Blocker** | the milestone fails if this ships: a crash, data loss, silent wrong output, a security hole, legal exposure, or a core job that can't be done |
| **High** | the milestone is damaged but survives; fix before ship if at all possible |
| **Medium** | a real defect, tolerable for this milestone; fix soon after |
| **Low** | a quality gap with no milestone impact |

"Polish" is no longer a severity. It survives only as a finding type (below).

## Stress Test's idea lane

The judge's rulings map onto the scale:

| Ruling | Level |
|---|---|
| Fatal | Blocker |
| Serious | High or Medium, by score |
| Contained | Low, or no finding |
| Refuted | no finding |

## Stress Test's tool lane

The tool lane keeps its own score table (frequency + cost per hit + reach),
which already outputs High, Medium and Low; the Blocker conditions above
override any score. See `references/tool-test.md` in stress-test.

## Finding types are separate labels

Glitch, Gap, Friction, Polish and Enhancement describe *what kind* of
finding it is, never how bad. A Polish finding can be Low; a Gap can be High.
Enhancements carry **Effort** (S / M / L / Overhaul) and **Value** (High /
Medium / Low) instead of a severity.
