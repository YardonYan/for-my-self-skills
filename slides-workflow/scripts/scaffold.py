#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""为一份幻灯片项目生成骨架目录与三份模板文件。

用法:
    python scripts/scaffold.py <项目目录> [--full] [--force]

生成结构:
    <项目目录>/
    ├── brief.md          简报（--full 用精致型模板，默认简洁型）
    ├── page-script.md    逐页稿（含两页示例字段）
    ├── style-spec.md     风格说明
    ├── assets/
    │   ├── raw/          原始资料
    │   ├── final/        正式素材
    │   └── reference/    风格参考
    └── out/              成品与备用稿

只依赖 Python 标准库，不联网。
"""
import argparse
import shutil
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
ASSETS = SKILL_DIR / "assets"

DIRS = [
    "assets/raw",
    "assets/final",
    "assets/reference",
    "out",
]

FILES = [
    ("brief-simple.md", "brief.md"),
    ("brief-full.md", "brief-full.md"),
    ("page-script.md", "page-script.md"),
    ("style-spec.md", "style-spec.md"),
]

README = """# 幻灯片项目

流程见 slides-workflow 的 SKILL.md，四个阶段：

1. 采集与逐页稿 —— 填 `{brief}`，写 `page-script.md`
2. 风格说明 —— 参考图放 `assets/reference/`，产出 `style-spec.md`
3. 选形态制作 —— 成品与 PDF 备用稿放 `out/`
4. 局部打磨 —— 按页改，检查清单全过再交付

## 当前状态

- [ ] 简报已确认
- [ ] 逐页稿已通过 `verify.py script`
- [ ] 风格方向已选定
- [ ] 三页样稿已确认（可编辑 PPTX 模式）
- [ ] 整套已完成
- [ ] 检查清单全过

## 命令

```bash
python <skill>/scripts/verify.py script .
python <skill>/scripts/verify.py assets .
```
"""


def build(target: Path, full: bool, force: bool) -> int:
    if target.exists() and any(target.iterdir()) and not force:
        print(f"目录非空，已中止：{target}")
        print("确认要覆盖模板文件时加 --force（只覆盖模板，不动素材）")
        return 1

    for d in DIRS:
        (target / d).mkdir(parents=True, exist_ok=True)

    created, skipped = [], []
    pairs = [p for p in FILES if (full or p[0] != "brief-full.md")]
    for src_name, dst_name in pairs:
        src = ASSETS / src_name
        dst = target / dst_name
        if not src.is_file():
            print(f"模板缺失：{src}")
            return 1
        if dst.exists() and not force:
            skipped.append(dst.name)
            continue
        shutil.copyfile(src, dst)
        created.append(dst.name)

    readme = target / "README.md"
    if not readme.exists() or force:
        readme.write_text(
            README.format(brief="brief-full.md" if full else "brief.md"),
            encoding="utf-8",
            newline="\n",
        )
        created.append("README.md")

    print(f"项目已就绪：{target}")
    for name in created:
        print(f"  新建  {name}")
    for name in skipped:
        print(f"  跳过  {name}（已存在）")
    print("\n素材目录：assets/raw、assets/final、assets/reference、out")
    print("下一步：填简报 → 写逐页稿 → python scripts/verify.py script <项目目录>")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="生成幻灯片项目骨架")
    ap.add_argument("target", help="项目目录，不存在会自动创建")
    ap.add_argument("--full", action="store_true", help="同时生成精致型简报模板")
    ap.add_argument("--force", action="store_true", help="覆盖已存在的模板文件")
    args = ap.parse_args()
    return build(Path(args.target).expanduser(), args.full, args.force)


if __name__ == "__main__":
    sys.exit(main())
