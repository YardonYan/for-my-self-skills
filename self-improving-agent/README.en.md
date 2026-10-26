# self-improving-agent — Turn Every Mistake into a Rule

> Log corrections, failures and knowledge gaps into `.learnings/`; promote recurring patterns into project rules or a new skill.

## What it solves

An agent forgets everything between sessions. The same trap gets hit again next week, because the lesson lived only in one conversation and never landed anywhere the next session would read.

This skill turns "remember that" into a structured, searchable, closable action:

- Three ledger files, one job each: `LEARNINGS.md` (lessons and corrections), `ERRORS.md` (command and external API failures), `FEATURE_REQUESTS.md` (missing capabilities)
- Every entry carries an ID in `TYPE-YYYYMMDD-XXX` form, plus priority, status and area; related entries are linked with `See Also`
- Once a pattern crosses the promotion threshold (recurrence ≥ 3, across 2 different tasks, inside a 30-day window), the verbose story is compressed into one preventive rule in `AGENTS.md` or `CLAUDE.md`
- Anything reusable on its own gets extracted into a new skill, with the original entry marked `promoted_to_skill`

## When to use it

```
Log this pitfall into .learnings/.
Review .learnings/ and promote the recurring patterns into rules.
This approach worked — extract it into a skill.
```

It also fires when the user says "why is this broken again" or "I told you before".

## Quick reference

| Situation | Action |
|---|---|
| The user corrected you | `LEARNINGS.md`, category `correction` |
| A command, build or API call failed | `ERRORS.md`, with the raw error and reproduction steps |
| Your knowledge turned out to be stale | `LEARNINGS.md`, category `knowledge_gap` |
| The user asked for something missing | `FEATURE_REQUESTS.md` |
| You found a better approach | `LEARNINGS.md`, category `best_practice` |
| It resembles an existing entry | Link with `See Also` and raise the priority |

## Where lessons get promoted

| Target file | What goes in | Platform |
|---|---|---|
| `AGENTS.md` | Agent workflow, tool patterns, automation rules | Any |
| `CLAUDE.md` | Project facts, conventions, caveats | Claude Code |
| `.github/copilot-instructions.md` | Project context and conventions | GitHub Copilot |
| `TOOLS.md` | Local tools, environment, credential locations | Any |
| `.workbuddy/memory/MEMORY.md` | Project-level long-term memory | WorkBuddy / CodeBuddy |

## What's inside

- Full Markdown templates for all three ledgers, plus field value tables
- ID rules, status transitions, closing the loop
- Duplicate detection (`grep` first, then `See Also`)
- Promotion threshold and promotion steps
- Criteria, flow and quality gates for extracting a new skill out of a lesson
- Multi-platform wiring (WorkBuddy / CodeBuddy / Claude Code / Codex CLI / GitHub Copilot), including optional hook script templates

## Boundaries

Scoped to the record → promote → extract chain. Fixing an active failure belongs to `self-healing` (if installed). One-off typos with no cross-session value are not logged.

## Install

```bash
git clone https://github.com/YardonYan/for-my-self-skills.git
cp -r for-my-self-skills/self-improving-agent <your-agent-skills-dir>/
```

On first use, create `.learnings/` in the project root and add the three files from the templates.

## License

Apache-2.0, see [LICENSE](./LICENSE).
