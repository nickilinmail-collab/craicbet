#!/usr/bin/env python3
"""
adapt_uk.py — Adapts CraicBet Irish casino pages to UK versions.
Usage: python3 tools/adapt_uk.py [--dry-run] [--pages PAGE1 PAGE2 ...]
       python3 tools/adapt_uk.py              # processes all casino pages
"""

import os, re, sys, shutil
from pathlib import Path

ROOT = Path(__file__).parent.parent
PAGES_DIR = ROOT / "pages"
UK_DIR = ROOT / "uk"
UK_DIR.mkdir(exist_ok=True)

DRY_RUN = "--dry-run" in sys.argv

# ── Pages to skip (betting-only, GAA, Irish-specific, already done) ──────────
SKIP = {
    # already manually created
    "best-casinos-ireland", "mobile-casinos", "betting-apps-ireland",
    "free-bets-ireland", "grai-licence-explained", "responsible-gambling",
    # betting/GAA — not relevant for UK casino section
    "betting-sites-ireland", "grai-licensed-betting-sites-ireland",
    "acca-betting-ireland", "acca-insurance-ireland", "acca-vs-singles",
    "accumulator-betting-ireland", "ante-post-betting-ireland",
    "all-ireland", "gaa-betting", "hurling-betting", "football-betting-ireland",
    # Irish bank-specific
    "aib-gambling-block", "bank-of-ireland-gambling-block", "ptsb-gambling-block",
    # GRAI-specific pages (no UK equivalent)
    "grai-tracker", "grai-licence-register", "grai-complaints-ireland",
    "grai-licensed-betting-sites-ireland", "grai-licence-explained",
    "why-no-grai-casino-licence-ireland", "no-grai-casino-ireland",
    # author/about — no need to duplicate
    "author-mark-craic", "about", "about-craicbet", "contact",
    "how-we-review", "privacy", "search", "guides", "sitemap",
    # UK already created
    "casino-sites-uk", "casino-apps-uk", "betting-apps-uk",
    "free-bets-uk", "ukgc-licence-explained", "gamstop-guide",
}

# ── Slug rename map: strip -ireland, rename for UK ───────────────────────────
def uk_slug(ie_slug: str) -> str:
    s = ie_slug
    # remove -ireland suffix
    s = re.sub(r"-ireland$", "", s)
    # remove -ireland- in the middle
    s = s.replace("-ireland-", "-")
    # rename specific patterns
    s = s.replace("-ie$", "")
    # append -uk if no -uk already
    if not s.endswith("-uk"):
        s = s + "-uk"
    return s

# ── Text replacement rules (order matters) ───────────────────────────────────
# Each: (pattern, replacement, flags)
TEXT_RULES = [
    # Remove GRAI warning banners entirely
    (r'<div[^>]*background:#fffbeb[^>]*>.*?No GRAI casino licence.*?</div>', '', re.DOTALL),
    (r'<p[^>]*background:#fef3f0[^>]*>.*?GRAI has not issued.*?</p>', '', re.DOTALL),
    # Remove GRAI licence number references
    (r'GRAI-0191-RB-26-0001[^<]*', '', 0),
    (r'Our partner operator holds GRAI betting licence[^.]+\.', '', 0),
    # Replace GRAI Compliant tags with UKGC Licensed
    (r'GRAI Compliant', 'UKGC Licensed', 0),
    (r'GRAI compliant', 'UKGC licensed', 0),
    # Currency: euros → pounds (before word replacements)
    (r'€(\d)', r'£\1', 0),
    (r'&euro;', '£', 0),
    (r'euro ', 'pound ', 0),
    (r'euros ', 'pounds ', 0),
    (r'EUR ', 'GBP ', 0),
    (r'en-IE', 'en-GB', 0),
    # Regulator text
    (r'\bGRAI\b', 'UKGC', 0),
    (r'Gambling Regulatory Authority of Ireland', 'UK Gambling Commission', 0),
    (r'Gambling Regulatory Authority', 'UK Gambling Commission', 0),
    # RG contacts
    (r'Gambling Awareness Trust[^<,\.]*1800 753 753[^<]*', 'GambleAware — begambleaware.org · National Gambling Helpline: 0808 8020 133 (free, 24/7)', 0),
    (r'1800 753 753', '0808 8020 133', 0),
    (r'gamblingcare\.ie', 'begambleaware.org', 0),
    (r'Gambling Awareness Trust', 'GambleAware', 0),
    (r'gamblingcare', 'begambleaware', 0),
    # Self-exclusion
    (r'Gambling Care', 'GambleAware', 0),
    # Country/locale
    (r'\birish players\b', 'UK players', re.IGNORECASE),
    (r'\birish player\b', 'UK player', re.IGNORECASE),
    (r'\bin Ireland\b', 'in the UK', re.IGNORECASE),
    (r'\bfor Ireland\b', 'for the UK', re.IGNORECASE),
    (r'\bIreland\b', 'the UK', re.IGNORECASE),
    (r'\birish\b', 'UK', re.IGNORECASE),
    # Payment methods — make UK-centric
    (r'Revolut is the most popular', 'PayPal and Visa debit are the most popular', 0),
    (r'Most popular in Ireland', 'Most popular in the UK', re.IGNORECASE),
    # lang attribute
    (r'lang="en"', 'lang="en-GB"', 0),
    (r'lang="en-IE"', 'lang="en-GB"', 0),
    (r'locale" content="en_IE"', 'locale" content="en_GB"', 0),
]

# ── Link/URL rules ────────────────────────────────────────────────────────────
def fix_links(html: str, ie_slug: str, uk_slug_val: str) -> str:
    # hreflang: add en-GB pointing to uk/ version, keep en-IE pointing to pages/
    # Remove old hreflang block and replace
    # canonical → uk version
    ie_url = f"https://craicbet.com/pages/{ie_slug}"
    uk_url = f"https://craicbet.com/uk/{uk_slug_val}"

    # Fix canonical
    html = html.replace(
        f'<link rel="canonical" href="{ie_url}">',
        f'<link rel="canonical" href="{uk_url}">'
    )
    # Fix OG url
    html = html.replace(
        f'<meta property="og:url" content="{ie_url}">',
        f'<meta property="og:url" content="{uk_url}">'
    )
    # Remove existing hreflang lines
    html = re.sub(r'\s*<link rel="alternate" hreflang="[^"]*" href="[^"]*">\n?', '\n', html)
    # Insert new hreflang after canonical
    hreflang = (
        f'  <link rel="alternate" hreflang="en-GB" href="{uk_url}">\n'
        f'  <link rel="alternate" hreflang="en-IE" href="{ie_url}">\n'
        f'  <link rel="alternate" hreflang="x-default" href="{ie_url}">\n'
    )
    html = html.replace(
        f'<link rel="canonical" href="{uk_url}">',
        f'<link rel="canonical" href="{uk_url}">\n{hreflang}'
    )

    # Fix breadcrumb links from pages/ to uk/ equivalents
    html = html.replace('href="best-casinos-ireland"', 'href="casino-sites-uk"')
    html = html.replace('href="mobile-casinos"', 'href="casino-apps-uk"')
    html = html.replace('href="free-bets-ireland"', 'href="free-bets-uk"')
    html = html.replace('href="responsible-gambling"', 'href="gamstop-guide"')
    html = html.replace('href="grai-licence-explained"', 'href="ukgc-licence-explained"')
    html = html.replace('href="betting-sites-ireland"', 'href="../pages/betting-sites-ireland"')

    # CSS paths: ../css/ → ../css/
    html = html.replace('href="../css/style.css"',
        'href="../css/style.css">\n  <link rel="stylesheet" href="../css/style-uk.css"')

    # Remove duplicate style-uk.css if already there
    html = re.sub(r'(<link rel="stylesheet" href="../css/style-uk.css"[^>]*>\s*)+',
                  '<link rel="stylesheet" href="../css/style-uk.css">\n  ', html)

    # Image/favicon paths already use /images/ (absolute) — OK
    # logo path: ../images/
    # Already correct for uk/ subdirectory

    # nav: internal links from uk/ — relative links within uk/ stay as is
    # links to pages/ from uk/ need ../pages/ prefix if they point to IE pages
    # We don't auto-fix all internal links — leave them pointing to IE equivalents
    # (they will work cross-site)

    return html

# ── Header/footer fixes ───────────────────────────────────────────────────────
def fix_header_footer(html: str, ie_slug: str, uk_slug_val: str) -> str:
    # Replace lang-switcher with UK version
    # Pattern: <div class="lang-switcher">...<a href="../uk/">...</a></div>
    # → <div class="lang-switcher"><a href="../pages/{ie_slug}">🇮🇪 IE</a><a href="{uk_slug_val}" class="active-lang">🇬🇧 UK</a></div>
    new_switcher = (
        f'<div class="lang-switcher">'
        f'<a href="../pages/{ie_slug}">🇮🇪 IE</a>'
        f'<a href="{uk_slug_val}" class="active-lang">🇬🇧 UK</a>'
        f'</div>'
    )
    html = re.sub(
        r'<div class="lang-switcher">.*?</div>',
        new_switcher,
        html,
        flags=re.DOTALL
    )

    # Add UK badge to logo (if not already there)
    if 'uk-badge' not in html:
        html = html.replace(
            'alt="CraicBet" style="height:40px;">',
            'alt="CraicBet" style="height:40px;"><span class="uk-badge">UK</span>'
        )
        # Fallback for pages with different img syntax
        html = html.replace(
            'alt="CraicBet Logo">',
            'alt="CraicBet Logo"><span class="uk-badge">UK</span>'
        )

    # Replace nav links in header
    old_nav_betting = '<a href="betting-sites-ireland">Betting</a>'
    new_nav_betting = '<a href="../pages/betting-sites-ireland">Betting 🇮🇪</a>'
    html = html.replace(old_nav_betting, new_nav_betting)

    # Replace GRAI footer section with UKGC equivalent
    html = re.sub(
        r'<h4>GRAI Guides</h4>.*?(?=<h4>|</div>)',
        '<h4>UKGC &amp; Safety</h4>'
        '<a href="ukgc-licence-explained">UKGC Licence</a>'
        '<a href="gamstop-guide">GamStop Guide</a>'
        '<a href="../pages/responsible-gambling">Responsible Gambling</a>',
        html,
        flags=re.DOTALL
    )

    # Replace RG footer line
    html = re.sub(
        r'Contact the Gambling Awareness Trust[^<]*1800 753 753[^<]*',
        'UK: GambleAware — <a href="https://www.begambleaware.org" '
        'target="_blank" rel="noopener">begambleaware.org</a> · '
        'National Gambling Helpline: 0808 8020 133 (free, 24/7)',
        html
    )

    # Replace footer RG paragraph
    html = re.sub(
        r'Ireland\'s independent betting &amp; casino guide',
        'CraicBet UK — independent casino guide for British players',
        html
    )

    # Remove plusfind.info CTA buttons (no UK partner)
    html = re.sub(
        r'<a href="https://plusfind\.info/[^"]*"[^>]*>.*?</a>',
        '<!-- UK partner CTA pending -->',
        html,
        flags=re.DOTALL
    )
    # Also remove gameslnk.cc
    html = re.sub(
        r'<a href="https://gameslnk\.cc/[^"]*"[^>]*class="btn[^"]*"[^>]*>.*?</a>',
        '',
        html,
        flags=re.DOTALL
    )
    # Remove "Also available" lines after CTA
    html = re.sub(
        r'<p[^>]*>Also available:.*?</p>',
        '',
        html,
        flags=re.DOTALL
    )

    return html

# ── Schema/meta fixes ─────────────────────────────────────────────────────────
def fix_schema(html: str, ie_slug: str, uk_slug_val: str) -> str:
    ie_url = f"https://craicbet.com/pages/{ie_slug}"
    uk_url = f"https://craicbet.com/uk/{uk_slug_val}"
    # Fix schema URLs
    html = html.replace(f'"item": "{ie_url}"', f'"item": "{uk_url}"')
    html = html.replace(f'"url": "{ie_url}"', f'"url": "{uk_url}"')
    html = html.replace('"inLanguage": ["en-IE", "ga", "pl"]', '"inLanguage": "en-GB"')
    html = html.replace('"inLanguage": "en-IE"', '"inLanguage": "en-GB"')
    html = html.replace('"areaServed": {"@type": "Country", "name": "Ireland"}',
                        '"areaServed": {"@type": "Country", "name": "United Kingdom"}')
    # Fix breadcrumb in schema
    html = html.replace(
        f'"item": "https://craicbet.com/pages/{ie_slug}"',
        f'"item": "https://craicbet.com/uk/{uk_slug_val}"'
    )
    return html

# ── Main adapt function ───────────────────────────────────────────────────────
def adapt_page(ie_slug: str) -> str | None:
    src = PAGES_DIR / f"{ie_slug}.html"
    if not src.exists():
        return None

    uk = uk_slug(ie_slug)
    dst = UK_DIR / f"{uk}.html"

    # Skip if UK version already manually created and is longer (better quality)
    if dst.exists() and dst.stat().st_size > src.stat().st_size * 0.9:
        return f"SKIP (exists): {uk}"

    html = src.read_text(encoding="utf-8")

    # Apply text rules
    for pattern, repl, flags in TEXT_RULES:
        try:
            if flags:
                html = re.sub(pattern, repl, html, flags=flags)
            else:
                html = re.sub(pattern, repl, html)
        except re.error:
            html = html.replace(pattern, repl)

    # Fix links, header/footer, schema
    html = fix_links(html, ie_slug, uk)
    html = fix_header_footer(html, ie_slug, uk)
    html = fix_schema(html, ie_slug, uk)

    # Update title/h1 date
    html = html.replace("October 2026", "November 2026")

    # lang attribute on <html>
    html = re.sub(r'<html lang="[^"]*">', '<html lang="en-GB">', html)

    if not DRY_RUN:
        dst.write_text(html, encoding="utf-8")

    return f"OK: {ie_slug} → uk/{uk}"

# ── Build list of pages to process ───────────────────────────────────────────
def get_casino_pages() -> list[str]:
    """Return IE slugs that are casino-related, not in SKIP list."""
    casino_patterns = re.compile(
        r'casino|slot|bonus|jackpot|blackjack|roulette|poker|baccarat|'
        r'live-casino|live-dealer|free-spin|wagering|payout|deposit|'
        r'withdrawal|payment|revolut|apple-pay|crypto|mobile-casino|'
        r'welcome-bonus|vip|cashback|high-rtp|no-deposit|fast-payout|'
        r'megaways|provably-fair|live-roulette|live-blackjack',
        re.IGNORECASE
    )
    skip_patterns = re.compile(
        r'betting-site|grai-licens|betting-ireland|acca-|accumulator|'
        r'ante-post|all-ireland|hurling|gaa-|horse-racing|football-betting|'
        r'sports-bet|arbitrage|asian-handicap|matched-betting|bankroll|'
        r'each-way|handicap-bet|in-play-bet|lay-bet|lucky-15|treble-bet|'
        r'round-robin|super-heinz|system-bet|trixie|yankee',
        re.IGNORECASE
    )
    pages = []
    for f in sorted(PAGES_DIR.glob("*.html")):
        slug = f.stem
        if slug in SKIP:
            continue
        if skip_patterns.search(slug):
            continue
        if casino_patterns.search(slug):
            pages.append(slug)
    return pages

# ── Run ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Specific pages mode
    if "--pages" in sys.argv:
        idx = sys.argv.index("--pages")
        pages = sys.argv[idx+1:]
    else:
        pages = get_casino_pages()

    print(f"{'[DRY RUN] ' if DRY_RUN else ''}Processing {len(pages)} pages...\n")

    ok, skipped, errors = 0, 0, 0
    new_urls = []

    for slug in pages:
        result = adapt_page(slug)
        if result is None:
            errors += 1
            print(f"  ERROR: {slug} not found")
        elif result.startswith("SKIP"):
            skipped += 1
            if "--verbose" in sys.argv:
                print(f"  {result}")
        else:
            ok += 1
            uk = uk_slug(slug)
            new_urls.append(f"https://craicbet.com/uk/{uk}")
            if "--verbose" in sys.argv or ok <= 10:
                print(f"  {result}")

    print(f"\nDone: {ok} adapted, {skipped} skipped, {errors} errors")

    # Append new URLs to sitemap (only new ones)
    if not DRY_RUN and new_urls:
        sitemap = ROOT / "sitemap.xml"
        content = sitemap.read_text()
        added = 0
        insertions = []
        for url in new_urls:
            if url not in content:
                insertions.append(
                    f'  <url><loc>{url}</loc>'
                    f'<lastmod>2026-11-06</lastmod>'
                    f'<changefreq>monthly</changefreq>'
                    f'<priority>0.6</priority></url>'
                )
                added += 1
        if insertions:
            content = content.replace(
                '</urlset>',
                '\n'.join(insertions) + '\n</urlset>'
            )
            sitemap.write_text(content)
        print(f"Sitemap: +{added} URLs added")
