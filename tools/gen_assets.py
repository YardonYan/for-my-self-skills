#!/usr/bin/env python3
"""生成 README 用的矢量配图。

零依赖，只输出 SVG 文本。运行：
    python tools/gen_assets.py

产物落在 assets/：
    cover.svg             封面（同时导出 1280x640 PNG 供社交预览）
    flow-choose-skill.svg 选型流程图
    skill-anatomy.svg     单个 Skill 的四件套结构图
    category-bar.svg      四类占比条

配色沿用 README 徽章色系，四类各一色，仅用于分类标识，不作装饰。
"""

import shutil
import subprocess
import tempfile
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"

INK = "#0B1220"
INK_SOFT = "#1E293B"
INK_LINE = "#2A3548"
PAPER = "#FAFAF7"
SURFACE = "#FFFFFF"
FG = "#1A1916"
MUTED = "#6B6964"
BORDER = "#E4E0D8"
ON_DARK = "#F5F5F2"
ON_DARK_MUTED = "#98A2B3"

CATS = [
    {
        "cn": "网页与前端",
        "color": "#2563EB",
        "when": ["要产出界面，", "或修界面上看得见的问题"],
        "skills": [
            "html-skill-effectiveness",
            "html-designer__skillhub",
            "mobile-design-spec",
            "markdown-renderer-fix",
        ],
    },
    {
        "cn": "文档与交付",
        "color": "#0F766E",
        "when": ["要把内容变成", "别人能直接打开的文件"],
        "skills": ["md-to-docx", "html-to-pdf", "slides-workflow", "wechat-mp-publish"],
    },
    {
        "cn": "工程流程与质量",
        "color": "#B45309",
        "when": ["要管怎么做，", "也要管做得对不对"],
        "skills": [
            "code-review",
            "dev-workflow",
            "task-skill-orchestrator",
            "merge-dev-docs",
            "skill-authoring",
            "self-improving-agent",
        ],
    },
    {
        "cn": "写作与表达",
        "color": "#6D28D9",
        "when": ["要把想法写成", "别人读得懂的东西"],
        "skills": ["tech-blog-generator", "yardon-writer", "prompt-optimizer"],
    },
]

SANS = "PingFang SC, Microsoft YaHei, Noto Sans SC, system-ui, sans-serif"
SERIF = "Iowan Old Style, Charter, Georgia, Times New Roman, serif"
MONO = "JetBrains Mono, SF Mono, Menlo, Consolas, monospace"

TOTAL = sum(len(c["skills"]) for c in CATS)


def has_cjk(s):
    return any("\u4e00" <= ch <= "\u9fff" or "\u3000" <= ch <= "\u303f" for ch in s)


def est_width(s, size):
    """粗略估算文本宽度：中文按 1em，西文按 0.55em。"""
    w = 0.0
    for ch in s:
        w += size * (1.0 if has_cjk(ch) else 0.55)
    return w


def t(x, y, s, size, fill, family=SANS, weight=400, anchor="start", ls=None, opacity=None):
    """一行文本。

    等宽与衬线字体族通常不含中文字形，遇到中文自动退回无衬线，避免栅格化出豆腐块。
    """
    if has_cjk(s) and family in (MONO, SERIF):
        family = SANS
    attrs = [f'x="{x}"', f'y="{y}"', f'font-family="{family}"', f'font-size="{size}"']
    if weight != 400:
        attrs.append(f'font-weight="{weight}"')
    if anchor != "start":
        attrs.append(f'text-anchor="{anchor}"')
    if ls is not None:
        attrs.append(f'letter-spacing="{ls}"')
    if opacity is not None:
        attrs.append(f'opacity="{opacity}"')
    attrs.append(f'fill="{fill}"')
    return f"<text {' '.join(attrs)}>{escape(s)}</text>"


def rect(x, y, w, h, fill, rx=0, stroke=None, sw=1, opacity=None):
    attrs = [f'x="{x}"', f'y="{y}"', f'width="{w}"', f'height="{h}"', f'rx="{rx}"']
    attrs.append(f'fill="{fill}"')
    if stroke:
        attrs.append(f'stroke="{stroke}"')
        attrs.append(f'stroke-width="{sw}"')
    if opacity is not None:
        attrs.append(f'opacity="{opacity}"')
    return f"<rect {' '.join(attrs)}/>"


def line(x1, y1, x2, y2, stroke, sw=1, dash=None, cap="round"):
    attrs = [
        f'x1="{x1}"', f'y1="{y1}"', f'x2="{x2}"', f'y2="{y2}"',
        f'stroke="{stroke}"', f'stroke-width="{sw}"', f'stroke-linecap="{cap}"',
    ]
    if dash:
        attrs.append(f'stroke-dasharray="{dash}"')
    return f"<line {' '.join(attrs)}/>"


def arrow_down(cx, y_from, y_to, color):
    head = 7
    return (
        f'<line x1="{cx}" y1="{y_from}" x2="{cx}" y2="{y_to - head}" '
        f'stroke="{color}" stroke-width="1.6" stroke-linecap="round"/>'
        f'<path d="M{cx - 5} {y_to - head - 1} L{cx + 5} {y_to - head - 1} L{cx} {y_to} Z" fill="{color}"/>'
    )


def svg(width, height, title, desc, body):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title)}">\n'
        f"<title>{escape(title)}</title>\n<desc>{escape(desc)}</desc>\n"
        + "\n".join(body)
        + "\n</svg>\n"
    )


# ---------------------------------------------------------------- cover

def cover():
    W, H = 1280, 640
    b = [rect(0, 0, W, H, INK)]

    # 顶边色带：宽度按四类技能数占比
    x = 0.0
    for c in CATS:
        w = W * len(c["skills"]) / TOTAL
        b.append(rect(round(x, 2), 0, round(w, 2), 8, c["color"]))
        x += w

    # 左栏
    b.append(t(80, 210, "AGENT SKILLS  ·  MIT  ·  2026", 12, ON_DARK_MUTED, MONO, ls="0.16em"))
    b.append(t(78, 306, "Yardon Skills", 76, ON_DARK, SERIF, 500, ls="-0.025em"))
    b.append(t(80, 358, f"{TOTAL} 个在真实项目里用过、整理出来的技能", 23, "#D5D9E0"))
    b.append(t(80, 392, "按用途分四类，装进任何支持 Agent Skills 的助手", 17, ON_DARK_MUTED))

    cx = 80
    for c in CATS:
        b.append(f'<circle cx="{cx + 4}" cy="{432}" r="4" fill="{c["color"]}"/>')
        b.append(t(cx + 16, 436, c["cn"], 15, "#B9C0CC"))
        b.append(t(cx + 28 + est_width(c["cn"], 15), 436, str(len(c["skills"])), 15, "#A8B2C4", MONO))
        cx += 28 + est_width(c["cn"], 15) + 14 + 22

    b.append(line(80, 480, 560, 480, INK_LINE, 1, cap="butt"))
    b.append(t(80, 522, "github.com/YardonYan/for-my-self-skills", 13, "#6B7688", MONO))

    # 书架：17 本等高的书，颜色按分类分组，不用随机高度假装数据
    count = TOTAL
    spine_w, gap, group_gap, shelf_h = 20, 5, 16, 196
    span = count * spine_w + (count - 1) * gap + (len(CATS) - 1) * group_gap
    sx = 700 + (520 - span) / 2
    base = 480
    for c in CATS:
        for _ in c["skills"]:
            b.append(rect(round(sx, 2), base - shelf_h, spine_w, shelf_h, INK_SOFT))
            b.append(rect(round(sx, 2), base - shelf_h, 1.5, shelf_h, "#33405C"))
            b.append(rect(round(sx, 2), base - shelf_h, spine_w, 9, c["color"]))
            sx += spine_w + gap
        sx += group_gap - gap
    b.append(rect(700, base, 520, 3, INK_LINE, rx=1.5))

    return svg(
        W, H, "Yardon Skills 封面",
        f"深色封面，标题 Yardon Skills，副标题 {TOTAL} 个技能分四类；"
        "右侧为 17 本等高的书脊，按四类着色。",
        b,
    )


# ---------------------------------------------------------------- flow

def flow():
    W = 1200
    b = [rect(0, 0, W, 760, PAPER)]
    b.append(t(60, 84, "不知道用哪个？按产出走一遍", 36, FG, SANS, 600, ls="-0.01em"))
    b.append(t(60, 118, f"{TOTAL} 个技能分四类。先问自己要产出什么，再看这一类里哪个对得上。", 15, MUTED))

    b.append(rect(470, 158, 260, 48, INK, rx=24))
    b.append(t(600, 188, "你的任务是什么？", 16, ON_DARK, SANS, 500, anchor="middle"))

    col_w, gap_x, left = 252, 24, 60
    centers = [left + i * (col_w + gap_x) + col_w / 2 for i in range(4)]

    bus_y = 236
    b.append(line(600, 206, 600, bus_y, "#C9C4B8", 1.6, cap="butt"))
    b.append(line(centers[0], bus_y, centers[-1], bus_y, "#C9C4B8", 1.6, cap="butt"))
    for cx in centers:
        b.append(arrow_down(cx, bus_y, 288, "#C9C4B8"))

    card_top = 288
    sep_y = card_top + 152
    items_y = sep_y + 30
    step = 27
    tallest = max(len(c["skills"]) for c in CATS)
    card_bottom = items_y + (tallest - 1) * step + 26

    for c, cx in zip(CATS, centers):
        x0 = cx - col_w / 2
        color = c["color"]

        b.append(rect(x0, card_top, col_w, 44, color, rx=8))
        b.append(t(x0 + 16, card_top + 28, c["cn"], 15, "#FFFFFF", SANS, 600))
        b.append(t(x0 + col_w - 16, card_top + 28, str(len(c["skills"])), 15, "#FFFFFF", MONO, 600, anchor="end"))

        b.append(rect(x0, card_top + 52, col_w, card_bottom - card_top - 52, SURFACE, rx=8, stroke=BORDER, sw=1.5))

        b.append(t(x0 + 16, card_top + 80, "什么时候用", 11, MUTED, SANS, ls="0.08em"))
        for j, ln in enumerate(c["when"]):
            b.append(t(x0 + 16, card_top + 104 + j * 22, ln, 13.5, FG))

        b.append(line(x0 + 16, sep_y, x0 + col_w - 16, sep_y, BORDER, 1, cap="butt"))
        b.append(t(x0 + 16, sep_y + 22, "这一类里", 11, MUTED, SANS, ls="0.08em"))

        for j, s in enumerate(c["skills"]):
            yy = items_y + 20 + j * step
            b.append(f'<circle cx="{x0 + 21}" cy="{yy - 4}" r="2.5" fill="{color}"/>')
            b.append(t(x0 + 33, yy, s, 12.5, FG, MONO))

    b.append(t(60, card_bottom + 66, "还是不确定：先读该技能 SKILL.md 的「何时用 / 何时不用」两节，或者直接把任务描述贴给助手，让它自己挑。", 13, MUTED))
    return svg(W, 760, "选型流程图", "从任务类型分四路，指向对应的技能分类与具体技能名。", b)


# ---------------------------------------------------------------- anatomy

def anatomy():
    W, H = 1000, 540
    b = [rect(0, 0, W, H, PAPER)]
    b.append(t(60, 82, "一个 Skill 的四件套", 34, FG, SANS, 600, ls="-0.01em"))
    b.append(t(60, 116, "目录扁平，每个技能自包含。缺任何一件都不收。", 15, MUTED))

    rows = [
        ("SKILL.md", "#B45309", "主规则", "触发条件、执行流程、边界、反模式。Agent 的加载入口"),
        ("README.md", "#0F766E", "中文说明", "解决什么、什么时候用、内含什么、边界在哪"),
        ("README.en.md", "#0F766E", "English", "与中文版章节一一对应，不是机器翻译腔"),
        ("LICENSE", "#2563EB", "许可", "与仓库主协议一致，第三方素材在 NOTICE 单独注明"),
        ("references/", "#6D28D9", "可选", "按需加载的细则与模板，不塞进主文件"),
    ]
    top, step = 186, 66
    b.append(line(78, top, 78, top + step * (len(rows) - 1), BORDER, 2, cap="butt"))

    for i, (name, color, tag, desc) in enumerate(rows):
        y = top + i * step
        b.append(f'<circle cx="78" cy="{y}" r="6" fill="{PAPER}" stroke="{color}" stroke-width="2.5"/>')
        b.append(t(108, y + 6, name, 17, FG, MONO, 600))

        cw = est_width(tag, 11) + 18
        b.append(rect(300, y - 11, round(cw, 1), 22, color, rx=4, opacity=0.12))
        b.append(t(309, y + 4, tag, 11, color, SANS, 500))

        b.append(t(470, y + 6, desc, 14, MUTED))

    b.append(line(60, 496, 940, 496, BORDER, 1, cap="butt"))
    b.append(t(60, 526, "复制整个目录就能独立使用：不依赖仓库其他路径，也不依赖网络。", 13, MUTED))
    return svg(W, H, "Skill 结构图", "SKILL.md、README.md、README.en.md、LICENSE 四件套，references 为可选。", b)


# ---------------------------------------------------------------- category bar

def category_bar():
    W, H = 1200, 180
    b = [rect(0, 0, W, H, PAPER)]
    b.append(t(60, 44, "四类构成", 16, FG, SANS, 600))
    b.append(t(60 + est_width("四类构成", 16) + 16, 44, f"{TOTAL} 个技能", 13, MUTED, MONO))

    x, bar_y, bar_h = 60, 72, 20
    width = W - 120
    for i, c in enumerate(CATS):
        w = width * len(c["skills"]) / TOTAL
        b.append(rect(round(x, 2), bar_y, round(w, 2), bar_h, c["color"]))
        b.append(t(round(x + w / 2, 2), bar_y + 15, str(len(c["skills"])), 13, "#FFFFFF", MONO, 600, anchor="middle"))
        x += w
        if i < len(CATS) - 1:
            b.append(rect(round(x - 0.75, 2), bar_y, 1.5, bar_h, PAPER))

    lx = 60
    for c in CATS:
        b.append(f'<circle cx="{lx + 4}" cy="{136}" r="4" fill="{c["color"]}"/>')
        b.append(t(lx + 16, 141, c["cn"], 13, FG))
        lx += 16 + est_width(c["cn"], 13) + 36
    return svg(W, H, "四类构成", "四个分类的技能数量占比：4 / 4 / 6 / 3。", b)


def main():
    OUT.mkdir(exist_ok=True)
    files = {
        "cover.svg": cover(),
        "flow-choose-skill.svg": flow(),
        "skill-anatomy.svg": anatomy(),
        "category-bar.svg": category_bar(),
    }
    for name, content in files.items():
        (OUT / name).write_text(content, encoding="utf-8")
        print(f"写出 assets/{name}  {len(content)} bytes")

    rasterize_cover()


def rasterize_cover():
    """把 cover.svg 导成 1280x640 PNG，供 GitHub 社交预览使用。

    rsvg 的 Pango 不解析逗号分隔的字体族列表，会把整串当族名而回退到默认字体，
    所以栅格化时换成单族名；仓库里保存的 SVG 仍保留标准 CSS 列表。
    """
    magick = shutil.which("magick") or shutil.which("rsvg-convert")
    if not magick:
        print("跳过 PNG：未找到 magick 或 rsvg-convert")
        return

    src = (OUT / "cover.svg").read_text(encoding="utf-8")
    for css_list, single in ((SANS, "Microsoft YaHei"), (SERIF, "Georgia"), (MONO, "Consolas")):
        src = src.replace(f'font-family="{css_list}"', f'font-family="{single}"')

    with tempfile.TemporaryDirectory() as tmp:
        tmp_svg = Path(tmp) / "cover.svg"
        tmp_svg.write_text(src, encoding="utf-8")
        target = OUT / "cover-1280x640.png"
        try:
            subprocess.run([magick, str(tmp_svg), str(target)], check=True, capture_output=True, timeout=120)
            print(f"写出 assets/{target.name}  {target.stat().st_size} bytes")
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
            print(f"PNG 导出失败：{exc}")


if __name__ == "__main__":
    main()
