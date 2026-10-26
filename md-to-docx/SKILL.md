---
name: md-to-docx
description: MD 文件无损转换 Word（.docx）——标题/表格/代码块/引用/列表/行内格式逐元素保真映射，附零缺失校验脚本。当用户要求"把 MD 转 Word/转成 docx/无损转换"、或需要把周报/档案/使用说明等 Markdown 文档落成 Word 文件时使用。pandoc 不可用时的高保真替代方案。
agent_created: true
version: 1.0.0
---

# MD → Word 无损转换（md-to-docx）

## 触发场景
- 用户要求"把这份 md 转成 word / docx / 无损转换"
- 周报、标准档案、使用说明等 Markdown 文档需要落成 Word 文件归档或提交

## 为什么不用 editor_sdk / tencent-docx
- tencent-docx 插件是"从零创建"，不接收源材料（且 MD 非 Office 格式）
- editor_sdk 的 doc_insert_text 逐段插入适合编辑/少量追加；964 行、31 张表格、10 个代码块的复杂 MD 逐段插入工作量巨大且易错位
- 本方案用 python-docx 直接按 Markdown AST 逐元素映射，一次生成、可控可验证，保真度最高

## 使用步骤

### 1. 准备依赖

```bash
pip install python-docx
```

脚本只依赖 `python-docx`，无其他第三方包。装在哪个环境都行，只要运行脚本的解释器能 import 到。

### 2. 运行转换
```bash
python scripts/md2docx.py <src.md> [dst.docx]
```
- dst 省略 = 与 src 同目录同名 `.docx`
- 转换脚本内置完整映射，无需修改源码即可处理常规 MD

### 3. 必须验证（无损硬性要求，不可跳过）
```bash
python scripts/md2docx_verify.py <src.md> <dst.docx>
```
- 输出 `RESULT: PASS` 才算完成；任何 `!!` 行都是问题，需修复后重转
- 校验口径：MD 每条内容行（标题/表格单元格/代码块行/引用/列表/正文）在 DOCX 中逐字可找（忽略空白与 markdown 符号）+ 标题/表格/代码块数量一致

### 4. 呈现结果
- 打开生成的 docx 供用户查看
- 输出文件与源 md 同目录同名，不另建文件夹

## 元素映射表（无损 = 内容不丢 + 视觉不降级）

| MD 元素 | Word 实现 |
| --- | --- |
| `#`~`######` 标题 | Heading 1~6（微软雅黑加粗、黑色、保留大纲结构，导航窗格可跳转） |
| `\| a \| b \|` 表格 | Table Grid（表头加粗 + 浅蓝底纹 D9E2F3、单元格 9pt、行不跨页 cantSplit） |
| ``` 代码块 | 逐行等宽（Consolas + 宋体 eastAsia）、浅灰底纹 F5F5F5、行距 1.0、左右缩进 |
| `>` 引用 | 左竖线（2E74B5）+ 浅底纹 F7F9FC + 左缩进 |
| `- ` 无序列表 | 手动项目符号（• / 嵌套 ◦）+ 分级左缩进 |
| `1. ` 有序列表 | 保留原文编号 + 悬挂缩进（防 Word 多列表编号续接错乱） |
| `---` 水平线 | 段落底部细灰线（BFBFBF） |
| `` `code` `` 行内代码 | 等宽 Consolas + 宋体，字号 -1 |
| `**bold**` | 加粗 |
| `*italic*` | 斜体（两侧非字母数字才匹配） |

## 关键踩坑（已修复，勿重复踩）

1. **斜体正则必须加两侧负向断言** `(?<![A-Za-z0-9])\*[^*]+\*(?![A-Za-z0-9])`
   ——否则 `111*84*30cm`（尺寸）里的 `*84*` 会被误判为斜体
2. **表格分隔行 `| --- |` 不能当水平线**——先判断 `startswith('|')` 表格分支，再判断 `^-{3,}$` 水平线；表格行解析时用 `^\|[\s\-:|]+\|$` 识别分隔行并跳过
3. **页面必须改 A4**——python-docx 默认模板是 Letter（21.59×27.94cm），中国文档要 `page_width=Cm(21)` / `page_height=Cm(29.7)`
4. **中文字体必须设 eastAsia**——`run.font.name` 只设西文，中文要额外 `rFonts.set(qn('w:eastAsia'), 字体)`；Normal 样式同理，否则 Word 里中文显示默认宋体/字体错乱
5. **代码块中文用宋体配 Consolas**——框线字符（│↓┌┐└┘→）在 Consolas 有字形，中文宋体全角宽 = 2×半角，对齐最接近原文 ASCII 图
6. **有序列表不用 Word 内置 List Number 样式**——多处列表会编号续接错乱；保留原文数字 + 悬挂缩进最稳
7. **emoji（💰⚠️）直接 Unicode 写入**——Word 自动用 Segoe UI Emoji 渲染，无需特殊处理

## 效果基准（实测）

一份 964 行技术档案：87 标题 / 31 表格 / 10 代码块 / 1441 内容行 → 验证 PASS，零缺失，输出 70.6 KB。

## 备注
- 转换脚本与验证脚本参数化通用，任何 MD 都可直接用
- 若 MD 含图片（`![](path)`），本脚本暂不嵌入图片；需要时在 `add_body` 前增加图片段落逻辑
