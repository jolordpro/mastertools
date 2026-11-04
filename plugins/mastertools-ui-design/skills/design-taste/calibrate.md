# Calibrate mode: one taste loop

About 20 minutes of the user's time. Stop and save when it's up. DT = the user's evidence folder (`SKILL.md`, Files): `~/.config/mastertools/design-taste/` unless `~/.config/mastertools/design-taste.dir` names another.

## First round only: set up
1. Copy this skill's empty `taste-profile.md` to `DT/taste-profile.md` (skip if the user already has a profile).
2. Build `DT/library/inventory.csv` with at least `id`, `name`, `url`, `lane` (proven, crafted or expressive), `job` and `device`: real shipped works from the canon and from award lists, spread over the jobs the user designs for. Capture them with `scripts/shoot.mjs` (desktop and phone sizes) and rate each one's dial in `DT/library/dial.csv` (`id`, `dial`).
3. Lock the test set once, before the user sees any work: `python3 -I scripts/lock_test_set.py DT`.

## Before the user sees anything
1. **Never touch the test set.** `DT/test-set/split.json` (read-only once locked) lists works that never appear in a round, a grid or a draft. Build rounds from its `train` list only.
2. **Aim** the round at what the model is least sure of: empty dial cells, profile rows with low confidence, variables tested in only one context.
3. **Fair pairs:** same job, same device. Most pairs stay within a lane; some cross lanes to place the user on the dial. Real works first; make a mockup only to isolate one variable, based on a real work with only that variable changed.
4. **Repeats:** put about 5 earlier fast-lane pairs back with A and B swapped (from round 2 on).
5. **Lock predictions:** write every pair's prediction and confidence from four sources into one file, then lock it:
   - `profile`: a fixed rule written into the round's build script before the user sees anything (earlier record first, then the dial rows, then Claude's reading; on test pairs it may not abstain)
     Fixed rules tend to predict worse than an agent reading the whole profile. Name the predictor that counts for a proof check in the build script before the user sees the round.
   - `frontend_design` (what plain frontend-design would favour): an independent agent that reads only the frontend-design skill and scores screenshots under neutral file names, so the baseline is neither a straw man nor shaped by the user's profile
   - optional `skill_agent`: the same kind of agent with this skill's SKILL.md and the user's taste-profile.md added; list it in the file's `"sources"`
   - `convention` (the option with the lower dial rating in `DT/library/dial.csv` wins)
   - `jury` (higher jury score wins; only where both works have one in `DT/library/awards.json`)

   `python3 -I scripts/lock_predictions.py DT/predictions/round-N.json` records the checksum in `DT/predictions/LOCK.log` and makes the file read-only. Publish the round only after that.

## The round
- **Fast lane, about 5 min:** about 60 picks with ← and →, no "why".
- **Slow lane, about 8 min:** 6–8 pairs: A / B / both / neither / depends, slight or strong, short why. Include trade-off sets (each option strong on one thing, weak on another).
- **Grid, about 5 min:** three works, "which two are alike, how is the third different?", then "why does that matter?" two or three times until it reaches a principle. Include works the user feels neutral about.
- **Motion:** live pages or short recordings, never stills; notes in motion-critique vocabulary.
- **Delivery:** a published Artifact that stores answers (read back with ArtifactData), or a local page with "Copy my answers" (`scripts/round-page.html` is a starting point). The user only clicks, uses arrow keys and pastes. Claude's picks stay hidden until the round ends.

## Close the loop
1. `python3 -I scripts/score_round.py DT round-N` scores every prediction source against the user's answers and writes `DT/scores/round-N.json`. Scores come only from this script, never from prose.
   `python3 -I scripts/breakdown.py DT round-N` splits the result by device and job, by profile rule, by dial direction, lists each repeat and tallies every work over the rounds named (`round-N round-1 ...`).
2. Update the user's `taste-profile.md` (offsets, dial cells, build rules, their words) and `canon.md`. Each row: evidence, confidence, date, source type. A variable becomes a rule only after it's tested in two contexts.
3. Tell the user in three lines: what you learned, what surprised you, the round's scores. Then show your picks with reasons.
4. Run `scripts/backup_decisions.py` (also daily).

## Proof checks (the skill stays "in training" until all five pass)
1. **Locked-away works:** predict the user's picks on pairs drawn from the test set. Mark those pairs `"part": "test"`; `score_round.py` then scores each part on its own. Record which test works a round spends in `DT/test-set/spent-round-N.json` before the user sees it.
2. **Beat every baseline that applies:** profile beats frontend_design, convention, and jury where it exists. `score_round.py` reports `head_to_head`: on pairs where the two disagree, how often each was right, with a sign test. Fresh works added for a check count as unseen when they enter no train pair first; record them in `DT/test-set/fresh-round-N.json`. Beating frontend_design but not convention means "the user likes the mainstream", not their taste.
3. **Near the user's ceiling:** accuracy on fresh pairs against the user's repeat consistency.
4. **Function checks** on everything the skill designs, by script (`scripts/check.mjs`): touch targets, WCAG AA contrast, step count vs the Proven benchmark (more steps allowed, with a named reason).
5. **Blind panel:** about 20 briefs, skill vs plain frontend-design, unlabeled, random order, 3–5 people who know the user's taste. Three questions per pair: which feels more like the user, which is the better work, which would you rather use to get the job done. With 20 pairs, about 15 wins is the bar (script reports each against chance). Claude prepares the page and message; the user sends it.

Report every result, including failures, and what changed because of it.

## Upkeep
- Re-capture the pattern library every few months (`scripts/shoot.mjs`, `scripts/ui.js`), add new specimens to `DT/library/inventory.csv` (new works may enter the test set only through a fresh, logged split), and retire principles that turn out to be one year's trend.
- Measurable values: `check.mjs` reports four taste notes (font families, filled buttons and ALL-CAPS labels on the first screen, serif display headings). They warn, never decide: fixed rules predict picks worse than the judge. Add a note only with a calm and a busy test page that prove it, plus a test.
- After a round is scored, run improve mode (`SKILL.md`) so real-use proposals and round results land together.
