<div align="center">

# yardon-writer

**A Chinese longform writing skill: make technical writing clear, and narrative writing worth reading.**

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Type](https://img.shields.io/badge/type-longform%20writing-8B5CF6.svg)](#two-modes)
[![Language](https://img.shields.io/badge/language-Chinese-D97706.svg)](#)

[中文](README.md) · **English**

</div>

---

> Explain the technology clearly, and make people want to keep reading. Serious material, written in a human voice.

This is a Chinese longform writing skill, not a generic "writing assistant" prompt. It turns structure, narrative rhythm, banned phrases, self-review and reading experience into executable rules. Decide the mode before writing; run the checklist before publishing.

## What it solves

- Technical posts that read like manuals: complete structure, no reason to keep reading
- Narrative posts that read like diaries: experiences without a point of view
- Mixing the two: lyricism where facts are needed, outlines where a story is needed
- Inventing experiences, numbers or dialogues just to fill the page

The core rule: **decide the mode first**. Technical writing keeps structure, code and searchability. Narrative writing pushes structure into the background and puts the person and the point of view first. Conflicts are resolved by mode, not blended into mush.

## When to use

Good for:

- WeChat articles, technical blogs, CSDN longform
- Project retrospectives, lessons learned, workplace observations
- Turning a PDF, a news link, a transcript or scattered notes into an article
- Continuing, expanding or rewriting an article in a consistent style

Not for:

- Short social posts (Moments, X/Twitter, Xiaohongshu)
- Titles, summaries or SEO keyword stuffing
- Writing that requires inventing a real personal experience

## Two modes

| Mode | Why the reader is here | Structure | Typical use |
|---|---|---|---|
| A: Technical | Find an answer, learn something | Sections, tables, code, chapter summary | Tutorials, internals, hands-on guides, debugging notes |
| B: Narrative | Hear a story, get a point of view | Lighter headings, transitions, first-person experience | Retrospectives, workplace observations, lessons, opinion pieces |

A simple test: **will the reader copy code after reading?** Yes → A. No → B.

## Workflow

1. Read the material and test the topic with HKR: interesting, informative, resonant — at least two of three
2. Pick a mode: A technical / B narrative
3. Pick an article prototype (five prototypes in `references/article-prototypes.md`)
4. Write: AI handles background, analogy candidates, structure and expansion; real experience, core angle and emotional expression come from the author
5. Run the four-layer self-check (`references/banned-and-check.md`)
6. Run the reading-experience check (`references/readability.md`)
7. Final review

## Files

```
yardon-writer/
├── SKILL.md
├── README.md
├── README.en.md
├── LICENSE
└── references/
    ├── style-core.md            style core, two modes, conflict resolution
    ├── voice-dna.md             language DNA: analogy formulas, self-Q&A, short judgments
    ├── article-prototypes.md    five article prototypes
    ├── banned-and-check.md      banned phrases and four-layer self-check
    └── readability.md           reading experience: numbers, emphasis, openings, rhythm
```

## Install

Ask an Agent Skills-compatible tool to install it:

```
Install this skill: https://github.com/YardonYan/for-my-self-skills/tree/main/yardon-writer
```

Or clone the repo and copy `yardon-writer/` into your agent's skills directory. Make sure `SKILL.md` sits at the root of the skill folder.

For tools without skill loading: open `SKILL.md` and paste it into the project rules or system prompt.

## Example prompts

```
Turn these notes into a longform WeChat article in my style.
Rewrite this project retrospective — no diary-style chronology.
Turn this PDF into a technical longform article.
This reads like AI wrote it. Rewrite it using the yardon-writer rules.
```

## Guardrails

- Never invent experiences, numbers, amounts or dialogues
- Explain a technical term the first time it appears
- Desensitize company material by default: no company names, client names, internal data or server addresses
- Do not fake objectivity. "I think" and "I got burned by this" are more credible than "the solution offers significant advantages"

## Tags

`writing` · `chinese` · `longform` · `technical-writing` · `narrative` · `style`

## License

Apache-2.0. See [LICENSE](LICENSE).
