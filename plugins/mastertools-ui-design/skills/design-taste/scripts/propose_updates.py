"""Find where real use says the build guide should change. Prints proposals with their evidence.

Thresholds are fixed here so a proposal can't be invented:
- review a rule: the user picked from at least 3 uses where it was in play, across at least 2 projects,
  and passed it over more often than they took it;
- fill a "no evidence yet" row: at least 4 of the user's picks or corrections on that job;
- judge drifting: of the last 10 uses with a judged ranking and the user's pick, the top pick matched fewer than 6.
Claude turns each proposal into an edit to the user's taste profile, applied only on their OK.
Run when the user asks ("improve my taste skill") and after each round is scored. Never on a timer.

usage: propose_updates.py
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from usage_report import analyze
from dt import profile_files
from log_use import JOBS

REVIEW_MIN_USES, REVIEW_MIN_PROJECTS = 3, 2
FILL_MIN = 4
DRIFT_WINDOW, DRIFT_MIN_AGREE = 10, 6


def empty_rows():
    """Build rules marked "No evidence yet" in the user's profile, as {job id: rule id}.
    A row's job cell matches a job id when every part of the id starts a word in the cell
    ("Docs article" -> docs-article, "Settings, dashboards" -> settings-dashboard)."""
    out = {}
    for path in profile_files():
        with open(path, encoding="utf-8") as fh:
            for rid, cell in re.findall(r"^\| ([A-Z]\d+) \| ([^|]+) \|.*No evidence yet", fh.read(), re.M | re.I):
                words = re.findall(r"[a-z0-9]+", cell.lower())
                for job in JOBS:
                    if all(any(w.startswith(part) for w in words) for part in job.split("-")):
                        out.setdefault(job, rid)
    return out


def propose(a):
    out = []
    for rid, st in a["rules"].items():
        n = st["taken"] + st["passed"]
        if n >= REVIEW_MIN_USES and len(st["projects"]) >= REVIEW_MIN_PROJECTS and st["passed"] > st["taken"]:
            whys = [f'"{a["whys"][u]}"' for u in st["uses"] if u in a["whys"]]
            out.append({"kind": "review rule", "target": rid,
                        "evidence": f"passed over {st['passed']} of {n} times, {len(st['projects'])} projects; uses {', '.join(st['uses'])}"
                                    + (f"; the user said {'; '.join(whys)}" if whys else "")})
    for job, rid in empty_rows().items():
        n = a["picks_by_job"].get(job, 0) + a["said_by_job"].get(job, 0)
        if n >= FILL_MIN:
            out.append({"kind": "fill row", "target": rid, "evidence": f"{n} picks or corrections on {job}"})
    recent = a["judged"][-DRIFT_WINDOW:]
    if len(recent) == DRIFT_WINDOW:
        agree = sum(j["agree"] for j in recent)
        if agree < DRIFT_MIN_AGREE:
            out.append({"kind": "judge drifting", "target": "judge step in SKILL.md",
                        "evidence": f"top pick matched the user {agree} of the last {DRIFT_WINDOW}"})
    return out


def main():
    a = analyze()
    props = propose(a)
    if not props:
        print(f"No proposals. {a['linked_picks']} picks tied to uses so far; a rule needs {REVIEW_MIN_USES} across "
              f"{REVIEW_MIN_PROJECTS} projects, an empty row needs {FILL_MIN}, the judge check needs {DRIFT_WINDOW}.")
        return
    for i, p in enumerate(props, 1):
        print(f"{i}. {p['kind']}: {p['target']}. Evidence: {p['evidence']}")


if __name__ == "__main__":
    main()
