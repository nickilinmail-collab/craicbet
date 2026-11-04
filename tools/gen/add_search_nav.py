#!/usr/bin/env python3
"""
Add a Search nav link after 'Guides' in all HTML pages under pages/, ga/, pl/.
Root-relative href="/pages/search" used in all files.
Run from repo root: python3 tools/gen/add_search_nav.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent  # /home/claude/craicbet

SEARCH_DIRS = [
    ROOT / "pages",
    ROOT / "pages" / "slots",
    ROOT / "pages" / "brands",
    ROOT / "pages" / "news",
    ROOT / "ga",
    ROOT / "pl",
]

SKIP_FILES = {"search.html"}

# The link to insert — root-relative
SEARCH_LINK = '<a href="/pages/search">&#128269; Search</a>'

# Pattern: find the Guides nav link (various forms including ga/pl translations)
# We want to insert our link right after the closing </a> of the Guides link
GUIDES_PATTERN = re.compile(
    r'(<a\s[^>]*href=["\'][^"\']*(?:guides|treoracha|poradniki)["\'][^>]*>.*?</a>)',
    re.IGNORECASE | re.DOTALL,
)


def already_has_search(content: str) -> bool:
    return '/pages/search' in content or 'href="search"' in content


NAV_CLOSE_PATTERN = re.compile(r'(</nav>)', re.IGNORECASE)


def add_search_link(content: str) -> str | None:
    if already_has_search(content):
        return None  # already done

    m = GUIDES_PATTERN.search(content)
    if m:
        # Insert search link right after the Guides </a>
        end = m.end()
        return content[:end] + '\n      ' + SEARCH_LINK + content[end:]

    # Fallback: insert before first </nav> inside the main nav block
    nav_m = re.search(r'<nav\s[^>]*id=["\']mainNav["\'][^>]*>(.*?)</nav>', content, re.IGNORECASE | re.DOTALL)
    if nav_m:
        # Insert before closing </nav>
        nav_end = nav_m.end(0) - len('</nav>')
        return content[:nav_end] + '\n      ' + SEARCH_LINK + '\n    ' + content[nav_end:]

    return None


def process_dir(dir_path: Path) -> tuple[int, int]:
    updated = 0
    skipped = 0
    if not dir_path.is_dir():
        return 0, 0

    for filepath in sorted(dir_path.glob("*.html")):
        if filepath.name in SKIP_FILES:
            continue
        try:
            original = filepath.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            print(f"  SKIP (read error): {filepath.name}: {e}", file=sys.stderr)
            skipped += 1
            continue

        result = add_search_link(original)
        if result is None:
            skipped += 1
            continue

        try:
            filepath.write_text(result, encoding="utf-8")
            updated += 1
        except Exception as e:
            print(f"  SKIP (write error): {filepath.name}: {e}", file=sys.stderr)
            skipped += 1

    return updated, skipped


def main():
    total_updated = 0
    total_skipped = 0
    for d in SEARCH_DIRS:
        u, s = process_dir(d)
        rel = d.relative_to(ROOT)
        print(f"{rel}: {u} updated, {s} skipped")
        total_updated += u
        total_skipped += s

    print(f"\nTotal: {total_updated} files updated, {total_skipped} skipped (already done or no Guides link)")


if __name__ == "__main__":
    main()
