# Short Visual Comparison (5+ Products)

Use this instead of the long-form Comparison template when the article compares 5+ products, tools, or platforms and the reader wants the differences at a glance.

The failure mode this replaces: five equal-length product essays, local-environment framing, footnotes in every paragraph, and a reader who leaves before the first table.

## Hard constraints

- 4,000–6,000 Chinese characters total, frontmatter included. Tables count; long prose does not get extra room.
- 5–8 tables and 1–2 visuals: one cover card, one positioning map or decision flow.
- No in-body citations, footnotes, or "source: ..." text. Keep research notes internal. Add one dated disclaimer at the end: data cutoff, price disclaimer, subjective ratings.
- Do not open with "I checked my local machine" or a list of config directories. Open with what each product delivers.
- Every product gets a one-line intro. Do not write five mini-essays.
- Include company, launch date, latest version or update, user/scale metric, entry price, and model list.
- If a metric is not public, write "官方未公开" or omit it. Never invent a number to fill a cell.

## Structure

1. **Opening**: five one-line intros, then one sentence on why they are not the same category.
2. **Cover + positioning map**: one axis (for example, distance from the code repo or work surface), five product cards, a scenario matrix, a decision flow.
3. **One-line table**: product | one-liner | company | launch / latest | users / scale | entry price.
4. **Model-strategy table**: platform-routed / single-vendor / multi-model / BYOK / fallback behavior.
5. **Skill-extension table**: template library / app store / Claude Code-compatible / IDE-integrated / repo-native.
6. **Commonality table**: MCP, Skills / `SKILL.md`, subagents or experts, cloud execution, local files, enterprise/audit. This answers "what is actually universal?" before the differences.
7. **One product deep dive**: latest version updates, advantage, why it survives, and the cost of that position. Use a table, not a history essay.
8. **Scenario matrix**: office / coding / large refactor / research / enterprise / onboarding. Use stars or 强/中/弱 and label it subjective.
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

## "Why it survives" table

When the reader asks why a product is still around in a crowded market, answer with a competition table, not a tribute:

| Competition | Its answer | The cost |
|---|---|---|
| Stronger coding tool | Compete on whole-project delivery, not code depth | Weak diff review |
| Stronger office tool | Compete on cross-app orchestration and automation | Weak office ecosystem |
| Commodity general agent | Cloud project container + always-on computer + event triggers | Unpredictable credits |
| Model not top-tier | Harness/routing and tool orchestration | Black-box, hard to tune |
| Funding pressure | Overseas revenue + fresh capital | Home market not launched |

End with one honest sentence: what it is good at, what it is not, and why that position is defensible or not.

## Visual guidance

- Use HTML/CSS + a headless browser screenshot for crisp Chinese labels. Do not use AI image generation for text-heavy diagrams; it garbles Chinese.
- Cover: an illustration without text, or an HTML title card over an illustration. Keep the title readable at mobile width.
- Positioning map: one axis, five cards, one matrix, one flow. Do not cram every feature into the image.
- Use 1600px-wide PNGs. At 1600px, body text should be at least 16px; card labels at least 15px.
- Keep the same color per product across the cover, the map, and the tables.

## Anti-patterns

- Five equal-length product sections with repeated feature lists.
- Opening with local config paths, `~/.codex`, `~/.workbuddy`, or "I installed all five".
- Footnotes, source blocks, or "according to ..." in the body.
- Star ratings without a "subjective, default configuration" label.
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
- [ ] No citations in the body; one dated disclaimer at the end.
- [ ] Total length is under 6,000 Chinese characters.
