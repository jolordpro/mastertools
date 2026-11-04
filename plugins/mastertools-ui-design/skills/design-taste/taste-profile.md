# Taste profile (starter, empty)

Starts empty: copy it to `~/.config/mastertools/design-taste/taste-profile.md` and fill it by running calibrate mode ("run a taste round", `calibrate.md`); never fill this copy inside the plugin.

Stored as **offsets from the canon**. Where the user agrees with the canon and frontend-design, there is no row. An empty table means no evidence yet.

Every row carries: evidence, confidence, date, source type. **said** = the user's words. **shown** = the user's picks. **guessed** = Claude's inference. Never upgrade a guess to said. Newer evidence counts more.

## How to predict the user
Read the whole profile and judge each pair; don't apply the rows below one by one. Write here, after each scored round, the method that predicted best and its score from `score_round.py`.

No rounds scored yet.

## Said
What the user has said they want, in their words. *(said, confidence)*

## Convention dial by context and job
| Context / job | Dial | Evidence | Confidence | Source | Date |
|---|---|---|---|---|---|

## Offsets from the canon
| Attribute | The user leans | vs canon | Contexts tested | Evidence | Confidence | Source | Date |
|---|---|---|---|---|---|---|---|

## Works the user has ranked (all rounds, all devices)
| Work | Job | Device | Won / shown | Rounds |
|---|---|---|---|---|

## The user's words for things
| Their word | What it means on screen | Source | Date |
|---|---|---|---|

## Consistency
Repeat pairs that agreed, from `score_round.py` (`consistency`). This is the ceiling a predictor can reach.

## Predictor scorecard
| Round | Profile | frontend_design | Convention | Jury | Notes |
|---|---|---|---|---|---|

## Build rules by job
What to build, drawn from the rows above. Give every rule an id (letter + number) so logs and "why this?" answers can cite it. A job with no evidence keeps a row that says **No evidence yet.** and falls back to the canon (`canon.md`, `patterns.md`). Tendencies, not laws.

### Every page
| Id | Build rule | Evidence | Confidence |
|---|---|---|---|

### By job
Jobs: homepage, product-page, docs-home, docs-article, app-flow, settings-dashboard, studio.
| Id | Job | Build rule | Evidence | Confidence |
|---|---|---|---|---|

### Close calls
| Id | Rule | Evidence |
|---|---|---|
