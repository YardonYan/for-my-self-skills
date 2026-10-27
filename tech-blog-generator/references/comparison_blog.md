# Short Visual Comparison (5+ Products)

Use this instead of the long-form Comparison template when the article compares 5+ products, tools, or platforms and the reader wants the differences at a glance.

The failure mode this replaces: five equal-length product essays, local-environment framing, footnotes in every paragraph, and a reader who leaves before the first table.

## Hard constraints

- 5,000–7,000 Chinese characters total, frontmatter included. Tables count; long prose does not get extra room.
- 5–8 tables and 1–2 visuals: one cover card, one positioning map or decision flow.
- No in-body citations, footnotes, or "source: ..." text. Keep research notes internal. Add one dated disclaimer at the end: data cutoff, price disclaimer, subjective ratings.
- Do not open with "I checked my local machine" or a list of config directories. Open with what each product delivers.
- Every product gets a one-line intro. Do not write five mini-essays.
- Every product gets a latest-version row and a unique-advantage cell. Never deep-dive only one product; if one gets extra detail, all five get equal treatment.
- Every star matrix needs a rubric and at least two concrete tasks (one office, one coding). Scores without evidence are not allowed.
- Include company, launch date, latest version or update, user/scale metric, entry price, and model list.
- If a metric is not public, write "官方未公开" or omit it. Never invent a number to fill a cell.

## Structure

1. **Opening**: five one-line intros, then one sentence on why they are not the same category.
2. **Cover + positioning map**: one axis (for example, distance from the code repo or work surface), five product cards, a scenario matrix, a decision flow.
3. **One-line table**: product | one-liner | company | launch / latest | users / scale | entry price.
4. **Model-strategy table**: platform-routed / single-vendor / multi-model / BYOK / fallback behavior.
5. **Skill-extension table**: template library / app store / Claude Code-compatible / IDE-integrated / repo-native.
6. **Commonality table**: MCP, Skills / `SKILL.md`, subagents or experts, cloud execution, local files, enterprise/audit. This answers "what is actually universal?" before the differences.
7. **Latest-version table for every product**: latest version/date, what changed, unique combination, still missing. Follow with one short paragraph on the competitive position of all five.
8. **Scoring rubric + task evidence**: six criteria with 5/3/1 definitions and office/coding weights; then one office task and one coding task, each with every product's expected output and why the score. Explain the biggest gap with the rubric. Label expected outputs as推断 unless you actually ran all products.
9. **Decision flow + four combinations + one personal pick.**
10. **One-line ending + dated disclaimer.**

## Model-strategy table

Group products by how they expose models, not by vendor list:

| Route | What it means | What the reader gives up |
|---|---|---|
| Platform-routed | User picks a tier; vendor hides the model | Model-level tuning |
| Single-vendor | One model family, tied to the plan | Vendor lock-in |
| Multi-model routing | User chooses per task; BYOK possible | Decision cost |
| Multi-model auto | Platform picks by default; manual override | Less predictable spend |
| Multi-model custom | User can add models/providers | Setup complexity |

## Skill-extension table

Group products by how extensions are packaged:

| Route | Typical packaging | Best for |
|---|---|---|
| Template library | Skills + MCP in a workspace, no local plugin | Non-technical users, project work |
| App store | Skills + Experts + Connectors + MCP | Office workflows |
| Claude Code-compatible | Plugins with Skills, Agents, Hooks, MCP, LSP | Teams migrating from Claude Code |
| IDE-integrated | Rules + Skills + Commands + Subagents + Hooks + MCP | Large repos, spec-driven teams |
| Repo-native | `AGENTS.md` + Skills + Plugins + MCP | Terminal-first engineering teams |

## Latest-version and competitive-position tables

Every product gets the same treatment. Do not deep-dive one product and reduce the other four to a line.

| Product | Latest version / date | What changed | Unique combination | Still missing |
|---|---|---|---|---|
| Product A | | | | |
| Product B | | | | |

Then a competitive-position table for all five:

| Product | What it relies on | Cost / risk |
|---|---|---|
| Product A | | |
| Product B | | |

End with one honest sentence about the trade-offs, not a tribute to one product.

## Scoring rubric + task evidence

Never publish a star matrix without the rubric and at least two concrete tasks.

| Criterion | 5 | 3 | 1 | Office weight | Coding weight |
|---|---|---|---|---|---|
| Task coverage | | | | 30% | 25% |
| Artifact usability | | | | 30% | 25% |
| Context access | | | | 20% | 20% |
| Operation depth | | | | 10% | 15% |
| Review/correction | | | | 5% | 10% |
| Onboarding | | | | 5% | 5% |

Pick one office task and one coding task. For every product, write the expected output and why the score. Explain the largest gap with the rubric. Do not present expected outputs as a live benchmark; say "按公开能力推演" unless you actually ran all products.

## Visual guidance

- Use HTML/CSS + a headless browser screenshot for crisp Chinese labels. Do not use AI image generation for text-heavy diagrams; it garbles Chinese.
- Cover: an illustration without text, or an HTML title card over an illustration. Keep the title readable at mobile width.
- Positioning map: one axis, five cards, one matrix, one flow. Do not cram every feature into the image.
- Use 1600px-wide PNGs. At 1600px, body text should be at least 16px; card labels at least 15px.
- Keep the same color per product across the cover, the map, and the tables.

## Anti-patterns

- Five equal-length product sections with repeated feature lists.
- Deep-diving one product while the other four get a single line. Equal treatment is mandatory.
- Opening with local config paths, `~/.codex`, `~/.workbuddy`, or "I installed all five".
- Footnotes, source blocks, or "according to ..." in the body.
- Star ratings without a rubric, weights, and at least two concrete task outputs.
- Comparing credit prices across products as if credits were the same unit.
- Stale user counts or prices without a date.
- A "common features" section that only lists logos instead of behaviors.

## Final checklist

- [ ] A reader can name the five products' work surfaces after the first screen.
- [ ] Every product has company, launch, latest, scale, price, models.
- [ ] Model strategy and Skill strategy are separate tables.
- [ ] Commonality is a table, not a paragraph.
- [ ] The deep-dive product has a "why it survives + cost" table.
- [ ] The scenario matrix makes office vs coding obvious.
- [ ] The star matrix has a rubric, weights, and two concrete task outputs.
- [ ] No citations in the body; one dated disclaimer at the end.
- [ ] Total length is under 7,000 Chinese characters.
