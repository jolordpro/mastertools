"""Break a scored round down by device/job, profile rule and dial direction.
usage: python3 -I breakdown.py <DT> <round> [<earlier round> ...]   (prints only)
The last section tallies each work over every round named.
"""
import csv, json, sys
D, rnd, rounds = sys.argv[1], sys.argv[2], sys.argv[2:]
P = json.load(open(f"{D}/predictions/{rnd}.json"))
names = P["names"]
pairs = {p["id"]: p for p in P["pairs"]}
dial = {r["id"]: int(r["dial"]) for r in csv.DictReader(open(f"{D}/library/dial.csv"))}
ans = {a["id"]: a for a in json.load(open(f"{D}/rounds/{rnd}-answers.json"))["answers"] if a.get("pick") in ("A", "B")}

def tally(rows):
    n = len(rows); k = sum(rows)
    return f"{k}/{n}" + (f" ({round(100 * k / n)}%)" if n else "")

seg, rule, src_seg, hi = {}, {}, {}, {}
claude = []
for pid, a in ans.items():
    p = pairs[pid]
    if p.get("repeat_of"):
        continue
    key = (f"{p['part']}: " if p.get("part") else "") + f"{p['job'].split()[0]} / {p['device'].split(',')[0]}"
    seg.setdefault(key, [])
    pr = p["predictions"]["profile"]
    if pr:
        seg[key].append(pr["pick"] == a["pick"])
        rule.setdefault(pr.get("rule", "?"), []).append(pr["pick"] == a["pick"])
    for s in ("frontend_design", "convention"):
        c = p["predictions"][s]
        if c:
            src_seg.setdefault((s, key), []).append(c["pick"] == a["pick"])
    da, db = dial[p["A"]], dial[p["B"]]
    if da != db:
        hi.setdefault(key, []).append(a["pick"] == ("A" if da > db else "B"))
    claude.append(p["claude_pick"]["pick"] == a["pick"])

print("profile by segment:"); [print("  ", k, tally(v)) for k, v in sorted(seg.items())]
print("profile by rule:"); [print("  ", k, tally(v)) for k, v in sorted(rule.items())]
print("other sources by segment:"); [print("  ", s, k, tally(v)) for (s, k), v in sorted(src_seg.items())]
print("higher-dial side won, by segment:"); [print("  ", k, tally(v)) for k, v in sorted(hi.items())]
print("Claude's own picks:", tally(claude))
print("repeats:")
for pid, p in pairs.items():
    if p.get("repeat_of") and pid in ans and p["repeat_of"] in ans:
        o = pairs[p["repeat_of"]]
        first = names[o[ans[p["repeat_of"]]["pick"]]]
        second = names[p[ans[pid]["pick"]]]
        print(f"   {p['repeat_of']} {p.get('part', '')} {o['device']}: {names[o['A']]} vs {names[o['B']]} -> {first}, then {second}",
              f"({ans[p['repeat_of']].get('ms')} ms, {ans[pid].get('ms')} ms)")
print("work win rates,", " + ".join(rounds) + ":")
w = {}
for r in rounds:
    RP = json.load(open(f"{D}/predictions/{r}.json"))
    names.update(RP["names"])
    rp = {p["id"]: p for p in RP["pairs"]}
    for a in json.load(open(f"{D}/rounds/{r}-answers.json"))["answers"]:
        if a.get("pick") not in ("A", "B") or a["id"] not in rp:
            continue
        for side in ("A", "B"):
            g = w.setdefault(rp[a["id"]][side], [0, 0])
            g[1] += 1; g[0] += a["pick"] == side
for k, (x, n) in sorted(w.items(), key=lambda t: -t[1][0] / t[1][1]):
    print(f"   {names[k][:22]:22} {x}/{n}")
