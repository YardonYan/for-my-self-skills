# merge-dev-docs — 两套开发文档合并

> 合并的本质是裁决冲突，不是摘要融合。

## 解决什么

把两套开发文档交给模型「融合一下」，产物一定比原文更模糊、更没约束力——而模糊表述在企业里等于没有规范。

这个 Skill 的前提判断很明确：**合并不是把两段话揉成一段**，而是逐条抽出主张、找出真冲突、给出有依据的裁决、最后写成一份能照着做的东西。

两个文件夹规模下还有三个额外的坑，不专门处理一定失败：

1. **污染** — 先读 A 再读 B，B 的措辞会被 A 的框架重塑，冲突矩阵里塞满「A 的说法 vs A 改写过的 B」
2. **内部不自洽** — 同一套文档内部就互相打架，必须先内部对齐再跨文档对齐
3. **时态混用** — 一套写旧设计、一套写新方案，直接合并会把已废弃的架构当现状写进去，读者照着干就出事

## 什么时候用

```
把这两套开发文档合并成一份可执行的规范。
对齐这两份架构文档，冲突的地方给我裁决。
取两家优点，合并成一版团队规范。
```

## 不适用

- 合并代码 → 用 diff / rebase
- 只有一套文档，要写或体检 → 直接编辑
- 两边内容几乎不重叠（各讲不同主题）→ 不需要裁决，统一目录结构拼接即可

## 六个阶段

| 阶段 | 做什么 |
|---|---|
| Phase 0 | 先确认四件事：以谁为基底、有没有代码库或线上环境当裁决证据、出分册还是单册、合并稿放哪谁维护 |
| Phase 1 | 清点两个文件夹：字节数、章节数、条目数、时态信号、主题覆盖清单 |
| Phase 2 | 各自独立画像，**不许交叉引用**——顺序反了后面全被污染 |
| Phase 3 | 抽原子条目 + 建冲突矩阵，每条带稳定 ID 与原文行号 |
| Phase 4 | 裁决真冲突，无证据时一律走人工确认，绝不按篇幅或职级定胜负 |
| Phase 5 | **硬闸**：停下来等用户过目，不许直接往下写 |
| Phase 6 | 写分册（架构设计与开发规范骨架不同，混写会出四不像） |
| Phase 7 | 沉淀决策记录与共同盲区 |

## 脚本

`scripts/claim-index.cjs` 负责机械活：目录清点、独立画像、原子条目抽取、跨文件夹重叠打分、覆盖缺口检测。Node 20+，零依赖。

```bash
node scripts/claim-index.cjs inventory <folderA> <folderB>
node scripts/claim-index.cjs profile <folderA> --tag A
node scripts/claim-index.cjs index <folderA> --tag A
node scripts/claim-index.cjs compare <folderA> <folderB> --min 0.18
```

脚本只给定位，判断必须自己回原文读。输出的三条纪律写在 `SKILL.md` 里，其中最关键一条：`SAME TOPIC` 只是候选，措辞差异大的真冲突会掉到 `ONLY IN` 里，每段都要回原文核。

## 内含

- 六阶段流程与每阶段的产物模板
- `references/judgment-rules.md`：冲突分类与裁决判据
- `assets/`：文档画像、冲突矩阵、ADR、废弃清单、合并后架构文档与开发规范六份模板
- 覆盖缺口检测——合并真正的增值处不是 A+B，而是暴露出两套文档共同的盲区

## 安装

```bash
git clone https://github.com/YardonYan/for-my-self-skills.git
cp -r for-my-self-skills/merge-dev-docs <your-agent-skills-dir>/
```

## 许可

Apache-2.0，见 [LICENSE](./LICENSE)。
