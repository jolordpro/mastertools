"""Summarize real use of the skill: DT/usage.jsonl joined with the user's picks in DT/decisions.jsonl.

Prints how often each job and mode came up, which build rules the user took or passed over
(on uses where their pick was logged with --use), and how often the judge's top pick matched theirs.
Numbers come only from the files; nothing is estimated.

usage: usage_report.py [--json]
"""
import argparse, json, os, sys
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dt import DT


def read_jsonl(name):
    path = os.path.join(DT, name)
    if not os.path.exists(path):
        return []
    rows = []
    with open(path, encoding="utf-8") as fh:
        lines = fh.readlines()
    for n, line in enumerate(lines, 1):
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except ValueError:
            print(f"skipped {name} line {n}: not JSON", file=sys.stderr)
    return rows


def analyze(uses=None, decisions=None):
    uses = read_jsonl("usage.jsonl") if uses is None else uses
    decisions = read_jsonl("decisions.jsonl") if decisions is None else decisions
    real = [d for d in decisions if d.get("kind") == "real-work"]
    by_id = {u["id"]: u for u in uses}
    picks = {}
    for d in real:  # the latest pick for a use wins; corrections (said) are never picks
        if d.get("source") == "shown" and d.get("use") in by_id and d.get("option"):
            picks[d["use"]] = d
    rules = defaultdict(lambda: {"taken": 0, "passed": 0, "projects": set(), "uses": []})
    judged = []
    for uid, d in picks.items():
        u = by_id[uid]
        chosen = next((o for o in u["options"] if o["label"] == d["option"]), None)
        if chosen is None:
            continue
        # A rule on every option can't be taken or passed over, so it says nothing about the user.
        shared = set.intersection(*(set(o["rules"]) for o in u["options"]))
        for rid in sorted({r for o in u["options"] for r in o["rules"]} - shared):
            st = rules[rid]
            st["taken" if rid in chosen["rules"] else "passed"] += 1
            st["projects"].add(u["project"])
            st["uses"].append(uid)
        top = min(u["options"], key=lambda o: o["rank"])
        if u.get("judge") in ("agent", "self") and len(u["options"]) > 1:
            judged.append({"use": uid, "at": u["at"], "judge": u["judge"], "agree": top["label"] == chosen["label"]})
    judged.sort(key=lambda j: j["at"])
    said = [d for d in real if d.get("source") == "said" and d.get("use") not in picks]
    return {
        "uses": len(uses),
        "by_job": dict(Counter(u["job"] for u in uses)),
        "by_mode": dict(Counter(u["mode"] for u in uses)),
        "by_judge": dict(Counter(u.get("judge", "none") for u in uses)),
        "checks_not_clean": sum(1 for u in uses if u.get("checks") not in ("pass", "not run")),
        "linked_picks": len(picks),
        "picks_by_job": dict(Counter(by_id[k]["job"] for k in picks)),
        "real_picks": len(real),
        "said": len(said),
        "said_by_job": dict(Counter(d.get("job") for d in said)),
        "rules": {k: {**v, "projects": sorted(v["projects"])} for k, v in sorted(rules.items())},
        "judged": judged,
        "whys": {d["use"]: d["why"] for d in picks.values() if d.get("why")},
    }


def render(a):
    out = [f"Uses logged: {a['uses']}. The user's picks tied to a use: {a['linked_picks']}. All real picks: {a['real_picks']} ({a['said']} in their own words)."]
    if not a["uses"]:
        out.append("Nothing logged yet.")
        return "\n".join(out)
    out.append("By job: " + ", ".join(f"{k} {v}" for k, v in sorted(a["by_job"].items())))
    out.append("By mode: " + ", ".join(f"{k} {v}" for k, v in sorted(a["by_mode"].items())))
    out.append("Judge: " + ", ".join(f"{k} {v}" for k, v in sorted(a["by_judge"].items())))
    out.append(f"Uses where a check failed or needed a fix: {a['checks_not_clean']}")
    j = a["judged"]
    if j:
        agree = sum(x["agree"] for x in j)
        out.append(f"Judge's top pick matched the user: {agree} of {len(j)}")
    if a["rules"]:
        out.append("Rules on uses the user picked from (taken / passed over / projects):")
        for rid, st in a["rules"].items():
            out.append(f"  {rid}: {st['taken']} / {st['passed']} / {len(st['projects'])}")
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    res = analyze()
    print(json.dumps(res, indent=1) if a.json else render(res))


if __name__ == "__main__":
    main()
