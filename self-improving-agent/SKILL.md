---
name: self-improving-agent
description: 自我改进与经验沉淀工作流。当用户纠正回答、命令或操作报错、发现知识过时、提出缺失功能，或要求记下来、沉淀经验、复盘、归档错误、把这次的方案提取成 skill 时使用；也用于周期性回顾 .learnings/ 目录，以及把反复出现的模式提升为项目规则（AGENTS.md、CLAUDE.md、.github/copilot-instructions.md、WorkBuddy 记忆文件）或抽取成新的可复用 skill。触发词包括 self-improving、learnings、corrections、error log、feature request、recurring pattern、promote to AGENTS.md、extract skill、复盘、沉淀、经验库、踩坑记录。
version: "1.0.0"
agent_created: true
summary: "自我改进 Agent 快速参考，按情境对照行动"
---

# Self-Improving Agent（自我改进与经验沉淀）

把每次纠正、报错、知识缺口沉淀到项目本地的 `.learnings/` 目录，让下一次会话不必重新踩坑；当某类问题反复出现时，把它提升为项目级规则或抽取成独立 skill。

核心产物是三个文件：`.learnings/LEARNINGS.md`（经验与纠正）、`.learnings/ERRORS.md`（命令与外部接口报错）、`.learnings/FEATURE_REQUESTS.md`（缺失功能）。

## 何时使用

出现下列任一情况时，先按本技能记录，再继续原任务：

- 用户纠正了刚才的回答或做法
- 命令、脚本、构建、测试执行失败
- 外部 API、MCP 工具、第三方服务调用失败
- 依据的知识（库版本、接口签名、内部约定）已过时
- 用户提出当前缺失的功能
- 调试过程不顺利，解决方案非显而易见
- 用户明确要求沉淀、复盘、归档、提取 skill

### 何时不用

- 正在主动修复一个进行中的失败：改用 `self-healing` 技能（若已安装），其条目以 `HEAL-` 前缀记入 `.learnings/HEALS.md`
- 纯一次性笔误、无需跨会话记忆的琐碎问题
- 已在 `.learnings/` 中有等价条目：补一条 `See Also` 链接并提升优先级，而不是重复新建

## 快速对照表

| 情境 | 动作 |
|------|------|
| 任务中途的活跃故障，需要立刻修 | 改用 `self-healing`（若已安装），条目前缀 `HEAL-`，写入 `.learnings/HEALS.md` |
| 过去发生的命令或操作失败（非正在修复） | 记入 `.learnings/ERRORS.md` |
| 用户纠正了你 | 记入 `.learnings/LEARNINGS.md`，分类 `correction` |
| 用户提出缺失功能 | 记入 `.learnings/FEATURE_REQUESTS.md` |
| API 或外部工具失败 | 记入 `.learnings/ERRORS.md`，附集成细节 |
| 知识过时 | 记入 `.learnings/LEARNINGS.md`，分类 `knowledge_gap` |
| 发现了更好的做法 | 记入 `.learnings/LEARNINGS.md`，分类 `best_practice` |
| 与已有条目相似 | 用 `**See Also**` 关联，并考虑提升优先级 |
| 经验具有普适性 | 提升到 `AGENTS.md` 或 `CLAUDE.md`（按所用 Agent 平台选择） |
| 反复出现的模式达到提升阈值 | 把提炼后的规则提升到项目规则文件或新建 skill |

## 初始化

在项目根目录创建 `.learnings/`（若不存在）：

```bash
mkdir -p .learnings
```

首次使用时按下面三个模板创建文件；文件已存在则直接追加条目。

### LEARNINGS.md 模板

```markdown
# Learnings

## [LRN-20250115-001] correction

**Logged**: 2025-01-15T10:00:00Z
**Priority**: high
**Status**: pending
**Area**: backend

### Summary
一句话说明学到了什么或纠正了什么。

### Details
当时的上下文、错误做法与正确做法。

### Suggested Action
下次遇到同类情况具体怎么做。

### Metadata
- **Source**: conversation
- **Category**: correction
- **Related Files**: path/to/file.ts
- **See Also**: LRN-20250110-001
```

### ERRORS.md 模板

```markdown
# Errors

## [ERR-20250115-A3F] build

**Logged**: 2025-01-15T10:00:00Z
**Priority**: high
**Status**: pending
**Area**: infra

### Summary
命令或调用失败的一句话描述。

### Error
原始报错信息（原文照抄关键行）。

### Context
- **Command**: `pnpm build`
- **Integration**: 外部服务名与接口（如适用）
- **Reproduction**: 稳定复现步骤

### Suggested Fix
具体修复动作，不要只写"排查一下"。

### Metadata
- **Source**: runtime
- **Related Files**: package.json
- **See Also**: ERR-20250110-001
```

### FEATURE_REQUESTS.md 模板

```markdown
# Feature Requests

## [FEAT-20250115-002] workflow

**Logged**: 2025-01-15T10:00:00Z
**Priority**: medium
**Status**: pending
**Area**: docs

### Summary
用户希望拥有但当前缺失的能力。

### User Request
用户原话。

### Suggested Implementation
可行的实现方向。

### Metadata
- **Source**: user
- **Related Files**:
- **See Also**:
```

## ID 生成规则

格式：`TYPE-YYYYMMDD-XXX`

- TYPE 取 `LRN`（经验）、`ERR`（错误）、`FEAT`（功能请求）
- YYYYMMDD 取当前日期
- XXX 取当日流水号或三位随机字符，如 `001`、`A7B`

示例：`LRN-20250115-001`、`ERR-20250115-A3F`、`FEAT-20250115-002`

## 字段取值

### 状态（Status）

| 取值 | 含义 |
|------|------|
| `pending` | 待处理 |
| `in_progress` | 正在处理 |
| `resolved` | 已解决 |
| `wont_fix` | 决定不处理（在 Resolution 里写明原因） |
| `promoted` | 已提升到项目规则文件 |
| `promoted_to_skill` | 已抽取为独立 skill |

### 优先级（Priority）

| 取值 | 适用情形 |
|------|----------|
| `critical` | 阻断核心功能、有数据丢失或安全风险 |
| `high` | 影响明显、涉及常用流程、反复出现 |
| `medium` | 影响中等，存在绕行方案 |
| `low` | 轻微不便、边缘场景、锦上添花 |

### 领域标签（Area）

| 标签 | 范围 |
|------|------|
| `frontend` | 界面、组件、客户端代码 |
| `backend` | 接口、服务、服务端代码 |
| `infra` | 持续集成、部署、容器、云 |
| `tests` | 测试文件、测试工具、覆盖率 |
| `docs` | 文档、注释、说明文件 |
| `config` | 配置文件、环境变量、设置项 |

### 分类（Category，仅 LEARNINGS）

`correction`（用户纠正）、`knowledge_gap`（知识过时）、`best_practice`（更优做法）。

## 处理闭环

问题解决后更新原条目，不要另开新条目：

1. 把 `**Status**: pending` 改为 `**Status**: resolved`
2. 在 Metadata 前插入解决信息块

```markdown
- **Resolved**: 2025-01-16T09:00:00Z
- **Commit/PR**: abc123 或 #42
- **Notes**: 简述实际做了什么
```

## 提升到项目记忆

当一条经验具有普适性（不是一次性修补）时，提升为项目永久记忆。

### 何时提升

- 经验适用于多个文件或功能模块
- 任何协作者（人或 AI）都应当知道
- 能防止同类错误重演
- 记录了项目特有的约定

### 提升目标

| 目标文件 | 适合放入的内容 | 适用平台 |
|----------|----------------|----------|
| `AGENTS.md` | Agent 工作流、工具使用模式、自动化规则 | 全部平台，WorkBuddy / CodeBuddy 首选 |
| `CLAUDE.md` | 面向 Claude 的项目事实、约定与注意事项 | Claude Code |
| `.github/copilot-instructions.md` | 面向 GitHub Copilot 的项目上下文与约定 | GitHub Copilot |
| `TOOLS.md` | 本机工具、环境、凭据位置等 | WorkBuddy / CodeBuddy |
| `.workbuddy/memory/MEMORY.md` | 项目级长期记忆与沉淀结论 | WorkBuddy / CodeBuddy |
| `.workbuddy/memory/YYYY-MM-DD.md` | 当日工作日志（只追加，不覆盖） | WorkBuddy / CodeBuddy |
| `~/.workbuddy/MEMORY.md` | 跨项目的用户长期偏好与硬性规则 | WorkBuddy / CodeBuddy |

注意：WorkBuddy 与 CodeBuddy 不使用 `CLAUDE.md`，对应位置是 `AGENTS.md` 与记忆文件；`CLAUDE.md` 仅在 Claude Code 环境生效。

### 提升步骤

1. 把冗长经验提炼成一句简洁的规则或事实
2. 写入目标文件的对应小节（文件不存在则创建）
3. 更新原条目：`**Status**: pending` 改为 `promoted`，并加 `**Promoted**: AGENTS.md`

### 示例

原始经验（冗长）：

> 这个仓库用 pnpm 管理依赖，之前用 npm install 装出来的 node_modules 结构和 lockfile 都不对，导致构建失败，排查了很久才发现问题出在包管理器上。

写入 `AGENTS.md`（简洁结论）：

```markdown
- 包管理器为 pnpm（非 npm），安装依赖用 `pnpm install`
```

原始经验（冗长）：

> 接口层代码是从 OpenAPI 生成的，手改会被覆盖。之前直接改生成文件，下次生成就没了。

写入 `AGENTS.md`（可执行步骤）：

```markdown
1. 重新生成客户端：`pnpm run generate:api`
2. 检查类型错误：`pnpm tsc --noEmit`
```

## 重复模式检测

记录新条目时先查重：

```bash
grep -r "关键词" .learnings/
```

命中已有条目时：

1. 在新条目加 `**See Also**: ERR-20250110-001`
2. 若同类问题反复出现，提升优先级
3. 判断是否属于系统性问题：
   - 缺文档 → 提升到 `AGENTS.md` 或 `CLAUDE.md`
   - 缺自动化 → 写入 `AGENTS.md`
   - 架构性问题 → 登记技术债

## 提升阈值（Promotion Rule）

同时满足以下三条时，把提炼后的规则写入系统提示级文件：

- `Recurrence-Count >= 3`
- 至少出现在 2 个不同任务中
- 发生在 30 天窗口内

这是本技能唯一的提升阈值，`self-healing` 的 Handoff 块以及聚合类技能（`learning-aggregator`、`learning-aggregator-ci`，若已安装）沿用同一规则。

提升后的规则写成简短的预防式指令（编码前或编码中该做什么），不要写成事故复盘长文。

### 承接 simplify-and-harden 的模式流

若已安装 `simplify-and-harden` 技能，按以下方式吸收其候选模式：

1. 从任务摘要中读取 `simplify_and_harden.learning_loop.candidates`
2. 以 `pattern_key` 作为稳定去重键
3. 在已有条目中查找该键：
   `grep -n "Pattern-Key: <pattern_key>" .learnings/LEARNINGS.md`
4. 命中则：`Recurrence-Count` 加一、更新 `Last-Seen`、补充 `See Also`
5. 未命中则新建 `LRN-` 条目，设置 `Source: simplify-and-harden`、`Pattern-Key`、`Recurrence-Count: 1` 以及 `First-Seen` / `Last-Seen`

## 周期性回顾

在自然断点处回顾 `.learnings/`：

- 开始一项大型任务之前
- 完成一个功能之后
- 进入有过往经验的模块时
- 活跃开发期间每周一次

### 快速状态检查

```bash
grep -h "Status\*\*: pending" .learnings/*.md | wc -l

grep -B5 "Priority\*\*: high" .learnings/*.md | grep "^## \["

grep -l "Area\*\*: backend" .learnings/*.md
```

### 回顾动作

- 关闭已修复的条目
- 提升具备普适性的经验
- 关联相关条目
- 升级反复出现的问题

## 检测触发词

在对话中出现下列表达时，立即按本技能记录：

**用户口吻**

- 记下来、沉淀一下、这个要记住
- 复盘一下、归档这个错误
- 这个方案挺好，提取成 skill
- 怎么又出问题了、我之前说过

**任务信号**

- 刚修复一个非显而易见的缺陷
- 调试过程曲折，结论值得复用
- 用到的知识可能已过时
- 用户主动补充或更正了先前信息

## 自动抽取新 skill

当一条经验值得成为独立可复用技能时，执行抽取。

### 抽取判定（满足任一即可）

| 标准 | 说明 |
|------|------|
| 反复出现 | 有 2 条以上 `See Also` 关联到同类问题 |
| 已验证 | 状态为 `resolved` 且修复方案可用 |
| 非显而易见 | 需要实际调试或调研才能发现 |
| 普适 | 不绑定特定项目，跨代码库可用 |
| 用户指定 | 用户明确说"把这个存成 skill" |

### 抽取流程

1. 确认候选条目满足抽取标准
2. 在技能目录下创建 `skills/<skill-name>/SKILL.md`
3. 用下方模板填充内容（把经验转成可执行的步骤，而不是叙述故事）
4. 更新原条目：状态改为 `promoted_to_skill`，补 `**Skill-Path**: skills/<skill-name>`
5. 在新会话中通读该 skill，确认其自包含（不依赖本次对话上下文）

### 新 skill 的 SKILL.md 模板

```markdown
---
name: skill-name
description: 第三人称描述该技能做什么、何时使用，并包含触发关键词。
agent_created: true
---

# Skill Name

## 何时使用
（列出触发场景）

## 操作步骤
1. （命令式步骤）
2. （命令式步骤）

## 检查清单
- [ ] （验证项）
```

### 抽取质量门槛

抽取前逐项确认：

- [ ] 方案经过实测可用
- [ ] 脱离原始上下文后描述依然清晰
- [ ] 代码示例自包含
- [ ] 无项目专属的硬编码值
- [ ] 命名符合规范（小写字母、数字与连字符）

## 多平台接入

| 平台 | 激活方式 | 配置位置 |
|------|----------|----------|
| WorkBuddy / CodeBuddy | 无 Hook 机制，靠本 SKILL.md 自动匹配触发 | 安装到 `~/.codebuddy/skills/` 或项目 `.codebuddy/skills/` |
| Claude Code | Hook（UserPromptSubmit、PostToolUse） | `.claude/settings.json` |
| Codex CLI | Hook（UserPromptSubmit、PostToolUse），需在 `config.toml` 中开启 `codex_hooks = true` | `<repo>/.codex/hooks.json` 或 `~/.codex/hooks.json` |
| GitHub Copilot | 指令文件通道（其 Hook 输出在提示与工具事件中被忽略，只能记录不能注入上下文） | `.github/copilot-instructions.md` |

### WorkBuddy / CodeBuddy 下的用法

没有自动 Hook，因此依赖两条通道保证不漏记：

1. 把摘要写入 `AGENTS.md`，让每次会话开头都能看到：

```markdown
## 自我改进

完成非显而易见的修复、被用户纠正、或命令报错后，按 self-improving-agent 技能记录到 `.learnings/`：
1. 按技能中的模板追加条目，生成 TYPE-YYYYMMDD-XXX 形式的 ID
2. 相关条目用 See Also 互相关联
3. 达到提升阈值的经验写入 AGENTS.md 或抽取成 skill
```

2. 会话收尾时主动自查：本次是否出现纠正、报错、知识缺口，有则先记录再结束。

### 与智能体的通用触发原则

无论使用哪个平台，出现下列情形都应记录：

1. 发现了非显而易见的事实（解法不是一步到位）
2. 自我纠正（初始思路是错的）
3. 学到了未成文的项目约定
4. 遭遇意外报错，尤其诊断过程困难
5. 找到了比原方案更好的做法

## Hook 集成（可选，仅 Claude Code 与 Codex）

Hook 为可选能力，需显式配置才会生效。以下两个脚本在 Claude Code 与 Codex CLI 通用（两者都通过 stdin 传入 JSON，并接受同样的 `additionalContext` 输出结构）；Copilot 的 Hook 只能记录、不能注入上下文，因此 Copilot 走指令文件通道。

原包中的 `scripts/activator.sh` 与 `scripts/error-detector.sh` 未随本版本分发，可按下列逻辑自建：

**activator.sh**（UserPromptSubmit，每次提示后注入约 50 至 100 token 的提醒）

```bash
#!/usr/bin/env bash
# 提醒模型在任务后评估是否记录 learnings
printf '%s' '{"hookSpecificOutput":{"additionalContext":"任务收尾时检查是否出现用户纠正、命令报错、知识缺口；若有，按 self-improving-agent 记录到 .learnings/。"}}'
```

**error-detector.sh**（PostToolUse，从 stdin 的 JSON 中解析 `tool_response` 并匹配错误特征）

```bash
#!/usr/bin/env bash
# 命中错误特征时输出 additionalContext 提醒
payload="$(cat)"
if printf '%s' "$payload" | grep -qiE '(error|failed|exception|traceback|command not found)'; then
  printf '%s' '{"hookSpecificOutput":{"additionalContext":"检测到执行失败，按 self-improving-agent 记录到 .learnings/ERRORS.md，并附上命令、报错原文与复现步骤。"}}'
else
  printf '%s' '{}'
fi
```

配置示例（Claude Code 的 `.claude/settings.json`），命令路径需指向技能实际安装位置，相对路径从项目根目录解析：

```json
{
  "hooks": {
    "UserPromptSubmit": [{
      "hooks": [{
        "type": "command",
        "command": "${CLAUDE_PROJECT_DIR}/.claude/skills/self-improvement/scripts/activator.sh"
      }]
    }],
    "PostToolUse": [{
      "hooks": [{
        "type": "command",
        "command": "${CLAUDE_PROJECT_DIR}/.claude/skills/self-improvement/scripts/error-detector.sh"
      }]
    }]
  }
}
```

## 版本控制取舍

**仅本地留存**（按开发者隔离）：

```gitignore
.learnings/
```

**纳入仓库**（团队共享）：不加入 `.gitignore`，经验成为团队共有知识。

**混合模式**（模板入库、条目私有）：

```gitignore
.learnings/*.md
!.learnings/.gitkeep
```

## 实践要点

1. 立即记录——问题刚发生时上下文最完整
2. 写得具体——让未来的会话能快速看懂
3. 附上复现步骤——错误类条目尤其重要
4. 关联相关文件——便于后续修复
5. 给出具体修复建议，而不是"需要排查"
6. 分类保持一致——便于检索过滤
7. 敢于提升——拿不准就写进 `AGENTS.md`
8. 定期回顾——过期经验会失去价值

## 检查清单

记录一条条目后自查：

- [ ] ID 符合 `TYPE-YYYYMMDD-XXX`，且未与已有条目重复
- [ ] 已先 `grep` 查重，命中则补 `See Also` 而非新建
- [ ] Summary 一句话说清，Details 保留复现上下文
- [ ] Priority 与 Area 已填
- [ ] 修复建议具体可执行
- [ ] 满足提升阈值的已同步写入目标规则文件
