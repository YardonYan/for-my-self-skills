<div align="center">

**中文** · [English](./README.en.md)

# Yardon Skills

#### 7 个在真实项目里用过、整理出来的 Agent Skills

[![Skills](https://img.shields.io/badge/Skills-7-10B981?style=flat-square)](#目录)
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
└── html-designer__skillhub/
```

每个目录都以 `SKILL.md` 为入口；`references/` 是按需读取的细节，不会一次性塞进上下文。

## 隐私边界

这个公开仓只有 7 个可公开的 Skill。个人上下文、私有 Skill、公司资料不在公开仓。示例里的姓名、邮箱、电话、公司名和数据都是虚构或占位；如果你在 Skill 里看到真实信息，请提 Issue。

## License

仓库根目录的 [LICENSE](./LICENSE) 是 Apache-2.0；[NOTICE](./NOTICE) 说明第三方例外。

6 个原创 Skill 使用 Apache-2.0：html-skill-effectiveness、markdown-renderer-fix、mobile-design-spec、task-skill-orchestrator、tech-blog-generator、yardon-writer。每个目录内附 `LICENSE`。

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

6 个原创 Skill 使用 Apache-2.0；`html-designer__skillhub` 为第三方 Skill，许可见其目录与原始来源。

Made by [@YardonYan](https://github.com/YardonYan)

</div>
