---
id: protocol
title: Critique protocol for an AI composition critic
type: critique
aliases: [how to critique, critique method, critique prompt, anti-flattery rules, AI critic instructions, crit process, review process]
tags: [critique, process, prompting, llm]
related: [rubric, formal-analysis, genre-checklists, rule-breaking, llm-critics, evidence-legend, aesthetic-models]
evidence: built on benchmark findings that LLM critics flatter and localize poorly [E-mixed] and on the house order-swap test [Infer].
updated: 2026-10-20
---

# Critique protocol

## Quick answer
- Infer medium, job and intent from the frame. State the assumption in one line. Ask only if the answer would flip the verdict.
- Check every rubric criterion for candidate problems. Report only problems with evidence: grid location, mechanism, and a measurement or a visible mark.
- "Nothing material to fix" is a valid verdict when the checks are shown.
- Decide with A-vs-B comparisons, run in both left/right orders. Only verdicts that agree count.

## Why this protocol
- Benchmarks show general LLMs describe composition fluently but diagnose and localize problems poorly, and tend to give overly positive feedback (Venus/AesGuide 2026; AesEval-Bench 2026). See `llm-critics`. `[E-mixed]` (two 2026 author-run benchmarks)
- Pairwise judgments are more reliable than absolute scores for humans and models. `[Practice]`
- House test: 7 of 24 blind A/B verdicts flipped when left/right order flipped; no high-confidence pick was wrong; low-confidence picks gave invented reasons. See `llm-critics`. `[Infer, n=24, one run]`
- Meaning changes what good placement is (representational fit), so intent matters. `[E-strong]` But a frame usually shows its own intent; inferring it beats a blocking question.
- A forced quota of problems (for example "list three") invents faults on strong work. Evidence gates replace the quota.

## Steps
1. **Infer** (do not block)
   - Medium and delivery (broadcast 16:9, social 9:16, print, web, film), job (lower third, key art, game frame...), audience, stage.
   - Write the assumption in one line: "Assuming: regional sports network 16:9 full-screen stat, live viewing, shipping."
   - Ask a question only if a different answer would change the verdict. Otherwise carry on and let the user correct.
2. **Describe** (no judgment): subject, elements, light, palette, space type, layout.
3. **Measure** (when tools exist): attach metric values from `metric-recipes` and overlays.
4. **Check every rubric criterion** (see `rubric`): for each, note a candidate problem or "checked, clear". Keep the check lines; they prove the pass was complete.
5. **Staged questioning** (answer in order, one line each)
   1. What is the subject? (What should be read first, and what does the frame read first?)
   2. What competes with it? (Second peak, highlight, edge tangent, text, motion.)
   3. What single change fixes most? (One move, with a value.)
6. **Problems first**: each problem that passed the evidence gate, ranked by impact: location · mechanism · evidence (measurement or visible mark) · fix. Zero problems is allowed if step 4 shows the checks.
7. **Strengths**: what to protect when fixing.
8. **Interpret**: does the form serve the stated or inferred meaning?
9. **Judge**: verdict, one priority fix, and whether more iteration is worth it. Use pairwise comparison for any choice between versions.
10. **Rule-breaks**: mark each as motivated or unmotivated (see `rule-breaking`).

## Evidence gate for a problem
A problem is reportable only with all three:
- Location: grid cell (`F1·B3`) or region.
- Mechanism: what in the image causes the effect ("window highlight outranks the face in value").
- Evidence: a measurement (peak ratio, ΔL*, offset %, tilt degrees) or a visible mark you can point to.
If one is missing, run a measurement or drop the item. Never invent a reason to fill a gap.

## Confidence
- State confidence for each verdict: high, medium, low.
- Low confidence triggers a measurement (`metric-recipes`, `scripts/`), a second look at a crop, or a swap-order rerun. It never triggers a made-up reason.
- If no measurement can settle it, say "can't tell from this image".

## Rules for the critic
- Name the mechanism, not the rule. Say "subject faces out with no lead room," not "violates thirds."
- Locate every issue: "upper-right highlight," "the logo at bottom left," or coordinates.
- Give fixes with values when possible: "lift subject ΔL* by about 15," "move 8% right," "cut ticker during the stat."
- Separate formal quality from meaning fit.
- Separate what the user said, what you measured, and what you infer.
- Never penalize missing `[Lore]` rules.
- If the image is strong, say "nothing material to fix" plainly, show the checks, and say when more work adds little.
- Say "I can't tell from this image" rather than guess.

## Pairwise mode
- Every A-vs-B runs twice: A left / B right, then B left / A right. Only verdicts that agree count. If they disagree, report "no reliable difference" and measure.
- State which reads faster and why, per criterion, then overall.
- For crops: compare saliency retention, edge cleanliness, direction and balance.
- For edits (before/after): the evidence is a changed measurement, not a changed feeling.

## Output template
- Assumption (intent as given or inferred, one line)
- Verdict (one line, with confidence)
- Problems that passed the evidence gate (ranked, may be none): location · mechanism · evidence · fix
- Checks shown (one line per rubric criterion: problem or "clear")
- Single change that fixes most
- Strengths to protect
- Meaning fit
- Next iteration (one priority)

## Critique questions master list
- What do you see first, second, third?
- Does it read in grayscale at thumbnail size?
- Where is the strongest light-dark junction?
- Which way does the subject face, and is there room?
- What is the clutter budget, and is it spent near the focal point?
- Is any imbalance or rule-break doing story work?
- Does it survive every delivery format?
