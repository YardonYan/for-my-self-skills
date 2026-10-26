# html-to-pdf — 打印优化 HTML 出 PDF

> CSS 就是排版语言，`@page` 直接控制纸张。中文不乱码、表格不散架、图片内嵌。

## 解决什么

要把一份 Markdown 或网页内容交成 PDF，绕不开这几个选择：

- **weasyprint**：Windows 上要装 GTK，依赖重
- **reportlab / fpdf**：中文要手工注册字体，表格排版代码量大
- **Word 转 PDF**：受 Office 版本和本机字体影响，中间还要过一道 docx
- **Chrome 无头**：装了 Chrome 或 Edge 就有，直接吃 CSS

这个 Skill 用 Chrome 无头模式，把三件事做成固定流程：写打印优化的 HTML → 图片一律 base64 内嵌 → 转 PDF 后核验页数与关键词，再把页面渲染成 PNG 自己看一眼。

## 什么时候用

```
把这份说明转成 PDF 交付。
出个 PDF 版方案，别给 md。
这份使用手册要给业务同事，做成 PDF。
```

## 三步做法

1. **写打印优化的 HTML**：`@page { size: A4; margin: 16mm 14mm }`，标题 `page-break-after: avoid`，表格行 `page-break-inside: avoid`，正文 12.5pt / 1.75 行高是中文 A4 的舒适值
2. **图片 base64 内嵌**：HTML 里写 `{{FIG1}}` 占位，生成时替换成 `data:image/png;base64,...`，避开本地路径沙箱问题，中间 HTML 也能单文件传阅
3. **Chrome 无头转 PDF**：`--headless=new --print-to-pdf=...`，输入路径必须转成 `file:///` URI

## 必做核验

不核验就说「生成好了」是这个流程最容易犯的错。三步都要过：

- 页数符合内容量预期
- 关键词逐个提取命中（标题、正文片段、英文片段）
- 渲染成 PNG 目视抽查：表格有没有断成两半、图有没有丢、长表格表头有没有孤立在页底

## 踩过的坑

1. **中文路径**：输出路径可以直接给中文，但输入的 HTML 必须用 `Path(x).as_uri()` 转 URI，否则静默失败
2. **目标 PDF 被占用**：PDF 正被阅读器打开时，Chrome 不报错，`returncode` 还是 0，但内容根本没更新。排查办法是比对源 HTML 与 PDF 的修改时间
3. **不要删源文件**：保留 HTML 源，改文案后重跑一条命令就能重出，只有 PDF 没源等于下次重写
4. **图内标题与图注重复**：流程图自带「图 5 xxx」时，`<figcaption>` 只写解释文字
5. **Pillow 画图中文**：字体用系统黑体，不要用 emoji（会渲染成豆腐块），要彩色圆点就用 `draw.ellipse()`
6. **改文案要回查配图**：正文从 5 步改成 4 步，图还是 5 步，这类不一致扫一遍渲染图最快发现

## 附带

同一批材料既要 PDF 又要网页时，共用一份源 HTML：PDF 走打印路径（`@page`、`page-break`），网页走屏幕路径（sticky 导航、宽容器）。README 之外的内容都写在 `SKILL.md` 里，包括多页互跳导航、Markdown 存档渲染、Tab 切换平行内容的最小实现。

## 依赖

- Chrome 或 Edge（脚本里带 `shutil.which` 查找，找不到时按注释改成自己机器上的路径）
- Python：`fitz`（PyMuPDF）用于核验页数与关键词

## 安装

```bash
git clone https://github.com/YardonYan/for-my-self-skills.git
cp -r for-my-self-skills/html-to-pdf <your-agent-skills-dir>/
```

## 许可

Apache-2.0，见 [LICENSE](./LICENSE)。
