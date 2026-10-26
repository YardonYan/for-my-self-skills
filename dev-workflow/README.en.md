# dev-workflow — Five-Stage Development Flow

> Requirement → design → implementation → code review → bug fix. Each stage has its own playbook, so the agent never jumps straight to writing code.

## What it solves

Writing code the moment a requirement arrives is the most common way to fail. Skipping requirement analysis builds the wrong thing; skipping design means rewriting halfway; skipping review ships the defects.

This skill splits development into five stages, infers the current stage from what the user said, then loads the matching playbook:

| Stage | Trigger keywords | Playbook |
|---|---|---|
| Requirement | requirement analysis, clarify the ask, break down the requirement | `reference/requirement.md` |
| Design | design doc, technical design, architecture, how to implement | `reference/design.md` |
| Implementation | implement, start coding, write it | `reference/implementation.md` |
| Code review | review, check the code, anything wrong | `reference/review.md` |
| Bug fix | bug, error, crash, exception, failing test | `reference/bug-fix.md` |

## When to use it

```
Analyze this requirement and give me the requirement doc first.
How should this be designed?
Start implementing this design.
Review this code for me.
Find and fix this bug.
```

## Automatic write-back

Requirement, design and code review output goes to `docs/` by default — no need to ask for a save every time:

- Single module: `docs/需求理解.md`, `docs/方案设计.md`, `docs/代码审查.md`
- Multiple modules: same filenames under `docs/<module>/`
- Appended, each block stamped `## YYYY-MM-DD HH:mm`, history never overwritten
- Optional `docs/模块索引.md` maps module names to document paths

## Bundled review guides

`reference/review-kit/` carries per-language review checklists: Go, Java, Python, Rust, C, C++, Qt, TypeScript, React, Vue and CSS/Less/Sass, plus dedicated architecture, security and performance guides and two templates.

These guides summarize public references (the Go official guide, Effective Go, the Uber Go Style Guide, JetBrains' SOLID discussion, MDN and others); source links are kept at the end of each document.

## How it relates to code-review

- `dev-workflow` is the **process**: which stage you're in, what each stage produces, where output lands
- `code-review` is the **standard**: the seven dimensions, the severity order, falsification and evidence discipline

With both installed, `code-review` supplies the standard when the flow reaches review, and `dev-workflow` keeps it inside the process.

## Install

```bash
git clone https://github.com/YardonYan/for-my-self-skills.git
cp -r for-my-self-skills/dev-workflow <your-agent-skills-dir>/
```

## License

Apache-2.0, see [LICENSE](./LICENSE).
