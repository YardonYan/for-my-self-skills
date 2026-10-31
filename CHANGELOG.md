# Changelog

All notable changes to the public skill set. Each skill has its own section so changes stay traceable.

## 2026-10-31

### skill-authoring 新增（第 17 个技能）

- 中文：新增 `skill-authoring`，把造 Skill 的调研与提炼方法独立成技能。核心是三件事：六路调研（原始论述、对话即兴、措辞表达、外部评价、决策行为、时间线近期）、三重验证（跨域复现、生成力、排他性，三关全过才算模型，过一到两关降为启发式，零关丢弃）、失败降级表（触发条件 → 一线修复 → 仍失败兜底三列写法）。
- English: Added `skill-authoring`, a standalone skill for the research and distillation work behind building a skill. Three core pieces: six research lanes (original writing, conversations, phrasing, external criticism, decisions, timeline), the triple filter (cross-domain recurrence, generative power, exclusivity — all three make a model, one or two degrade to a heuristic, none is discarded), and the three-column failure fallback table (trigger → first-line fix → fallback).
- 中文：随附两份清单。六问审计用于判断现成 Skill 的可信度与合规性：信息密度、失败降级、结论可溯源、自检可信度、可移植性、合规。反模式八条，含编造原话、常识包装成洞察、只收正面材料、信息不足硬写、关键词统计当自检、路径写死、检查点变阻塞、处理真人材料不提示同意。
- English: Ships two checklists. A six-question audit for judging an existing skill's credibility and compliance: information density, failure fallbacks, traceable claims, credibility of self-checks, portability, compliance. And eight anti-patterns, including fabricated quotes, common sense dressed as insight, positive-only material, writing past insufficient information, keyword counting passed off as a check, hardcoded paths, checkpoints that block delivery, and handling real people's material without consent.
- 中文：方法参考 `alchaincyf/nuwa-skill`（MIT）后重写，并改掉三处判断：信源不设绝对行业黑名单，按可追溯性分权重，机构官方渠道可作一手；自检不采用关键词统计，改为必须产出过或不过的事实依据；路径不硬编码单一工具的 skills 目录，按宿主平台约定处理。未复制其原文，来源与差异在技能 README 与 SKILL.md 末尾标出。
- English: The method was inspired by `alchaincyf/nuwa-skill` (MIT) and then rewritten, with three judgement changes: sources are weighted by traceability instead of an absolute industry blocklist, official channels can count as primary; self-checks must produce a pass-or-fail fact rather than a keyword count; paths follow the host platform instead of hardcoding one tool's skills directory. No original text was copied; the source and the differences are noted at the end of the skill README and SKILL.md.
- 中文：新增 `skill-authoring/` 四件套（`SKILL.md`、`README.md`、`README.en.md`、`LICENSE`）。根 `README.md` 与 `README.en.md` 的技能数 16 改为 17，工程流程与质量分类 5 改为 6，目录表、Skills 详情区、仓库结构图同步挂入口；英文版依赖表补该技能为无依赖。
- English: Added the four-file set under `skill-authoring/` (`SKILL.md`, `README.md`, `README.en.md`, `LICENSE`). Root `README.md` and `README.en.md` moved from 16 to 17 skills and from 5 to 6 in the Engineering Workflow and Quality group; the catalog table, the Skills detail section and the repository layout diagram are cross-linked, and the English dependency table lists this skill as dependency-free.

## 2026-10-28

### tech-blog-generator 增加多产品短对比模板

- 中文：新增 `references/comparison_blog.md`，面向 5 个以上产品/工具的横向对比。硬约束：5–7 千字、5–8 张表、1–2 张图；正文不放脚注/引用；不从本地环境切入；每个产品必须有一句话定位、公司、上线、最新、用户/规模、入门价、模型。
- English: Added `references/comparison_blog.md` for comparisons of 5+ products/tools. Hard constraints: 5–7k Chinese characters, 5–8 tables, 1–2 visuals; no in-body citations; no local-environment framing; each product needs a one-liner, company, launch, latest update, user/scale metric, entry price and model list.
- 中文：把对比拆成五层：模型路线（平台调度/单供应商/多模型）、Skill 扩展路线（模板库/应用商店/Claude Code 兼容/IDE 集成/仓库原生）、共通能力（MCP、Skills、子代理、云端、本地文件、企业审计）、每个产品的最新版本/独有组合/代价、场景评分标准与两个任务产出。不能只深挖一个产品。
- English: Split the comparison into five layers: model strategy, Skill-extension strategy, common capabilities, a latest-version/unique-combination/cost row for every product, and a scoring rubric with two concrete task outputs. Never deep-dive only one product.
- 中文：场景星级必须给评分项、权重、两个任务的实际/预期产出；不能只给分数。
- English: Scenario stars require criteria, weights, and two concrete task outputs; scores alone are not enough.
- 中文：新增深挖版：8 层护城河矩阵（工作面/上下文/分发/扩展/成本/信任/切换成本/资本品牌）、证据表（最强/最弱/什么会杀死它）、竞争格局表；深挖版 8–10 千字、9–11 张表；核心是因果链表、协作图和护城河衰减表。
- English: Added a deep variant: an eight-dimension moat matrix (work surface, context, distribution, extension, cost, trust, switching cost, capital/brand), an evidence table (strongest / weakest / what would kill it) and a competition map; 8–10k characters and 9–11 tables; the causal-chain, collaboration and moat-decay tables carry the depth.
- 中文：新增压缩版：7–8 千字、7 张表、3 张图；保留一句话表、最新版本表、护城河矩阵、因果链、模型/Skill、评分标准、任务表；删掉与因果链重复的证据/竞争/新玩家/衰减表，任务表改成每家一行两列。
- English: Added a compressed variant: 7–8k characters, 7 tables and 3 visuals; keep the one-line, latest-version, moat matrix, causal chain, model/Skill, scoring and task tables; drop the evidence/competition/new-entrant/decay tables that repeat the causal chain, and make the task table product-first with 5 rows.
- 中文：压缩时先删过渡句和元评论（“这张表说明”“不是拍脑袋”），保留数据口径、术语解释和评分理由。
- English: In the compression pass, cut transition/meta sentences first ("this table shows", "not made up"); keep data caveats, term definitions and score reasons.
- 中文：`SKILL.md`、`blog_templates.md`、`README.md` 同步挂入口；5+ 产品场景优先走短图文模板，不再套用长篇对比结构。
- English: Cross-linked from `SKILL.md`, `blog_templates.md` and `README.md`; 5+ product comparisons now route to the short visual template instead of the long-form structure.

### yardon-writer 增加短图文对比原型

- 中文：`references/article-prototypes.md` 新增“6. 短图文对比型（A 模式变体）”，适用 5 个以上产品横向对比；重心是一张定位图 + 模型/Skill/共通能力三张表 + 场景矩阵 + 选型流程，正文控制在 5–7 千字。
- English: Added "6. Short Visual Comparison (A-mode variant)" to `references/article-prototypes.md` for 5+ product comparisons; the focus is one positioning map, three tables (models, Skills, common capabilities), a scenario matrix and a decision flow, with the body kept to 5–7k Chinese characters.
- 中文：选原型速查表同步增加“5 个以上产品横向对比 → 6 短图文对比型”。
- English: The prototype picker table now maps "5+ products side by side" to prototype 6.

## 2026-10-26

### wechat-mp-publish 增加 upload 子命令

- 中文：新增 `upload`，只做一件事：把图片搬进微信图床。支持 Markdown、HTML、图片目录三种输入，逐张调 `media/uploadimg` 换取 `mmbiz.qpic.cn` 地址，输出「原地址 → 微信地址」清单；加 `--rewrite` 生成替换版副本，原文件不动，加 `--json` 输出机器可读映射。
- English: Added the `upload` subcommand, which does exactly one thing: move images onto the WeChat CDN. It accepts a Markdown file, an HTML file or an image folder, uploads each image through `media/uploadimg` to get an `mmbiz.qpic.cn` URL, and prints an old-to-new mapping. `--rewrite` writes a replaced copy without touching the original; `--json` emits a machine-readable mapping.
- 中文：`convert` / `push` 现在会先把工作目录切到目标文件所在目录，从任意位置用绝对路径调用都能正确解析相对图片路径；`-o` 的输出落在目标文件旁边。
- English: `convert` and `push` now switch to the target file's directory first, so relative image paths resolve correctly no matter where you invoke them from, and `-o` writes next to the target file.
- 中文：修正对 `48001` 的绝对化判断。原文写「未认证的个人订阅号调 draft/add 会返回 48001」，但另有实测报告称个人未认证号的 token、`uploadimg`、`add_material`、`draft/add` 四步全通，只有 `freepublish/submit` 需企业认证。两种说法冲突，改为不预设结论：先 `doctor` 再 `push --dry-run` 实测，真报 48001 才回退粘贴。
- English: Corrected an over-confident claim about `48001`. The docs previously stated that unverified personal accounts get `48001` from `draft/add`; another tested report shows all four steps (token, `uploadimg`, `add_material`, `draft/add`) working on an unverified personal account, with only `freepublish/submit` needing business verification. The two conflict, so the skill no longer assumes either: run `doctor`, then `push --dry-run`, and fall back to pasting only if `48001` actually appears.

### 新增 wechat-mp-publish

- 中文：新增 `wechat-mp-publish`，把「Markdown → 公众号」这条链路补全。核心解决图片丢失：微信只渲染 `mmbiz.qpic.cn` 上的图，外链与第三方图床会被过滤且有 Referer 防盗链，所以推送前必须把每张正文图走 `media/uploadimg` 换成微信图床地址。
- English: Added `wechat-mp-publish`, closing the Markdown-to-WeChat pipeline. The core fix is images: WeChat only renders images hosted on `mmbiz.qpic.cn`, while external links and third-party image hosts get filtered and hit Referer hotlink protection. Every body image must go through `media/uploadimg` before publishing.
- 中文：四个子命令：`convert`（Markdown 转全内联样式 HTML，可粘贴）、`check`（过滤规则合规检查）、`push`（传图 + 传封面 + 写草稿箱）、`doctor`（凭据与连通性自检）。只依赖 Python 标准库。
- English: Four subcommands: `convert` (Markdown to all-inline HTML, paste-ready), `check` (filter-rule compliance), `push` (upload images, upload cover, write draft), `doctor` (credential and connectivity check). Standard library only.
- 中文：渲染器按微信的脾气来：整段加粗自动变金句块，代码块用 `section` + `br` 而非 `pre`，mermaid 直接报错拦住，表格超过 3 列给提示。内置青竹、墨黑、经典蓝三套主题，改 `assets/themes.json` 即可扩展。
- English: The renderer follows WeChat's rules: an all-bold paragraph becomes a pull-quote, code blocks use `section` plus `br` instead of `pre`, mermaid blocks fail fast, and tables wider than 3 columns trigger a warning. Three themes ship in `assets/themes.json`; adding one needs no code change.
- 中文：明确不做发布。2025 年 7 月起 `freepublish/submit` 对个人主体与未认证企业号已回收，草稿箱接口也需认证账号（未认证返回 48001），所以工具止步于草稿箱，发布由人点。错误码 40164 / 40007 / 48001 / 40008 / 45004 均给中文处置建议。
- English: Publishing is deliberately out of scope. Since July 2025 `freepublish/submit` is closed to personal and unverified business accounts, and the draft API itself needs a verified account (`48001` otherwise), so the tool stops at the draft box and a human clicks publish. Error codes 40164, 40007, 48001, 40008 and 45004 all map to plain-language fixes.
- 中文：归入「文档与交付」类，该类由 3 增至 4，说明改为「转换要保真，演示要能看懂，发布要落到位」。公开层 15 → 16 个，原创 14 → 15 个。
- English: Filed under Documents and Delivery, which grew from 3 to 4 and now reads "conversions keep fidelity, decks read clearly, publishing lands intact". Public layer 15 → 16, original skills 14 → 15.

### 新增 slides-workflow

- 中文：新增 `slides-workflow`，把一套用 AI 做 PPT 的方法论落成可复用 Skill：四阶段流程（采集与逐页稿 → 风格说明 → 选形态制作 → 局部打磨），前两阶段设硬闸；三形态（HTML Slides / 整页图片 / 可编辑 PPTX）各有硬约束、制作提示词与验收清单；含图片稿还原方法、九个已知失败模式、两个零依赖校验脚本。
- English: Added `slides-workflow`, turning an AI deck-production methodology into a reusable skill: a four-stage flow (gather and page script, style spec, choose format and build, targeted polish) with hard gates after the first two stages; three formats (HTML Slides, image pages, editable PPTX) each with constraints, a build prompt and an acceptance checklist; plus the image-to-PPTX reconstruction method, nine known failure modes and two zero-dependency verification scripts.
- 中文：归入「文档与交付」类，该类数量由 2 增至 3，说明同步改为「转换要保真，演示要能被看懂」。公开层 14 → 15 个，原创 13 → 14 个。
- English: Filed under Documents and Delivery, which grew from 2 to 3 skills; its description now reads "conversions keep fidelity, decks have to be understood". Public layer 14 → 15, original skills 13 → 14.
- 中文：`verify.py script` 输出 `RESULT: PASS` 才算通过，会逐条报出页码缺失、字段名拼错、必填字段为空、图片引用不存在；`verify.py assets` 额外检查未引用文件与序号连续性。
- English: `verify.py script` prints `RESULT: PASS` only when clean, reporting missing page numbers, misspelled field names, empty required fields and unresolved image references; `verify.py assets` additionally checks unreferenced files and numbering continuity.

### README 分类重构

- 中文：两份根 README 由 14 个 Skill 平铺改为按四类分组：网页与前端（4）、文档与交付（2）、工程流程与质量（5）、写作与表达（3）。分类口径是「用在哪一步」，一个 Skill 只归一类。
- English: Both root READMEs switched from a flat list of 14 skills to four groups: Web and Frontend (4), Documents and Delivery (2), Engineering Workflow and Quality (5) and Writing and Expression (3). The criterion is where the skill sits in the work; each skill belongs to exactly one group.
- 中文：新增「分类」章节，用一张表说明每类管什么、含几个 Skill，并带锚点直达该类清单；目录表拆成四张分组表；Skills 章节按同样分组，每个 Skill 折叠成一行摘要，点开才展开详情。
- English: Added a Categories section with a table explaining what each group covers and how many skills it holds, linking straight to the matching list. The catalog is now four grouped tables, and the Skills section follows the same grouping with each skill collapsed to a one-line summary.
- 中文：兼容性表按分类顺序重排；仓库结构图加上分类分隔注释，并说明目录保持扁平、分类只体现在 README 里，以免 `tree/main/<skill-name>` 直链和安装命令失效。
- English: The compatibility table was reordered to match the groups. The repository layout diagram gained category divider comments and a note that the directory layout stays flat, so `tree/main/<skill-name>` links and install commands keep working.

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
