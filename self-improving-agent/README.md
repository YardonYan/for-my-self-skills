# self-improving-agent — 把踩过的坑变成不会再踩的规则

> 每次纠正、报错、知识缺口都写进 `.learnings/`；反复出现的模式提升成项目规则或新 Skill。

## 解决什么

AI 每开一个新会话就失忆一次。同一个坑，今天踩完明天还踩，因为教训只留在这次对话里，没落到任何会被下次读到的位置。

这个 Skill 把「记录」变成一个有格式、可检索、有闭环的动作，而不是让模型随口说一句「以后注意」：

- 三个产物文件，各管一类：`LEARNINGS.md`（经验与纠正）、`ERRORS.md`（命令与外部接口报错）、`FEATURE_REQUESTS.md`（缺失功能）
- 每条带 `TYPE-YYYYMMDD-XXX` 形式的 ID、优先级、状态、领域标签，同类问题用 `See Also` 互相关联
- 达到提升阈值（复发 ≥3 次、跨 2 个任务、30 天窗口内）时，把冗长经验压缩成一句预防式规则，写进 `AGENTS.md` 或 `CLAUDE.md`
- 值得独立复用的，抽取成新的 Skill，原条目标记 `promoted_to_skill`

## 什么时候用

```
把这次的踩坑沉淀到 .learnings/。
回顾一下 .learnings/，把反复出现的经验提升成规则。
这个方案挺好，提取成 skill。
```

也会在用户说「怎么又出问题了」「我之前说过」时自动触发。

## 快速对照

| 情境 | 动作 |
|---|---|
| 用户纠正了你 | `LEARNINGS.md`，分类 `correction` |
| 命令 / 构建 / API 调用失败 | `ERRORS.md`，附报错原文与复现步骤 |
| 依据的知识已过时 | `LEARNINGS.md`，分类 `knowledge_gap` |
| 用户提出缺失功能 | `FEATURE_REQUESTS.md` |
| 发现了更好的做法 | `LEARNINGS.md`，分类 `best_practice` |
| 与已有条目相似 | 加 `See Also` 关联，并提升优先级 |

## 提升去哪

| 目标文件 | 放什么 | 适用平台 |
|---|---|---|
| `AGENTS.md` | Agent 工作流、工具使用模式、自动化规则 | 通吃 |
| `CLAUDE.md` | 项目事实、约定与注意事项 | Claude Code |
| `.github/copilot-instructions.md` | 项目上下文与约定 | GitHub Copilot |
| `TOOLS.md` | 本机工具、环境、凭据位置 | 通用 |
| `.workbuddy/memory/MEMORY.md` | 项目级长期记忆 | WorkBuddy / CodeBuddy |

## 内含

- 三个文件的完整 Markdown 模板与字段取值表
- ID 生成规则、状态流转、处理闭环
- 重复模式检测（`grep` 查重 + `See Also`）
- 提升阈值与提升步骤
- 从经验抽取新 Skill 的判定标准、流程与质量门槛
- 多平台接入方式（WorkBuddy / CodeBuddy / Claude Code / Codex CLI / GitHub Copilot），含可选的 Hook 脚本模板

## 边界

只管「记录、提升、抽取」这一条链路。正在进行的故障修复走 `self-healing`（若已安装），本 Skill 不承担。纯一次性笔误、无需跨会话记忆的琐事不记。

## 安装

```bash
git clone https://github.com/YardonYan/for-my-self-skills.git
cp -r for-my-self-skills/self-improving-agent <your-agent-skills-dir>/
```

首次使用时在项目根目录建 `.learnings/` 目录，按模板建三个文件即可。

## 许可

Apache-2.0，见 [LICENSE](./LICENSE)。
