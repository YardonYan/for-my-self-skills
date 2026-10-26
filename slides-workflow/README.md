# slides-workflow — 从素材到成稿的幻灯片生产流程

> 内容先行，形态后选。先把「要说什么」定死，再定「长什么样」，最后才决定做成 HTML、整页图片还是可编辑 PPTX。

## 解决什么

用 AI 做 PPT 最常见的失败不是「做不出来」，而是做到一半发现方向错了：

- AI 自己分页、自己写文案，做完一版发现页序和重点都不对，只能推翻重来
- 没有风格说明，逐页各做各的，改到第七页时前面几页已经不像同一套
- 选错形态：只想发给人看，却被要求交付可编辑 PPTX；或者后面要反复改，却做成了一堆图片

时间看起来都花在排版上，真正决定返工次数的是开头的信息是否定清、风格是否统一、形态是否选对。这个 Skill 把这条链路拆成四个阶段，前两个阶段设成硬闸，不确认就不往下走。

## 什么时候用

```
帮我把这堆资料整理成一份汇报 PPT。
要做一份 20 分钟的培训课件，素材整理好了。
这套 PPT 要反复改，怎么让 AI 做出来我能编辑的版本？
我有一版图片稿，想转成能改的 PPTX。
这几页怎么改都不对，帮我看看问题在哪。
```

## 四个阶段

| 阶段 | 做什么 | 产出 |
|---|---|---|
| 一 采集与逐页稿 | 六件事问清、素材分三目录、逐页 7 字段 | `page-script.md` |
| 二 风格说明 | 参考图拆成配色字体版式，多方向选一 | `style-spec.md` |
| 三 选形态制作 | HTML Slides / 整页图片 / 可编辑 PPTX 三选一 | 成品 + PDF 备用稿 |
| 四 局部打磨 | 五段式修改指令，按页改 | 定版 |

阶段一和阶段二结束都有硬闸。跳过闸门不是省时间，是按倍数返工。

## 三种形态怎么选

| 你的情况 | 选哪种 |
|---|---|
| 现场讲，要动画或交互 | HTML Slides |
| 只想先看效果，或只发给人看 | 整页图片 |
| 后续还要频繁改，或要交给同事编辑 | 可编辑 PPTX |
| 有必须遵循的企业模板 | 可编辑 PPTX，直接沿用母版 |
| 封面要视觉冲击，内容页要能改 | 混用 |

三种形态各自的硬约束、制作提示词和验收清单，各有一份说明：`references/mode-html.md`、`references/mode-image.md`、`references/mode-pptx.md`。

## 内含

- **四个阶段的作业方法**：简报两型（简洁 / 精致）、逐页稿 7 字段、风格说明模板、五段式修改指令
- **三套制作提示词**：HTML Slides、整页图片、可编辑 PPTX，都是从实际项目里跑出来的版本，含验收口径
- **图片稿还原方法**：混合还原、清背景旧字、拆不干净时怎么交代
- **九个已知失败模式**：从「AI 自行分页」到「两轮没改善还在重复生成」，症状对应处置
- **两个校验脚本**：项目脚手架 + 逐页稿与素材完整性校验，只用 Python 标准库

## 脚本

```bash
python scripts/scaffold.py <项目目录> --full   # 生成简报、逐页稿、风格说明骨架 + 素材目录
python scripts/verify.py script <项目目录>      # 校验逐页稿：页码连续、7 字段齐全、待补充统计
python scripts/verify.py assets <项目目录>      # 校验素材：引用文件是否存在、有无未引用文件、序号连续性
```

`verify.py` 输出 `RESULT: PASS` 才算通过，否则逐条列出页码与字段名。字段名必须与 `references/page-script.md` 里的写法一致，写成「布局」而不是「建议布局」会报缺字段。

## 边界

- **不做无素材的凭空创作**。素材不够时先要材料，不硬编内容
- **不做企业模板的像素级复刻**。要严格遵循品牌模板时，人做比 AI 快
- **不承诺交付物必须联网才能放映**
- **不把「图片看起来对」当成「内容正确」**，数字与单位要回到原始资料核

## 与仓里其他 Skill 的关系

- 纯文档排版不走这里：Markdown 转 Word 用 `md-to-docx`，HTML 转 PDF 用 `html-to-pdf`
- 需要单文件 HTML 交付物（报告、看板）用 `html-skill-effectiveness`，本 Skill 的 HTML 模式专攻 16:9 逐页演示
- 内容写作阶段可以先用 `tech-blog-generator` 或 `yardon-writer` 把文字理顺，再进逐页稿

## 安装

```bash
git clone https://github.com/YardonYan/for-my-self-skills.git
cp -r for-my-self-skills/slides-workflow <your-agent-skills-dir>/
```

或让 Agent 自己装：

```
帮我安装这个 skill：https://github.com/YardonYan/for-my-self-skills/tree/main/slides-workflow
```

## 依赖

不需要额外依赖。两个脚本只用 Python 标准库，Python 3.8 及以上可运行。

制作阶段用到的外部 Skill（frontend-slides、huashu-design、visual-explainer、ppt-master 同类工具）不是本仓内容，按你的环境自选，不装也能用，提示词里换掉名称即可。

## 许可

Apache-2.0，见 [LICENSE](./LICENSE)。
