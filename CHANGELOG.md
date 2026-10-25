# Changelog

All notable changes to the public skill set. Each skill has its own section so changes stay traceable.

## 2026-10-26

### Repository

- 中文：公开目录重写为中英文双语；新增 7 个 Skill 的用途、触发场景、标签、安装方式和兼容性说明；公开层固定为 7 个技能。
- English: Rewrote the catalog in Chinese and English; added purpose, triggers, tags, install steps and compatibility for all 7 skills; the public layer is now fixed at 7 skills.
- 中文：`yardon-router` 因引用私有技能，已从公开层移到私有层；公开仓不再包含它。
- English: Moved `yardon-router` out of the public layer because it references private skills.

### html-skill-effectiveness

- 中文：增加 `category: frontend` 与发现标签：`html`、`single-file`、`report`、`dashboard`、`presentation`、`interactive`。
- English: Added `category: frontend` and discovery tags: `html`, `single-file`, `report`, `dashboard`, `presentation`, `interactive`.

### markdown-renderer-fix

- 中文：增加 `category: frontend` 与发现标签：`markdown`、`sse`、`streaming`、`encoding`、`chinese`、`mermaid`、`katex`、`code-highlighting`。
- English: Added `category: frontend` and discovery tags: `markdown`, `sse`, `streaming`, `encoding`, `chinese`, `mermaid`, `katex`, `code-highlighting`.

### mobile-design-spec

- 中文：增加 `category: mobile` 与发现标签：`mobile`、`ios`、`android`、`harmonyos`、`wechat-miniprogram`、`responsive`、`safe-area`、`accessibility`、`wcag`。
- English: Added `category: mobile` and discovery tags: `mobile`, `ios`, `android`, `harmonyos`, `wechat-miniprogram`, `responsive`, `safe-area`, `accessibility`, `wcag`.

### task-skill-orchestrator

- 中文：保留原有标签，增加 `category: orchestration`；在根目录补充平台要求说明（OpenClaw `sessions_spawn` 与 5 类 Sub Agent）。
- English: Kept the existing tags, added `category: orchestration`, and documented the platform requirement (OpenClaw `sessions_spawn` plus 5 sub-agents).

### tech-blog-generator

- 中文：增加 `category: writing` 与发现标签：`technical-writing`、`blog`、`tutorial`、`documentation`、`bilingual`、`chinese`。
- English: Added `category: writing` and discovery tags: `technical-writing`, `blog`, `tutorial`, `documentation`, `bilingual`, `chinese`.

### yardon-writer

- 中文：新增中英文 README 和 Apache-2.0 LICENSE；增加 `category: writing` 与发现标签：`writing`、`chinese`、`longform`、`technical-writing`、`narrative`、`style`。
- English: Added Chinese/English READMEs and an Apache-2.0 LICENSE; added `category: writing` and discovery tags: `writing`, `chinese`, `longform`, `technical-writing`, `narrative`, `style`.

### html-designer__skillhub

- 中文：新增中英文 README，说明这是 SkillHub 第三方 Skill、来源与版本，并补充安装、适用场景和标签；没有附加来源不明的 LICENSE。
- English: Added Chinese/English READMEs documenting that this is a third-party SkillHub skill, its source and version, plus install, use cases and tags. No LICENSE was added because the original license is not included.
- 中文：从 `_skillhub_meta.json` 移除本机安装路径。
- English: Removed the local install path from `_skillhub_meta.json`.

### tech-blog-generator

- 中文：增加 `category: writing` 与发现标签：`technical-writing`、`blog`、`tutorial`、`documentation`、`bilingual`、`chinese`。
- English: Added `category: writing` and discovery tags: `technical-writing`, `blog`, `tutorial`, `documentation`, `bilingual`, `chinese`.
- 中文：移除包含本机路径的一次性 `scripts/backfill-contributions.ps1`。
- English: Removed the one-off `scripts/backfill-contributions.ps1` that contained a local path.

## Earlier

- 2026-10-22: Added `yardon-writer`, `yardon-router` and the public/private source split.
- 2026-10-21: Initial public skill set; collected Anthropic official and design/taste skill packs.
