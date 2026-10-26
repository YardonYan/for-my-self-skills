<div align="center">

**中文** · [English](./README.en.md)

# Yardon Skills

#### 14 个在真实项目里用过、整理出来的 Agent Skills

[![Skills](https://img.shields.io/badge/Skills-14-10B981?style=flat-square)](#目录)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Standard-8B5CF6?style=flat-square)](#兼容性)
[![License](https://img.shields.io/badge/License-Apache--2.0-D97706?style=flat-square)](#license)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-D97706?style=flat-square&logo=anthropic&logoColor=white)](#兼容性)
[![Codex](https://img.shields.io/badge/Codex-compatible-10B981?style=flat-square&logo=openai&logoColor=white)](#兼容性)
[![Qoder](https://img.shields.io/badge/Qoder-compatible-3B82F6?style=flat-square)](#兼容性)

</div>

这些 Skill 都按 [Agent Skills](https://agentskills.io) 开放标准组织。Claude Code、Codex、Qoder、Cursor、CodeBuddy 等支持该标准的工具可以直接加载。每个目录都有 `SKILL.md`，先读它，再按需读 `references/`。

不是提示词合集，也不是把所有能力塞进一个巨型 prompt。每个 Skill 只解决一类问题，触发条件、产出形态和边界都写在 `SKILL.md` 里。装上之后，Agent 在该用的时候会自己读。

## 目录

| Skill | 一句话 | 标签 | 文档 |
|---|---|---|---|
| [html-skill-effectiveness](./html-skill-effectiveness/) | 生成单文件 HTML 工件：报告、看板、对比、幻灯片、交互解释器 | `html` `single-file` `dashboard` `report` | [中文](./html-skill-effectiveness/README.md) · [EN](./html-skill-effectiveness/README.en.md) |
| [markdown-renderer-fix](./markdown-renderer-fix/) | 修复 Markdown 渲染、SSE 中文乱码、代码高亮、Mermaid、KaTeX | `markdown` `sse` `encoding` `frontend` | [中文](./markdown-renderer-fix/README.md) · [EN](./markdown-renderer-fix/README.en.md) |
| [mobile-design-spec](./mobile-design-spec/) | iOS、Android、HarmonyOS、小程序、H5 五套移动端尺寸规范 | `mobile` `ios` `android` `harmonyos` | [中文](./mobile-design-spec/README.md) · [EN](./mobile-design-spec/README.en.md) |
| [task-skill-orchestrator](./task-skill-orchestrator/) | 把复杂任务拆成依赖 DAG，分波次并行给多个 Sub Agent | `orchestration` `dag` `multi-agent` | [中文](./task-skill-orchestrator/README.md) · [EN](./task-skill-orchestrator/README.en.md) |
| [tech-blog-generator](./tech-blog-generator/) | 从代码或文档生成技术博客、教程和技术说明 | `technical-writing` `blog` `documentation` | [中文](./tech-blog-generator/README.md) · [EN](./tech-blog-generator/README.en.md) |
| [yardon-writer](./yardon-writer/) | 中文长文写作风格，技术文与叙事文双模式 | `writing` `chinese` `longform` | [中文](./yardon-writer/README.md) · [EN](./yardon-writer/README.en.md) |
| [code-review](./code-review/) | AI 生成代码的七维审查清单：只出问题清单，不动手修 | `code-review` `ai-code` `code-audit` | [中文](./code-review/README.md) · [EN](./code-review/README.en.md) |
| [self-improving-agent](./self-improving-agent/) | 把纠正、报错与知识缺口沉淀成项目规则或新 Skill | `learnings` `memory` `retrospective` | [中文](./self-improving-agent/README.md) · [EN](./self-improving-agent/README.en.md) |
| [md-to-docx](./md-to-docx/) | Markdown 无损转 Word，逐元素保真，附零缺失校验脚本 | `markdown` `docx` `python-docx` | [中文](./md-to-docx/README.md) · [EN](./md-to-docx/README.en.md) |
| [html-to-pdf](./html-to-pdf/) | 打印优化 HTML + Chrome 无头转 PDF，中文不乱码 | `pdf` `headless-chrome` `print` | [中文](./html-to-pdf/README.md) · [EN](./html-to-pdf/README.en.md) |
| [prompt-optimizer](./prompt-optimizer/) | 一份草稿 prompt 出四种策略版本，对比挑一个 | `prompt-engineering` `llm` `rewrite` | [中文](./prompt-optimizer/README.md) · [EN](./prompt-optimizer/README.en.md) |
| [dev-workflow](./dev-workflow/) | 开发五步法，每步有手册，附各语言审查指南包 | `dev-workflow` `code-review` `sdlc` | [中文](./dev-workflow/README.md) · [EN](./dev-workflow/README.en.md) |
| [merge-dev-docs](./merge-dev-docs/) | 两套开发文档合并：裁决冲突而不是摘要融合 | `documentation` `conflict-matrix` `adr` | [中文](./merge-dev-docs/README.md) · [EN](./merge-dev-docs/README.en.md) |
| [html-designer__skillhub](./html-designer__skillhub/) | 网页视觉设计：排版、配色、层级、栅格、可访问性 | `web-design` `html` `css` `landing-page` | [中文](./html-designer__skillhub/README.md) · [EN](./html-designer__skillhub/README.en.md) |

## 安装

### 让 Agent 自己装

在支持 Agent Skills 的工具里直接说：

```
帮我安装这个 skill：https://github.com/YardonYan/for-my-self-skills/tree/main/<skill-name>
```

把 `<skill-name>` 换成目录表里的任意一个，例如：

```
帮我安装这个 skill：https://github.com/YardonYan/for-my-self-skills/tree/main/tech-blog-generator
```

### 手动安装

```bash
git clone https://github.com/YardonYan/for-my-self-skills.git
cp -r for-my-self-skills/<skill-name> <your-agent-skills-dir>/
```

不同工具的 skills 目录不同。Claude Code 常见为 `~/.claude/skills/`，其他工具看官方文档。关键是让 `<skill-name>/SKILL.md` 位于技能目录的根部。

### 不支持 Skill 加载

打开 `<skill-name>/SKILL.md`，把全文贴进项目规则、系统提示词或对话开头。规则会生效，但不会像 Skill 那样按触发条件自动加载。

## Skills

### html-skill-effectiveness

**一句话**：把人们略读的 Markdown，变成人们真正会读的单文件 HTML。

**解决什么**：Markdown 是线性的，表达不了并排对比、可缩放架构图、带备注的幻灯片、实时仪表盘。这个 Skill 让 Agent 输出一个自包含 HTML 文件，内联 CSS/JS，零外部依赖，浏览器直接打开。

**什么时候用**：要一份报告、方案对比、数据看板、演示页、交互解释器，并且希望交付物只有一个文件、可以直接发人。

**内含**：13 种页面模式、五维评审标准、DevLoop 迭代流程、7 条工艺规则（反 AI 味、颜色、字体、层级、动效、可访问性、UX 法则），以及状态覆盖和表单校验契约。

**示例触发**：

```
帮我把这周的数据做成一份单文件 HTML 看板。
把这几个方案整理成并排对比页，能直接发同事。
把这份技术说明做成带演讲者备注的幻灯片。
```

**边界**：不做鉴权、支付、后端逻辑和实时数据库。遇到这些场景会拒绝并说明原因。

**标签**：`html` `single-file` `report` `dashboard` `presentation` `interactive` `frontend`

文档：[中文](./html-skill-effectiveness/README.md) · [English](./html-skill-effectiveness/README.en.md)

### markdown-renderer-fix

**一句话**：从数据流根因修复中文乱码、Markdown 渲染异常和流式输出问题。

**解决什么**：中文乱码看起来只是编码问题，实际会经过后端解码、JSON 转义、HTTP 传输、前端 TextDecoder、Markdown 解析等多个阶段。只改一处常常治不好。这个 Skill 按阶段排查，并给出前后端成对的生产级解法。

**什么时候用**：SSE 流式输出出现“锟斤拷”、Markdown 表格/代码块/Mermaid/KaTeX 渲染异常、工具调用输出需要过滤、中文在前端显示不正常。

**内含**：8 阶段数据流排查、前后端编码模板、代码高亮/Mermaid/KaTeX 修复、工具调用过滤、v3.0.0 实战案例。

**示例触发**：

```
SSE 流式输出的中文变成了锟斤拷，帮我从根因排查。
Markdown 里的 Mermaid 不显示，代码块也没有高亮。
流式输出把工具调用的 JSON 也显示出来了，帮我过滤掉。
```

**标签**：`markdown` `sse` `streaming` `encoding` `chinese` `mermaid` `katex` `frontend`

文档：[中文](./markdown-renderer-fix/README.md) · [English](./markdown-renderer-fix/README.en.md)

### mobile-design-spec

**一句话**：把五套移动端尺寸规范落到代码，并说得出每条改动的依据。

**解决什么**：移动端代码里大量“看着差不多”的数值：触控热区不够、内容贴边、底部按钮被手势区挡住、字号太小、单位用错平台。这个 Skill 把 iOS、Android、HarmonyOS、微信小程序、H5 的规则集中到一处，覆盖平板、折叠屏、车机和大屏。

**什么时候用**：写或改移动端/响应式页面，查机型尺寸和安全区，做多端设计稿标注，换算 pt/dp/sp/vp/fp/lpx/rpx/px/rem/vw/dvh，检查可点区域和字号下限。

**内含**：五套平台规范、机型参数与安全区、单位换算、折叠屏多态布局、WCAG 2.2 校验、零依赖换算/检查脚本。规则数值取自 Apple HIG、Material Design 3、HarmonyOS Design、微信小程序文档、MDN 和 WCAG，数据基准 2026-10。

**示例触发**：

```
这个移动端页面底部按钮被手势区挡住了，按 iOS/Android 规范改。
帮我把这张设计稿标成 iOS、Android、鸿蒙、小程序、H5 五套尺寸。
检查这个页面的触控热区和字号是否达标。
```

**依赖**：核心规则只读 `SKILL.md` 即可；附带脚本需要 Node.js >= 18。

**标签**：`mobile` `ios` `android` `harmonyos` `wechat-miniprogram` `responsive` `safe-area` `accessibility` `wcag`

文档：[中文](./mobile-design-spec/README.md) · [English](./mobile-design-spec/README.en.md)

### task-skill-orchestrator

**一句话**：把复杂需求拆成依赖感知的 DAG，分波次并行派发给多个 Sub Agent。

**解决什么**：面对“同时调研三家公司并汇总成一份报告”这类任务，默认做法是串行：A 做完做 B，B 做完做 C。这个 Skill 先拆子任务和依赖，能并行的分到同一波，最后统一汇总，减少等待和上下文来回。

**什么时候用**：一个请求自然拆成多个独立子目标、需要多线并进、批量处理、复杂任务编排。

**内含**：DAG 拆解、波次调度、Sub Agent 角色分工、结果汇总、失败重试与并发控制。

**平台要求**：为 OpenClaw 的 `sessions_spawn` Sub Agent 机制设计，需要可用的 `file-agent`、`search-agent`、`browser`、`app-agent`、`computer-agent`。其他平台需要自行替换派发层。

**示例触发**：

```
同时调研这三家公司，最后汇总成一份对比报告。
把这个大任务拆一下，能并行的并行，最后统一交付。
批量处理这些文件，每 5 个一波，失败的单独重试。
```

**标签**：`orchestration` `dag` `multi-agent` `parallel` `subagents` `task-planning`

文档：[中文](./task-skill-orchestrator/README.md) · [English](./task-skill-orchestrator/README.en.md)

### tech-blog-generator

**一句话**：把代码和文档变成读得下去的技术博客，而不是术语堆砌。

**解决什么**：技术写作最容易写成“代码复述”或“正确但没信息量”的套话。这个 Skill 按资深工程师的写作过程走：先分析代码架构，再选文体，动笔时执行 21 条反空话规则，最后做 3 遍自审。

**什么时候用**：上传代码文件或技术文档，要求写博客、写教程、解释代码、生成文档；中英文技术写作都可以。

**内含**：21 条写作规则、6 种文体、3 遍自审、中英双语模板。只管技术写作，不做营销文案、UI 文案和闲聊。

**示例触发**：

```
把这份 Python 项目代码写成一篇技术博客。
根据这份设计文档写一篇教程，面向刚接触这个框架的读者。
把这几个模块的实现讲清楚，写成一篇有代码、有取舍的文章。
```

**标签**：`technical-writing` `blog` `tutorial` `documentation` `bilingual` `chinese`

文档：[中文](./tech-blog-generator/README.md) · [English](./tech-blog-generator/README.en.md)

### yardon-writer

**一句话**：中文长文写作风格，技术文讲清楚，叙事文让人读下去。

**解决什么**：技术文容易写成说明书，叙事文容易写成流水账，两种文体混着写就两头不靠。这个 Skill 先裁决文体，再按对应的结构、节奏和禁用词规则写，最后过阅读体验自检。

**什么时候用**：公众号文章、技术博客、CSDN 长文、项目复盘、经验总结、职场观察；也适合把一个 PDF、新闻链接、语音转文字或零散想法写成文章。

**两种模式**：A 技术长文保留分节、表格、代码和本章小结；B 叙事长文弱化小标题，用转场句推进，第一人称经历和观点为核心。

**边界**：不写朋友圈、推特、小红书短帖；不编造经历、数据、金额和对话；涉及公司业务默认脱敏。

**示例触发**：

```
把这段素材写成一篇公众号长文，按我的风格。
这篇项目复盘帮我重写，不要写成流水账。
把这个 PDF 里的内容整理成一篇技术长文。
这篇文章读起来太像 AI 写的，按 yardon-writer 的规则改一遍。
```

**标签**：`writing` `chinese` `longform` `technical-writing` `narrative` `style`

文档：[中文](./yardon-writer/README.md) · [English](./yardon-writer/README.en.md)

### code-review

**一句话**：审计与修复分离，review 只出问题清单，不动手改。

**解决什么**：AI 写的代码有几类病从外观上看不出来——调用不存在的 API（幻觉签名）、`except: pass` 吞错误悄悄给默认值（表面正常数据已错）、20 行需求搭三层抽象、项目里已有轮子又造一个。这个 Skill 用七维清单逐条扫，每条问题必须带定位行号、根因、影响面和修复方向，证据不足的只标「待验证」。

**什么时候用**：用 AI 写代码要把关、接手别人（或 AI）的代码做体检、交付前想多一道质检。

**内含**：七维检查清单（正确性 / 幻觉与静默降级 / 性能与资源 / 冗余与一致性 / 安全 / 过度工程 / 可验证性）、严重度排序铁律、证伪流程、能力边界表、故障剧本与交付前自检清单。

**边界**：只读审查。顺手修复、顺手重构都算越界；性能调优只报方向不代跑；渗透测试级安全审计不做。

**示例触发**：

```
用 code-review 审查这段代码，只出问题清单不要改。
交付前用 code-review 做一次七维自检。
这段代码是 AI 生成的，重点扫幻觉 API 和静默降级。
```

**标签**：`code-review` `ai-code` `code-audit` `read-only` `quality-gate`

文档：[中文](./code-review/README.md) · [English](./code-review/README.en.md)

### self-improving-agent

**一句话**：每次纠正、报错、知识缺口都写进 `.learnings/`，反复出现的模式提升成规则。

**解决什么**：AI 每开一个新会话就失忆一次，同一个坑今天踩完明天还踩，因为教训只留在这次对话里。这个 Skill 把「记录」变成有格式、可检索、有闭环的动作：三个账本文件分管经验、报错与缺失功能，每条带 ID、优先级、状态与领域标签，同类问题用 `See Also` 关联，复发达阈值时压缩成一句预防式规则写进项目规则文件。

**什么时候用**：被用户纠正、命令报错、发现知识过时、用户提出缺失功能、要求复盘沉淀，或想把一套做法提取成新 Skill。

**内含**：三个账本的完整模板与字段取值表、ID 生成规则、状态流转与处理闭环、重复模式检测、提升阈值、从经验抽取 Skill 的判定与质量门槛、多平台接入方式（含可选 Hook 脚本）。

**边界**：只管记录、提升、抽取这条链路。正在进行的故障修复走 `self-healing`；纯一次性笔误不记。

**示例触发**：

```
把这次的踩坑沉淀到 .learnings/。
回顾一下 .learnings/，把反复出现的经验提升成规则。
这个方案挺好，提取成 skill。
```

**标签**：`learnings` `memory` `retrospective` `self-improving` `knowledge-base`

文档：[中文](./self-improving-agent/README.md) · [English](./self-improving-agent/README.en.md)

### md-to-docx

**一句话**：按 Markdown 逐元素映射到 Word，转完还要跑零缺失校验，`RESULT: PASS` 才算完成。

**解决什么**：pandoc 要另装、中文样式不跟手；在线转换站不能传公司文档；手动粘贴进 Word 格式全掉、表格错行。这个 Skill 用 `python-docx` 直接按结构映射，然后用脚本逐字校验：Markdown 里每一条内容行都要能在 docx 里找到，标题、表格、代码块数量也要一致。

**什么时候用**：Markdown 文档要落成 Word 归档或提交——周报、标准档案、使用说明、方案。

**内含**：完整元素映射表（标题 / 表格 / 代码块 / 引用 / 列表 / 水平线 / 行内格式）、六级标题与表格底纹实现、七个已踩过的坑（斜体正则误判尺寸、表格分隔行误判水平线、A4 与 Letter、中文字体 eastAsia、有序列表编号续接、代码块框线字符对齐）、转换与校验两个参数化脚本。

**依赖**：`pip install python-docx`，仅此一个第三方包。

**边界**：Markdown 图片暂不嵌入，需要时自行补图片段落逻辑。

**示例触发**：

```
把这份 md 转成 word，我要无损的。
这份周报落成 docx 归档。
这份说明书给业务同事，转成 Word 发过去。
```

**标签**：`markdown` `docx` `word` `python-docx` `document-conversion`

文档：[中文](./md-to-docx/README.md) · [English](./md-to-docx/README.en.md)

### html-to-pdf

**一句话**：CSS 就是排版语言，`@page` 直接控制纸张，中文不乱码、表格不散架。

**解决什么**：weasyprint 在 Windows 要装 GTK；reportlab 中文要手工注册字体、表格排版代码量大；Word 转 PDF 受 Office 版本和本机字体影响。这个 Skill 用 Chrome 无头模式，把三件事做成固定流程：写打印优化的 HTML、图片一律 base64 内嵌、转完核验页数与关键词再渲染成 PNG 目视检查。

**什么时候用**：说明书、使用手册、报告、方案要交成 PDF；交付对象不熟悉 Markdown 渲染。

**内含**：打印 CSS 关键规则、base64 内嵌做法、Chrome 无头命令与 URI 转义、三重核验（页数 / 关键词 / 渲染目检）、六个踩坑（中文路径静默失败、PDF 被占用不报错、源文件必须保留、图内标题重复、Pillow 中文与 emoji、改文案要回查配图），以及同一份源 HTML 同时出 PDF 与网页的做法。

**依赖**：Chrome 或 Edge；`fitz`（PyMuPDF）用于核验。

**标签**：`pdf` `html` `headless-chrome` `print` `document-delivery`

文档：[中文](./html-to-pdf/README.md) · [English](./html-to-pdf/README.en.md)

### prompt-optimizer

**一句话**：一份草稿 prompt 进去，四种策略的成品出来，对比挑一个。

**解决什么**：「AI 没理解我的意思」九成不是模型不行，是 prompt 缺了它需要的东西——受众、输出格式、边界条件、什么叫作完成了。这个 Skill 不做温和润色，而是按四种不同思路各重写一版，让你看到同一需求在不同组织方式下的效果差异。

**什么时候用**：提示词写不清晰、AI 反复理解错、需要确定性输出、或者只是想让指令更有效。

**内含**：四种策略（详细展开 / 角色扮演 / 结构化 / 逆向提炼）、每种策略的优化方向与适用场景、统一输出格式与策略对比表、五条不越界原则。

**边界**：不改变原意、不硬包装已经够好的 prompt；语言跟随输入。

**示例触发**：

```
帮我优化这个 prompt，给我几个版本对比。
AI 没理解我的意思，帮我把这个需求写清楚。
```

**标签**：`prompt-engineering` `prompt` `rewrite` `llm`

文档：[中文](./prompt-optimizer/README.md) · [English](./prompt-optimizer/README.en.md)

### dev-workflow

**一句话**：需求理解 → 方案设计 → 代码实现 → 代码审查 → Bug 修复，每步有自己的作业手册。

**解决什么**：拿到需求直接开写是最常见的失败起点。缺需求理解会做出没人要的东西，缺方案设计会写到一半推翻重来，缺代码审查把问题留到交付。这个 Skill 拆成五步，按用户说的话判断当前在哪一步，再加载对应手册。

**什么时候用**：需求分析、方案与架构设计、开始写代码、代码 review、bug 定位与修复。

**内含**：五个阶段的手册（需求 / 设计 / 实现 / 审查 / 修 bug）、三步自动落盘规则（`docs/` 追加写入带时间标题）、按语言分开的审查指南包（Go / Java / Python / Rust / C / C++ / Qt / TypeScript / React / Vue / CSS），外加架构、安全、性能三份专项指南。

**说明**：审查指南是公开资料的整理归纳（Go 官方指南、Uber Go Style Guide、JetBrains 的 SOLID 讨论、MDN 等），引用链接保留在各篇文末。

**边界**：`dev-workflow` 管流程，审查标准交给 `code-review`，两者可并存。

**示例触发**：

```
帮我分析这个需求，先出需求理解。
按这个方案开始写代码。
这个 bug 帮我定位修复。
```

**标签**：`dev-workflow` `code-review` `sdlc` `requirement` `documentation`

文档：[中文](./dev-workflow/README.md) · [English](./dev-workflow/README.en.md)

### merge-dev-docs

**一句话**：合并的本质是裁决冲突，不是摘要融合。

**解决什么**：把两套开发文档交给模型「融合一下」，产物一定比原文更模糊、更没约束力，而模糊表述等于没有规范。这个 Skill 逐条抽出主张、找出真冲突、给出有依据的裁决，最后写成能照着做的规范。它还专门处理三个必踩的坑：先读 A 再读 B 造成的措辞污染、单套文档内部自相矛盾、新旧设计时态混用。

**什么时候用**：两套开发文档要合一份、架构文档要互相对齐、团队规范要取两家优点。

**内含**：六阶段流程（确认前提 / 清点 / 独立画像 / 抽条目建矩阵 / 裁决 / 硬闸 + 写分册 / 沉淀）、`judgment-rules.md` 裁决判据、六份模板（文档画像、冲突矩阵、ADR、废弃清单、合并后架构文档与开发规范）、`claim-index.cjs` 清点与重叠打分脚本（Node 20+ 零依赖）。

**边界**：不合并代码（用 diff / rebase）；只有一套文档不需要它；两边主题不重叠直接拼目录即可。

**示例触发**：

```
把这两套开发文档合并成一份可执行的规范。
对齐这两份架构文档，冲突的地方给我裁决。
取两家优点，合并成一版团队规范。
```

**标签**：`documentation` `conflict-matrix` `adr` `dev-docs` `merge`

文档：[中文](./merge-dev-docs/README.md) · [English](./merge-dev-docs/README.en.md)

### html-designer__skillhub

**一句话**：把网页设计原则落成可直接打开的 HTML/CSS 页面。

**解决什么**：页面“能用但不好看”，字号、行距、留白、层级没有依据，配色靠感觉，移动端和桌面端各自为政。这个 Skill 用排版、配色、栅格、视觉层级和可访问性规则，把设计意图写成干净的 HTML/CSS。

**什么时候用**：落地页、营销页、作品集、设计系统、配色与字体方案，或把设计稿/设计描述落成 HTML。

**内含**：4 份设计参考（图形设计、术语、UI/UX、网页设计）、5 个可直接打开的 HTML 示例、设计流程与可访问性检查清单。

**说明**：这是从 SkillHub 收集的第三方 Skill，不是 Yardon 原创；目录内保留原始 `SKILL.md`、`references/` 和 `assets/`，来源与版本见 `_skillhub_meta.json`。

**示例触发**：

```
做一个极简的产品落地页，排版、配色和留白要专业。
把这个作品集页面重设计，保持内容不变。
给我一套适合 SaaS 官网的字体和配色方案，并落成 HTML。
```

**标签**：`web-design` `html` `css` `typography` `color` `landing-page` `portfolio` `accessibility`

文档：[中文](./html-designer__skillhub/README.md) · [English](./html-designer__skillhub/README.en.md)

## 兼容性

| Skill | 运行依赖 | 平台说明 |
|---|---|---|
| html-skill-effectiveness | 无外部依赖 | 任何支持 Agent Skills 的工具 |
| markdown-renderer-fix | 无 / 标准库 | 前端与全栈项目都适用 |
| mobile-design-spec | Node.js >= 18（仅脚本） | 只读规则不需要 Node |
| task-skill-orchestrator | OpenClaw `sessions_spawn` + 5 类 Sub Agent | 其他平台需替换派发层 |
| tech-blog-generator | 无 | 任何支持 Agent Skills 的工具 |
| yardon-writer | 无 | 中文长文场景 |
| code-review | 无 | 任何支持 Agent Skills 的工具 |
| self-improving-agent | 无 | 需要项目内可写 `.learnings/` |
| md-to-docx | Python + python-docx | 转换与校验脚本都需要 |
| html-to-pdf | Chrome/Edge + PyMuPDF | 仅核验步骤需要 PyMuPDF |
| prompt-optimizer | 无 | 任何支持 Agent Skills 的工具 |
| dev-workflow | 无 | 可选配合 code-review 使用 |
| merge-dev-docs | Node.js >= 20（仅脚本） | 只读规则与模板不需要 Node |
| html-designer__skillhub | 无 | 第三方 Skill，见目录内来源说明 |

常见工具：Claude Code、Codex、Qoder、Cursor、CodeBuddy，以及任何兼容 Agent Skills 标准的 Agent。具体加载方式以工具文档为准。

## 仓库结构

```
for-my-self-skills/
├── README.md                 中文目录
├── README.en.md              English catalog
├── CHANGELOG.md              每个 Skill 的变更说明
├── html-skill-effectiveness/
│   ├── SKILL.md              主规则（Agent 加载入口）
│   ├── README.md / README.en.md
│   ├── references/
│   └── docs/ assets/ tools/
├── markdown-renderer-fix/
├── mobile-design-spec/
├── task-skill-orchestrator/
├── tech-blog-generator/
├── yardon-writer/
├── code-review/
├── self-improving-agent/
├── md-to-docx/
│   ├── SKILL.md
│   └── scripts/              转换与零缺失校验脚本
├── html-to-pdf/
├── prompt-optimizer/
├── dev-workflow/
│   ├── SKILL.md
│   └── reference/            五阶段手册 + review-kit 审查指南包
├── merge-dev-docs/
│   ├── SKILL.md
│   ├── assets/               六份模板
│   └── scripts/              claim-index.cjs
└── html-designer__skillhub/
```

每个目录都以 `SKILL.md` 为入口；`references/` 是按需读取的细节，不会一次性塞进上下文。

## 隐私边界

这个公开仓只有 14 个可公开的 Skill。个人上下文、私有 Skill、公司资料不在公开仓。示例里的姓名、邮箱、电话、公司名和数据都是虚构或占位；如果你在 Skill 里看到真实信息，请提 Issue。

## License

仓库根目录的 [LICENSE](./LICENSE) 是 Apache-2.0；[NOTICE](./NOTICE) 说明第三方例外。

13 个原创 Skill 使用 Apache-2.0：html-skill-effectiveness、markdown-renderer-fix、mobile-design-spec、task-skill-orchestrator、tech-blog-generator、yardon-writer、code-review、self-improving-agent、md-to-docx、html-to-pdf、prompt-optimizer、dev-workflow、merge-dev-docs。每个目录内附 `LICENSE`。

`html-designer__skillhub` 是从 SkillHub 收集的第三方 Skill，目录内没有独立 LICENSE 文件；复用或再分发前请核对原始来源与许可。

## Contributing

Issue 和 PR 都欢迎。为了让每个 Skill 的变更可追溯，约定：

- 一个 PR 尽量只改一个 Skill
- 提交信息用 `docs(<skill>): ...`、`feat(<skill>): ...`、`fix(<skill>): ...`
- 不把个人经历、公司名、客户信息、服务器地址写进公开 Skill
- 新增示例数据用虚构值，并说明是示例

## Changelog

每个 Skill 的变更记录见 [CHANGELOG.md](./CHANGELOG.md)。

---

<div align="center">

[Apache-2.0 License](./LICENSE) · 自由使用 / 修改 / 再分发（保留版权与许可声明）

13 个原创 Skill 使用 Apache-2.0；`html-designer__skillhub` 为第三方 Skill，许可见其目录与原始来源。

Made by [@YardonYan](https://github.com/YardonYan)

</div>
