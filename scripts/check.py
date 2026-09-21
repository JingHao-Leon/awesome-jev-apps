#!/usr/bin/env python3
"""校验 awesome-jev-apps 仓库的一致性：data/projects.json ↔ README.md。

检查项：
1. 每个条目字段完整（name / url / category / description）
2. URL 全部为 https 且不重复
3. 每个条目 URL 都出现在 README 中
4. README 中的分类统计数字与数据文件一致（合计 + 五个分类）

用法：python scripts/check.py  （退出码非 0 表示不一致）
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "projects.json"
README = ROOT / "README.md"

CATEGORIES = ["优质开源应用", "SDK 与集成", "官方资源", "教程与评测", "社区讨论"]

errors: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    readme = README.read_text(encoding="utf-8")
    entries = data["entries"]

    seen: set[str] = set()
    for i, e in enumerate(entries):
        name = e.get("name", f"<条目 {i}>")
        for field in ("name", "url", "category", "description"):
            if field not in e:
                fail(f"[{name}] 缺少字段: {field}")
        if e.get("category") not in CATEGORIES:
            fail(f"[{name}] 未知分类: {e.get('category')}")
        url = e.get("url") or ""
        if not url.startswith("https://"):
            fail(f"[{name}] URL 必须是 https: {url}")
            continue
        if url in seen:
            fail(f"URL 重复: {url}")
        seen.add(url)
        if url not in readme:
            fail(f"[{name}] URL 未出现在 README 中: {url}")

    counts = {c: sum(1 for e in entries if e["category"] == c) for c in CATEGORIES}
    total = len(entries)

    declared_meta = data.get("meta", {}).get("entry_count")
    if declared_meta is not None and declared_meta != total:
        fail(f"meta.entry_count={declared_meta} 与实际条目数 {total} 不符")

    m = re.search(r"收录 \*\*(\d+)\*\* 条资源", readme)
    if not m:
        fail("README 缺少统计行「收录 **N** 条资源」")
    elif int(m.group(1)) != total:
        fail(f"README 统计合计 {m.group(1)} ≠ 数据文件 {total}")

    for cat in CATEGORIES:
        m = re.search(re.escape(cat) + r"\]\(#[^)]*\)\s*\*\*(\d+)\*\*", readme)
        if not m:
            fail(f"README 统计行缺少分类「{cat}」或格式不符")
        elif int(m.group(1)) != counts[cat]:
            fail(f"分类「{cat}」README 计数 {m.group(1)} ≠ 数据文件 {counts[cat]}")

    if errors:
        print(f"✗ {len(errors)} 个问题：")
        for msg in errors:
            print(f"  - {msg}")
        return 1

    print(f"✓ 一致性校验通过：{total} 条条目，" + "，".join(f"{c} {n}" for c, n in counts.items()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
