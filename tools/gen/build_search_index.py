#!/usr/bin/env python3
"""
Build a JSON search index from all CraicBet HTML pages.
Outputs pages/search-index.json — array of {title, url, description, h1, text}.
Run from repo root: python3 tools/gen/build_search_index.py
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent  # /home/claude/craicbet

SKIP_FILES = {
    "index.html",   # root index — but only the root one
    "robots.txt",
    "sitemap.xml",
    "404.html",
    "search.html",
}

SEARCH_DIRS = [
    ("pages",         "/pages"),
    ("pages/slots",   "/pages/slots"),
    ("pages/brands",  "/pages/brands"),
    ("pages/news",    "/pages/news"),
    ("ga",            "/ga"),
    ("pl",            "/pl"),
]

def strip_tags(html: str) -> str:
    """Remove HTML tags and decode common entities."""
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"&amp;", "&", text)
    text = re.sub(r"&lt;", "<", text)
    text = re.sub(r"&gt;", ">", text)
    text = re.sub(r"&nbsp;", " ", text)
    text = re.sub(r"&mdash;", "—", text)
    text = re.sub(r"&ndash;", "–", text)
    text = re.sub(r"&rsaquo;", "›", text)
    text = re.sub(r"&[a-z]+;", " ", text)
    text = re.sub(r"&#\d+;", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_meta(content: str, name: str) -> str:
    m = re.search(
        r'<meta\s[^>]*name=["\']' + re.escape(name) + r'["\'][^>]*content=["\']([^"\']*)["\']',
        content, re.IGNORECASE
    )
    if not m:
        m = re.search(
            r'<meta\s[^>]*content=["\']([^"\']*)["\'][^>]*name=["\']' + re.escape(name) + r'["\']',
            content, re.IGNORECASE
        )
    return m.group(1).strip() if m else ""


def extract_title(content: str) -> str:
    m = re.search(r"<title>([^<]*)</title>", content, re.IGNORECASE)
    if not m:
        return ""
    title = strip_tags(m.group(1))
    # Strip site suffix variants
    title = re.sub(r"\s*[|\-—]\s*CraicBet\s*$", "", title, flags=re.IGNORECASE)
    return title.strip()


def extract_h1(content: str) -> str:
    m = re.search(r"<h1[^>]*>(.*?)</h1>", content, re.IGNORECASE | re.DOTALL)
    return strip_tags(m.group(1)).strip() if m else ""


def extract_body_text(content: str, limit: int = 300) -> str:
    """Extract first ~300 chars of visible text from <article> or <main>."""
    # Try <article> first, then <main>, then body
    for tag in ("article", "main"):
        m = re.search(rf"<{tag}[\s>].*?</{tag}>", content, re.IGNORECASE | re.DOTALL)
        if m:
            block = m.group(0)
            # Remove script/style blocks
            block = re.sub(r"<script[^>]*>.*?</script>", " ", block, flags=re.IGNORECASE | re.DOTALL)
            block = re.sub(r"<style[^>]*>.*?</style>", " ", block, flags=re.IGNORECASE | re.DOTALL)
            # Remove nav/header/footer inside article/main
            block = re.sub(r"<nav[^>]*>.*?</nav>", " ", block, flags=re.IGNORECASE | re.DOTALL)
            text = strip_tags(block)
            if len(text) > 50:
                return text[:limit]
    # Fallback: strip entire body
    body_m = re.search(r"<body[^>]*>(.*?)</body>", content, re.IGNORECASE | re.DOTALL)
    if body_m:
        body = body_m.group(1)
        body = re.sub(r"<script[^>]*>.*?</script>", " ", body, flags=re.IGNORECASE | re.DOTALL)
        body = re.sub(r"<style[^>]*>.*?</style>", " ", body, flags=re.IGNORECASE | re.DOTALL)
        body = re.sub(r"<header[^>]*>.*?</header>", " ", body, flags=re.IGNORECASE | re.DOTALL)
        body = re.sub(r"<footer[^>]*>.*?</footer>", " ", body, flags=re.IGNORECASE | re.DOTALL)
        body = re.sub(r"<nav[^>]*>.*?</nav>", " ", body, flags=re.IGNORECASE | re.DOTALL)
        text = strip_tags(body)
        return text[:limit]
    return ""


def build_url(rel_dir: str, filename: str) -> str:
    """Convert directory + filename to clean URL path."""
    stem = Path(filename).stem
    if rel_dir == "pages":
        return f"/pages/{stem}"
    elif rel_dir == "pages/slots":
        return f"/pages/slots/{stem}"
    elif rel_dir == "pages/brands":
        return f"/pages/brands/{stem}"
    elif rel_dir == "pages/news":
        return f"/pages/news/{stem}"
    elif rel_dir == "ga":
        return f"/ga/{stem}"
    elif rel_dir == "pl":
        return f"/pl/{stem}"
    return f"/{rel_dir}/{stem}"


def process_file(filepath: Path, url: str) -> dict | None:
    try:
        content = filepath.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        print(f"  SKIP (read error): {filepath}: {e}", file=sys.stderr)
        return None

    title = extract_title(content)
    description = extract_meta(content, "description")
    h1 = extract_h1(content)
    text = extract_body_text(content)

    # Skip pages with no meaningful content
    if not title and not h1:
        return None

    return {
        "title": title,
        "url": url,
        "description": description,
        "h1": h1,
        "text": text,
    }


def main():
    index = []
    seen_urls: set[str] = set()

    for rel_dir, url_prefix in SEARCH_DIRS:
        dir_path = ROOT / rel_dir
        if not dir_path.is_dir():
            print(f"  Skipping missing dir: {dir_path}", file=sys.stderr)
            continue

        html_files = sorted(dir_path.glob("*.html"))
        print(f"{rel_dir}: {len(html_files)} files")

        for filepath in html_files:
            fname = filepath.name

            # Skip special files
            if fname in SKIP_FILES:
                continue
            # Skip root index.html only when in pages/ not subdirs
            if fname == "index.html" and rel_dir in ("pages", "ga", "pl"):
                continue

            url = build_url(rel_dir, fname)
            if url in seen_urls:
                continue
            seen_urls.add(url)

            entry = process_file(filepath, url)
            if entry:
                index.append(entry)

    output_path = ROOT / "pages" / "search-index.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, separators=(",", ":"))

    size_kb = output_path.stat().st_size / 1024
    print(f"\nWrote {len(index)} entries to {output_path}")
    print(f"File size: {size_kb:.1f} KB")
    if size_kb > 2048:
        print("WARNING: search-index.json exceeds 2 MB!", file=sys.stderr)


if __name__ == "__main__":
    main()
