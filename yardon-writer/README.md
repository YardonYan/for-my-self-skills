<div align="center">

# yardon-writer

**中文长文写作 Skill：技术文讲清楚，叙事文让人读下去。**

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Type](https://img.shields.io/badge/type-longform%20writing-8B5CF6.svg)](#两种模式)
[![Language](https://img.shields.io/badge/language-中文-D97706.svg)](#)

**中文** · [English](README.en.md)

</div>

---

> 把技术讲清楚，同时让人愿意读下去。硬核的内容，用活人的语气写。

这是一套中文长文写作 Skill，不是通用“写作助手”提示词。它把技术长文的结构、叙事长文的节奏、禁用词、自检清单和阅读体验拆成可执行的规则，写之前先判断文体，写之后按清单逐项过。

## 解决什么问题

- 技术文容易写成说明书：结构齐但没人想读
- 叙事文容易写成流水账：有经历但没有观点
- 两种文体混着写：该讲清楚的地方抒情，该讲故事的地方列提纲
- 写着写着开始编经历、编数据、编对话

这个 Skill 的核心是**先裁决文体，再动笔**。技术文保留结构、代码和可检索性；叙事文弱化结构，把人和观点放到前面。两边冲突的地方不硬融，按文体选。

## 什么时候用

适合：

- 公众号文章、技术博客、CSDN 长文
- 项目复盘、经验总结、职场观察
- 把一个 PDF、新闻链接、语音转文字或零散想法写成文章
- 按固定风格续写、扩写、改写成一篇完整长文

不适合：

- 朋友圈、推特、小红书短帖
- 纯标题、摘要、SEO 关键词堆砌
- 没有素材、要求凭空编一段真实经历的写作

## 两种模式

| 模式 | 读者来干什么 | 结构 | 典型场景 |
|---|---|---|---|
| A 技术长文 | 查答案、学东西 | 分节、表格、代码、本章小结都保留 | 教程、原理解析、实战、踩坑记录 |
| B 叙事长文 | 听故事、拿观点 | 弱化小标题，用转场句推进，第一人称经历为核心 | 项目复盘、职场观察、经验分享、观点解读 |

判断标准很简单：**读者读完之后会不会去复制代码。** 会，就是 A；不会，就是 B。

## 写作流程

1. 吃素材，判选题。过 HKR 质检：有趣、有信息量、能共鸣，至少占两项
2. 选模式：A 技术文 / B 叙事文
3. 定文章原型（五种原型见 `references/article-prototypes.md`）
4. 开写：AI 负责背景知识、类比候选、结构建议和按角度扩写；真实经历、核心角度、情绪表达由人来给
5. 过四层自检（`references/banned-and-check.md`）
6. 过阅读体验自检（`references/readability.md`）
7. 终审定稿

## 文件结构

```
yardon-writer/
├── SKILL.md
├── README.md
├── README.en.md
├── LICENSE
└── references/
    ├── style-core.md            风格内核、双模式规则、冲突裁决
    ├── voice-dna.md             语言 DNA：类比公式、自问自答、短句判断
    ├── article-prototypes.md    五种文章原型与写法重心
    ├── banned-and-check.md      双向禁用清单、四层自检
    └── readability.md           阅读体验层：数字分级、加粗收敛、开头、节奏
```

## 安装

让支持 Agent Skills 的工具自己装：

```
帮我安装这个 skill：https://github.com/YardonYan/for-my-self-skills/tree/main/yardon-writer
```

或者 clone 后把 `yardon-writer/` 放进工具的 skills 目录，确保目录根部有 `SKILL.md`。

不支持 Skill 加载的平台：打开 `SKILL.md`，把全文贴进项目规则或系统提示词。

## 示例触发

```
把这段素材写成一篇公众号长文，按我的风格。
这篇项目复盘帮我重写，不要写成流水账。
把这个 PDF 里的内容整理成一篇技术长文。
这篇文章读起来太像 AI 写的，按 yardon-writer 的规则改一遍。
```

## 底线

- 不编造具体经历、数据、金额、对话
- 技术文里术语第一次出现必须解释
- 涉及公司业务默认脱敏：不写公司名、客户名、内部数据、服务器地址
- 不装客观。写「我认为」「我踩过」，比写「该方案具备显著优势」可信

## 标签

`writing` · `chinese` · `longform` · `technical-writing` · `narrative` · `style`

## License

Apache-2.0，见 [LICENSE](LICENSE)。
