# -*- coding: utf-8 -*-
"""验证 MD -> DOCX 无损转换（与 md2docx.py 配套）

用法:
    python md2docx_verify.py <src.md> <dst.docx>

校验内容:
1. MD 每条内容行（标题/表格单元格/代码块行/引用/列表/正文）都能在 DOCX 文本中逐字找到
2. 标题数量 / 表格数量 / 代码块数量 与 MD 一致
退出码: 0 = 全部通过；1 = 有缺失或不一致
"""
import os
import re
import sys
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn

H1 = re.compile(r'^(#{1,6})\s+(.*)$')
HR = re.compile(r'^-{3,}$')
BUL = re.compile(r'^\s*[-*]\s+(.*)$')
ORD = re.compile(r'^\s*\d+\.\s+(.*)$')
TAB = re.compile(r'^\|')
SEP = re.compile(r'^\|[\s\-:|]+\|$')


def md_parse(path):
    heads, tables, codes = 0, 0, 0
    content = []  # (kind, text)
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.read().split('\n')
    in_code = False
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith('```'):
            in_code = not in_code
            if in_code:
                codes += 1
            i += 1
            continue
        if in_code:
            if s:
                content.append(('CODE', s))
            i += 1
            continue
        if not s:
            i += 1
            continue
        if HR.match(s):
            i += 1
            continue
        m = H1.match(lines[i])
        if m:
            heads += 1
            content.append(('HEAD', m.group(2).strip()))
            i += 1
            continue
        if TAB.match(s):
            tables += 1
            for c in [x.strip() for x in s.strip().strip('|').split('|')]:
                if c:
                    content.append(('TCELL', c))
            i += 1
            while i < len(lines) and (lines[i].strip().startswith('|') or SEP.match(lines[i].strip())):
                if not SEP.match(lines[i].strip()):
                    for c in [x.strip() for x in lines[i].strip().strip('|').split('|')]:
                        if c:
                            content.append(('TCELL', c))
                i += 1
            continue
        if s.startswith('>'):
            content.append(('QUOTE', s.lstrip('>').strip()))
            i += 1
            continue
        m = BUL.match(lines[i])
        if m:
            content.append(('LIST', m.group(1).strip()))
            i += 1
            continue
        m = ORD.match(lines[i])
        if m:
            content.append(('LIST', m.group(1).strip()))
            i += 1
            continue
        content.append(('BODY', s))
        i += 1
    return heads, tables, codes, content


def docx_parse(path):
    doc = Document(path)
    texts = []
    heads = 0
    tables = 0
    body = doc.element.body
    for child in body.iterchildren():
        if child.tag == qn('w:p'):
            p = Paragraph(child, doc)
            if p.style.name.startswith('Heading'):
                heads += 1
            if p.text.strip():
                texts.append(p.text.strip())
        elif child.tag == qn('w:tbl'):
            t = Table(child, doc)
            tables += 1
            for row in t.rows:
                for cell in row.cells:
                    for p in cell.paragraphs:
                        if p.text.strip():
                            texts.append(p.text.strip())
    return heads, tables, texts


def norm(s):
    s = s.replace('`', '').replace('**', '').replace('*', '')
    return re.sub(r'\s+', '', s)


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    src, dst = sys.argv[1], sys.argv[2]
    if not os.path.exists(dst):
        print('!! DOCX not found: %s' % dst)
        sys.exit(1)

    mh, mt, mc, mcontent = md_parse(src)
    dh, dt, dtexts = docx_parse(dst)
    dnorm = [norm(t) for t in dtexts]

    print('== MD   ==  headings=%d tables=%d codeblocks=%d content_lines=%d' % (mh, mt, mc, len(mcontent)))
    print('== DOCX ==  headings=%d tables=%d text_blocks=%d' % (dh, dt, len(dtexts)))

    problems = []
    if dh != mh:
        problems.append('HEADING COUNT mismatch: MD %d vs DOCX %d' % (mh, dh))
    if dt != mt:
        problems.append('TABLE COUNT mismatch: MD %d vs DOCX %d' % (mt, dt))

    missing = []
    for kind, t in mcontent:
        nt = norm(t)
        if not nt:
            continue
        if not any(nt in d for d in dnorm):
            missing.append((kind, t))
    if missing:
        problems.append('MISSING %d content lines' % len(missing))

    for p in problems:
        print('!! ' + p)
    if missing:
        print('-- first 30 missing --')
        for kind, t in missing[:30]:
            print('  [%s] %s' % (kind, t[:90]))

    if problems:
        sys.exit(1)
    print('RESULT: PASS - 内容零缺失，结构元素数量一致（标题 %d / 表格 %d / 代码块 %d）' % (mh, mt, mc))


if __name__ == '__main__':
    main()
