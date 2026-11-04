#!/usr/bin/env python3
"""selftest.py: runs the known-positive / known-negative checks for look.py and vision.swift.
Prints PASS/FAIL (or SKIP when Apple Vision is absent) per check; exits non-zero on any FAIL."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests"))


def main():
    try:
        import test_metrics
    except ImportError as exc:
        print("FAIL  cannot import tests: %s" % exc)
        return 2
    results = test_metrics.run_all()
    for name, status, detail in results:
        print("%-4s  %s%s" % (status, name, ("   [%s]" % detail) if detail and status != "PASS" else ""))
    fails = [r for r in results if r[1] == "FAIL"]
    print("\n%d PASS, %d FAIL, %d SKIP" % (sum(r[1] == "PASS" for r in results), len(fails), sum(r[1] == "SKIP" for r in results)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
