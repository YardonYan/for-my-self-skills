# dev-workflow — 开发流程五步法

> 需求理解 → 方案设计 → 代码实现 → 代码审查 → Bug 修复。每一步有自己的作业手册，不会一步跳到写代码。

## 解决什么

拿到一个需求直接开写，是最常见的失败起点。缺需求理解会做出没人要的东西，缺方案设计会写到一半推翻重来，缺代码审查会把问题留到交付。

这个 Skill 把开发过程拆成五步，按用户说的话判断当前在哪一步，然后加载对应手册执行：

| 步骤 | 触发关键词 | 手册 |
|---|---|---|
| 需求理解 | 需求分析、理解需求、整理需求、帮我梳理 | `reference/requirement.md` |
| 方案设计 | 方案设计、技术设计、架构设计、怎么实现 | `reference/design.md` |
| 代码实现 | 代码实现、开始写代码、帮我实现 | `reference/implementation.md` |
| 代码审查 | 代码审查、Review、检查代码、看看有没有问题 | `reference/review.md` |
| Bug 修复 | bug、报错、崩溃、异常、测试失败 | `reference/bug-fix.md` |

## 什么时候用

```
帮我分析这个需求，先出需求理解。
方案怎么设计？
按这个方案开始写代码。
帮我 review 一下这段代码。
这个 bug 帮我定位修复。
```

## 自动落盘

需求理解、方案设计、代码审查三步的产物默认写入 `docs/`，不需要你每次说「保存一下」：

- 单模块：`docs/需求理解.md`、`docs/方案设计.md`、`docs/代码审查.md`
- 多模块：`docs/<module>/` 下同名文件
- 追加写入，每次带 `## YYYY-MM-DD HH:mm` 时间标题，不覆盖历史
- 可选维护 `docs/模块索引.md` 记录模块与文档路径映射

## 附带的审查指南包

`reference/review-kit/` 里是按语言分开的代码审查清单：Go、Java、Python、Rust、C、C++、Qt、TypeScript、React、Vue、CSS/Less/Sass，外加架构审查、安全审查、性能审查三份专项指南和两套模板。

这些指南是公开资料的整理归纳（Go 官方指南、Effective Go、Uber Go Style Guide、JetBrains 的 SOLID 讨论、MDN 等），引用链接保留在各篇文末。

## 与 code-review 的分工

- `dev-workflow` 是**流程**：管五步怎么走、每步产出什么、产物写到哪里
- `code-review` 是**审查标准**：管七维清单、严重度排序、证伪与证据纪律

两步都装了的话，走到代码审查时由 `code-review` 提供标准，`dev-workflow` 负责把它放进流程里。

## 安装

```bash
git clone https://github.com/YardonYan/for-my-self-skills.git
cp -r for-my-self-skills/dev-workflow <your-agent-skills-dir>/
```

## 许可

Apache-2.0，见 [LICENSE](./LICENSE)。
