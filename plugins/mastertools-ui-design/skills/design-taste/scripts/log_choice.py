"""Append one real-work design choice to DT/decisions.jsonl.

Logs the design attribute, context, job and dial only. Refuses text that looks like
client content (emails, links, money, phone numbers, long passages).
With --use <id> (printed by log_use.py) and --option <label>, the pick is tied to that use,
so usage_report.py can tell which rules the user took or passed over and whether the judge agreed.
"""
import argparse, json, os, re, sys
from datetime import datetime, timezone
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dt import DT, ready

CONTEXTS = {"marketing", "dashboard", "mobile-app", "portfolio", "e-commerce", "other"}
SUSPECT = [
    (re.compile(r"[\w.+-]+@[\w-]+\.\w"), "an email address"),
    (re.compile(r"https?://|www\."), "a link"),
    (re.compile(r"[$€£]\s?\d"), "a money amount"),
    (re.compile(r"\+?\d[\d\s().-]{8,}\d"), "a phone-like number"),
]

def check(field, text):
    if text is None:
        return
    if len(text) > 160:
        sys.exit(f"refused: {field} is {len(text)} characters. Log the design attribute in a few words, not content.")
    for rx, what in SUSPECT:
        if rx.search(text):
            sys.exit(f"refused: {field} contains {what}. Never log client content.")

def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--context", required=True, choices=sorted(CONTEXTS))
    ap.add_argument("--job", required=True)
    ap.add_argument("--attribute", required=True)
    ap.add_argument("--picked", required=True)
    ap.add_argument("--over", required=True)
    ap.add_argument("--dial", type=int, required=True, choices=[1, 2, 3, 4, 5])
    ap.add_argument("--source", required=True, choices=["shown", "said"])
    ap.add_argument("--why")
    ap.add_argument("--use", help="id printed by log_use.py for the brief this pick answers")
    ap.add_argument("--option", help="label of the option the user chose, as given to log_use.py")
    a = ap.parse_args(argv)
    for f in ("job", "attribute", "picked", "over", "why", "option"):
        check(f, getattr(a, f))
    if a.use and not re.fullmatch(r"u-\d{14}-[0-9a-f]{4}", a.use):
        sys.exit(f"refused: --use {a.use} is not an id from log_use.py")
    row = {"at": datetime.now(timezone.utc).isoformat(timespec="seconds"), "kind": "real-work",
           "context": a.context, "job": a.job, "attribute": a.attribute, "picked": a.picked,
           "over": a.over, "dial": a.dial, "source": a.source}
    if a.why:
        row["why"] = a.why
    if a.use:
        row["use"] = a.use
    if a.option:
        row["option"] = a.option
    if not ready():
        print("not logged: the Design Taste folder is not reachable from here")
        return
    path = os.path.join(DT, "decisions.jsonl")
    with open(path, "a") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"logged to {path}: {a.attribute} -> {a.picked} (dial {a.dial}, {a.source})")

if __name__ == "__main__":
    main()
