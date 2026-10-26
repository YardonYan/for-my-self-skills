# code-review — Seven-Dimension Review for AI-Generated Code

> Audit and fix are separate. Review is read-only: produce an issue list, change nothing.

## What it solves

Code written by AI has failure modes that don't show on the surface:

- Calls an API that does not exist (hallucinated signature) — the argument names look plausible
- `except: pass` swallows the error and silently returns a default (silent degradation) — output looks fine, data is already wrong
- Three layers of abstraction for a 20-line requirement, empty base classes (over-engineering)
- Rebuilds a wheel the project already has — only visible with a repo-wide view

Plus the classics: dead code, debug leftovers, unclosed handles, external calls without timeouts, and edits made with no baseline to compare against.

The skill walks a seven-dimension checklist. Every issue must carry a file:line location, root cause, blast radius and fix direction. Anything that cannot be verified is tagged `to-verify`, never written as a conclusion.

## When to use it

```
Review this code with code-review — issue list only, don't touch it.
Run a pre-delivery seven-dimension check on this module.
This code was AI-generated; focus on hallucinated APIs and silent degradation.
```

## The seven dimensions

| # | Dimension | What gets checked |
|---|---|---|
| ① | Correctness bugs | Boundary cases (empty / None / single element / extremes / NaN / cross-day), Windows path separators, CJK encoding corruption, naive vs aware datetimes, data semantics |
| ② | Hallucination & silent degradation | Hallucinated API signatures, `except: pass` blacklist, degradation without a quality flag, config keys that don't exist |
| ③ | Performance & resources | Object allocation / string concat / I/O inside loops, unclosed handles, whole-file loads into memory, external calls without timeout, "it got faster" with no profile numbers |
| ④ | Redundancy & consistency | Dead code (confirm with repo-wide Grep), debug leftovers, extract only at 3+ repeats, duplicate wheels, `_v2` / `_final` suffixed files |
| ⑤ | Security & leakage | Hardcoded secrets, SQL string concat, sensitive data in logs |
| ⑥ | Product & over-engineering | Deletion test (would removing it break anything?), empty base classes, half-finished work built on data that isn't ready |
| ⑦ | Verifiability & reversibility | Blind edits with no baseline, critical paths without tests, "should work" delivery |

Severity order: **correctness > security > maintainability > simplicity > performance > elegance**.

## Workflow

1. Recon: read the target files in full (never fragments), Grep repo-wide for references, record the runtime
2. Walk all seven dimensions; for suspicious APIs, check the official signature or test locally
3. Falsify every confirmed bug once — construct a counterexample (empty, single element, extreme, NaN, cross-day) and try to break your own claim
4. Emit the issue list and **stop** there, waiting for the user to pick what to fix
5. After confirmation, switch to the normal coding flow — fixing is out of scope for this skill

## Boundaries

| Capability | Status |
|---|---|
| Read-only review with an issue list | ✓ core |
| Opportunistic fixes or refactors | ✗ high risk, audit and fix are separate |
| Running performance tuning | ✗ reports direction and baseline requirements only |
| Penetration testing, professional security audit | ✗ common leak patterns only |

## Install

```bash
git clone https://github.com/YardonYan/for-my-self-skills.git
cp -r for-my-self-skills/code-review <your-agent-skills-dir>/
```

Or let the agent install it:

```
Install this skill: https://github.com/YardonYan/for-my-self-skills/tree/main/code-review
```

## License

Apache-2.0, see [LICENSE](./LICENSE).
