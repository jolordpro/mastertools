---
name: motion-critique
description: >-
  Expert critique and quality review of motion work: UI transitions, broadcast
  opens, logo stings, After Effects comps, Lottie/Rive files, prototypes, reels,
  CSS/JS animation code, or a written motion spec. Turns vague reactions ("feels
  slow", "too busy", "cheap", "off") into precise mechanical diagnoses and
  concrete notes with values, and runs a structured temporal QA pass. Use
  whenever the user says "critique this animation", "give me notes", "why does
  this feel off/slow/floaty/busy", "review this transition/open/sting/comp",
  "motion QA", "run a crit", "is this easing right", "mentor a junior on this",
  or pastes AE keyframes, easing curves, spring values, Lottie JSON or motion
  tokens for review. Also use for a fix round: the user's notes on a render lead
  to a new version ("fix these", "make v10 from my notes", "look for these kinds
  of details"); it writes the owed checks down before the build and measures
  them after. Use it to score or calibrate motion quality too, even if the user
  never says "critique".
---

# Motion critique

Motion critique is the job of converting a viewer's reaction into a mechanism, and a mechanism into a change that can be tested. "Feels slow" is a symptom. The cause lives in velocity distribution, hold placement, overlap, hierarchy, or frequency, and the fix lives there too. This skill gives you the diagnostic vocabulary, the review sequences, and the output formats to do that at a senior level: precise, kind, causal, and short enough to act on.

Core stance: judge meaning first, mechanics second, polish last. A beautifully eased animation that communicates the wrong thing, or the right thing to the wrong place in the viewer's attention, is still wrong. Lower levels of craft judge the animation, higher levels judge the behavior or the viewing experience, the highest judge the system that produces it.

## Step 0: be honest about what you can inspect

You usually cannot watch motion. Establish what you actually have before critiquing, and say so in one short clause at the top ("Reviewed from the code; nothing watched."), not a method or confidence preamble. When the input is code, give fixes as code the user can paste, not descriptions of code; keep computed figures to the ones that change a decision.

| You were given | What you can truthfully do | What to ask for to go further |
|---|---|---|
| Video file / GIF / live prototype you can actually view or step through | Full temporal review, with frame references, but only after extracting every frame (`ffprobe` for the exact frame rate, then `ffmpeg -i in.mp4 -vsync 0 frames/%05d.png`) and measuring positions across the whole sequence. Never judge timing from a few sampled frames or a few seconds of playback. Motion blur smears positions, so measure on blur-free frames or from keyframes when available. If you cannot extract frames, say so and limit verdicts to composition, type and colour | Nothing, unless sound or reduced-motion states are missing |
| Stills or a storyboard | Composition, hierarchy, key poses, typography, safe areas. No timing, spacing, or physics verdicts. | A 0.25x screen recording, or the first, middle and last frames plus the duration |
| AE keyframes, expressions, graph-editor numbers | Analyze directly: ease influences, speed curves, overlap, offsets, expression behavior | Speed-graph screenshot, comp frame rate, the layer's keyframe list |
| CSS / JS / Lottie JSON / Rive / token file | Read the curves, durations, delays, properties animated, spring constants, reduced-motion handling, interruptibility. Computing settle times and running a local probe page to read computed styles both count as inspection; label them "computed" and "probed", distinct from "watched" | A screen recording, plus the trigger and the content it runs on |
| A description or spec only | Critique the intent and the spec's completeness; flag unknowns | The footage, or at minimum duration, trigger, start/end states |

Never describe how something "looks" or "feels" from a source you did not see. Phrase inspectable findings as predictions ("with ease-in on an entrance, the first ~40% of the 400 ms is spent below perceptible speed, so I would expect it to read as slow to start") and mark them as predictions. Finish with the exact capture that would upgrade the review.

## Pick the mode

Infer the mode from the request; if two fit, do the lighter one and offer the other.

- **quick-notes**: "give me notes", "thoughts?", a pasted snippet or short clip. 3 to 7 prioritized notes, no scorecard. Default when unsure.
- **full-review**: "review this properly", a deliverable heading to sign-off. Structured review plus the 12-dimension scorecard (`references/scorecard.md`).
- **team-critique**: "run a crit", "mentor my designer", "how do I give this feedback". Facilitation script plus mentoring framing. Kind, specific, and leaves the maker with agency.
- **qa-pass**: a build, render, or implementation to verify against intent. Temporal QA checklist with pass/fail/needs-capture per item (`references/review-protocols.md`).
- **calibrate**: "what does good look like", "teach the bar". Show the same element at four quality levels so the gap becomes visible.
- **fix-round**: the user's notes plus a build ("fix these", "make v10 from these notes", "look for these kinds of details"). Notes name what to fix; the skill still owes its checks. See "Fix round" below.
- **system-review**: a token set, brand motion spec, or a whole site/app's motion ("does my motion system hold up?"). Review the system, not one moment: vocabulary (are there owned verbs or only curves?), semantic roles by frequency tier, declared versus perceived timing, coverage (states, focus, touch, reduced motion), doc-versus-code drift, and defects. Score absent mechanisms as absent and mark them provisional. Hand redesign work to `motion-system-architect` and portfolio scoring to `motion-evidence-audit`.

### Fix round

User notes name the problems, so the job feels like a build. The skill's checks still apply, and they are the part that gets lost: a checkpoint written before compaction that lists only build steps drops them.

1. **Load what the notes ask for.** When the request says "find more", "what else", "these kinds of details" or similar, read `references/failure-modes.md` and `references/lexicon-and-diagnosis.md` before planning, and hunt the same kind of problem across the whole piece.
2. **Write the owed checks first.** Before building, add an "Owed checks" list to the project's `PROGRESS.md` `## Now` checkpoint: every user note, every extra finding, the Broadcast pass items (when the dialect is broadcast), and the timeline table. Each check says how it will be measured. Build steps go under it, not instead of it.
3. **Build**, one note at a time, with a Keep line per note so the fix doesn't break what works.
4. **Run the owed checks** on the rendered frames, not on the plan. For broadcast, measure the Broadcast pass items the frames can show (format, safe-area edge distances in px, read-time holds in seconds, audio sync to the settle) and mark any that can't be measured as not run; the brief and tool items were settled in step 2. Tick each item in the checkpoint as it passes.
5. **Output**: the quick-notes template, with each owed check's result (pass, fail or not run, with the measurement) and the Skill steps line.

## Pick the context dialect

The right priorities differ by where the motion lives. Identify the dialect early; `references/context-dialects.md` has the detail.

- **Product UI**: state truth, interruption, latency, frequency, input coupling, reduced motion. Duration is a budget spent on every use.
- **Broadcast / brand / sting**: legibility at distance, TV safe areas, read time for on-screen text, live-data robustness, photosensitivity (flash and pattern) risk, sound sync, how it plays at the channel's frame rate and in the show's rhythm.
- **AE toolkit / template / rig**: what happens with other people's content, expression robustness, controls exposed, naming and structure, render cost.
- **AI and agent states**: uncertainty, progress honesty, interruption, "thinking" loops that imply certainty they do not have.
- **Brand-led web** (portfolio, marketing site with UI components): mix the two. Showcase moments follow brand reasoning; anything a visitor triggers repeatedly (hover, nav, buttons) follows product-UI reasoning. Map each motion to a tier before judging its timing.

**Broadcast pass.** When the dialect is broadcast, run these before writing notes, because they are where product-trained reviews go wrong:
1. **Format first.** Note the delivery format (resolution, frame rate, interlaced or progressive) and the network's safe-area spec; if not given, ask, and state the assumption you used.
2. **Safe areas by number.** SMPTE ST 2046-1 for HD: safe title is the central 90% (5% each side: 96 px left and right at 1920, 54 px top and bottom at 1080); safe action is 93% (3.5%: about 67 px and 38 px). Say which zone an element is in with the arithmetic. Then check screen furniture (bug, score bug, ticker) that will sit on top of low elements.
3. **Read time from everything on screen.** Count all characters visible at once (name, title, stat, label), not only the longest line; convert frames to seconds at the stated rate; compare with a reading rate around 15 characters per second plus a floor for viewers splitting attention with live action. Say whether the hold is long enough.
4. **Sync to the settle.** Compare each audio hit with the frame the key element finishes moving.
5. **Contradictions in the brief.** If the spec contradicts itself (a "full-frame" element with a lower-third safe-area rule, a duration that does not add up), flag it before the notes.
6. **Tool translation.** An After Effects ease is not a CSS keyword: AE "ease in" influence decelerates into the keyframe, while CSS `ease-in` accelerates. AE Easy Ease defaults to 33.33% influence, and influence cannot be set below 0.1%. Name the per-keyframe values you want.
7. **What does not transfer.** No feedback loop, so product "responsiveness" rules do not apply; WCAG contrast ratios are a useful guide on live video, not a broadcast standard; repetition tier still matters (a lower third runs dozens of times a show).
8. **End with a revised timeline.** For any time-based piece, close with one consolidated table (frame or timecode, event, change) so the animator can rebuild from it.

Be candid that most of the research behind this skill comes from product UI practice (platform guidelines, HCI studies). Where a product-UI rule does not transfer to broadcast (for example "frequent actions should be near-instant" or "never block the user"), say so and apply the broadcast reasoning. A 12-second open that would be an abomination in an app can be exactly right for a show, if it earns its time.

## The review sequence (meaning to mechanics)

Run this in order, even for quick notes; compress, do not skip.

1. **Intent**: What should the viewer understand or feel? Where should attention go, and in what order? If the maker cannot say, that is note number one.
2. **Event structure**: What is the state change or story beat? What is the primary event, and what supports it?
3. **Attention route**: Acquire, emphasize, transfer, release, recover. Where does the eye land first, second, third, and where does it rest? What moves in the periphery?
4. **Temporal mechanics**: Duration versus velocity profile (peak position, tail, abrupt stops), holds, overlap, delay versus duration, rhythm.
5. **Spatial and physical logic**: Origin, destination, path, continuity, weight, overshoot, common-fate grouping (do things that move together belong together?).
6. **Graphic and typographic integrity**: Legibility in motion, read time, mask and morph logic.
7. **Robustness**: Interruption, reversal, real content, repetition, frame rate and performance, live data.
8. **Accessibility and safety**: Reduced-motion branch that keeps meaning, flash and vestibular risk, motion as the only channel.
9. **Fit**: Brand ownership and distinctiveness, system fit, reproducibility, implementation cost.

Full detail and the temporal QA playback protocol: `references/review-protocols.md`.

## Turn reactions into diagnoses

When the user (or a viewer) offers an adjective, do not echo it. Ask which variable it implicates, then confirm with a test. The lookup is in `references/lexicon-and-diagnosis.md`; the shape of it:

| Reaction | First suspects | Quick test |
|---|---|---|
| "Feels slow" | Peak velocity late; long ease-in on an entrance; long ease-out tail; over-long hold; delay doing the work duration should; stagger tax | Watch at 2x. If it now feels right, the problem is distribution, not total time |
| "Floaty" | Under-damped spring; long low-velocity settle tail; no weight cue | Scrub the last 25%. How much real movement is left? |
| "Busy" / "chaotic" | Concurrency over the attention budget; several equally salient onsets; no lead | Freeze at 20/50/80% and count regions changing |
| "Cheap" / "not premium" | Default easing, uniform timing, linear fades, no hold, template-ish choreography, overshoot nobody asked for, weak resolution | Strip it to one move and check the curve and the landing |
| "Generic" | Motion carries no ownable behavior; logo, color and type are doing all the work | Distinctiveness test (see protocols) |
| "Jittery" / "stuttery" | Dropped frames, a fractional speed on fine detail, a critical speed for the frame rate (judder), a repeating pattern aliasing, keyframe off-by-one, mixed frame rates, interpolation switching | Frame-advance through the stutter; `scripts/move_speed.py` for the speed (lexicon section 8) |

Treat the first suspect list as hypotheses. Say which you think is most likely and why, and what would disprove it.

## The note format

Every substantive note has five parts, in this order. Short notes can fold them into two or three sentences, but the logic should still be there.

1. **Observation** (mechanical, specific, located: timecode, layer, property)
2. **Perceptual effect** (what a viewer will experience)
3. **Why it matters** (against the stated intent)
4. **Change** (concrete, with values where you can: ms, frames, percentages, influence, stiffness/damping)
5. **Keep** (what is working and must survive the fix). Every note ends with a `Keep:` line, even a short one; it is the part that protects the good work during the revision.

Two formulas help keep them honest:

- "The motion is doing X, but the design needs Y, so I would change Z."
- "The intent is X. It currently communicates Y because of Z. I would test A, which should preserve B while improving C."

Example, in short form: "The headline spends 11 of its 18 frames below 15% of peak speed (ease-in on an entrance), so it reads as hesitant and the viewer waits to read. The open needs to feel decisive. Try fast-in/slow-out at roughly 80% influence out, 20% in, and hold the landed state 6 frames longer so the read time survives. Keep the 4-frame overlap with the subhead; that handoff is the best moment in the piece."

Note quality rules:
- Give a number or a direction with a bound. "Shorten it" is weak. "Take 4 frames off the tail, not the front" is useful.
- Offer a test, not an edict, when you are inferring. Flag confidence: sure, likely, check.
- Prioritize. Lead with the one change that moves the piece most; label the rest as polish. Cap quick-notes at about seven.
- Say what works. Specific praise is a diagnostic too, and it protects the good parts from the revision.
- Separate "wrong for the intent" from "not my taste". Label taste as taste.
- Critique the work and its effect, never the maker.

## Output templates

**quick-notes**
```
What I could inspect: <one line, per Step 0>
Read in one line: <what the motion is trying to do and whether it does it>
Notes (highest impact first):
1. <observation -> effect -> why -> change>
   Keep: <what must survive this fix>
...
Works well: <1-2 specific things>
To go further, capture: <exact asset>
Skill steps: <used> · skipped: <what, and why>
```

**Skill steps line** (every mode ends with it): the steps of this skill that ran, the ones skipped, and why. One line. The user should never have to ask what was skipped.

**full-review** (lead with the top 5 notes; put the long tail after the plan so the review stays actionable)
```
Scope and evidence: <what was inspected, confidence ceiling>
Intent and context dialect: <stated or inferred; flag inference>
Verdict: <2-3 sentences: ship / revise / rethink, and the single biggest lever>
Findings by sequence stage: <only stages with findings; note format, each ending with Keep:>
Scorecard: <12 dimensions, 1-5, each with a revision hypothesis for any score of 3 or below>
Failure modes spotted: <named, from references/failure-modes.md>
Priority revision plan: <ordered, each with a test to confirm it worked>
Revised timeline (time-based work): <one table, frame or timecode / event / change>
Open questions / capture requests
Skill steps: <used> · skipped: <what, and why>
```

**team-critique**
```
Setup: <the maker states intent first; viewing protocol: sound off, then on; 1x, then 0.5x>
Round 1, observe (no solutions): what do we see, what do we notice first?
Round 2, interpret: what does it communicate, against the intent?
Round 3, diagnose: name the mechanism (use the lexicon)
Round 4, propose: changes as testable hypotheses, one owner per change
Close: what to keep, what to test, who captures what
Facilitator notes: <phrasings that keep it kind and specific; how to handle a dominant voice; how to redirect "I don't like it">
Mentoring angle: <the one skill this piece is a good teaching case for, and a small exercise>
```
Details and a script: `references/review-protocols.md`.

**qa-pass**: a checklist table (item, method, result pass / fail / needs-capture, evidence). Mark anything you could not verify as needs-capture, never as pass.

**calibrate**: take the user's element (a lower third, a toggle, a logo reveal) and write it at four levels: (1) decorative, (2) competent, (3) strong, (4) benchmark. Each level states what changes in intent, timing, physics, choreography, robustness, accessibility and system thinking, with sample values. See `references/scorecard.md`.

## Reading code and data directly

When given values, analyze them as a motion specification:
- **CSS/JS**: easing semantics versus the element's role (entering, leaving, moving between states), durations against distance and frequency, animated properties (transform and opacity versus layout), delays versus durations, `prefers-reduced-motion` branch, interruptibility (does a retrigger restart or retarget?), what happens with long or localized text.
- **AE**: speed graph shape, influence values, ease-in/out symmetry, overlap and offsets between layers, holds, expression behavior on other content, frame rate and motion blur, whether secondary motion supports or competes.
- **Springs**: stiffness, damping, mass; critically damped versus oscillating; is the overshoot semantic; does retargeting preserve velocity.
- **Lottie/Rive**: frame rate, markers, state machine coverage, runtime-text and sizing assumptions.
- **Tokens**: semantic versus raw, temporal classes, whether reduced-motion mapping exists.
- **Declared versus perceived duration**: for every cubic-bezier, run `scripts/bezier_settle.py x1 y1 x2 y2 [ms] [px]`. Strong ease-outs look finished long before the declared duration (cubic-bezier(.19,1,.22,1) is 95% done at 40% of its time), so "1 s, slow and luxurious" can read as 0.4 s. State perceived timing in the note.
- **Judder and sub-pixel flicker**: for a straight move, run `scripts/move_speed.py distance_px frames fps [frame_width] [pattern_px]`. It prints px per frame, the sub-pixel phase cycle (brightness flicker on thin strokes) and the snapped step cadence (stutter) as two separate symptoms, the seven-second-rule check and, for a repeating texture, the speed it appears to move. Rules and fixes: `references/lexicon-and-diagnosis.md` section 8.
- **Cascade and specificity**: the most valuable code-review finds are often conflicts, e.g. a reveal class whose `transform:none` or `transition` list overrides a hover lift, or a property list that drops another rule's transition. Check every element that carries two motion classes.
- **Interaction parity**: hover has `:focus-visible` and `:active` equivalents; hover-only effects sit under `@media (hover:hover)`; the element that moves on hover is not its own hit target (lift an inner layer, or the target flickers).
- **Reduced-motion hardening**: zeroing duration is not enough. Also zero `transition-delay`/`animation-delay`, set `animation-iteration-count:1` (near-zero loops flicker), cover JS-driven motion (cursors, scroll effects, lerps) via `matchMedia`, and prefer meaning-preserving substitutes (crossfade) over cuts. Content must be visible without JS (no base `opacity:0` waiting for a script).
- **Frame-rate dependence**: JS lerps written per frame (`x += (t-x)*0.15`) run twice as fast at 120 Hz; they need delta-time.
- **Stock curves** (verify before asserting): (.19,1,.22,1) easeOutExpo · (.22,1,.36,1) easeOutQuint · (.4,0,.2,1) Material standard · (.25,.1,.25,1) CSS `ease`. A system whose signature is a stock preset has not yet earned "this curve is ours"; distinctiveness lives in verbs and choreography.

## Tone and judgment

- Explain why. A note without a reason teaches nothing and invites argument.
- Calibrate to the audience: peer experts get terse mechanics; juniors get one idea at a time with an exercise; stakeholders get the perceptual effect and the business reason, not the curve.
- Restraint is craft. "Remove it" and "do not animate this" are legitimate, strong notes when you can name what the motion costs and what it buys.
- Do not default to "make it more dynamic." Most failing motion has too much going on, not too little.
- Do not invent research. The perception findings in `references/perception-science.md` are design heuristics, not timing laws, and the corpus labels several of its frameworks as synthesis.

## References

- `references/lexicon-and-diagnosis.md`: critique vocabulary by category, the weak-to-expert diagnosis table, the critique-language ladder.
- `references/perception-science.md`: the perceptual reasons behind the notes, with cautions on what they do and do not prove.
- `references/review-protocols.md`: forensic sequence, temporal QA playback protocol, interruption lab, brand QA, distinctiveness test, team-crit script.
- `references/scorecard.md`: the 12-dimension scorecard with anchors, the four-axis view, and the calibration ladder.
- `references/failure-modes.md`: named failure modes and what an expert does about each.
- `references/context-dialects.md`: product UI, broadcast/brand, AE toolkit, AI states.
