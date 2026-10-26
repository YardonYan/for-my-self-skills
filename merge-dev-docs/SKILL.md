---
name: merge-dev-docs
description: Merge two or more folders of development documents (dev guides, coding conventions, architecture docs, 开发文档, 研发手册, 架构设计, 规范文档) into one coherent set by taking the strengths of each and adjudicating conflicts. Use when the user wants to combine, reconcile, unify, or align overlapping or conflicting written standards across two document sets, including 两套文档合并 / 取两家优点 / 合并规范 / 对齐两份文档 / 统一团队文档 / 架构文档对齐. Not for merging code, and not for writing a document from scratch.
argument-hint: <文件夹A路径> <文件夹B路径> [--out <输出目录>] [--arch] [--spec]
---

# Merge Dev Docs

## Overview

把两套文档合成为一份可执行的规范。核心认知：**合并的本质是裁决冲突，不是摘要融合**。直接把两套文档整体交给模型「融合一下」，产物一定比原文更模糊、更没约束力——模糊表述在企业里等于没有规范。

两个文件夹规模下有三个额外难点，必须专门处理，否则合并一定失败：

1. **污染**：先看完 A 再看 B，B 的措辞会被 A 的框架重塑，冲突矩阵里塞满「A 的说法 vs A 改写过的 B」，假冲突与漏冲突一起变多。
2. **内部不自洽**：同一文件夹内部就可能互相打架，必须先内部对齐再跨文件夹对齐。
3. **时态混用**：两套文档通常一个写着旧设计、一个写着新方案，直接合并会把已废弃的架构当现状写进去，读者照着干就出事。

按六个阶段走，每个阶段的产物是下一阶段的输入，不许跳步。**Phase 3 结束有硬闸，必须停下来等用户过目。**

## When NOT to use

- 合并的是代码而不是文档 → 用 diff / rebase
- 只有一套文档，要写或体检 → 直接编辑，或先做单文件夹体检
- 两边内容几乎不重叠（各覆盖不同主题）→ 不需要裁决，统一目录结构即可拼接，跳过 Phase 4

## Phase 0 — 先确认四件事

动手前必须拿到明确答案，缺一项就问，不要猜：

1. **哪两套、以谁为基底**。基底决定章节顺序与行文风格。文件夹级场景下，基底是**整套**而非单篇。
2. **有没有代码库或线上环境可以当裁决证据**。这一项直接决定 Phase 4 的裁决能不能给出确定结论，详见 `references/judgment-rules.md` 第三节。无证据时架构层冲突必须全部走人工确认，**绝不允许凭文档篇幅、作者职级或团队立场定胜负**。
3. **出分册还是单册**。架构设计与开发规范是两种体裁，骨架不同；混在一起会产出「四不像文档」。默认出分册。
4. **合并稿放哪、谁维护**。放仓库外（wiki / .docx）两个月内会重新分裂成两份。

## Phase 1 — 清点两个文件夹

```bash
node scripts/claim-index.cjs inventory <folderA> <folderB>
```

一次输出：每篇文档的字节数、章节数、条目数；**时态信号**（已废弃 / 待实施 / 现状的候选行）；两边各自的主题覆盖清单。

读原始文本确认两件事，脚本只给你定位，判断必须自己读：

- 同一文件夹内部是否互相矛盾。内部矛盾先在本文件夹内解决，别把 A 的内部矛盾带进跨文件夹裁决。
- 有无 README、会议纪要、周报混进来当开发文档用。这些不是规范，Phase 1 就该排除。

## Phase 2 — 各自独立画像，不许交叉引用

```bash
node scripts/claim-index.cjs profile <folderA> --tag A
node scripts/claim-index.cjs profile <folderB> --tag B
```

**两份画像必须分别做完再看对方。** 顺序反了，后面所有比较都被污染。

各自产出一份画像（用 `assets/doc-profile.md` 模板）：文档清单与各自定位、覆盖了哪些主题、**该套文档独有的判断与理由**、作者与日期证据、自称覆盖但实际没写的部分。

画像阶段的目的是把「这套文档为什么这么写」挖出来。跨文件夹裁决时经常发现真冲突的根因在这里——一边是深思熟虑的权衡，一边是没想过。

## Phase 3 — 抽条目 + 建冲突矩阵

```bash
node scripts/claim-index.cjs index <folderA> --tag A
node scripts/claim-index.cjs index <folderB> --tag B
node scripts/claim-index.cjs compare <folderA> <folderB> --min 0.18
```

长文件夹用 `--offset/--limit` 分页读，单次不超过 120 条。每条 claim 带稳定 ID（`A/架构设计.md:12`，含文档路径）与原文行号，后续所有引用只用这个 ID。**一份没有出处的合并稿无法被 review。**

**关于脚本输出的三条纪律：**

- **SAME TOPIC 只是候选，不是全部真冲突。** 它按章节相似度打分，措辞差异大的真冲突会掉到 RELATED 甚至 ONLY IN 里。测试里「单集群 vs 多活」「PG vs MySQL」这类硬冲突全部落在 ONLY IN 段。**每个 ONLY IN 段都要回原文读一遍，确认它在对方面不是被写成了另一个措辞。**
- **DOC-LEVEL asymmetry 是最容易漏真冲突的地方**，逐条看完。
- **COVERAGE GAPS 是合并真正的增值处**：不是 A+B，而是暴露出共同盲区。

分主题分批做，不要整文件夹一次性判完：先按主题聚类（哪几篇讲部署、哪几篇讲数据模型），每个主题一张矩阵、一批裁决。全局性的时态判定和术语表先行做掉。

矩阵填进 `assets/conflict-matrix.md`，**先填表再写正文。**

## Phase 4 — 裁决真冲突

详见 `references/judgment-rules.md`。三条铁律：

- **不投票、不折中。** 「两边都保留」是最坏结果，读者不知道该听谁。
- **先判时态。** 每条 claim 先标 已落地 / 已废弃 / 待实施。已废弃的直接进淘汰区，不参与裁决；待实施的标注 `[待实施]` 不与已落地规则混写。这是架构文档合并的头号杀手。
- **无证据就承认。** 输出 `待裁决` 并列出两方主张、影响面、需要谁定夺。宁可留一个明确空洞，也不留一个虚假一致。

每条裁决写一句理由，附 claim ID。

## Phase 5 — 硬闸：停下来

**冲突矩阵产出后必须停止，向用户交付并等回话。不许接着写合并稿。**

交付三样：两套画像、填好的冲突矩阵、裁决建议清单（每条写明建议方案 + 依据 + 若被推翻的影响面）。

理由：这些裁决里有相当一部分没有客观事实可依（无代码可查时尤甚），只是基于文本质量的倾向判断。用户要先看清依据，才知道哪些需要去争取、哪些可以放手。跳过硬闸直接给成稿，等于替他做完 80% 的裁决且不提供复核入口。

## Phase 6 — 写分册

裁决确认后写，两个体裁各用一套骨架：

- **架构设计文档** → `assets/merged-arch-doc.md`：系统定位与边界、上下文关系、组件职责、关键流程时序、数据模型与所有权、部署拓扑、技术决策记录
- **开发规范文档** → `assets/merged-dev-spec.md`：第一天、目录落位、命名、分层与依赖、错误处理、数据变更、测试、评审发布、术语表

两份都写时，**先写架构再写规范**，规范里指向架构文档而不是复述它。

以基底骨架重写，遵循：

- **一条规则一行，可执行。** 读者照着就能做。
- **保留具体名字。** 文件路径、命名模式、命令、数值阈值——具体性是文档唯一的约束力来源。
- **抽象原则句删掉。** 「代码要保持简洁」「注意性能」这类两边都写的空话全删。**删条目是合并的主要动作之一**，文档变薄是正常结果。
- **标注出处与核对日期。** 每条后附 `[A/文档.md:7 + B/文档.md:12]`，文件头写 `最后核对：YYYY-MM-DD`。

## Phase 7 — 沉淀决策与盲区

- 每个真冲突一条 ADR（`assets/adr.md`），必须包含「什么情况会推翻它」。
- 淘汰区清单单列一份，说明淘汰了什么、为什么不留。**作者看到自己写的东西被删且无说明，下次会直接加回去。**
- COVERAGE GAPS 转待办，指明谁补、补进哪个文件。
- 交付前跑 `references/judgment-rules.md` 末尾的自检清单。

## 输出给用户时

报三个数字加一份清单：抽取条目数（两边各多少篇多少条）、裁决掉的冲突数、待裁决数与共同盲区数。附画像、矩阵、分册路径。

明确说出哪些地方是替他做的判断、哪些是他拍过板的。那才是他复核的对象。

## Resources

- `scripts/claim-index.cjs` — 目录清点、独立画像、原子条目抽取、跨文件夹重叠打分、覆盖缺口检测。Node 20+，无依赖。
  - `inventory <dirA> <dirB>` — 清点 + 时态信号 + 主题覆盖
  - `profile <dir> --tag A` — 单文件夹文档级画像
  - `index <dir> --tag A` — 原子条目枚举，claim ID 含文档路径
  - `compare <dirA> <dirB>` — 跨文件夹对比，四类输出
- `references/judgment-rules.md` — 时态判定、四元式比较、真冲突解法、无代码证据下的裁决路径、留下门槛、失败模式、自检清单。
- `assets/doc-profile.md` — 独立画像模板。
- `assets/conflict-matrix.md` — 冲突矩阵表模板。
- `assets/merged-arch-doc.md` — 架构设计文档骨架。
- `assets/merged-dev-spec.md` — 开发规范文档骨架。
- `assets/adr.md` — 单条决策记录模板。
- `assets/deprecated.md` — 淘汰区清单模板。