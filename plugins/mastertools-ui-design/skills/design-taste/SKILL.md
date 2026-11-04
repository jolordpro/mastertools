---
name: design-taste
description: "The user's UI taste layer: build rules by job drawn from the user's measured picks, a taste judge that ranks options the way the user picks, the canon of top-tier shipped UI (Airbnb, Uber, DoorDash, Apple and peers) and a pattern library, with a 1-5 convention dial. Load it alongside frontend-design whenever Claude designs, builds, critiques, picks between or reshapes UI for the user: websites, apps, dashboards, docs, product pages, layouts, flows, mockups, components, landing pages. Also use for 'give me this at dial 2', 'which option fits my taste', 'run a taste round', 'calibrate my taste', 'improve my taste skill', and when the user picks between design options or corrects a design (log it). Not for applying a named brand system or motion critique alone (motion-critique)."
---

# Design taste (v0.7, in training)

If `~/.claude/overlays/design-taste/README.md` exists, read it first: the user's own picks, examples and paths. They win over this skill's defaults.

**At the start of every brief, check this text is current.** Open `VERSION` in this skill's folder with the Read tool. If it says any number other than 0.7, this text is stale (a session keeps the text it started with): open `SKILL.md` in the same folder with the Read tool and follow that instead.

Status: **in training**. Until the five proof checks in `calibrate.md` pass, say "in training" when a fit call leans on the profile. A new profile starts empty: until calibrate mode has filled it, build from the canon and the pattern library, and say the profile has no evidence yet.

Brand-neutral. Never borrow a personal or client brand's colours, type or voice here.

## The user's profile
The profile is the user's own: `taste-profile.md`, with their build rules by job, offsets from the canon, dial positions, ranked works and words. Read it from the first place that has one: the overlay folder above, then `DT/taste-profile.md` (DT is the evidence folder, under Files). When neither exists, copy this folder's empty `taste-profile.md` to `DT/taste-profile.md` and fill it by running calibrate mode. Never write picks into this skill's folder.

## On a real brief
1. **Read** the user's profile (build rules by job, with ids) and `anti-patterns.md`. Open `patterns.md` for flows. Open each file with the Read tool, one call per file. Never print several files through one shell command: in zsh a line like `echo =====` fails and silently drops every file after it.
2. **Place the brief** on the convention dial: 1 = proven convention, 2 = polished convention with one owned detail, 3 = crafted (Linear, Stripe class), 4 = expressive within a usable product, 5 = award-site expressive. Use the profile's row for the job. Where it says "no evidence yet", or has no row, say so and use the canon.
3. **Build the options.** Usually three; two or four when the brief calls for it. **Every option answers the same screen** (all Goals screens, all home screens). A different step of the flow is a different brief, not a rival option.
   - **Proven**: the pattern-library answer at top-app polish. Leave it out when the brief clearly calls for something else. When `patterns.md` has no row for the job, draw it from two or three named canon apps that do this job, and say there is no library row.
   - **Fit**: built from the profile's rules for this job.
   - **Stretch**: one notch up the dial, when the brief allows.
   Never pad with options built only to look different.
4. **Check each option**: `node scripts/check.mjs <page> ios --shot <name>-phone.png` and `node scripts/check.mjs <page> desktop --shot <name>-desktop.png`. Fix contrast, target and overflow failures. Build anything tappable (rows, cards, chips) as a button or link, or give it `cursor: pointer`; the target check can't see a plain block, and says "no tap targets found" when a phone page has none. For flows, count steps against the Proven benchmark in `patterns.md` (more is allowed with a named reason). Read the `taste` notes; they are warnings, not failures.
5. **Judge.** Start a fresh agent with `judge.md` and the screenshots under neutral names (A, B, C), shuffled so A is not always Proven. It lists what each screen shows, then ranks them by "which would the user pick" and names one fix each. Before you trust the rank, check its lists against the screenshots; a wrong list means a wrong rank, so say so. If it says an option answers a different brief, rebuild that option for the same screen and judge again; if there's no time, rank it last and tell the user why. With no subagents available, judge in your own context from `judge.md` and call it "self-judged".
6. **One fix pass** on the judge's top option, using its fix and any check notes. Re-run the checks on what you changed.
7. **Show the user** the options ranked, the judge's top pick first: what each is, its dial, the rule ids it leans on, one line each. Say "close call" when the judge said so.
8. **Log the use**, quietly, before you send:
   `python3 -I scripts/log_use.py --text 0.7 --job <job> --device <desktop|phone|both> --mode design --judge <agent|self> --option "<label>:<dial>:<rule ids>:<judge rank>" ... --checks "<pass or what was fixed>"`
   Example option: `--option "Fit:2:A1,A3,F2:1"`. Leave the rule ids empty (`"Proven:1::2"`) while the profile has no rules.
   `--job` is the profile's row for the screen: `homepage`, `product-page`, `docs-home`, `docs-article`, `app-flow` (sign-in, filters, cart, a step-by-step task), `settings-dashboard` (any home, overview, goals or settings screen inside an app), `studio`. Use `other` only when none fits, and say why in your reply.
   `--checks` names the kind of fix only ("small targets", "contrast"), never page text. Keep the id it prints. If it says "not logged", carry on; don't mention it. If it says "stale text", re-read `SKILL.md` with the Read tool before your next design step.

Tendencies, not laws. Break one when the brief earns it and say why in one line. A design that ticks every rule but feels flat is a miss. Learn patterns, never copy: no lifted layouts, code, logos, brand colours or illustrations.

## When the user reacts (always log it, in the same message)
The user's own words are the most valuable thing this skill collects. When they pick, reject or correct:
- **Picks** ("B", "the second one, but calmer"): `python3 -I scripts/log_choice.py --use <id> --option <label they chose> --context <context> --job <job> --attribute "<what differed>" --picked "<label>" --over "<the others>" --dial <dial> --source shown --why "<their words, short>"`
- **Corrects** ("make the header calmer", "too busy"): the same command with `--source said` and no `--option`, `--attribute` naming the design attribute and `--why` their words. A correction is not a pick.
- `--context` is one of marketing, dashboard, mobile-app, portfolio, e-commerce, other. `--job` matches the use (homepage, product-page, docs-home, docs-article, app-flow, settings-dashboard, studio, other).
- Log the design attribute only, never client names, copy or data. The script refuses emails, links, money and long text.
- If they say nothing about the options, log nothing. Never invent a pick.

## Improve mode
"improve my taste skill", "what has the taste log learned", and after each round is scored:
1. `python3 -I scripts/usage_report.py` for the summary, then `python3 -I scripts/propose_updates.py`.
2. For each proposal, read the log lines it cites and draft the edit to the user's profile (its build rules, or the evidence rows after a round). Each changed row keeps its evidence, confidence, date and source.
3. Show the user the proposals and their evidence in plain words. Apply an edit to their profile only on their OK.
4. "No proposals" is a normal answer. Say how many picks are logged and what each threshold needs.

Never edit profile rows while a round's predictions are locked and unscored (see `DT/predictions/LOCK.log`).

## Precedence with frontend-design
Load `frontend-design:frontend-design` too, when installed; without it, keep its quality floor below by hand. Where they disagree:
1. Its quality floor always wins: responsive to phone width, visible keyboard focus, reduced motion respected, contrast and target sizes (checked by script).
2. The user's build rules in their profile (source **shown** or **said**) beat its style opinions.
3. The Proven option follows convention on purpose. Its "avoid defaults" list applies only to AI tells (cream and terracotta, the generic SaaS card kit, template chrome), never to patterns the canon proves. Example: near-black text (#1D1D1F to #222) is a canon value from Apple, Airbnb and DoorDash, not a tell.
4. Otherwise, follow frontend-design.

## Files
In this folder:
- `taste-profile.md`: the empty starter for the user's profile (build rules by job with ids, offsets from the canon, dial positions, ranked works, their words). Copy it to DT and fill it by calibrating; the filled copy is the evidence behind every fit call.
- `judge.md`: the brief for the fresh taste judge.
- `canon.md`: what top-tier UI does and why, with the products it came from.
- `patterns.md`: the pattern library by job. Draw the Proven option from here, not from memory.
- `anti-patterns.md`: what never ships.
- `calibrate.md`: taste rounds and the proof checks.
- `ROADMAP.md`: planned updates with their evidence. Read it in improve mode and before building a new version.
- `scripts/`: `check.mjs` (function checks, taste notes, screenshots), `log_use.py`, `log_choice.py`, `usage_report.py`, `propose_updates.py`, capture, scoring and backup.

Evidence (never in this plugin): the per-user folder DT, by default `~/.config/mastertools/design-taste/`, created on the first log. To keep it elsewhere (a synced folder that several accounts share), put its path on the first line of `~/.config/mastertools/design-taste.dir`. Contents: `taste-profile.md`, `usage.jsonl`, `decisions.jsonl`, `patterns/`, `library/`, `test-set/` (locked), `predictions/`, `grids/`, `scores/`.

## Steering phrases
- "dial N": re-render at that dial position.
- "more proven" / "more expressive": move one notch.
- "why this?": name the rule id, its profile row and the evidence.

## Calibrate mode
"run a taste round", "calibrate", "train my taste": follow `calibrate.md`.
