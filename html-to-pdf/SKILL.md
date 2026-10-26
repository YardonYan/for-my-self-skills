---
name: html-to-pdf
description: 把内容转成 PDF 交付（说明书、使用手册、报告、方案、周报）。用打印优化的 HTML + Chrome 无头模式出 PDF，中文不乱码、表格不散架、图片可内嵌。当用户说"转成 pdf""出个 pdf 版""说明书别给 md 给 pdf"时使用。含中文字体、打印分页、路径编码、结果核验的完整做法。
---

# HTML → PDF 交付（Chrome 无头模式）

## 什么时候用
- 用户要"转成 PDF"的说明书 / 使用手册 / 报告 / 方案
- 交付对象是业务人员（不熟悉 markdown 渲染）
- 需要控制分页、表格不跨页断裂、配图随文

## 为什么不用别的
- `weasyprint`：Windows 上要装 GTK，依赖重
- `reportlab` / `fpdf`：中文要手工注册字体，写表格排版代码量大
- Word 转 PDF：受 Office 版本与本机字体影响，且要过一道 docx
- **Chrome 无头**：装了 Chrome 或 Edge 就有，CSS 就是排版语言，`@page` 直接控制纸张

## 三步做法

### 1. 写打印优化的 HTML
关键 CSS：

```css
@page { size: A4; margin: 16mm 14mm; }
body { font-family:"Microsoft YaHei","PingFang SC",sans-serif;
       font-size:12.5pt; line-height:1.75; color:#222; }
h2 { page-break-after: avoid; }        /* 标题不与正文分离 */
tr { page-break-inside: avoid; }        /* 表格行不跨页断开 */
figure, .tip { page-break-inside: avoid; }
```

- body 字号 `12.5pt` 是中文 A4 通用舒适值；表格 `11.5pt`
- 左列窄、右列宽的对照表用 `td.k`（浅底纹 + 加粗）做行标题
- 提醒块用左边框 4px 红线 + 浅底，比纯文字醒目

### 2. 图片一律 base64 内嵌
HTML 里写占位符 `{{FIG1}}`，用 Python 替换：

```python
b64 = base64.b64encode(open(png, "rb").read()).decode("ascii")
html = html.replace("{{FIG1}}", "data:image/png;base64," + b64)
```

避免 Chrome 读本地相对路径时的沙箱问题，也让中间 HTML 单文件可移植。

### 3. Chrome 无头转 PDF

```python
from pathlib import Path
import subprocess, shutil

# 找不到就换成自己机器上的路径：
#   macOS   /Applications/Google Chrome.app/Contents/MacOS/Google Chrome
#   Linux   google-chrome / chromium
CHROME = shutil.which("chrome") or r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
    "--no-pdf-header-footer",                          # 去掉页眉页脚
    "--run-all-compositor-stages-before-draw",
    "--virtual-time-budget=8000",                      # 等图片/字体就绪
    f"--print-to-pdf={PDF}",
    Path(tmp_html).as_uri(),                           # 中文路径必须转 URI
]
subprocess.run(cmd, capture_output=True, text=True)
```

## 必做核验（别凭感觉说"生成好了"）

```python
import fitz   # 已装，比 pypdf 稳
d = fitz.open(PDF)
print("页数 =", d.page_count)
text = "\n".join(p.get_text() for p in d)
for kw in ["标题关键词", "某个示例句子", "英文片段"]:
    print(kw, kw in text)
```

**视觉核对**：把页面渲染成 PNG 自己看一眼，排版问题肉眼最快：

```python
pix = d[i].get_pixmap(dpi=100)
pix.save(f"p{i+1}.png")
```
重点看：表格有没有断裂成两半、图有没有丢、长表格表头是否孤立在页底。

## 踩坑清单

1. **中文路径**：`--print-to-pdf` 的输出路径可以直接给中文，但输入的 HTML 必须用 `Path(x).as_uri()` 转成 `file:///` URI，否则静默失败。
2. **PowerShell 输出被吞**：本会话环境里 PowerShell 常出现 `exit 0` 但 stdout 为空。解决：脚本里把结果写进 `$env:TEMP\xxx.txt`，再用 Read 工具读。
3. **不要删源文件**：保留 HTML 源（放 `assets/_xxx_src.html` 之类），改文案后重跑一条命令即可重出 PDF；只有 PDF 没有源，下次改一个字都要重写。
4. **图内标题与文档图注重复**：流程图自身带"图 5 xxx"标题时，文档里的 `<figcaption>` 就别再写"图 5"，只写解释性文字。
5. **图与正文不一致**：改文案后记得回头看配图里的措辞（常见错误：正文改成 4 步，图还是 5 步）。
6. **Pillow 画图中文**：用 `C:/Windows/Fonts/msyh.ttc`（常规）与 `msyhbd.ttc`（加粗）；**不要用 emoji**（`🔴` 会渲染成豆腐块），要彩色圆点就用 `draw.ellipse()` 画。
7. **目标 PDF 被占用会静默失败（最坑）**：若 PDF 正被预览器/阅读器打开，Chrome **不报错**，`returncode` 仍是 0，但 PDF 内容根本没更新。**排查**：比对源 HTML、图片与 PDF 的 `LastWriteTime`，源更新了而 PDF 没变就是这个问题。**绕开**：换个输出文件名生成，再删旧文件重命名（被锁文件执行删除或重命名会抛"另一个进程正在使用此文件"）。生成脚本里最好加一道自检：输出 PDF 的修改时间必须晚于源文件。
8. **改了文案要同步回头查配图**：正文从 5 步改成 4 步后，图还是 5 步、图注还写"五步"，这类不一致肉眼扫一遍渲染图最快发现。

## 判断标准
- `.pdf` 生成且大小合理（含图通常 200KB 以上）
- 页数符合内容量预期
- 关键词提取全中
- 渲染抽查至少首页 + 最密的一页表格

## 实战案例

一份企业知识库问答智能体的使用说明：HTML（12 章节、11 张表、1 张流程图）→ 6 页 PDF 456KB，表格无断裂，中英混排正常。同一份源 HTML 出四件套：`_usage_src.html`（源）+ `build_pdf.py`（转 PDF）+ `check_pdf.py`（关键词核验）+ `render_pdf.py`（渲染成 PNG 目视检查）。

## 配套：多页 HTML 交付（同一批文档做成可互跳的网页）

同一套材料既要 PDF 又要网页时，做法是**共用一份源 HTML**：PDF 走打印路径（`@page`、`page-break`），网页走屏幕路径（sticky 导航、宽容器）。不要维护两套内容。

### 三页互跳的最小实现
每页顶部内联同一段导航，当前页加 `class="on"` 高亮，链接用同目录相对路径（中文文件名可直接写，浏览器会自行编码）：

```html
<nav class="topnav">
  <span class="brand">智能体名称</span>
  <a href="xxx-功能介绍.html" class="on">功能介绍</a>
  <a href="xxx-使用说明.html">使用说明</a>
  <a href="xxx-实测对话.html">实测对话</a>
</nav>
```

```css
.topnav{position:sticky;top:0;z-index:60;background:#2f3b4c;color:#fff;
        display:flex;gap:6px;padding:0 24px;flex-wrap:wrap;}
.topnav .brand{margin-right:auto;font-weight:bold;padding:14px 0;}
.topnav a{color:rgba(255,255,255,.8);text-decoration:none;padding:14px 16px;
          border-bottom:3px solid transparent;}
.topnav a.on{color:#fff;border-bottom-color:#7fb2e5;font-weight:bold;}
@media print{.topnav{display:none;}}   /* 打印时导航自动消失 */
```

导航与样式全部内联进各页，不依赖外部 CSS/JS —— 单文件可单独传阅、可直接双击打开。

### 把 markdown 记录渲染成网页
智能体的回复常以 markdown 存档（`~~~markdown` 包裹）。渲染成网页比贴源码可读得多：

```python
# 隔离 venv 里装：pip install markdown
import markdown
def render_md(text):
    return markdown.Markdown(
        extensions=["tables", "fenced_code", "sane_lists"]
    ).convert(text)
```

解析存档时用**状态机**区分提问块与回复块：遇到 ```` ``` ```` 进提问态、遇 `~~~markdown` 进回复态，回复态只认 `~~~` 收尾（这样回复正文里的 ``` 代码块不会被误判成结束）。用 `#### xx回复 Nmin` 这类标题行可提取耗时标签。

### 排版要点
- `.md` 容器内限制标题字号（h1 约 19px、h2 17px），否则存档里的 `#` 级标题会撑爆页面
- `hr` 做淡（`border-top:1px solid #e6ebf1`），避免满屏黑线刺眼
- `blockquote` 给浅底 + 左竖线，把原来的 `>` 符号转成视觉缩进
- 表格沿用与 PDF 一致的浅蓝表头

### 核对排版
`shot.py`：Chrome `--headless=new --screenshot --window-size=1240,H`，直接用 `Path(html).as_uri()` 传路径。截完自己看一眼，比读源码快得多。

### 平行内容用 Tab 切换，不要一次性铺开
5 组以上平行内容（多组测试记录、多版本方案、多场景示例）全展开会很长，读者找不到重点。改成顶部按钮 + 下方内容区：

```html
<button class="tab on" onclick="showTab(1)">测试一</button>
<button class="tab"    onclick="showTab(2)">测试二</button>
<div class="pane on" id="pane1">…</div>
<div class="pane"    id="pane2">…</div>
<script>
function showTab(i){
  var t = document.querySelectorAll('.tab'), p = document.querySelectorAll('.pane');
  for (var k = 0; k < t.length; k++){
    t[k].classList.toggle('on', k === i - 1);
    p[k].classList.toggle('on', k === i - 1);
  }
  window.scrollTo({ top: document.getElementById('tabs').offsetTop - 70, behavior: 'smooth' });
}
</script>
```
`.pane{display:none}` / `.pane.on{display:block}` 即可，无需框架。按钮文字建议「序号 + 一句话说明」（如"测试二　产品品类辨析"），光有编号读者不知道点哪个。
