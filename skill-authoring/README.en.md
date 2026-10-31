# skill-authoring — Research and Distillation for Building Skills

> Sloppy research means you are laying out the wrong thing beautifully. Weak distillation means you have repackaged common sense.

## What it solves

Two ways to build a useless Skill, and neither is visible in the finished file.

**The research is skewed.** Read only the person's own books and you get the version they wanted you to see. Read only external commentary and you get everyone else's version of them. Read only recent activity and a passing remark becomes a lifelong position. Pick the wrong sources and every later step amplifies the error.

**The distillation is soft.** Thirty candidate points shipped as-is, and the reader remembers none. "Think long-term" dressed up as a unique insight falls apart on contact. Only positive material collected, and you ship a perspective with no blind spots, which is the most dangerous kind.

This Skill handles exactly two things: cut the research cleanly, and distill it hard. Three evidenced models beat ten correct but empty principles.

## When to use it

```
Build me a Munger perspective skill, focused on how he judges investments.
Turn our production validation flow into a Skill — I'll send you the material.
This Skill claims 15 official examples all scored A. Check whether that holds up.
I need to turn a pile of issues and retros into an installable Skill. Where do I start?
```

## Three reusable methods

| Method | Used in | Core idea |
|---|---|---|
| Six-lane research | Research | Original writing, conversations, phrasing, external criticism, decisions, timeline. Six lanes, six files. Skip one and the picture tilts |
| Triple filter | Distillation | Cross-domain recurrence, generative power, exclusivity. All three and it becomes a model; one or two and it degrades to a heuristic; none and it is discarded |
| Failure fallback table | Writing | Trigger condition → first-line fix → fallback if that fails. Three columns covering the cases you know will break. A case with no row has never been run |

## Workflow

1. Scope the source: person, topic or document set, and whether primary material exists
2. Run six-lane research, each lane written to `references/research/01` through `06`, tagged primary, secondary or inferred
3. Distill: run candidates through the triple filter, route by how many gates they pass
4. Write `SKILL.md`: fill the failure fallback table, set three checkpoints, write honest boundaries specific enough to guide a decision
5. Verify: one known question, one edge case, one voice check. Two rounds without a pass means shipping with the weak spots written into the boundaries

## Two checklists included

- **Six questions for auditing an existing Skill**: information density, failure fallbacks, traceable claims, credibility of self-checks, portability, compliance. The first five decide whether it works; the sixth decides whether it can enter a public library
- **Eight anti-patterns**: fabricated quotes, common sense dressed as insight, positive-only material, writing past insufficient information, keyword counting passed off as a check, hardcoded paths, checkpoints that block delivery, handling real people's material without consent

## Boundaries

| Capability | Status |
|---|---|
| Splitting research lanes and filtering candidates | ✓ Core |
| Designing failure fallbacks and self-checks | ✓ Core |
| Auditing third-party Skills for credibility and compliance | ✓ Six-question checklist |
| Layout, styling, template filling | ✗ Not its job |
| Judging whether a claim is true for you | ✗ Provides the evidence standard, the call stays with you |
| Sourcing material around copyright or licensing | ✗ Listed as an anti-pattern |

## Install

```bash
git clone https://github.com/YardonYan/for-my-self-skills.git
cp -r for-my-self-skills/skill-authoring <your-agent-skills-dir>/
```

Or let the agent install it:

```
Install this skill: https://github.com/YardonYan/for-my-self-skills/tree/main/skill-authoring
```

## License

Apache-2.0, see [LICENSE](./LICENSE).

The six-lane research split, the triple filter and the failure fallback table were inspired by [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) (MIT) and then rewritten: sources are weighted by traceability instead of an absolute blocklist, self-checks are verifiable items instead of keyword counts, and paths follow the host platform's convention instead of being hardcoded. No original text was copied.
