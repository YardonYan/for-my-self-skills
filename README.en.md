<div align="center">

[中文](./README.md) · **English**

# Yardon Skills

#### Seventeen Agent Skills I use and maintain in real projects

[![Skills](https://img.shields.io/badge/Skills-17-10B981?style=flat-square)](#catalog)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Standard-8B5CF6?style=flat-square)](#compatibility)
[![License](https://img.shields.io/badge/License-Apache--2.0-D97706?style=flat-square)](#license)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-D97706?style=flat-square&logo=anthropic&logoColor=white)](#compatibility)
[![Codex](https://img.shields.io/badge/Codex-compatible-10B981?style=flat-square&logo=openai&logoColor=white)](#compatibility)
[![Qoder](https://img.shields.io/badge/Qoder-compatible-3B82F6?style=flat-square)](#compatibility)

</div>

These skills follow the [Agent Skills](https://agentskills.io) open standard. Tools that support the standard — Claude Code, Codex, Qoder, Cursor, CodeBuddy and others — can load them directly. Every folder has a `SKILL.md`; read it first, then load `references/` only when needed.

This is not a prompt dump or one giant system prompt. Each skill solves one class of problem, with explicit trigger conditions, output shape and boundaries. When the task matches, the agent loads the skill on its own.

Grouped by where the skill sits in your work, four categories, one skill each. Scan the table to find the direction, then open the category you need.

## Categories

| Category | What it covers | Skills |
|---|---|---|
| [Web and Frontend](#web-and-frontend) | Produce interfaces, or fix what is visibly broken in them. Page specs, visual design, mobile sizing, plus rendering-layer debugging for Markdown and SSE. | 4 |
| [Documents and Delivery](#documents-and-delivery) | Turn content into a file someone else can just open: conversions keep fidelity, decks read clearly, publishing lands intact. | 4 |
| [Engineering Workflow and Quality](#engineering-workflow-and-quality) | Own how the work gets done and whether it is right. Requirement-to-design flow, review standards, parallel task orchestration, document merge adjudication, research and distillation for building skills, and how lessons persist. | 6 |
| [Writing and Expression](#writing-and-expression) | Turn thinking into something a person reads clearly and a model executes precisely. | 3 |

## Catalog

### Web and Frontend

Produce interfaces, or fix what is visibly broken in them. Page specs, visual design, mobile sizing, plus rendering-layer debugging for Markdown and SSE.

| Skill | One-liner | Tags | Docs |
|---|---|---|---|
| [html-skill-effectiveness](./html-skill-effectiveness/) | Generate single-file HTML artifacts: reports, dashboards, comparisons, slide decks, interactive explainers | `html` `single-file` `dashboard` `report` | [中文](./html-skill-effectiveness/README.md) · [EN](./html-skill-effectiveness/README.en.md) |
| [html-designer__skillhub](./html-designer__skillhub/) | Web visual design: typography, color, hierarchy, grids and accessibility | `web-design` `html` `css` `landing-page` | [中文](./html-designer__skillhub/README.md) · [EN](./html-designer__skillhub/README.en.md) |
| [mobile-design-spec](./mobile-design-spec/) | Mobile sizing rules for iOS, Android, HarmonyOS, WeChat Mini Program and H5 | `mobile` `ios` `android` `harmonyos` | [中文](./mobile-design-spec/README.md) · [EN](./mobile-design-spec/README.en.md) |
| [markdown-renderer-fix](./markdown-renderer-fix/) | Fix Markdown rendering, SSE garbled Chinese, code highlighting, Mermaid and KaTeX | `markdown` `sse` `encoding` `frontend` | [中文](./markdown-renderer-fix/README.md) · [EN](./markdown-renderer-fix/README.en.md) |

### Documents and Delivery

Turn content into a file someone else can just open: conversions keep fidelity, decks read clearly, publishing lands intact.

| Skill | One-liner | Tags | Docs |
|---|---|---|---|
| [md-to-docx](./md-to-docx/) | Lossless Markdown to Word with element-by-element fidelity and a zero-loss check | `markdown` `docx` `python-docx` | [中文](./md-to-docx/README.md) · [EN](./md-to-docx/README.en.md) |
| [html-to-pdf](./html-to-pdf/) | Print-optimized HTML to PDF via headless Chrome, CJK text intact | `pdf` `headless-chrome` `print` | [中文](./html-to-pdf/README.md) · [EN](./html-to-pdf/README.en.md) |
| [slides-workflow](./slides-workflow/) | Raw material to finished deck: page script, style spec, then one of three formats | `slides` `ppt` `pptx` `deck` | [中文](./slides-workflow/README.md) · [EN](./slides-workflow/README.en.md) |
| [wechat-mp-publish](./wechat-mp-publish/) | Markdown to a WeChat draft, and images that survive the trip | `wechat` `markdown` `publishing` | [中文](./wechat-mp-publish/README.md) · [EN](./wechat-mp-publish/README.en.md) |

### Engineering Workflow and Quality

Own how the work gets done and whether it is right. Requirement-to-design flow, review standards, parallel task orchestration, document merge adjudication, and how lessons persist.

| Skill | One-liner | Tags | Docs |
|---|---|---|---|
| [code-review](./code-review/) | Seven-dimension review checklist for AI-generated code: issue list only, no edits | `code-review` `ai-code` `code-audit` | [中文](./code-review/README.md) · [EN](./code-review/README.en.md) |
| [dev-workflow](./dev-workflow/) | Five-stage development flow with per-stage playbooks and per-language review guides | `dev-workflow` `code-review` `sdlc` | [中文](./dev-workflow/README.md) · [EN](./dev-workflow/README.en.md) |
| [task-skill-orchestrator](./task-skill-orchestrator/) | Turn a complex request into a dependency-aware DAG and dispatch it in parallel waves to sub-agents | `orchestration` `dag` `multi-agent` | [中文](./task-skill-orchestrator/README.md) · [EN](./task-skill-orchestrator/README.en.md) |
| [merge-dev-docs](./merge-dev-docs/) | Merge two sets of dev docs by adjudicating conflicts, not summarizing | `documentation` `conflict-matrix` `adr` | [中文](./merge-dev-docs/README.md) · [EN](./merge-dev-docs/README.en.md) |
| [skill-authoring](./skill-authoring/) | Research and distillation for building skills: six lanes, triple filter, failure fallback table | `skill-authoring` `research` `distillation` `quality-gate` | [中文](./skill-authoring/README.md) · [EN](./skill-authoring/README.en.md) |
| [self-improving-agent](./self-improving-agent/) | Turn corrections, failures and knowledge gaps into project rules or a new skill | `learnings` `memory` `retrospective` | [中文](./self-improving-agent/README.md) · [EN](./self-improving-agent/README.en.md) |

### Writing and Expression

Turn thinking into something a person reads clearly and a model executes precisely.

| Skill | One-liner | Tags | Docs |
|---|---|---|---|
| [tech-blog-generator](./tech-blog-generator/) | Turn code or technical docs into readable technical blog posts and tutorials | `technical-writing` `blog` `documentation` | [中文](./tech-blog-generator/README.md) · [EN](./tech-blog-generator/README.en.md) |
| [yardon-writer](./yardon-writer/) | Chinese longform writing in two modes: technical and narrative | `writing` `chinese` `longform` | [中文](./yardon-writer/README.md) · [EN](./yardon-writer/README.en.md) |
| [prompt-optimizer](./prompt-optimizer/) | One draft prompt in, four strategy variants out, pick one | `prompt-engineering` `llm` `rewrite` | [中文](./prompt-optimizer/README.md) · [EN](./prompt-optimizer/README.en.md) |

## Install

### Let the agent install it

In any Agent Skills-compatible tool, say:

```
Install this skill: https://github.com/YardonYan/for-my-self-skills/tree/main/<skill-name>
```

Replace `<skill-name>` with one of the folders above, for example:

```
Install this skill: https://github.com/YardonYan/for-my-self-skills/tree/main/tech-blog-generator
```

### Manual install

```bash
git clone https://github.com/YardonYan/for-my-self-skills.git
cp -r for-my-self-skills/<skill-name> <your-agent-skills-dir>/
```

Skill directories differ by tool. Claude Code commonly uses `~/.claude/skills/`; check your tool's docs. What matters is that `<skill-name>/SKILL.md` sits at the root of the skill folder.

### Tools without skill loading

Open `<skill-name>/SKILL.md` and paste it into the project rules, system prompt or the start of the conversation. The rules still work, but the tool will not auto-load the skill on matching triggers.

## Skills

Grouped the same way as above. Collapsed, each entry shows only the skill name and its one-liner; expand for what it solves, when to use it, what is inside and where it stops.

### Web and Frontend

Produce interfaces, or fix what is visibly broken in them. Page specs, visual design, mobile sizing, plus rendering-layer debugging for Markdown and SSE.

<details>
<summary><b>html-skill-effectiveness</b> — Turn documents people skim into single-file HTML documents people actually read.</summary>

**What it solves:** Markdown is linear. It cannot express side-by-side comparisons, zoomable architecture diagrams, slide decks with speaker notes, or live dashboards. This skill makes the agent produce one self-contained HTML file with inline CSS/JS, zero external dependencies, openable directly in a browser.

**When to use it:** You need a report, a comparison page, a data dashboard, a slide deck or an interactive explainer delivered as a single file you can send to someone.

**Inside:** 13 page patterns, a five-dimension critique system, the DevLoop iteration process, seven craft rules (anti-AI-slop, color, typography, hierarchy, motion, accessibility, laws of UX), plus state-coverage and form-validation contracts.

**Example prompts:**

```
Turn this week's data into a single-file HTML dashboard.
Lay these options out as a side-by-side comparison I can send to my team.
Turn this technical note into a slide deck with speaker notes.
```

**Boundaries:** No auth, payments, backend logic or real-time databases. The skill refuses those and explains why.

**Tags:** `html` `single-file` `report` `dashboard` `presentation` `interactive` `frontend`

Docs: [中文](./html-skill-effectiveness/README.md) · [English](./html-skill-effectiveness/README.en.md)

</details>

<details>
<summary><b>html-designer__skillhub</b> — Turn web design principles into clean, openable HTML/CSS pages.</summary>

**What it solves:** Pages that work but look unpolished: arbitrary type sizes, line heights, spacing and hierarchy; colors chosen by feel; mobile and desktop layouts that do not share a grid. This skill applies typography, color, grid, hierarchy and accessibility rules to produce clean HTML/CSS.

**When to use it:** Landing pages, campaign pages, portfolios, design systems, type and color schemes, or turning a mockup/design brief into HTML.

**Inside:** 4 design references (graphic design, glossary, UI/UX, web design), 5 openable HTML examples, a design workflow and an accessibility checklist.

**Note:** This is a third-party skill collected from SkillHub, not original work by Yardon. The original `SKILL.md`, `references/` and `assets/` are kept here; source and version are recorded in `_skillhub_meta.json`.

**Example prompts:**

```
Build a minimal product landing page with professional typography, color and spacing.
Redesign this portfolio page without changing the content.
Give me a type and color system for a SaaS website, then implement it in HTML.
```

**Tags:** `web-design` `html` `css` `typography` `color` `landing-page` `portfolio` `accessibility`

Docs: [中文](./html-designer__skillhub/README.md) · [English](./html-designer__skillhub/README.en.md)

</details>

<details>
<summary><b>mobile-design-spec</b> — Apply five mobile sizing systems to code and explain the source of every change.</summary>

**What it solves:** Mobile code is full of “looks about right” numbers: touch targets too small, content touching the screen edge, bottom buttons hidden by the gesture area, text below the readable minimum, wrong units per platform. This skill centralizes the rules for iOS, Android, HarmonyOS, WeChat Mini Program and H5, plus tablets, foldables, car displays and large screens.

**When to use it:** Writing or changing mobile/responsive pages, looking up device sizes and safe areas, producing multi-platform design annotations, converting pt/dp/sp/vp/fp/lpx/rpx/px/rem/vw/dvh, or checking tap targets and minimum font sizes.

**Inside:** Five platform rule sets, device parameters and safe areas, unit conversion, foldable layouts, WCAG 2.2 checks, and zero-dependency conversion/lint scripts. Values come from Apple HIG, Material Design 3, HarmonyOS Design, WeChat Mini Program docs, MDN and WCAG; data baseline is 2026-10.

**Example prompts:**

```
The bottom button is hidden by the gesture area. Fix it for iOS and Android.
Annotate this mockup for iOS, Android, HarmonyOS, Mini Program and H5.
Check this page's tap targets and font sizes.
```

**Dependency:** The core rules only need `SKILL.md`; bundled scripts need Node.js >= 18.

**Tags:** `mobile` `ios` `android` `harmonyos` `wechat-miniprogram` `responsive` `safe-area` `accessibility` `wcag`

Docs: [中文](./mobile-design-spec/README.md) · [English](./mobile-design-spec/README.en.md)

</details>

<details>
<summary><b>markdown-renderer-fix</b> — Fix garbled Chinese, broken Markdown and streaming output at the data-flow root.</summary>

**What it solves:** Garbled Chinese looks like an encoding bug, but the data crosses backend decoding, JSON escaping, HTTP transport, frontend TextDecoder and Markdown parsing. Fixing one stage often is not enough. This skill diagnoses each stage and ships paired frontend/backend fixes.

**When to use it:** SSE streaming shows garbled text, Markdown tables/code blocks/Mermaid/KaTeX render incorrectly, tool-call output needs filtering, or Chinese text displays badly in the frontend.

**Inside:** An eight-stage data-flow diagnosis, frontend/backend encoding templates, code-highlighting/Mermaid/KaTeX fixes, tool-call filtering, and v3.0.0 production cases.

**Example prompts:**

```
SSE streaming turns Chinese into garbled characters. Find the root cause.
Mermaid diagrams do not render and code blocks are not highlighted.
The stream is printing the tool-call JSON. Filter it out.
```

**Tags:** `markdown` `sse` `streaming` `encoding` `chinese` `mermaid` `katex` `frontend`

Docs: [中文](./markdown-renderer-fix/README.md) · [English](./markdown-renderer-fix/README.en.md)

</details>

### Documents and Delivery

Turn content into a file someone else can just open: conversions keep fidelity, decks read clearly, publishing lands intact.

<details>
<summary><b>md-to-docx</b> — Map Markdown to Word element by element, then prove nothing was dropped. `RESULT: PASS` or it isn't done.</summary>

**What it solves:** pandoc needs another install and CJK styling work; online converters can't take internal documents; copy-paste collapses formatting and misaligns tables. This skill maps structure directly with `python-docx`, then verifies character by character: every Markdown content line must appear in the docx, and heading, table and code-block counts must match.

**When to use it:** Markdown that has to become Word for archiving or submission — weekly reports, standard archives, manuals, proposals.

**Inside:** A complete element mapping table (headings / tables / code / quotes / lists / rules / inline formatting), heading and table shading implementations, seven pitfalls already handled (italic regex eating dimensions, table separators read as rules, A4 vs Letter, CJK `eastAsia` fonts, ordered-list renumbering, box-drawing alignment), plus two parameterised scripts for conversion and verification.

**Dependency:** `pip install python-docx` — the only third-party package.

**Boundaries:** Images are not embedded yet; add an image-paragraph step when needed.

**Example prompts:**

```
Convert this md to Word — it has to be lossless.
Turn this weekly report into a docx for archiving.
This manual goes to non-technical colleagues; give me a Word file.
```

**Tags:** `markdown` `docx` `word` `python-docx` `document-conversion`

Docs: [中文](./md-to-docx/README.md) · [English](./md-to-docx/README.en.md)

</details>

<details>
<summary><b>html-to-pdf</b> — CSS is the typesetting language; `@page` controls the paper. CJK intact, tables whole.</summary>

**What it solves:** weasyprint needs GTK on Windows; reportlab means registering CJK fonts and writing table layout in code; Word-to-PDF depends on the Office version and local fonts. This skill uses headless Chrome in a fixed three-step flow: write print-optimized HTML, inline images as base64, then verify page count and keywords and render pages to PNG for a visual check.

**When to use it:** Manuals, handbooks, reports and proposals delivered as PDF to people who don't render Markdown.

**Inside:** The key print CSS rules, the base64 inlining approach, the headless Chrome command with URI escaping, three verification passes (page count / keywords / render check), six pitfalls (silent failure on CJK paths, locked PDFs reporting success, never deleting the source, duplicate figure titles, CJK and emoji in Pillow, stale figures after copy edits), and the one-source-two-outputs pattern for PDF plus web.

**Dependencies:** Chrome or Edge; `fitz` (PyMuPDF) for verification.

**Tags:** `pdf` `html` `headless-chrome` `print` `document-delivery`

Docs: [中文](./html-to-pdf/README.md) · [English](./html-to-pdf/README.en.md)

</details>

<details>
<summary><b>slides-workflow</b> — Content first, format second. Settle what the deck says, then what it looks like, then whether it becomes HTML, image pages or an editable PPTX.</summary>

**What it solves:** The usual AI deck failure isn't "it can't produce one" — it's discovering halfway through that the direction was wrong. The model paginates on its own, the finished draft has the wrong page order and emphasis, and you throw it away. Without a style spec every page is designed separately until the deck looks like three decks. Pick the wrong format and you need an editable PPTX when you only wanted something to read. This skill splits the work into four stages with hard gates after the first two.

**When to use it:** Turning a pile of material into a report or training deck, deciding between HTML and an editable PPTX, converting an image deck back into something editable, or finding out why a few pages never come out right.

**Inside:** The four-stage method (two brief types, the seven-field page script, the style spec template, the five-part revision request), three build prompts (HTML Slides, image pages, editable PPTX, each with an acceptance checklist), the image-to-PPTX reconstruction method and the rule about clearing original text, nine known failure modes, and two zero-dependency verification scripts.

**Boundaries:** No decks from thin air, no pixel-perfect brand template reproduction, no deliverables that need a network connection to present. Plain document conversion belongs to `md-to-docx` and `html-to-pdf`.

**Example prompts:**

```
Turn these materials into a report deck.
This deck will be revised repeatedly — how do I get an editable version out of AI?
I have a deck as images and want a PPTX I can edit.
```

**Tags:** `slides` `ppt` `pptx` `presentation` `deck` `workflow`

Docs: [中文](./slides-workflow/README.md) · [English](./slides-workflow/README.en.md)

</details>

<details>
<summary><b>wechat-mp-publish</b> — Markdown in, WeChat draft out. Fixes the problem that keeps biting: images vanish after pasting.</summary>

**What it solves:** Publishing to WeChat rarely fails on layout. It fails on images. `![](images/a.png)` in Markdown becomes a broken icon once pasted, and hosting on Gitee or OSS does not help — WeChat only renders images from its own CDN and adds Referer hotlink protection. This skill uploads every image through `media/uploadimg` to get an `mmbiz.qpic.cn` URL before writing the article body.

**When to use it:** Publishing markdown to WeChat, images that disappear after upload, or pushing an article into the draft box.

**Inside:** Markdown to all-inline HTML (WeChat strips style and class tags), three themes, automatic image upload and oversized-image compression, field-limit validation, draft push, a credential and connectivity check, plus an error-code table for 40164, 40007 and 48001.

**Boundaries:** Stops at the draft box and never clicks publish. No Xiaohongshu or Zhihu layout. Does not write the article.

**Example prompts:**

```
Lay this article out for our WeChat account.
Why do my images disappear after uploading?
Push this markdown into the WeChat draft box.
```

**Tags:** `wechat` `markdown` `publishing` `inline-style` `draft`

Docs: [中文](./wechat-mp-publish/README.md) · [English](./wechat-mp-publish/README.en.md)

</details>

### Engineering Workflow and Quality

Own how the work gets done and whether it is right. Requirement-to-design flow, review standards, parallel task orchestration, document merge adjudication, and how lessons persist.

<details>
<summary><b>code-review</b> — Audit and fix are separate. Review produces an issue list and changes nothing.</summary>

**What it solves:** AI-written code has failure modes that don't show on the surface — calls to APIs that don't exist (hallucinated signatures), `except: pass` swallowing errors and returning defaults (output looks fine, data is already wrong), three layers of abstraction for a 20-line requirement, and rebuilt wheels the project already had. This skill walks a seven-dimension checklist; every issue carries a file:line location, root cause, blast radius and fix direction, and anything unverified is tagged `to-verify`.

**When to use it:** Gating code you wrote with AI, reviewing inherited (or AI-generated) code, or adding one more check before delivery.

**Inside:** Seven dimensions (correctness / hallucination and silent degradation / performance and resources / redundancy and consistency / security / over-engineering / verifiability), the severity order, the falsification step, a capability table, troubleshooting scripts and a pre-delivery checklist.

**Boundaries:** Read-only. Opportunistic fixes and refactors are out of scope; performance tuning gets a direction, not a run; no penetration testing.

**Example prompts:**

```
Review this code with code-review — issue list only, don't touch it.
Run a pre-delivery seven-dimension check on this module.
This code was AI-generated; focus on hallucinated APIs and silent degradation.
```

**Tags:** `code-review` `ai-code` `code-audit` `read-only` `quality-gate`

Docs: [中文](./code-review/README.md) · [English](./code-review/README.en.md)

</details>

<details>
<summary><b>dev-workflow</b> — Requirement → design → implementation → code review → bug fix, each stage with its own playbook.</summary>

**What it solves:** Writing code the moment a requirement arrives is the classic failure. Skipping requirement analysis builds the wrong thing; skipping design means rewriting halfway; skipping review ships the defects. This skill splits the work into five stages, infers the current one from what you said, and loads the matching playbook.

**When to use it:** Requirement analysis, design and architecture, starting implementation, code review, or locating and fixing a bug.

**Inside:** Five stage playbooks (requirement / design / implementation / review / bug fix), automatic write-back to `docs/` with timestamped blocks, and per-language review guides (Go, Java, Python, Rust, C, C++, Qt, TypeScript, React, Vue, CSS) plus architecture, security and performance guides.

**Note:** The review guides summarize public references (the Go official guide, the Uber Go Style Guide, JetBrains' SOLID discussion, MDN and others); source links are kept at the end of each document.

**Boundaries:** `dev-workflow` owns the process; the review standard comes from `code-review`. Both can coexist.

**Example prompts:**

```
Analyze this requirement and give me the requirement doc first.
Start implementing this design.
Find and fix this bug.
```

**Tags:** `dev-workflow` `code-review` `sdlc` `requirement` `documentation`

Docs: [中文](./dev-workflow/README.md) · [English](./dev-workflow/README.en.md)

</details>

<details>
<summary><b>task-skill-orchestrator</b> — Decompose a complex request into a dependency-aware DAG and dispatch it in parallel waves to sub-agents.</summary>

**What it solves:** For a request like “research three companies and produce one comparison report”, the default approach is sequential: A, then B, then C. This skill splits the work into subtasks and dependencies, runs independent work in the same wave, and aggregates the results, reducing waiting and context switching.

**When to use it:** A request naturally breaks into independent sub-goals, needs parallel work, batch processing or complex task orchestration.

**Inside:** DAG decomposition, wave scheduling, sub-agent roles, result aggregation, failure retry and concurrency control.

**Platform requirements:** Designed for OpenClaw's `sessions_spawn` sub-agent mechanism. It expects `file-agent`, `search-agent`, `browser`, `app-agent` and `computer-agent`. Other platforms need to replace the dispatch layer.

**Example prompts:**

```
Research these three companies in parallel and produce one comparison report.
Break this large task down, run what can be parallel, and deliver one result.
Process these files in batches of five and retry failures separately.
```

**Tags:** `orchestration` `dag` `multi-agent` `parallel` `subagents` `task-planning`

Docs: [中文](./task-skill-orchestrator/README.md) · [English](./task-skill-orchestrator/README.en.md)

</details>

<details>
<summary><b>merge-dev-docs</b> — Merging is conflict adjudication, not summarization.</summary>

**What it solves:** Ask a model to "blend" two sets of dev docs and the output is always vaguer than either input — and a vague spec is no spec. This skill extracts claims one by one, finds the real conflicts, adjudicates each with evidence and writes something executable. It also handles three traps that break a naive merge: wording contamination from reading A before B, a single set contradicting itself, and old and new designs mixed in tense.

**When to use it:** Two sets of development documents need to become one, architecture docs need aligning, or a team standard should take the best of both.

**Inside:** A phased flow (settle premises / inventory / independent profiles / extract claims and build the matrix / adjudicate / hard gate then write the volumes / record decisions), `judgment-rules.md` for adjudication criteria, six templates (doc profile, conflict matrix, ADR, deprecation list, merged architecture doc and merged dev spec), and `claim-index.cjs` for inventory and overlap scoring (Node 20+, zero dependencies).

**Boundaries:** Not for merging code (use diff / rebase), not needed for a single document set, and unnecessary when the two sets cover unrelated topics.

**Example prompts:**

```
Merge these two sets of development documents into one executable spec.
Align these two architecture docs and adjudicate the conflicts.
Take the best of both and produce one team standard.
```

**Tags:** `documentation` `conflict-matrix` `adr` `dev-docs` `merge`

Docs: [中文](./merge-dev-docs/README.md) · [English](./merge-dev-docs/README.en.md)

</details>

<details>
<summary><b>skill-authoring</b> — Building a skill is not a template problem. It is how clean the research is and how hard the distillation cuts.</summary>

**What it solves:** Two ways to ship a useless skill, neither visible in the finished file. Skewed research: read only the person's own books and you get the version they wanted you to see; read only outside commentary and you get everyone else's version; read only recent activity and a passing remark becomes a lifelong position. Soft distillation: thirty candidates shipped as-is and the reader remembers none, or "think long-term" dressed up as a unique insight. This skill does two things only — cut the research cleanly, distill it hard.

**When to use it:** Turning a person, a topic, or a pile of project docs and issues into a loadable skill; or auditing a third-party skill to decide whether its claims hold up.

**Inside:** Six research lanes with a source-weighting table, the triple filter's pass/fail routing, the three-column failure fallback table, three checkpoints, weak-vs-strong honest boundaries, the difference between a verifiable check and a keyword count, plus a six-question audit for existing skills and eight anti-patterns.

**Boundaries:** No layout, no template filling, and no verdict on whether a claim is true for you — it gives the evidence standard only. Explicitly refuses to source material around copyright or licensing.

**Example prompts:**

```
Build me a Munger perspective skill, focused on how he judges investments.
Turn our production validation flow into a Skill — I'll send you the material.
This Skill claims every example scored A. Check whether that holds up.
```

**Tags:** `skill-authoring` `research` `distillation` `quality-gate` `evidence`

Docs: [中文](./skill-authoring/README.md) · [English](./skill-authoring/README.en.md)

</details>

<details>
<summary><b>self-improving-agent</b> — Log every correction, failure and knowledge gap into `.learnings/`; promote the recurring ones into rules.</summary>

**What it solves:** An agent forgets everything between sessions, so the same trap gets hit next week — the lesson lived only in one conversation. This skill turns "remember that" into a structured, searchable, closable action: three ledger files for lessons, failures and missing features, each entry carrying an ID, priority, status and area, related entries linked with `See Also`, and patterns past the threshold compressed into one preventive rule in the project rules file.

**When to use it:** You were corrected, a command failed, your knowledge turned out stale, the user asked for something missing, or you want to extract a reusable approach into a new skill.

**Inside:** Full templates and field tables for the three ledgers, ID rules, status transitions and closing the loop, duplicate detection, the promotion threshold, criteria and quality gates for extracting a skill, and multi-platform wiring including optional hook scripts.

**Boundaries:** Scoped to record, promote and extract. Active failure fixing belongs to `self-healing`; one-off typos are not logged.

**Example prompts:**

```
Log this pitfall into .learnings/.
Review .learnings/ and promote the recurring patterns into rules.
This approach worked — extract it into a skill.
```

**Tags:** `learnings` `memory` `retrospective` `self-improving` `knowledge-base`

Docs: [中文](./self-improving-agent/README.md) · [English](./self-improving-agent/README.en.md)

</details>

### Writing and Expression

Turn thinking into something a person reads clearly and a model executes precisely.

<details>
<summary><b>tech-blog-generator</b> — Turn code and docs into technical blog posts people can actually read, not terminology dumps.</summary>

**What it solves:** Technical writing often becomes a code paraphrase or correct-but-empty filler. This skill follows a senior engineer's writing process: analyze the code architecture, choose a genre, apply 21 anti-fluff rules, then run three review passes.

**When to use it:** Upload code or technical docs and ask for a blog post, tutorial, code explanation or documentation. Chinese and English are both supported.

**Inside:** 21 writing rules, 6 genre templates, 3 review passes and bilingual templates. It focuses on technical writing only — not marketing copy, UI copy or casual chat.

**Example prompts:**

```
Turn this Python project into a technical blog post.
Write a tutorial from this design doc for readers new to the framework.
Explain these modules in an article with code and trade-offs.
```

**Tags:** `technical-writing` `blog` `tutorial` `documentation` `bilingual` `chinese`

Docs: [中文](./tech-blog-generator/README.md) · [English](./tech-blog-generator/README.en.md)

</details>

<details>
<summary><b>yardon-writer</b> — Chinese longform writing: technical posts stay clear, narrative posts stay readable.</summary>

**What it solves:** Technical posts turn into manuals, narrative posts turn into diaries, and mixing the two satisfies neither. This skill decides the mode first, applies the matching structure, rhythm and banned-phrase rules, then runs a reading-experience check.

**When to use it:** WeChat articles, technical blogs, CSDN longform, project retrospectives, lessons learned and workplace observations. Also useful for turning a PDF, news link, transcript or scattered notes into an article.

**Two modes:** Mode A keeps sections, tables, code and chapter summaries. Mode B pushes headings into the background, uses transitions, and puts first-person experience and a point of view first.

**Boundaries:** Not for short social posts. Never invent experiences, numbers, amounts or dialogues. Company material is desensitized by default.

**Example prompts:**

```
Turn these notes into a longform WeChat article in my style.
Rewrite this project retrospective — no diary-style chronology.
Turn this PDF into a technical longform article.
This reads like AI wrote it. Rewrite it using the yardon-writer rules.
```

**Tags:** `writing` `chinese` `longform` `technical-writing` `narrative` `style`

Docs: [中文](./yardon-writer/README.md) · [English](./yardon-writer/README.en.md)

</details>

<details>
<summary><b>prompt-optimizer</b> — One draft prompt in, four finished variants out, pick the one that fits.</summary>

**What it solves:** "the model didn't understand me" is almost never the model — the prompt is missing audience, output format, constraints or a definition of done. This skill doesn't polish; it rewrites the same request four ways so you can see how organization changes the result.

**When to use it:** A prompt that isn't landing, a model that keeps missing the point, a need for deterministic output, or simply an instruction that should be more effective.

**Inside:** Four strategies (detailed expansion / role-play / structured decomposition / reverse-engineered), optimization directions and use cases for each, a uniform output format with a comparison table, and five principles that keep the rewrite in bounds.

**Boundaries:** Never changes the intent and never wraps a prompt that is already good; matches the input language.

**Example prompts:**

```
Optimize this prompt and give me a few versions to compare.
The model keeps missing my point — rewrite this request clearly.
```

**Tags:** `prompt-engineering` `prompt` `rewrite` `llm`

Docs: [中文](./prompt-optimizer/README.md) · [English](./prompt-optimizer/README.en.md)

</details>

## Compatibility

| Skill | Runtime dependency | Platform notes |
|---|---|---|
| html-skill-effectiveness | None | Any Agent Skills-compatible tool |
| html-designer__skillhub | None | Third-party skill; see its source notes |
| mobile-design-spec | Node.js >= 18 (scripts only) | Rules work without Node |
| markdown-renderer-fix | None / stdlib | Frontend and full-stack projects |
| md-to-docx | Python + python-docx | Required by both scripts |
| html-to-pdf | Chrome/Edge + PyMuPDF | PyMuPDF only for the verification step |
| slides-workflow | Python 3.8+ (scripts only) | Production-stage external skills are optional; prompts work without them |
| wechat-mp-publish | Python 3.8+ (scripts only) | Draft push needs a verified account; paste route does not |
| code-review | None | Any Agent Skills-compatible tool |
| dev-workflow | None | Pairs well with code-review |
| task-skill-orchestrator | OpenClaw `sessions_spawn` + 5 sub-agents | Other platforms need a custom dispatch layer |
| merge-dev-docs | Node.js >= 20 (scripts only) | Rules and templates work without Node |
| skill-authoring | None | Reference-only; no scripts, no network tools required |
| self-improving-agent | None | Needs a writable `.learnings/` in the project |
| tech-blog-generator | None | Any Agent Skills-compatible tool |
| yardon-writer | None | Chinese longform writing |
| prompt-optimizer | None | Any Agent Skills-compatible tool |

Common tools: Claude Code, Codex, Qoder, Cursor, CodeBuddy, and any Agent Skills-compatible agent. Check your tool's docs for the exact load path.

## Repository layout

```
for-my-self-skills/
├── README.md                 Chinese catalog (grouped)
├── README.en.md              English catalog (grouped)
├── CHANGELOG.md              per-skill change notes
│
│   ── Web and Frontend (4) ──
├── html-skill-effectiveness/
│   ├── SKILL.md              main rules (agent entry point)
│   ├── README.md / README.en.md
│   ├── references/
│   └── docs/ assets/ tools/
├── html-designer__skillhub/
├── mobile-design-spec/
├── markdown-renderer-fix/
│
│   ── Documents and Delivery (4) ──
├── md-to-docx/
│   ├── SKILL.md
│   └── scripts/              conversion and zero-loss verification
├── html-to-pdf/
├── slides-workflow/
│   ├── SKILL.md
│   ├── references/           four-stage method and three build prompts
│   ├── assets/               brief, page script and style spec templates
│   └── scripts/              scaffold.py, verify.py
├── wechat-mp-publish/
│   ├── SKILL.md
│   ├── references/           API details, WeChat filter rules
│   ├── assets/               colour themes
│   └── scripts/              wmp.py (convert / check / push / doctor)
│
│   ── Engineering Workflow and Quality (6) ──
├── code-review/
├── dev-workflow/
│   ├── SKILL.md
│   └── reference/            five stage playbooks + review-kit guides
├── task-skill-orchestrator/
├── merge-dev-docs/
│   ├── SKILL.md
│   ├── assets/               six templates
│   └── scripts/              claim-index.cjs
├── skill-authoring/
│   └── SKILL.md              research lanes, triple filter, fallback table, six-question audit
├── self-improving-agent/
│
└── Writing and Expression (3)
    ├── tech-blog-generator/
    ├── yardon-writer/
    └── prompt-optimizer/
```

The directory layout stays flat; the grouping lives in these READMEs only. That keeps every `tree/main/<skill-name>` link working and leaves the install commands untouched.

Every folder uses `SKILL.md` as the entry point. `references/` is loaded on demand, not injected into every prompt.

## Privacy boundary

This public repo contains only the 16 public skills. Personal context, private skills and company material are not included. Names, emails, phone numbers, companies and data in examples are fictional or placeholders. If you find real information in a skill, please open an issue.

## License

The root [LICENSE](./LICENSE) is Apache-2.0; [NOTICE](./NOTICE) documents the third-party exception.

Fifteen original skills are Apache-2.0: html-skill-effectiveness, markdown-renderer-fix, mobile-design-spec, task-skill-orchestrator, tech-blog-generator, yardon-writer, code-review, self-improving-agent, md-to-docx, html-to-pdf, prompt-optimizer, dev-workflow, merge-dev-docs, slides-workflow and wechat-mp-publish. Each folder includes a `LICENSE` file.

`html-designer__skillhub` is a third-party skill collected from SkillHub. It does not include a separate LICENSE file; check the original source and its license before reuse or redistribution.

## Contributing

Issues and PRs are welcome. To keep each skill traceable:

- Keep a PR focused on one skill when possible
- Use commit messages like `docs(<skill>): ...`, `feat(<skill>): ...`, `fix(<skill>): ...`
- Do not put personal experiences, company names, client information or server addresses into public skills
- Use fictional values in examples and mark them as examples

## Changelog

Per-skill changes are recorded in [CHANGELOG.md](./CHANGELOG.md).

---

<div align="center">

[Apache-2.0 License](./LICENSE) · free to use / modify / redistribute with copyright and license notices

Fifteen original skills are Apache-2.0; `html-designer__skillhub` is a third-party skill — see its folder and original source for licensing.

Made by [@YardonYan](https://github.com/YardonYan)

</div>
