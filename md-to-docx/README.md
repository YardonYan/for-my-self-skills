# md-to-docx — Markdown 无损转 Word

> 按 Markdown 逐元素映射到 Word，转换完还要跑一遍零缺失校验，`RESULT: PASS` 才算完成。

## 解决什么

Markdown 转 Word 的常见做法，每条都有代价：

- **pandoc**：要单独装，中文样式不跟手，表格底纹、代码块底纹、引用竖线都得再调
- **在线转换站**：文档内容要上传，公司档案不能走
- **手动复制粘贴进 Word**：格式全掉，表格错行，代码块变普通段落

这个 Skill 用 `python-docx` 直接按 Markdown 结构逐元素映射，一次生成，然后跑脚本逐字校验内容有没有丢。校验口径很硬：Markdown 里每一条内容行（标题 / 表格单元格 / 代码块行 / 引用 / 列表 / 正文）都要能在 docx 里逐字找到，标题、表格、代码块数量也要一致。

## 什么时候用

```
把这份 md 转成 word，我要无损的。
这份周报落成 docx 归档。
这份说明书给业务同事，转成 Word 发过去。
```

## 元素映射

| Markdown | Word |
|---|---|
| `#` ~ `######` 标题 | Heading 1~6，微软雅黑加粗，保留大纲结构，导航窗格可跳转 |
| `\| a \| b \|` 表格 | Table Grid，表头加粗 + 浅蓝底纹，单元格 9pt，行不跨页 |
| 代码块 | 逐行等宽（Consolas + 宋体），浅灰底纹，行距 1.0 |
| `>` 引用 | 左竖线 + 浅底纹 + 左缩进 |
| `- ` / `1. ` 列表 | 分级缩进；有序列表保留原文编号，避开 Word 多列表编号续接错乱 |
| `---` 水平线 | 段落底部细灰线 |
| 行内 `code` / `**bold**` / `*italic*` | 对应 run 格式 |

## 几个已经踩过的坑

1. 斜体正则必须加两侧负向断言，否则 `111*84*30cm` 这类尺寸里的 `*84*` 会被当成斜体
2. 表格分隔行 `| --- |` 不能当水平线判断，要先走表格分支
3. `python-docx` 默认模板是 Letter，中文文档必须改成 A4
4. 中文字体只设 `run.font.name` 无效，要额外设 `rFonts` 的 `w:eastAsia`
5. 有序列表别用 Word 内置 List Number 样式，多处列表会编号续接错乱
6. 代码块里的框线字符（│ ↓ ┌ ┐ └ ┘ →）用宋体配 Consolas，全角宽 = 2 × 半角，对齐最接近原文 ASCII 图

## 依赖

```
pip install python-docx
```

只有这一个第三方包。转换与校验都是纯命令行参数化脚本，任何 Markdown 都能直接用。

## 已知限制

Markdown 里的图片（`![](path)`）暂不嵌入，需要时在脚本里补图片段落逻辑。

## 安装

```bash
git clone https://github.com/YardonYan/for-my-self-skills.git
cp -r for-my-self-skills/md-to-docx <your-agent-skills-dir>/
pip install python-docx
```

## 用法

```bash
python scripts/md2docx.py <src.md> [dst.docx]
python scripts/md2docx_verify.py <src.md> <dst.docx>   # 必须 PASS
```

## 许可

Apache-2.0，见 [LICENSE](./LICENSE)。
