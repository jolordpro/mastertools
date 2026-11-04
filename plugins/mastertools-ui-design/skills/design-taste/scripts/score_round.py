"""Score a round's locked predictions against the user's answers.

usage: score_round.py DT ROUND        (e.g. round-1)
Reads DT/predictions/ROUND.json (verifies its checksum against LOCK.log) and
DT/rounds/ROUND-answers.json. Writes DT/scores/ROUND.json and prints a table.
Accuracy per source counts only pairs where the source made a call. p is the one-sided
binomial chance of doing at least that well by coin flip. When pairs carry a "part"
(test or train), each part is also scored on its own as part_<name>.
A prediction file may name extra sources in "sources"; they are scored the same way.
head_to_head: on pairs where the profile and another source both call and disagree,
how often each was right, with a one-sided sign test for the profile (proof check 2).
Each extra source gets the same duel against every built-in source in head_to_head_<name>.
"""
import hashlib, json, math, os, sys

SOURCES = ("profile", "frontend_design", "convention", "jury")

def binom_p(k, n):
    return sum(math.comb(n, i) for i in range(k, n + 1)) / 2 ** n if n else None

def main(dt, rnd):
    pred_path = os.path.join(dt, "predictions", f"{rnd}.json")
    digest = hashlib.sha256(open(pred_path, "rb").read()).hexdigest()
    locked = [l for l in open(os.path.join(dt, "predictions", "LOCK.log")) if f" {rnd}.json " in l]
    if not locked or f"sha256={digest}" not in locked[-1]:
        sys.exit("refused: prediction file does not match its locked checksum")
    pf = json.load(open(pred_path))
    pred = {p["id"]: p for p in pf["pairs"]}
    sources = SOURCES + tuple(s for s in pf.get("sources", ()) if s not in SOURCES)
    ans = json.load(open(os.path.join(dt, "rounds", f"{rnd}-answers.json")))
    picks = {a["id"]: a for a in ans["answers"] if a.get("pick") in ("A", "B")}
    out, repeats = {}, []
    def tally(src, part=None):
        hit = n = 0
        for pid, a in picks.items():
            p = pred.get(pid)
            if not p or p.get("repeat_of") or (part and p.get("part") != part):
                continue
            call = p["predictions"].get(src)
            if call is None:
                continue
            n += 1
            hit += call["pick"] == a["pick"]
        return {"correct": hit, "called": n, "accuracy": round(hit / n, 3) if n else None, "p_vs_chance": round(binom_p(hit, n), 4) if n else None}
    def duel(other, part=None, me="profile"):
        mine = theirs = 0
        for pid, a in picks.items():
            p = pred.get(pid)
            if not p or p.get("repeat_of") or (part and p.get("part") != part):
                continue
            x, y = p["predictions"].get(me), p["predictions"].get(other)
            if x is None or y is None or x["pick"] == y["pick"]:
                continue
            mine += x["pick"] == a["pick"]
            theirs += y["pick"] == a["pick"]
        n = mine + theirs
        res = {"disagree": n, "profile_right": mine, "other_right": theirs, "p_profile_better": round(binom_p(mine, n), 4) if n else None}
        return res if me == "profile" else {"disagree": n, f"{me}_right": mine, "other_right": theirs, f"p_{me}_better": res["p_profile_better"]}
    for src in sources:
        out[src] = tally(src)
    # Rounds with a locked-away test part (proof check 1) also score each part on its own.
    for part in sorted({p["part"] for p in pred.values() if p.get("part")}):
        out[f"part_{part}"] = {src: tally(src, part) for src in sources}
    parts = [None] + sorted({p["part"] for p in pred.values() if p.get("part")})
    out["head_to_head"] = {(f"part_{pt}" if pt else "all"): {src: duel(src, pt) for src in sources if src != "profile"} for pt in parts}
    for extra in sources[len(SOURCES):]:
        out[f"head_to_head_{extra}"] = {(f"part_{pt}" if pt else "all"): {src: duel(src, pt, extra) for src in SOURCES} for pt in parts}
    for pid, p in pred.items():
        if p.get("repeat_of") and pid in picks and p["repeat_of"] in picks:
            first = picks[p["repeat_of"]]["pick"]
            # the repeat shows the same works swapped, so the same choice is the opposite side
            same = picks[pid]["pick"] != first
            repeats.append(same)
    side = [a["pick"] for a in picks.values()]
    out["consistency"] = {"repeats": len(repeats), "agree": sum(repeats)}
    out["side_bias"] = {"left": side.count("A"), "right": side.count("B")}
    out["answered"] = len(picks)
    os.makedirs(os.path.join(dt, "scores"), exist_ok=True)
    json.dump(out, open(os.path.join(dt, "scores", f"{rnd}.json"), "w"), indent=2)
    for k, v in out.items():
        print(k, v)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
