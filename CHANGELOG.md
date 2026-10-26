# Changelog

All notable changes to the public skill set. Each skill has its own section so changes stay traceable.

## 2026-10-26

### 新增 7 个 Skill（从私有工作仓筛选）

- 中文：从私有工作仓筛选 7 个可公开的原创 Skill 迁入：`code-review`、`self-improving-agent`、`md-to-docx`、`html-to-pdf`、`prompt-optimizer`、`dev-workflow`、`merge-dev-docs`。筛选口径为原创、无公司实体内容（公司名、客户、内网路径、价格与费率）、无私有仓库或内部平台依赖、内容通用可复用。
- English: Moved seven public-safe original skills over from the private work repo: `code-review`, `self-improving-agent`, `md-to-docx`, `html-to-pdf`, `prompt-optimizer`, `dev-workflow` and `merge-dev-docs`. Selection criteria: original work, no company-identifying content (names, clients, intranet paths, pricing, fee rates), no dependency on a private repo or internal platform, and generic enough to reuse.
- 中文：迁移时清除了个人绝对路径与内部项目名，删除市场侧的定价字段与生成的 `CONTRIBUTORS` 文件，补齐 `LICENSE`、`.gitignore` 与四套插件清单（Claude Code / CodeBuddy / Codex / Cursor）。
- English: On migration, personal absolute paths and internal project names were stripped, marketplace pricing fields and generated `CONTRIBUTORS` files were dropped, and `LICENSE`, `.gitignore` plus four plugin manifests (Claude Code / CodeBuddy / Codex / Cursor) were added.
- 中文：公开层由 7 个 Skill 增至 14 个，原创 Skill 由 6 个增至 13 个；两份根 README 的徽章、目录表、Skills 章节、兼容性表与仓库结构同步更新。
- English: The public layer grew from 7 to 14 skills, and original skills from 6 to 13. Both root READMEs had their badges, catalog, skill sections, compatibility table and repository layout updated.

### code-review

- 中文：新增。七维审查清单与审计修复分离工作流，含证伪流程、能力边界表、故障剧本与交付前自检清单；改为适合公开仓的 README，删除 SkillHub 案例填写草稿。
- English: New. Seven-dimension review checklist with audit-fix separation, including the falsification step, capability table, troubleshooting scripts and a pre-delivery checklist. README rewritten for the public repo; the SkillHub listing draft was removed.

### self-improving-agent

- 中文：新增。`.learnings/` 三账本记录、提升阈值、Skill 抽取流程与多平台接入；移除 frontmatter 中的 `suggested_price`、`pricing_tier`、`pricing_model` 三个市场字段。
- English: New. Three `.learnings/` ledgers, the promotion threshold, the skill-extraction flow and multi-platform wiring. Removed the `suggested_price`, `pricing_tier` and `pricing_model` marketplace fields from the frontmatter.

### md-to-docx

- 中文：新增。逐元素映射表、七个已踩过的坑、转换与零缺失校验脚本；脚本调用方式改为通用的 `python scripts/...`，依赖说明改为 `pip install python-docx`，删除个人 venv 绝对路径与内部档案名。
- English: New. Element mapping table, seven pitfalls already handled, and the conversion plus zero-loss verification scripts. Invocation is now the generic `python scripts/...`, the dependency note reads `pip install python-docx`, and the personal venv path and internal archive name were removed.

### html-to-pdf

- 中文：新增。打印 CSS、base64 内嵌、Chrome 无头命令、三重核验与六个踩坑；Chrome 路径改为 `shutil.which` 查找并注明各平台路径，实战案例中的个人目录与内部项目名已脱敏。
- English: New. Print CSS, base64 inlining, the headless Chrome command, three verification passes and six pitfalls. Chrome is now resolved via `shutil.which` with per-platform notes, and the personal directory and internal project name in the case study were sanitized.

### prompt-optimizer

- 中文：新增。一稿四版（详细展开 / 角色扮演 / 结构化 / 逆向提炼）与策略对比表；frontmatter 中的 `license: MIT` 改为跟随仓库 Apache-2.0，补 `version` 字段。
- English: New. One draft in, four variants out (detailed expansion, role-play, structured decomposition, reverse-engineered) with a strategy comparison table. The frontmatter `license: MIT` was aligned to the repository's Apache-2.0, and a `version` field was added.

### dev-workflow

- 中文：新增。五阶段手册、`docs/` 自动落盘规则、按语言分开的审查指南包；README 说明 review-kit 是公开资料的整理归纳并保留引用链接。
- English: New. Five stage playbooks, the automatic `docs/` write-back rules and per-language review guides. The README states that review-kit summarizes public references and keeps their source links.

### merge-dev-docs

- 中文：新增。六阶段合并流程、裁决判据、六份模板与 `claim-index.cjs` 清点打分脚本；内容原本无公司实体痕迹，仅补许可与插件清单。
- English: New. The phased merge flow, adjudication criteria, six templates and the `claim-index.cjs` inventory and scoring script. The content carried no company-identifying traces; only the license and plugin manifests were added.

### License

- 中文：新增根 `LICENSE`（Apache-2.0）与 `NOTICE`，两份 README 增加许可 footer；6 个原创 Skill 为 Apache-2.0，`html-designer__skillhub` 为第三方例外。
- English: Added a root `LICENSE` (Apache-2.0) and `NOTICE`, plus a license footer in both READMEs. Six original skills are Apache-2.0; `html-designer__skillhub` is a third-party exception.

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
