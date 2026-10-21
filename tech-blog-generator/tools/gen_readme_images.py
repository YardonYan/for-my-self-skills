# -*- coding: utf-8 -*-
"""为 tech-blog-generator 生成 README 配图。

字体约定：中文一律走 msyh / msyhbd，Consolas 只用于纯英文与代码片段，
否则中文字形会渲染成方块。
"""
import os

from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")

REG = "C:/Windows/Fonts/msyh.ttc"
BOLD = "C:/Windows/Fonts/msyhbd.ttc"
MONO = "C:/Windows/Fonts/consola.ttf"

BG_TOP = (13, 20, 34)
BG_BOT = (24, 38, 63)
CARD = (28, 44, 74)
CARD2 = (35, 54, 88)
LINE = (62, 88, 130)
TXT = (255, 255, 255)
SUB = (150, 166, 188)
DIM = (104, 120, 145)

BLUE = (79, 195, 247)
PURPLE = (167, 139, 250)
MINT = (110, 231, 183)
AMBER = (245, 176, 66)
PAPER = (250, 250, 247)
INK = (26, 25, 22)
HAIRLINE = (232, 229, 223)
MUTED = (107, 105, 100)


def f(path, size):
    return ImageFont.truetype(path, size)


def vgrad(size, c1, c2):
    w, h = size
    strip = Image.new("RGB", (1, h))
    d = ImageDraw.Draw(strip)
    for y in range(h):
        t = y / max(h - 1, 1)
        d.point((0, y), fill=tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3)))
    return strip.resize((w, h))


def card(draw, box, radius=16, fill=CARD, outline=LINE, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def arrow(draw, x1, y, x2, color=LINE, head=12, w=4):
    draw.line([x1, y, x2 - head, y], fill=color, width=w)
    draw.polygon([(x2, y), (x2 - head - 2, y - 9), (x2 - head - 2, y + 9)], fill=color)


def hero():
    W, H = 1500, 540
    img = vgrad((W, H), BG_TOP, BG_BOT)
    d = ImageDraw.Draw(img)

    d.text((70, 52), "把代码和文档，变成读得下去的技术博客", font=f(BOLD, 42), fill=TXT)
    d.text((70, 114), "Transform source code and docs into production-ready technical blog posts",
           font=f(REG, 22), fill=SUB)

    TY0, TY1 = 186, 464

    # ── 左：输入 ──────────────────────────────────────────────────
    d.text((70, TY0 - 32), "输入  INPUT", font=f(BOLD, 20), fill=BLUE)
    files = [("main.go", BLUE), ("worker.go", BLUE), ("design.md", PURPLE)]
    for i, (name, color) in enumerate(files):
        y = TY0 + i * 66
        card(d, [70, y, 310, y + 56], radius=12, fill=CARD2, outline=color, width=2)
        d.rounded_rectangle([88, y + 18, 100, y + 38], radius=3, fill=color)
        d.text((114, y + 15), name, font=f(MONO, 18), fill=TXT)

    arrow(d, 322, (TY0 + TY1) / 2, 396, color=LINE, w=3, head=11)

    # ── 中：引擎 ─────────────────────────────────────────────────
    card(d, [408, TY0 - 4, 908, TY1], radius=18, fill=CARD, outline=LINE, width=2)
    d.text((436, TY0 + 14), "Skill 引擎  ENGINE", font=f(BOLD, 21), fill=AMBER)

    rows = [("6 种文体模板", "Tutorial · Deep Dive · Comparison · Postmortem · Quick Tip · Architecture", BLUE),
            ("21 条写作规则", "12 canonical rules + 9 AI-specific rules, severity-graded", AMBER),
            ("3 遍自审流程", "Structure audit → Sentence audit → Reader perspective audit", MINT)]
    for i, (cn, en, color) in enumerate(rows):
        y = TY0 + 54 + i * 76
        card(d, [436, y, 880, y + 64], radius=12, fill=CARD2, outline=color, width=2)
        d.rectangle([436, y, 442, y + 64], fill=color)
        d.text((462, y + 12), cn, font=f(BOLD, 20), fill=TXT)
        d.text((462, y + 40), en, font=f(REG, 14), fill=DIM)

    arrow(d, 920, (TY0 + TY1) / 2, 996, color=LINE, w=3, head=11)

    # ── 右：成稿 ─────────────────────────────────────────────────
    d.text((1008, TY0 - 32), "成稿  DELIVERABLE", font=f(BOLD, 20), fill=MINT)
    d.rounded_rectangle([1008, TY0, 1430, TY1], radius=16, fill=PAPER, outline=HAIRLINE, width=2)
    d.text((1032, TY0 + 18), "DEEP DIVE · 8 min · zh", font=f(MONO, 13), fill=MUTED)
    d.text((1032, TY0 + 44), "缓冲 Channel 如何", font=f(BOLD, 23), fill=INK)
    d.text((1032, TY0 + 76), "实现天然背压", font=f(BOLD, 23), fill=INK)

    for i, w in enumerate((356, 322, 366, 258)):
        d.rounded_rectangle([1032, TY0 + 122 + i * 20, 1032 + w, TY0 + 130 + i * 20],
                            radius=4, fill=HAIRLINE)

    d.rounded_rectangle([1032, TY0 + 212, 1406, TY0 + 258], radius=8, fill=(30, 32, 38))
    d.text((1048, TY0 + 220), "func Dispatch(jobs <-chan Job) {", font=f(MONO, 13), fill=(226, 226, 226))
    d.text((1048, TY0 + 238), "    queue := make(chan Job, 100)", font=f(MONO, 13), fill=MINT)

    img.save(os.path.join(OUT, "hero.png"))
    print("hero.png")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    hero()
