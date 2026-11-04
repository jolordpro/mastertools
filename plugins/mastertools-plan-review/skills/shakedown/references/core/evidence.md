# Evidence

Shared by challenger, shakedown and stress-test. Edit in `core/`, never in a copy.

## The ladder

Every finding and every factual claim carries one label. Never label above
what the environment allows (the verification ceiling).

| Label | Earned when |
|---|---|
| **Verified** | run or reproduced here; the failure (or the fact) was observed |
| **Sourced** | an outside source says so, and the source and quoted line are given |
| **Traced** | followed end to end in the artifact on paper, not executed |
| **Argued** | reasoning from stated facts only; nothing in the artifact or a source shows it |
| **Hypothesis** | plausible; the Verify steps are the test that would settle it |

Shakedown's three report classes are the same rungs: Verified, Traced,
Hypothesis. Sourced and Argued are used where the work has outside facts
(research, product behavior) or is a plan with nothing to trace.

## Receipts inline

- A claim's receipt sits next to it: the command and its output, `file:line`,
  or the URL and the quoted line.
- No receipt, no Verified or Sourced label. Drop it to Argued or Hypothesis.
- "I checked" is not a receipt. The thing checked is.

## Design the check before trusting it

A check that cannot fail is decoration.

- **Name the input that would make the check fail** before running it. If no
  such input exists, the check proves nothing.
- **Pick a witness that can fail:** a test that runs the changed code, a
  probe that reads the real output, a counterexample fed on purpose.
- **Run the check once against a known failure** where that's cheap. A
  detector that has never caught anything has not been shown to work.
- **A skip is never a pass.** A check that didn't run is reported as "not
  run," with why.
- **An empty or zero result is a finding about the method** until a known
  positive shows the method can see.

## Claim check

Plans and revisions carry claims that were never checked. Before a plan
reaches the human:

1. List every factual claim it rests on, one checkable line each.
2. A fresh checker (see `independence.md`) marks each VERIFIED, WRONG (with
   the correct fact) or UNVERIFIABLE (with why), and quotes its receipt.
3. Fix each WRONG claim; carry each UNVERIFIABLE one as a flagged assumption.
4. Report the count: checked, wrong, still unverified, and who checked.
