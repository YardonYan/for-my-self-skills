#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验幻灯片项目：逐页稿字段完整性，或素材与逐页稿的对应关系。

用法:
    python scripts/verify.py script <项目目录> [--assets-dir <目录>]
    python scripts/verify.py assets <项目目录>

script 检查:
    1. 页码从第 1 页连续，不重复不跳号
    2. 每页 7 个字段齐全且字段名拼写正确
    3. 标题、想表达的意思、屏幕文字、建议布局 不允许为空
    4. 统计「待补充」缺口
    5. 给了 --assets-dir 时，检查引用的图片文件是否存在

assets 检查:
    1. assets/raw、assets/final、assets/reference 三个目录是否存在
    2. 逐页稿引用的图片是否都在 assets/final
    3. final 里有没有没被任何一页引用的文件
    4. out/ 下的数字前缀图片是否从 01 连续（图片稿模式）

输出 RESULT: PASS 时退出码为 0，否则为 1。只依赖 Python 标准库。
"""
import argparse
import re
import sys
from pathlib import Path

FIELDS = [
    "标题",
    "想表达的意思",
    "屏幕文字",
    "数据与来源",
    "图片素材",
    "建议布局",
    "演讲备注",
]
STRICT_FIELDS = {"标题", "想表达的意思", "屏幕文字", "建议布局"}
IMAGE_EXT = (".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif", ".avif")

RE_PAGE = re.compile(r"^##\s*第\s*(\d+)\s*页\s*$")
RE_FIELD = re.compile(r"^-\s*\*\*(.+?)\*\*\s*[：:]\s*(.*)$")
RE_IMG_REF = re.compile(r"`([^`]+?\.(?:png|jpg|jpeg|webp|svg|gif|avif))`", re.I)
RE_NUM_FILE = re.compile(r"^(\d{2,})_.+\.(?:png|jpg|jpeg|webp)$", re.I)


def setup_stdout():
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


def parse_script(path):
    """返回 (pages, errors)，pages 为 [{no, fields:{name:content}}]。"""
    if not path.is_file():
        return [], [f"找不到逐页稿：{path}"]

    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    pages, errors = [], []
    cur = None
    cur_field = None

    for line in lines:
        m = RE_PAGE.match(line)
        if m:
            cur = {"no": int(m.group(1)), "fields": {}}
            pages.append(cur)
            cur_field = None
            continue

        if line.startswith("## "):
            cur = None
            cur_field = None
            continue

        if cur is None:
            continue

        m = RE_FIELD.match(line)
        if m:
            name = m.group(1).strip()
            cur["fields"].setdefault(name, m.group(2).strip())
            cur_field = name
            continue

        if cur_field and line.strip():
            prev = cur["fields"].get(cur_field, "")
            cur["fields"][cur_field] = (prev + "\n" + line.strip()).strip()

    if not pages:
        errors.append("没有解析到任何「## 第 N 页」，检查标题格式")
    return pages, errors


def check_script(project, assets_dir=None):
    script_path = project / "page-script.md"
    pages, errors = parse_script(script_path)
    warns = []

    if pages:
        nums = [p["no"] for p in pages]
        if nums != list(range(1, len(nums) + 1)):
            dup = sorted({n for n in nums if nums.count(n) > 1})
            if dup:
                errors.append(f"页码重复：{dup}")
            expect = list(range(1, len(nums) + 1))
            miss = [n for n in expect if n not in nums]
            extra = [n for n in nums if n > len(nums)]
            if miss:
                errors.append(f"页码缺失：{miss}")
            if extra:
                errors.append(f"页码超出范围：{extra}")
            if not dup and not miss and not extra:
                errors.append(f"页码顺序不对：{nums}")

    todo = []
    referenced = {}
    total_fields = 0

    for page in pages:
        no = page["no"]
        fields = page["fields"]
        total_fields += len(fields)

        unknown = [f for f in fields if f not in FIELDS]
        if unknown:
            errors.append(f"第 {no} 页 字段名不认识：{'、'.join(unknown)}（7 个标准字段见 references/page-script.md）")

        for name in FIELDS:
            if name not in fields:
                errors.append(f"第 {no} 页 缺字段：{name}")
                continue
            value = fields[name].strip()
            if not value:
                if name in STRICT_FIELDS:
                    errors.append(f"第 {no} 页 {name} 为空")
                else:
                    warns.append(f"第 {no} 页 {name} 为空")
                continue
            if "待补充" in value:
                todo.append((no, name))
            if name == "图片素材":
                refs = RE_IMG_REF.findall(value)
                if refs:
                    referenced[no] = refs

    if assets_dir is not None:
        for no, refs in sorted(referenced.items()):
            for ref in refs:
                if not (assets_dir / ref).is_file():
                    errors.append(f"第 {no} 页 引用的图片不存在：{ref}（查找于 {assets_dir}）")

    print(f"逐页稿：{script_path}")
    print(f"页数：{len(pages)}    字段总数：{total_fields}    待补充：{len(todo)}")
    if todo:
        for no, name in todo:
            print(f"  待补充  第 {no} 页 {name}")
    for w in warns:
        print(f"  [WARN]  {w}")
    for e in errors:
        print(f"  [ERROR] {e}")
    print("RESULT: PASS" if not errors else "RESULT: FAIL")
    return 0 if not errors else 1


def check_assets(project):
    errors, warns = [], []
    dirs = ["assets/raw", "assets/final", "assets/reference"]
    for d in dirs:
        if not (project / d).is_dir():
            errors.append(f"缺目录：{d}")

    final_dir = project / "assets" / "final"
    pages, parse_errors = parse_script(project / "page-script.md")
    errors.extend(parse_errors)

    referenced = set()
    for page in pages:
        value = page["fields"].get("图片素材", "")
        for ref in RE_IMG_REF.findall(value):
            referenced.add(ref)
            if final_dir.is_dir() and not (final_dir / ref).is_file():
                errors.append(f"第 {page['no']} 页 引用的图片不存在：{ref}")

    if final_dir.is_dir():
        on_disk = {p.name for p in final_dir.iterdir()
                   if p.is_file() and p.suffix.lower() in IMAGE_EXT}
        unused = sorted(on_disk - referenced)
        if unused:
            warns.append(f"final 里有 {len(unused)} 个文件未被逐页稿引用：{', '.join(unused[:8])}"
                         + (" …" if len(unused) > 8 else ""))

    out_dir = project / "out"
    if out_dir.is_dir():
        nums = []
        for p in out_dir.iterdir():
            m = RE_NUM_FILE.match(p.name)
            if m:
                nums.append(int(m.group(1)))
        if nums:
            nums.sort()
            expect = list(range(1, len(nums) + 1))
            if nums != expect:
                errors.append(f"out/ 图片序号不连续：{nums}")

    print(f"项目：{project}")
    print(f"逐页稿引用图片：{len(referenced)} 个")
    for w in warns:
        print(f"  [WARN]  {w}")
    for e in errors:
        print(f"  [ERROR] {e}")
    print("RESULT: PASS" if not errors else "RESULT: FAIL")
    return 0 if not errors else 1


def main():
    setup_stdout()
    ap = argparse.ArgumentParser(description="校验幻灯片项目")
    ap.add_argument("stage", choices=["script", "assets"], help="script=逐页稿，assets=素材")
    ap.add_argument("project", help="项目目录")
    ap.add_argument("--assets-dir", default=None, help="script 阶段额外校验图片时的素材目录")
    args = ap.parse_args()

    project = Path(args.project).expanduser().resolve()
    if not project.is_dir():
        print(f"[ERROR] 项目目录不存在：{project}")
        print("RESULT: FAIL")
        return 1

    if args.stage == "script":
        assets_dir = Path(args.assets_dir).expanduser().resolve() if args.assets_dir else None
        return check_script(project, assets_dir)
    return check_assets(project)


if __name__ == "__main__":
    sys.exit(main())
